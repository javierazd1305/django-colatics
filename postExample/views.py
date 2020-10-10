from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def post_example(request):
    if request.method == "POST":
        print(request.POST.get("name"))
        data = {
            "app": "app example",
            "data": "This is an example of a post request to django server"
        }
        return (HttpResponse(json.dumps(data)))


@csrf_exempt
def post_example_2(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data['data']["name"]
        return (HttpResponse(json.dumps(name)))


def get_example(request):
    return (HttpResponse("get request example"))
