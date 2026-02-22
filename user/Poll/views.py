from django.shortcuts import render
from django.http import JsonResponse
from .models import pollModel

# Create your views here.
def poll_create (request):
    pass

def poll_view(request):
    pass


def poll(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
    
    


    if request.method == 'GET':
        data = pollModel.objects.all()[:10]
        datas = {"result": list(data.values('title', 'content'))}
        return JsonResponse(datas)

# how can i convert data into json ??

# how can i set data as jsno table ??