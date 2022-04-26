from django.shortcuts import render

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def page1Func(request):
    return render(request, 'page1.html')


def page2Func(request):
    return render(request, 'page2.html')

def cartFunc(request):
    name = request.POST["name"]
    price = request.POST["price"]
    print(name, price) #넘어오면 찍힌다.
    product = {'name':name, 'price':price}
    
    productList = []
    if "shop" in request.session:
        productList = request.session['shop'] #첫 번째 꺼내
        productList.append(product) #두번째 상품을 넣어
        request.session['shop'] = productList #세션에넣어
        
    else:
        productList.append(product) #첫번째 상품을 productlist에 넣어
        request.session['shop'] = productList
        
    print(productList)
    context = {} #html에 보낼 용도
    context['products'] = request.session['shop']
    return render(request, 'cart.html', context)

def buyFunc(request):
    if "shop" in request.session:
        productList = request.session['shop']
        print(productList)
        
        total = 0
        for pro in productList:
            total += int(pro['price'])
        print(total)   
        request.session.clear() # session 안에 모든 키 삭제
        
    return render(request, 'buy.html', {'total':total}) 