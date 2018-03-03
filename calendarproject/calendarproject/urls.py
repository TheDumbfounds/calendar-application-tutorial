from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('calendar', views.CalendarListView.as_view(), name='calendar'),
    path('signup', views.signup, name='signup'),
    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('entry/<int:pk>', views.EntryDetailView.as_view(), name='details'),
    path('entry/add', views.add, name='add'),
    path('entry/delete/<int:pk>', views.delete, name='delete'),
    path('admin/', admin.site.urls),
]
