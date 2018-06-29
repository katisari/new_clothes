from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import JsonResponse
# stripe.api_key = "sk_test_eo8n9U6JGbt0Sxmm5PQYdJtu"


# token = request.form['stripeToken'] # Using Flask

# charge = stripe.Charge.create(
#     amount=999,
#     currency='usd',
#     description='Example charge',
#     source=token,
# )
def logo(request):
    return render(request, 'order/index.html')
def login(request):
    return render(request, 'order/login.html')

def login_process(request):
    b = User.objects.get(email=request.POST['email'])
    if b.user_type=="admin":
        return redirect('/admin')
    else:
        return redirect('/')
    return HttpResponse("yo")
    

def admin(request):
    content = {
        'all_order': Order.objects.all()
    }
    return render(request, 'order/admin.html', content)

def logoff(request):
    request.session.flush()
    return redirect('/login')

def grey_hoodie(request):
    return render(request, 'order/descriptor.html')

def index(request):
    if 'cart_num' not in request.session:
        request.session['cart_num'] = 0
    
    request.session['user_id'] = 1
    all = Item.objects.all()
    apparels = []
    swag = []
    books = []
    misc = []
    for item in all:
        if item.category == "apparels":
            apparels.append({'pic_link': item.photos.get(category__startswith="main").link, 'id' :item.id, 'name': item.name, 'price': item.price})
        elif item.category == "swag":
            swag.append({'pic_link': item.photos.get(category__startswith="main").link, 'id' :item.id, 'name': item.name, 'price': item.price})
        elif item.category == "books":
            books.append({'pic_link': item.photos.get(category__startswith="main").link, 'id' :item.id, 'name': item.name, 'price': item.price})
        else:
            misc.append({'pic_link': item.photos.get(category__startswith="main").link, 'id' :item.id, 'name': item.name, 'price': item.price})
    content = {
        'apparels_list': apparels,
        'swag_list': swag,
        'books_list': books,
        'misc_list': misc

    }
    return render(request, 'order/main_page.html', content)

def order(request):
    print(request.session['user_id'])
    cart_item = User.objects.get(id=request.session['user_id']).cart_items.all()
    item_total = 0
    for item in cart_item:
        item_total += item.price
    print(item_total)
    tax = float(item_total) * .09
    tax = float("{0:.2f}".format(tax))
    item_total = float("{0:.2f}".format(item_total))
    ordertotal = float(item_total)+float(tax)+5.99
    ordertotal = float("{0:.2f}".format(ordertotal))
    content = {
        "cart_items": cart_item,
        "item_total" : item_total,
        "tax": tax,
        "order_total" : ordertotal
    }

    return render(request, 'order/order.html', content)

def photo_api(request):
    print(" ******************IN USERS API *************************")
    photos = Photo.objects.filter(name__startswith=request.POST['searching'])
    return render(request, 'order/pic_api.html', {'photos': photos})


@csrf_exempt
def addcart(request):
    if request.method == "POST":
        print('id is',request.POST['item_id'])
        request.session['cart_num'] += 1
        this_user = User.objects.get(id=1)
        this_item = Item.objects.get(id=int(request.POST['item_id']))
        this_user.cart_items.add(this_item)
    return JsonResponse({'cart_num': request.session['cart_num']})