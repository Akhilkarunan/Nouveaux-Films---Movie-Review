from django.shortcuts import render ,redirect ,get_object_or_404   
 # convenient shortcut function  ,getting an object from a database using a model’s manager , get a single object based on a query

from django.views.generic import View  ,UpdateView ,DeleteView ,CreateView

from movie_review1 import models

from .models import MovieModels ,Review 

from movie_review1.forms import Userform ,LoginForm ,ReviewForm ,MovieForm

from movie_review1.models import User

from django.contrib.auth import authenticate ,logout ,login

from django.contrib.auth.decorators import login_required

from  django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.core.mail import send_mail








def is_user(fn):

    def wrapper(request,**kwargs):

        id = kwargs.get("pk")

        obj = MovieModels.objects.get(id=id)

        if obj.User_id == request.user:

            return fn(request,**kwargs)
        
        else:

            return redirect("login")
    
    return wrapper


# def is_review_user(fn):

#     def wrapper(request,**kwargs):

#         id = kwargs.get("pk")

#         obj = Review.objects.get(id=id)

#         if obj.user_id == request.user:

#             return fn(request,**kwargs)
        
#         else:

#             return redirect("login")
    
#     return wrapper

# Create your views here.

class RegistraionView(View):  #email

    def get(self,request):

        form=Userform

        return render(request,"registration.html",{"form":form})
    

    def post(self,request):

        form=Userform(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            User.objects.create_user(**form.cleaned_data)

            #smtp email sending

            subject ="Welcome to Nouveaux Films!"

            message ='Welcome to Nouveaux Films! ' \
            'We re thrilled to have you join our community of movie enthusiasts. ' \
            'Get ready to explore, review, and share your favorite films with us.' \
            
            ' Need help? Contact us at support@nouveauxfilms.com.' \
            '' \
            '' \
            ' © 2025 Nouveaux Films. All rights reserved.'

            from_email ='akhilkarunan0@gmail.com'

            recipient_list =[form.cleaned_data.get('email')]

            send_mail(subject,message,from_email,recipient_list,fail_silently=False)

            return redirect ("login")


class LoginView(View):

    def get(self, request):
        form = LoginForm()  # Corrected form initialization
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pword = form.cleaned_data.get("password")
            
            user = authenticate(request, username=uname, password=pword)

            if user:
                login(request, user)  # Corrected function (lowercase `login`)
                return redirect("movie_list")  # Redirect to movie list page
            
        return render(request, "login.html", {"form": form})  # Show form with errors





class Add_movie(View):

    def get(slef,request):

        form =MovieForm

        return render(request,"add_movie.html",{"form":form})
    
    def post (self,request):

        form = MovieForm(request.POST,request.FILES)  #for image upload

        if form.is_valid():

            MovieModels.objects.create(**form.cleaned_data)

            return redirect("movie_list")




class MovieUpdateView(UpdateView):

    model = MovieModels

    fields = ['Movie_name','Movie_language','Directer','Release_date','description','poster']

    template_name = 'movieupdate.html'

    success_url = reverse_lazy('movie_list')



class Movie_list(View):

 def get(self,request):

    movies =MovieModels.objects.all()
    
    return render(request,"movie_list.html",{'movies':movies})  




class Movie_detail(View):
  
  def get(self,request, pk):
    movie = get_object_or_404(MovieModels, pk=pk)
    reviews = movie.reviews.all()  
    return render(request, 'movie_detail.html', {'movie': movie, 'reviews': reviews}) 

class MovieDeleteview(DeleteView):

    model =MovieModels

    template_name ="MovieDeleted.html"

    success_url = reverse_lazy("movie_list")







# @method_decorator(decorator=is_user, name="dispatch")
class AddReviewView(View):

    def get(self, request, **kwargs):
        id = kwargs.get("pk")
        movie =MovieModels.objects.get(id=id)
        form = ReviewForm()
        return render(request, "add_review.html", {"form": form, "movie": movie})

    def post(self, request, **kwargs):
        id = kwargs.get("pk")
        data =MovieModels.objects.get(id=id)
        
        form = ReviewForm(request.POST)
        

        if form.is_valid():
            Review.objects.create(**form.cleaned_data,User_id=request.user,movie=data)

        form = ReviewForm

        return redirect("movie_list")   
            
            

        
    


@method_decorator(decorator=is_user, name="dispatch")
class ReviewUpdateView(UpdateView):

    model = Review

    fields = ['rating','comment']

    template_name = 'Reviewupdate.html'

    success_url = reverse_lazy('movie_list')
    

@method_decorator(decorator=is_user, name="dispatch")
class ReviewDeleteview(DeleteView):

    model =Review

    template_name ="reviewDeleted.html"

    success_url = reverse_lazy("movie_list")    





#logout

class Signout(View):

    def get(self,request) :
    

      logout(request)

      print(request.user)

      return redirect("login")  



            





            
            

        


            