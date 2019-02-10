from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from crm import models
from crm import forms
from django import conf
import os, json
from django.utils.timezone import datetime  # 這個datetime是照django的時區
from django.db.utils import IntegrityError


@login_required
def dashboard(request):
    return render(request, "crm/dashboard.html", locals())


@login_required
def stu_enrollment(request):
    customers = models.CustomerInfo.objects.all()
    class_list = models.ClassList.objects.all()

    if request.method == "POST":
        customer_id = request.POST.get("customer_id")
        class_grade_id = request.POST.get("class_grade_id")
        try:
            enrollment_obj = models.StudentEnrollment.objects.create(
                customer_id=customer_id,
                class_grade_id=class_grade_id,
                # request.user拿到的是Django內建的user
                consultant_id=request.user.id,
            )
            # print(enrollment_obj.contract_agreed)
        except IntegrityError as e:  # 已生成過報名表了
            enrollment_obj = models.StudentEnrollment.objects.get(customer_id=customer_id, class_grade_id=class_grade_id)
            # print(enrollment_obj.contract_agreed)
            if enrollment_obj.contract_agreed:
                return redirect("/crm/stu_enrollment/%s/contract_audit/" % enrollment_obj.id)
            else:
                msg = "The student has not submitted the form yet."

        # print(request.META['HTTP_HOST'])
        host = request.META['HTTP_HOST']  # 主機域名
        enrollment_link = "%s/crm/enrollment/%s/" % (host, enrollment_obj.id)
        # print("enrollment_link", enrollment_link)

    return render(request, "crm/stu_enrollment.html", locals())


def enrollment(request, enrollment_id):
    """學員在線報名"""
    enrollment_obj = models.StudentEnrollment.objects.get(id=enrollment_id)

    if enrollment_obj.contract_agreed:
        return HttpResponse("合同正在審核中")

    if request.method == "POST":
        print(request.POST)
        customer_form = forms.CustomerForm(instance=enrollment_obj.customer, data=request.POST)
        if customer_form.is_valid():
            # print(customer_form.cleaned_data)
            customer_form.save()
            enrollment_obj.contract_agreed = True
            enrollment_obj.contract_signed_date = datetime.now()
            enrollment_obj.save()
            return HttpResponse("已成功提交報名資料，請等待審核通過。")
        else:
            print(customer_form.errors)
    else:
        customer_form = forms.CustomerForm(instance=enrollment_obj.customer)
    # 列出以上傳之文件
    uploaded_files = []
    enrollment_upload_dir = os.path.join(conf.settings.CRM_FILE_UPLOAD_DIR, enrollment_id)
    if os.path.isdir(enrollment_upload_dir):  # 判斷是否是目錄並且存在
        uploaded_files = os.listdir(enrollment_upload_dir)  # 列出資料夾內所有的文件

    return render(request, "crm/enrollment.html", locals())


# csrf_exempt 不做csrf驗證
@csrf_exempt
def enrollment_file_upload(request, enrollment_id):
    print(request.FILES)
    print(conf.settings.CRM_FILE_UPLOAD_DIR)
    enrollment_upload_dir = os.path.join(conf.settings.CRM_FILE_UPLOAD_DIR, enrollment_id)
    if not os.path.isdir(enrollment_upload_dir):  # 判斷是否是目錄並且存在
        os.mkdir(enrollment_upload_dir)
    file_obj = request.FILES.get("file")

    if len(os.listdir(enrollment_upload_dir)) < 2:
        with open(os.path.join(enrollment_upload_dir, file_obj.name), "wb") as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
    else:
        return HttpResponse(json.dumps({"status": False, "err_msg": "最多只能有兩個文件"}))

    return HttpResponse(json.dumps({"status": True, "err_msg": ""}))


@login_required
def enrollment_contract_audit(request, enrollment_id):
    enrollment_obj = models.StudentEnrollment.objects.get(id=enrollment_id)
    if request.method == "POST":
        enrollment_form = forms.EnrollmentForm(instance=enrollment_obj, data=request.POST)
        customer_form = forms.CustomerForm(instance=enrollment_obj.customer)
        if enrollment_form.is_valid():
            print(enrollment_form.cleaned_data)
            enrollment_form.save()
            # 創建學生，get_or_create()有就取出，無就創建
            stu_obj = models.Student.objects.get_or_create(customer=enrollment_obj.customer)[0]
            # print(stu_obj)
            stu_obj.class_grade.add(enrollment_obj.class_grade)
            stu_obj.save()
            # 改成已報名
            enrollment_obj.customer.status = 1
            enrollment_obj.customer.save()
            return redirect("/kingadmin/crm/customerinfo/%s/change/" % enrollment_obj.customer.id)
        else:
            return render(request, "crm/enrollment_contract_audit.html", locals())
    else:
        customer_form = forms.CustomerForm(instance=enrollment_obj.customer)
        enrollment_form = forms.EnrollmentForm(instance=enrollment_obj)
        return render(request, "crm/enrollment_contract_audit.html", locals())
