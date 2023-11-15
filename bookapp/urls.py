from django.urls import path

from bookapp import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('add/',views.add_book,name='add_book'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('book/<int:book_id>/', views.detail, name='detail'),
]