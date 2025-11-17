from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    author_img = models.ImageField()
    image = models.CharField(max_length=200)
    content = RichTextField()
    # content = models.TextField()
    description = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    likes =models.PositiveBigIntegerField(default=0)
    slug = models.SlugField()
    
    def __str__(self):
        return self.author
    
class Comment (models.Model):
    blog_post = models.ForeignKey(Post,related_name='comment', on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Commented by {self.name} on {self.blog_post.title}"