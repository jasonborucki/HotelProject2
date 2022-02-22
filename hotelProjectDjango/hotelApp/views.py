from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd
from django.urls import reverse_lazy
from .models import PredResults, Results
import plotly.express as px
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

csv = pd.read_csv(r'C:\Users\mjasb\DjangoCSV.csv')
fig = px.histogram(csv, x="is_canceled", color="lead_time_range")


class CustomLoginView(LoginView):
    template_name = 'hotelApp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('hotelApp:home')


class TaskList(LoginRequiredMixin,ListView):
    model = PredResults
    context_object_name = 'home'




def hotelApp(request):
    return render(request, 'hotelApp/hotelApp.html')


def predict_chances(request):

    if request.POST.get('action') == 'post':

        adults = float(request.POST.get('adults'))
        repeated_guest = float(request.POST.get('repeated_guest'))
        hotel_type = float(request.POST.get('hotel_type'))
        direct_binary = float(request.POST.get('direct_binary'))
        children = float(request.POST.get('children'))
        babies = float(request.POST.get('babies'))
        cancellations_binary = float(request.POST.get('cancellations_binary'))
        uncanceled_binary = float(request.POST.get('uncanceled_binary'))
        booking_changes = float(request.POST.get('booking_changes'))
        waiting_list = float(request.POST.get('waiting_list'))
        required_parking = float(request.POST.get('required_parking'))
        special_requests = float(request.POST.get('special_requests'))
        average_rate = float(request.POST.get('average_rate'))
        lead_time = float(request.POST.get('lead_time'))

        model = pd.read_pickle(r'C:\Users\mjasb\hotel.pickle')

        # Make prediction
        result = model.predict([[adults, repeated_guest, hotel_type, direct_binary, children, babies, cancellations_binary, uncanceled_binary, booking_changes, waiting_list, required_parking, special_requests, average_rate, lead_time]])

        classification = result[0]
        PredResults.objects.create(adults=adults, repeated_guest=repeated_guest, hotel_type=hotel_type,
                                   direct_binary=direct_binary,children=children, babies=babies, cancellations_binary=cancellations_binary,
                                   uncanceled_binary=uncanceled_binary,booking_changes=booking_changes, waiting_list=waiting_list, required_parking=required_parking,
                                   special_requests=special_requests,average_rate=average_rate, lead_time=lead_time, classification=classification)

        print(classification)
        return JsonResponse({'result': classification, 'adults': adults,
                             'repeated_guest': repeated_guest, 'hotel_type': hotel_type, 'direct_binary': direct_binary,'children': children, 'babies': babies,
                             'cancellations_binary': cancellations_binary, 'uncanceled_binary': uncanceled_binary, 'booking_changes': booking_changes,'waiting_list': waiting_list, 'required_parking': required_parking,
                             'special_requests': special_requests, 'average_rate': average_rate, 'lead_time': lead_time},
                            safe=False)


class ViewResults(LoginRequiredMixin,ListView):
    model = Results
    context_object_name = 'view_results'


