from django.urls import path
from TestApp import views

urlpatterns = [
    path('entreprise/create', views.add_entreprise, name='add-entreprise'),
    path('responsable/create', views.add_responsable, name='add-responsable'),
    path('pdl/create', views.add_pdl, name='add-pdl'),
    path('entreprise',views.view_entreprise),
    path('user/create',views.add_user,name='add-user'),
    path('users',views.getUsers,name='users'),
    path('login',views.login ,name='login'),
    path('entreprise/<int:id>/', views.get_entreprise_id, name='entreprise-detail'),
    path('responsable/<int:id>/', views.get_responsable_id, name='responsable-detail'),
    path('pdl/<int:id>/', views.get_pdl_id, name='pdl-detail'),

]
