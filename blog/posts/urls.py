from django.urls import path
from .import views

app_name="posts"

urlpatterns = [
    path('create/',views.post_create),
    path('detail/<int:id>',views.post_detail,name='detail'),
    path('list/',views.post_list,name='list'),
    path('update/<int:id>/',views.post_update),
    path('delete/<int:id>/',views.post_delete)
    
]
