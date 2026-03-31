from django.urls import path
from .views import *

urlpatterns = [
    path('',home_page, name='home_page'),
    path('login_page/',login_page, name='login_page'),
    path('logout_page/',logout_page, name='logout_page'),

    path('category/create/',category_create, name='category_create'),
    path('category/<int:pk>/edit/',category_edit, name='category_edit'),
    path('category/<int:pk>/delete/',category_delete, name='category_delete'),
    path('category/list/',category_list, name='category_list'),

    path('product/create/',product_create, name='product_create'),
    path('product/<int:pk>/edit/',product_edit, name='product_edit'),
    path('product/<int:pk>/delete/',product_delete, name='product_delete'),
    path('product/list/',product_list, name='product_list'),

    path('kafedra/create/',kafedra_create, name='kafedra_create'),
    path('kafedra/<int:pk>/edit/',kafedra_edit, name='kafedra_edit'),
    path('kafedra/<int:pk>/delete/',kafedra_delete, name='kafedra_delete'),
    path('kafedra/list/',kafedra_list, name='kafedra_list'),

    path('teacher/create/',teacher_create, name='teacher_create'),
    path('teacher/<int:pk>/edit/',teacher_edit, name='teacher_edit'),
    path('teacher/<int:pk>/delete/',teacher_delete, name='teacher_delete'),
    path('teacher/list/',teacher_list, name='teacher_list'),

    path('group/create/',group_create, name='group_create'),
    path('group/<int:pk>/edit/',group_edit, name='group_edit'),
    path('group/<int:pk>/delete/',group_delete, name='group_delete'),
    path('group/list/',group_list, name='group_list'),

    path('student/create/',student_create, name='student_create'),
    path('student/<int:pk>/edit/',student_edit, name='student_edit'),
    path('student/<int:pk>/delete/',student_delete, name='student_delete'),
    path('student/list/',student_list, name='student_list'),
    path('profile/',profile, name='profile'),

]