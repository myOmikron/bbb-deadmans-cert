from django.http import JsonResponse
from django.views.generic import TemplateView


class IsDeadmanEnabledView(TemplateView):
    def get(self, request, *args, **kwargs):
        response = 200
        data = {"success": False, "result": ""}
        if "client_id" not in request.GET:
            data["result"] = "Parameter client_id is missing"
            response = 400
        if "meeting_id" not in request.GET:
            data["result"] = "Parameter meeting_id is missing"
            response = 400
        if response == 200:
            data["success"] = True
            data["result"] = {"IsDeadmanEnabled": True}
        return JsonResponse(data, status=response)
