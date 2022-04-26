from django.shortcuts import render

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def showFunc(request):
    print('GET 요청 처리')
    gen = request.GET.get('gen')
    return render(request,'show.html',{'gen':gen})