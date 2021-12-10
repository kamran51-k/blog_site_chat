from django.urls import path
from .views import about_view, contact_view, index_view, post_detail_view,register_request,login_request,logout_request

urlpatterns = [
    path('',index_view,name='index_page'),
    path('post-detail/<int:post_id>/',post_detail_view,name='detail_page'),
    path("register", register_request, name="register_page"),
    path("login", login_request, name="login_page"),
    path("logout", logout_request, name="logout_page"),
    path('about',about_view,name='about_page'),
    path('contact',contact_view,name='contact_page')



]