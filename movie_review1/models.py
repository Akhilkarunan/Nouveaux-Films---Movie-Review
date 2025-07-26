from django.db import models
from django.contrib.auth.models import User

# Models for movie details
class MovieModels(models.Model):
    Movie_name = models.CharField(max_length=50)
    Movie_language = models.CharField(max_length=50)
    Directer = models.CharField(max_length=50)  
    Release_date = models.DateField()
    description = models.TextField(null=True ,blank=True)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Uncomment if needed

    def __str__(self):
        return self.Movie_name

class Review(models.Model):
    movie = models.ForeignKey(MovieModels, on_delete=models.CASCADE, related_name='reviews')
    User_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=100 ,null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review of {self.movie.Movie_name}"
    

 