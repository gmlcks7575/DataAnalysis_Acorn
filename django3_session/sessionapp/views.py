from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def setOsFunc(request):
    #print('request GET :', request.GET) #<QueryDict: {}>
    
    if "favorite_os" in request.GET:
        print('request GET :', request.GET["favorite_os"])
        
        #request.session['세션키']
        request.session['f_os'] = request.GET["favorite_os"] #f_os라는 key로 세션을 생성
        return HttpResponseRedirect("/showos") #redirect 방식 (client를 컴을 통해 요청을 함)
    
    else:
        return render(request, 'seletos.html') #forward (server가 직접 파일을 선택해 client로 전송(push))

def showOsFunc(request):
    dict_context = {}
    
    if "f_os" in request.session:
        print('유효시간:', request.session.get_expiry_age())
        dict_context['select_os'] = request.session['f_os']
        dict_context['message'] = "그대 선택한 운영체제는 %s"%request.session['f_os']
    else:
        dict_context['select_os'] = None
        dict_context['message'] = "운영체제를 선택하지 않았어요"
    
    # del request.session['f_os'] # 세션삭제
    request.session.set_expiry(5) # 세션 유효기간을 5초로 제한  
    
    return render(request, 'show.html', dict_context)      
        