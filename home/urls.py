from django.urls import path 
from home import views
from django.http import HttpResponse


urlpatterns=[
    # path('hello/', views.say_hello),
    path('', views.home, name='home'),
    path('details/<int:todo_id>/',views.detail, name='details'),
    path('delete/<int:todo_id>/' , views.delete , name='delete'),
    path('update/<int:todo_id>', views.update, name='update'),
    path('create/', views.create, name='create'),
]