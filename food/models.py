from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    # email=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=225)
    item_desc = models.CharField(max_length=225)
    item_price = models.IntegerField()    
    item_image = models.CharField(max_length=500,default="https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png")
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("food:detail",kwargs={"pk": self.pk})

    def __str__(self):
        return self.item_name