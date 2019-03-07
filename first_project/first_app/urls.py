from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('',views.index,name="index"),
    path('form/',views.NewUser,name="NewUser"),
    path('<int:id>/<str:gender>/',views.medical_conditions,name="medical_conditions"),
]
