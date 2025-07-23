from django.urls import path
from users.views import UserView

urlpatterns = [
    path('<str:id>/', UserView.as_view(), name='user-detail')
]
