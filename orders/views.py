from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from orders.forms import AddOrderForm, EditOrderForm
from orders.models import Order


def home_page(request):
    orders = Order.objects.filter().order_by('-date_created')
    pending_orders = Order.objects.filter(pending=True)
    pending = len(pending_orders)
    in_transit_orders = Order.objects.filter(in_transit=True)
    in_transit = len(in_transit_orders)
    received_orders = Order.objects.filter(received=True)
    received = len(received_orders)
    complete_orders = Order.objects.filter(completed=True)
    complete = len(complete_orders)
    total = Order.objects.count()
    paginator = Paginator(orders, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'orders': page_obj,
        'pending': pending,
        'in_transit': in_transit,
        'received': received,
        'complete': complete,
        'total': total
    }
    return render(request, 'orders/home_page.html', context)


def order_add(request):
    if request.method == 'POST':
        form = AddOrderForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home_page')

    form = AddOrderForm()
    context = {
        'form': form
    }
    return render(request, 'orders/order_add.html', context)


def order_detail(request, pk):
    order = Order.objects.filter(id=pk)
    orders = Order.objects.all()

    return render(request, 'orders/order_detail.html',
                  context={'order': order, 'orders':orders})


def order_delete(request, pk):
    order = Order.objects.filter(id=pk).first()
    order.delete()
    return redirect('home_page')


def orders_in_transit(request, pk):
    order = Order.objects.filter(id=pk).first()
    order.pending = False
    order.completed = False
    order.received = False
    order.in_transit = True
    order.save()
    return redirect('in_transit_list')


def in_transit_list(request):
    orders = Order.objects.filter(in_transit=True).order_by('date_created')
    return render(request, 'orders/in_transit.html',
                    context ={'orders': orders})


def order_received(request, pk):
    order = Order.objects.filter(id=pk).first()
    order.pending = False
    order.completed = False
    order.received = True
    order.in_transit = False
    order.save()
    return redirect('received_list')


def received_list(request):
    orders = Order.objects.filter(received=True).order_by('date_created')
    return render(request, 'orders/received.html',
                    context ={'orders': orders})


def order_pending(request, pk):
    order = Order.objects.filter(id=pk).first()
    order.pending = True
    order.completed = False
    order.received = False
    order.in_transit = False
    order.save()
    return redirect('pending_list')


def pending_list(request):
    orders = Order.objects.filter(pending=True).order_by('date_created')
    return render(request, 'orders/pending.html',
                    context ={'orders': orders})


def complete_order(request, pk):
    order = Order.objects.filter(id=pk).first()
    order.pending = False
    order.completed = True
    order.received = False
    order.in_transit = False
    order.save()
    return redirect('completed_list')


def completed_list(request):
    orders = Order.objects.filter(completed=True).order_by('-date_created')
    return render(request, 'orders/completed.html',
                  context={'orders': orders})


def order_edit(request, pk):
    order = Order.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = EditOrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    form = EditOrderForm(instance=order)
    return render(request, 'orders/order_edit.html',
                  context={'order': order, 'form': form})


def amount(request):
    pending_orders = Order.objects.filter(pending=True)
    pending = len(pending_orders)
    in_transit_orders = Order.objects.filter(in_transit=True)
    in_transit = len(in_transit_orders)
    received_orders = Order.objects.filter(received=True)
    received = len(received_orders)
    complete_orders = Order.objects.filter(complete=True)
    complete = len(complete_orders)
    total = Order.objects.count()
    print(total)
    context = {
        'pending': pending,
        'in_transit': in_transit,
        'received': received,
        'complete': complete,
        'total': total
    }
    return render(request, 'orders/home_page.html', context)


def search(request):
    query = request.GET.get('q')
    orders = Order.objects.filter(
        Q(client__icontains=query) | Q(articul__icontains=query))
    return render(request, 'orders/home_page.html',
                  context={'orders': orders})