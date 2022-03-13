from ast import Try
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
br=[]
def index(request):
    DIRECTIONS = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
    response = json.dumps([{}])
    return HttpResponse(response,content_type="text/json")

def get_result_from_AI(request):

    if(request.method == "GET"):
        try:
            response = json.dumps([{'table':br}])
        except:
            response = json.dumps([{'msg':'error'}])
    # if(request.method == "POST"):
    #     # try:
    #         # print(request.body)
    #     data=json.loads(request.body)
    #     a00=data["a00"]
    #     a01=data["a01"]
    #     response = json.dumps([{'a00':a00,'a01':a01}])
    #     # response=json.dumps([{"msg":data["a01"]}])
    #     # except:
    #         # response = json.dumps([{'msg':"data"}])
    
    return HttpResponse(response,content_type="text/json")

@csrf_exempt
def get_data_to_ai(request):
    if(request.method == "POST"):
        data=json.loads(request.body)
        for i in range(3):
            l=[]
            for j in range(3):
                l.append(int(data["a"+str(i)+str(j)]))
            br.append(l)
        response=json.dumps([{"table":br}])
    return HttpResponse(response,content_type="text/json")