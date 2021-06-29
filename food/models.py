from django.db import models
class Recipe(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    prep_time = models.CharField(max_length=100, null=False, blank=False)
    cook_time = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to="images/", null=False, blank=False)

    stars = models.SmallIntegerField(
        blank=False, null=False, default=1,
        choices=[
            (1,"Our star"),(2,"Two star"),(3,"Three stars"),(4,"Four stars"),(5,"Five stars")
        ]
    )
    posted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Ingredient(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    order = models.IntegerField(blank=False, null=False)
    recipe = models.ForeignKey(Recipe, blank=False, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title

class Step(models.Model):
    title = models.TextField(null=False, blank=False)
    order = models.IntegerField(blank=False, null=False)
    recipe = models.ForeignKey(Recipe, blank=False, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title
class Blog(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    author= models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    image = models.ImageField(upload_to="images/", null=False, blank=False)

    posted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class GetInTouch(models.Model):
    name = models.CharField(max_length=150,blank=False,null=False)
    email = models.CharField(max_length=150,blank=False,null=False)
    subject = models.CharField(max_length=150,blank=False,null=False)
    message = models.TextField(blank=False,null=False)
    sent_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class GetEmail(models.Model):
    email = models.CharField(max_length=150,blank=False,null=False)
    def __str__(self):
        return self.email
# Create your models here.
