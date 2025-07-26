"""
URL configuration for movie_review project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie_review1 import views
from django.contrib.auth.views import LoginView


#test image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',views.RegistraionView.as_view(),name="register"),  #registration of user
    
    path("login/",views.LoginView.as_view(),name ="login"),
    path("movielist/",views.Movie_list.as_view(),name="movie_list"),
    path('movie/<int:pk>/', views.Movie_detail.as_view(), name='movie_detail'),
    path('movie/<int:pk>/review', views.AddReviewView.as_view(), name='add_review'),
    path('add-movie/', views.Add_movie.as_view(), name='add_movie'),
    path('logout/',views.Signout.as_view(), name='logout'),
    path('movieupdate/<int:pk>',views.MovieUpdateView.as_view(),name='updatemovie'),
    path("moviedelete/<int:pk>",views.MovieDeleteview.as_view(),name="delete"),
    path('reviewupdate/<int:pk>',views.ReviewUpdateView.as_view(),name="reviewupdate"),
    path("reviewdelete/<int:pk>",views.ReviewDeleteview.as_view(),name='reviewdelete'),

    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)