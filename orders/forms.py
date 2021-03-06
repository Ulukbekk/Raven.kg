from django import forms

from orders.models import Order


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('client', 'insta', 'address', 'phone', 'model',
                  'color', 'size', 'amount', 'articul', 'price'
                  )


class EditOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('client', 'insta', 'address', 'phone', 'model',
                  'color', 'size', 'amount', 'articul', 'price', 'pending',
                  'in_transit', 'received', 'completed'
                  )
