from django.urls import include, path
from . import views
from . import api

urlpatterns = [
    # INDEX PAGE WITH LINKS
    path('', views.AirlineList.as_view(), name='index'),
    
    # REST ENDPOINTS
    path('api/airlines_list', api.AirlinesList.as_view(), name='airlines_list_api'),
    path('api/airline_info/<int:pk>', api.AirlineDetail.as_view(), name='airline_detail_api'),
    path('api/airport_list', api.AirportList.as_view(), name='airport_list_api'),
    path('api/airport_info/<int:pk>', api.AirportDetail.as_view(), name='airport_detail_api'),
    path('api/equipment_list', api.EquipmentList.as_view(), name='equipment_list_api'),
    path('api/equipment_info/<int:pk>', api.EquipmentDetail.as_view(), name='equipment_detail_api')
]