from django.db import models

class Image(models.Model):
        #caption=models.CharField(max_length=100)
        image=models.ImageField(upload_to="myimage")
        date=models.DateTimeField(auto_now_add=True)

#def __str__(self):
        # return self.caption
