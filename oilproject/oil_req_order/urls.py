from oil_req_order import views
from django.urls import path
urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('form',views.form)
]