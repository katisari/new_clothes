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

def index(request):
    if 'cart_num' not in request.session:
        request.session['cart_num'] = 0
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
    return render(request, 'order/order.html')

def photo_api(request):
    print(" ******************IN USERS API *************************")
    photos = Photo.objects.filter(name__startswith=request.POST['searching'])
    return render(request, 'order/pic_api.html', {'photos': photos})

@csrf_exempt
def addcart(request):
    print("hello")
    request.session['cart_num'] += 1
    this_user = User.objects.get(id=1)
    this_item = Item.objects.get(id=1)
    this_user.cart_items.add(this_item)
    return JsonResponse({'cart_num': request.session['cart_num']})