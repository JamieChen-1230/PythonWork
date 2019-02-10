from django.shortcuts import redirect


class BaseKingAdmin(object):
    def __init__(self):
        if "delete_selected_objects" not in self.actions:
            self.actions.extend(self.default_actions)

    list_display = []
    list_filter = []
    search_fields = []
    readonly_fields = []
    filter_horizontal = []
    list_per_page = 5
    default_actions = ["delete_selected_objects"]
    actions = []

    def delete_selected_objects(self, request, querysets):
        app_name = querysets[0]._meta.app_label
        model_name = querysets[0]._meta.model_name
        admin_class = self  # admin_class就是自己本身
        objs_id = ""
        for obj in querysets:
            objs_id += str(obj.id)+","
        # print(objs_id)
        return redirect("/kingadmin/%s/%s/%s/delete/" % (app_name, model_name, objs_id))
