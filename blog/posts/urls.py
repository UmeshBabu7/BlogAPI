from django.urls import path
from .import views

app_name='posts'
urlpatterns = [
    path('',views.post_list),
    path('detail/<int:id>/',views.post_detail,name='detail')
]