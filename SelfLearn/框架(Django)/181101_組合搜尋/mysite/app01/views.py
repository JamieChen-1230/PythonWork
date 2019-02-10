from django.shortcuts import render
from app01 import models


def video(request, *args, **kwargs):
    condition = {
        # "level_id": 1,
        # "classification_id": 2,
    }
    for k, v in kwargs.items():
        temp = int(v)
        kwargs[k] = temp
        if temp:
            # 不等於0就加入
            condition[k] = temp

    class_list = models.Classification.objects.all()
    level_list = models.Level.objects.all()
    # 把原本的status_choice轉換成字典形式
    status_list = list(map(lambda x: {"id": x[0], "name": x[1]}, models.Video.status_choice))

    video_list = models.Video.objects.filter(**condition)

    return render(request, "video.html", locals())


# 包含一個多對多，再多就過於複雜，實務上也不常見
def video2(request, *args, **kwargs):
    # 建立查詢字典
    condition = {}
    # 因為網址傳過來的資料是字串，所以需要先轉成int
    for k, v in kwargs.items():
        temp = int(v)
        kwargs[k] = temp
    print("kwargs ", kwargs)
    # 這兩個list可以單獨存在不會受到他人影響，所以可先創建
    direction_list = models.Direction.objects.all()
    level_list = models.Level.objects.all()

    """
    if direction_id == 0:
        對class_list無影響(因列出所有分類)，故可以直接創建class_list
        if classification_id == 0:
            表不須增加關於分類的查詢條件
            pass
        else:
            須加上要查詢的classification_id
            condition["classification_id"] = classification_id
    else: (direction_id != 0)
        分類顯示會受到direction影響(列出當前方向下的分類)
        class_list = direction_obj.classification.all()
        if classification_id = 0:
            為查詢條件添加classification_id__in
            condition["classification_id__in"] = [當前方向下的所有分類id]
        else:
            if 方向與分類匹配:
                condition["classification_id"] = classification_id
            else:(不匹配)
                為查詢條件添加classification_id__in
                condition["classification_id__in"] = [當前方向下的所有分類id]
                幫kwargs更改classification_id，因為當前方向下無此分類
                kwargs["classification_id"] = 0
    """
    # 網址傳過來的id資料
    direction_id = kwargs.get("direction_id")
    classification_id = kwargs.get("classification_id")
    level_id = kwargs.get("level_id")
    # 增加關於Classification的查詢條件
    if direction_id == 0:
        # direction為全部，故Classification也為全部
        class_list = models.Classification.objects.all()
        if classification_id == 0:
            pass
        else:
            condition["classification_id"] = classification_id
    else:
        # classification會根據direction而改變
        direction_obj = models.Direction.objects.filter(id=direction_id).first()
        class_list = direction_obj.classification.all()

        # 當前direction下的classification_id元組陣列
        num_list = direction_obj.classification.all().values_list("id")
        print("num_list ", num_list)
        # 若此direction下無任何classification要把classification_id_list設為空
        if not num_list:
            classification_id_list = []
        else:
            # 過濾雜訊，變為真正可用的classification_id_list
            classification_id_list = list(zip(*num_list))[0]

        if classification_id == 0:
            # 為查詢條件添加classification_id__in
            condition["classification_id__in"] = classification_id_list
            print("classification_id_list", classification_id_list)
        else:
            if classification_id in classification_id_list:
                # classification_id與direction匹配
                condition["classification_id"] = classification_id
            else:
                # -------------EX: 當前方向的類: [1, 2], 當前分類: 5-------------
                # 幫kwargs更改classification_id，因為當前方向下無此分類
                kwargs["classification_id"] = 0
                condition["classification_id__in"] = classification_id_list
                print("classification_id_list", classification_id_list)

    # 增加關於level的查詢條件，因為direction跟video無直接關聯，故不必添加
    if level_id == 0:
        pass
    else:
        condition["level_id"] = level_id
    # 根據條件篩選video，並建立video_list
    video_list = models.Video.objects.filter(**condition)

    return render(request, "video2.html", locals())
