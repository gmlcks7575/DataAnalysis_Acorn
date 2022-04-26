from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
def mainFunc(request): #요청을 받는 것은 request가 있어야 한다.
    return render(request, "index.html")

class CallView(TemplateView):
    template_name = "callget.html"
'''    
def insertFunc(request):
    return render(request, 'insert.html')
'''
#get
'''
def insertokFunc(request):
    #irum = request.GET.get('name') #GET방식으로 받는다
    irum = request.GET['name']
    print(irum)
    return render(request, 'list.html', {'irum':irum})
'''
#post
def insertFunc(request):
    if request.method == 'GET':
        print('GET 요청 처리')
        return render(request,'insert.html') # forward방식
    
    elif request.method == 'POST':
        print('POST 요청 처리')
        irum = request.POST.get('name')
        return render(request, 'list.html', {'irum':irum})
    
    else:
        print('요청 에러')
        