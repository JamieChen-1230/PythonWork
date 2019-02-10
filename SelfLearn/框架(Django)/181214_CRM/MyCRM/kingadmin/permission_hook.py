
def view_my_own_customers(request):
    # print("running permission hook....")
    if str(request.user.id) == request.GET.get("consultant"):
        # print("允許訪問自己的客戶")
        return True
    else:
        return False
