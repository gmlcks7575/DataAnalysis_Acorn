from django.shortcuts import render, redirect
from myguest.models import Guest
from datetime import datetime
from django.http.response import HttpResponseRedirect
#from django.utils import timezone

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html') #forwarding : 서버에서 서버 파일 직접 호출

def ListFunc(request):
    print(Guest.objects.filter(title__contains = 'hi')) #where 조건
    print(Guest.objects.filter(id = 1)) #where 조건
    print(Guest.objects.filter(title = 'bye')) #where 조건
    print(Guest.objects.get(id=1)) #where 조건 # 하나 반환

    gdatas = Guest.objects.all()
    #gdatas = Guest.objects.all().order_by('title') #ascending sort
    #gdatas = Guest.objects.all().order_by('-title') #descending sort
    #gdatas = Guest.objects.all().order_by('-id', 'title') # id descending sort, title ascending sort
    #gdatas = Guest.objects.all().order_by('-id', 'title')[0:2] # id descending sort, title ascending sort

    return render(request, 'list.html',{'gdatas':gdatas})

def InsertFunc(request):
    return render(request, 'insert.html')

def InserOkFunc(request):
    if request.method=="POST":
        #print(request.POST.get("title"))
        #print(request.POST["title"])
        Guest(
            title = request.POST.get("title"), #왼쪽은 테이블 column명 오른쪽은 입력한 변수명
            content = request.POST.get("content"),
            regdate = datetime.now(), # timezone.now()
        ).save() #insert into
        
    #return HttpResponseRedirect('/guest') #추가 후 목록 보기 redirect 방식 : 클라이언트를 통해 자료 요청
    return redirect('/guest') #shortcut

#수정하기
"""
gtab = Guest.objects.get(id=해당id)
gtab.title = '수정제목'
gtab.content = '수정내용'
gtab.save() "update 테이블명 set ..."
"""
#삭제하기
"""
gtab = Guest.objects.get(id=해당id)
gtab.delete() "delete from 테이블명..."
"""