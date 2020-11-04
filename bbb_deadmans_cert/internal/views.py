from datetime import datetime

from django.http import JsonResponse
from django.views.generic import TemplateView


def check_missing_parameter(get):
    response = 200
    data = {"success": False, "result": ""}
    if "client_id" not in get:
        data["result"] = "Parameter client_id is missing"
        response = 400
    if "meeting_id" not in get:
        data["result"] = "Parameter meeting_id is missing"
        response = 400
    return data, response


class IsDeadmanEnabledView(TemplateView):
    def get(self, request, *args, **kwargs):
        data, response = check_missing_parameter(request.GET)
        if response == 200:
            data["success"] = True
            data["result"] = {"IsDeadmanEnabled": True}
        return JsonResponse(data, status=response, reason=data["result"])


class StartBreakView(TemplateView):
    def get(self, request, *args, **kwargs):
        data, response = check_missing_parameter(request.GET)
        if response == 200:
            data["success"] = True
            data["result"] = "Break started at " + str(datetime.time(datetime.now())) + " UTC"
        return JsonResponse(data, status=response, reason=data["result"])


class StopBreakView(TemplateView):
    def get(self, request, *args, **kwargs):
        data, response = check_missing_parameter(request.GET)
        if response == 200:
            data["success"] = True
            data["result"] = "Break stopped at " + str(datetime.time(datetime.now())) + " UTC"
        return JsonResponse(data, status=response, reason=data["result"])


class SetNoDeadmanView(TemplateView):
    def get(self, request, *args, **kwargs):
        data, response = check_missing_parameter(request.GET)
        if response == 200:
            data["success"] = True
            data["response"] = "Pressed button at " + str(datetime.time(datetime.now())) + " UTC"
        return JsonResponse(data, status=response, reason=data["result"])

