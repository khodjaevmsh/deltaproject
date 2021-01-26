from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search_result, name="search_results"),
    path('post/<slug:slug>/', views.post_detail, name='post_detail_url'),
    path('register/', views.register, name='register'),
    path('post/<slug:slug>/leave-comment',
         views.leave_comment, name='leave_comment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
