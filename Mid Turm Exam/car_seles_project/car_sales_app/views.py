from django.shortcuts import render,redirect
from . forms import CommentForm
from . import models
from .models import Car, Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
# Create your views here.

# @login_required  
# def buy_car(request,id):
#     ordered_car = Car.objects.get(id = id)

#     if ordered_car.quantity > 0:
#         ordered_car.quantity -= 1
#         ordered_car.save()

#         req_car = Order.objects.filter(user=request.user, car=ordered_car)

#         if req_car.exists():
#             order = req_car.first()
#             order.quantity += 1
#             order.save()
#             messages.success(request, 'Order placed succesfully')
#             return redirect('profile')
#         else:
#             order = Order.objects.create(user=request.user, car=ordered_car,quantity = 1)
#             messages.success(request, 'Order placed succesfully')
#             return redirect('profile')
#     else:
#         messages.error(request, 'Car is not available due to low quantity.')
#         return render(request, 'car_details.html')
    


@login_required  
def buy_car(request, id):
    print("line num 39")
    print(id)
    car = Car.objects.get(id=id)
    print("line num 42")
    print(car)
    if request.method == 'POST':
        if car.quantity > 0:
            car.quantity -= 1
            car.save()
            Order.objects.create(user=request.user, car=car)
            # Provide feedback to the user
            return redirect('profile')  # Redirect to car list or any other page
        else:
            # Handle case when car is out of stock
            messages.success(request, 'Car is not available due to low quantity.')
            return redirect('profile')
    else:
        # Handle case when the request method is not POST
        return redirect('detail_car', id=id)


    
class DetailPostView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.user = self.request.user
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object # Car model er object ekhane store korlam
        comments = car.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context