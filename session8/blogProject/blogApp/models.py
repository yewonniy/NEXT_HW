from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    time = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()

    def __str__(self):
        return self.content

class Recomment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="recomments")
    re_content = models.TextField()

    def __str__(self):
        return self.content