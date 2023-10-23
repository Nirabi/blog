from django.urls import path



from .views import Blogdeleteview,  Bloglistview, Blogupdateview, Blogdetailview, Blogcreateview, Blogdeleteview


urlpatterns = [
    path('post/<int:pk>/delete/',
        Blogdeleteview.as_view(), name='post_delete'),
    path('post/new/', Blogcreateview.as_view(), name='post_new'),
    path('post/<int:pk>/', Blogdetailview.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/',
        Blogupdateview.as_view(), name='post_edit'),
    path('',Bloglistview.as_view(),name='home'),
]