from django.urls import path
from . import views

urlpatterns =[
    path('', views.login_page, name="login_page"),
    path('singup/', views.sing_up_page, name="singup"),
    path('create/', views.create_user, name="create_user"),
    path('singin/', views.home_page, name="home"),
    path('sing_out/', views.sing_out),
    path('create_note/',views.create_note, name="create_note"),
    path('home/', views.home_view, name="home"),
    path('delete/<int:task_id>', views.delete_task, name="delete_task"),
    path('update/<int:task_id>', views.update_view, name="update_task"),
    path('update/',views.update_task, name="update_task"),
]
