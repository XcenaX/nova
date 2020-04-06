from django.urls import path

from . import views

app_name= "main"
urlpatterns = [
    path('', views.index, name='index'),  
    path('404', views.not_found, name='not_found'),
    path('about-us', views.about, name='about'),
    path('base', views.base, name='base'),
    path('blogs', views.blogs, name='blogs'),
    path('blog/<int:id>', views.blog, name='blog'),
    path('career', views.career, name='career'),
    path('category/<slug:category>', views.category_blogs, name='blog_category'),
    path('contact-us', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('pricing', views.pricing, name='pricing'),
    path('privacy', views.privacy, name='privacy'),
    path('rawImages', views.raw_images, name='raw_images'),
    path('registration', views.registration, name='registration'),
    path('services', views.services, name='services'),
    path('terms', views.terms, name='terms'),
    path('typography', views.typography, name='typography'),  
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('admin-panel', views.admin_panel, name='admin-panel'),
    path('weather', views.weather, name='weather'),
]