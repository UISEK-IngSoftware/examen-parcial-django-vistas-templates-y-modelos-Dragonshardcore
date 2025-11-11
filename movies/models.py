from django.db import models



class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    director_name = models.CharField(max_length=50)
    synopsis = models.TextField()  
    release_year = models.DateField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    