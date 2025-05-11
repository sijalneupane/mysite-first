
from django.urls import path,include
from . import views

app_name='food'
urlpatterns = [
    # /food
    # path('', views.index, name='index'),
    path('', views.IndexPageView.as_view(), name='index'),
    # /food/item
    path('<int:pk>/',views.DetailPageView.as_view(),name='detail'),
    #food/item
    path('item/', views.item, name='item'),
    # add item
    path('add/',views.CreateItem.as_view(),name='create_item'),
    # edit item
    path('update/<int:id>/',views.update_item,name='update_item'),
    # edit item
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
]
