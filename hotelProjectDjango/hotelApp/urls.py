
from django.urls import path
from . import views
from .views import CustomLoginView, TaskList, ViewResults
from django.contrib.auth.views import LogoutView

app_name = 'hotelApp'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="hotelApp:login"), name="logout"),
    path('', TaskList.as_view(), name="home"),
    path('hotelApp/', views.predict_chances, name="submit_prediction"),
    path('results/', ViewResults.as_view(), name="view_results"),
]
