from django import forms
from  .models import Review ,MovieModels


class Userform(forms.Form):

     username = forms.CharField(max_length=100)

     first_name =forms.CharField(max_length=100)

     last_name =forms.CharField(max_length=100)

     password =forms.CharField(widget=forms.PasswordInput)
 
     email=forms.EmailField()


class LoginForm(forms.Form):
    username  =forms.CharField(max_length=50)
    password  =forms.CharField(max_length=50,widget=forms.PasswordInput)     


class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieModels  # Use your model name (Movie or MovieModels)
        fields = ['Movie_name', 'Movie_language', 'Directer', 'Release_date', 'description', 'poster']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'Release_date': forms.DateInput(attrs={'type': 'date'}),
        }



class ReviewForm(forms.ModelForm):

     class Meta:

          model =Review
          fields = ['username','rating','comment']
          widgets ={
               "comment" : forms.Textarea(attrs={'rows':4}),
          }

    


   
