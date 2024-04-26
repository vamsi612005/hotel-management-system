from django.urls import path
from . import views

urlpatterns = [
    path('',views.hotelhome,name='hotelhome'),
    path('uploadhotel/',views.uploadhotel,name='uploadhotel'),
    path('viewhotel/',views.viewhotel,name='viewhotel'),
    path('hotelviewprofile/',views.hotelviewprofile,name='hotelviewprofile'),
    path('hoteladdemail',views.hoteladdemail,name='hoteladdemail'),
    path('hoteladdfirstname',views.hoteladdfirstname,name='hoteladdfirstname'),
    path('hoteladdlastname',views.hoteladdlastname,name='hoteladdlastname'),
    path('hotelstaffmanagementht',views.hotelstaffmanagementht,name='hotelstaffmanagementht'),
    path('hoteladdstaff',views.hoteladdstaff,name='hoteladdstaff'),
    path('deletehotel',views.deletehotel,name='deletehotel'),
    path('updatehotel/<int:obj_id>/', views.updatehotel, name='updatehotel'),
    path('deletestaff',views.deletestaff,name='deletestaff'),
    path('updatestaff/<int:obj_id>/', views.updatestaff, name='updatestaff'),
    path('hotelroombooking',views.hotelroombooking,name="hotelroombooking"),
]