from django.shortcuts import render
from sangpum.models import Maker, Product
from django.db.models import Sum, Count, Avg, StdDev

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def List1(request):
    makers = Maker.objects.all()
    return render(request, 'list1.html', {'makers':makers})

def List2(request):
    products = Product.objects.all()
    pcount = len(products)
    
    print(Product.objects.all().count())
    
    for r in products.values_list(): # tuple type으로 모두 출력
        print(r)
        
    print(products.aggregate(Count('price')))
    print(products.aggregate(Sum('price')))
    print(products.aggregate(Avg('price')))  
    print(products.aggregate(StdDev('price')))
        
    return render(request, 'list2.html', {'products':products, 'pcount':pcount})

def List3(request):
    mid = request.GET.get('id')
    products = Product.objects.filter(maker_name=mid)
    pcount = len(products)
    return render(request, 'list2.html', {'products':products, 'pcount':pcount})
