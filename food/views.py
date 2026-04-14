import json
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from .services import *
from config.settings import MEDIA_ROOT
from .forms import *
def home_page(request):
    if request.GET:
        product = get_product_by_id(request.GET.get("product_id", 0))
        return JsonResponse(product)

def order_page(request):
    if request.GET:
        user = get_user_by_phone(request.GET.get("phone_number",0))
        return JsonResponse(user,safe=False)

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    orders = []
    orders_list = request.COOKIES.get("orders")
    total_price = request.COOKIES.get("total_price",0)
    print(orders_list)
    print(total_price)
    if orders_list:
        for key, val in json.loads(orders_list).items():
            orders.append(
                {
                "product": Product.objects.get(pk=int(key)),
                "count": val
                }
            )
    ctx = {
        'categories': categories,
        'products': products,
        'orders':orders,
        'total_price':total_price,
        'MEDIA_ROOT': MEDIA_ROOT
    }

    response = render(request, 'food/index.html', ctx)
    response.set_cookie("greeting", 'hello')
    return response

def main_order(request):
    model=Customer()
    if request.POST:
        try:
            model = Customer.objects.get(phone_number=request.POST.get("phone_number", ""))
        except:
            model = Customer()
        form = CustomerForm(request.POST or None, instance=model)
        if form.is_valid():
            customer = form.save()
            formOrder = OrderForm(request.POST or None, instance=Order())
            if formOrder.is_valid():
                order = formOrder.save(customer=customer)
                print("order:",order)
                orders_list = request.COOKIES.get("orders")


                for key,value in json.loads(orders_list).items():
                    product = get_product_by_id(int(key))

                    counts = value
                    order_product = OrderProduct(
                        count=counts,
                        price = product['price'],
                        product_id = product['id'],
                        order_id = order.id
                    )
                    order_product.save()

                return redirect("index")
            else:
                print(formOrder.errors)
        else:
            print(form.errors)

    categories = Category.objects.all()
    products = Product.objects.all()
    orders = []
    orders_list = request.COOKIES.get("orders")
    total_price = request.COOKIES.get("total_price")
    if orders_list:
        for key, val in json.loads(orders_list).items():
            orders.append(
                {
                "product": Product.objects.get(pk=int(key)),
                "count": val
                }
            )
    ctx = {
        'categories': categories,
        'products': products,
        'orders':orders,
        'total_price':total_price,
        'MEDIA_ROOT': MEDIA_ROOT,
    }

    response = render(request, 'food/order.html', ctx)
    response.set_cookie("greeting", 'hello')
    return response

def send_order(request):
    # return redirect('index')
    return render(request,'food/order.html')


def finalize_order(request):
    """
    Buyurtmani yakunlash va email yuborish funksiyasi.
    """
    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone_number')


        subject = f"Yangi Buyurtma: {f_name} {l_name}"
        message = (
            f"Mijoz ismi: {f_name} {l_name}\n"
            f"Telefon: {phone}\n"
            f"Email: {email}\n"
            f"Maxway loyihasidan xabar."
        )

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            print("Email muvaffaqiyatli uchdi! 🚀")
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")

        return redirect('index')

    return redirect('index')


    from .models import Order

    Order.objects.create(
        customer=f"{f_name} {l_name}",
        address=region if region else "Manzil ko'rsatilmadi",
        phone=phone,
        payment_type="naqd"
    )
