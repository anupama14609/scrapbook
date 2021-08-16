from django.urls import path 
from ajaxapp.views import ScrapFriendView

urlpatterns = [ 
    path('', ScrapFriendView.as_view(), name='scrapfriend_view'),
    # path('django-view', MyView.as_view(), name='my-view'),
]