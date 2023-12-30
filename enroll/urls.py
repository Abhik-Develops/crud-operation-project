from django.urls import path
from enroll.views import *

urlpatterns = [
    path('', add_show, name="addandshow"),
    path('delete/<int:id>/', delete_data, name="deletedata"),
    path('update/<int:id>/', update_data, name='updatedata'),
]
