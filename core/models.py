from django.db import models

PICTURE_LOCATION_CHOICES = (
    ('Top','Top'),
    ('Left','Left'),
    ('Right','Right'),
    ('Bottom','Bottom'),
)

# Create your models here.
class Page(models.Model): #creates pages on website
    created_at = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 255, default=None)
    upload = models.ImageField(
            upload_to ='{}/uploads'.format(title), height_field = None, 
            width_field = None, max_length = 100
    )
    picture_position = models.CharField(max_length = 5, choices = PICTURE_LOCATION_CHOICES, default=None)
    main_content = models.TextField()

    def __str__(self):
        return self.title
    
class Post(models.Model):
    PROBLEM_CHOICES = (
        ('Carpentry', 'Carpentry'),
        ('Landscaping', 'Landscaping'),
        ('Maintenance', 'Maintenance'),
        ('Other','Other'),
    )

    f_name = models.CharField(max_length = 255)
    l_name = models.CharField(max_length = 254)
    email_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length = 255)
    category = models.CharField(max_length = 15, choices=PROBLEM_CHOICES, default=None)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 255)
    upload = models.ImageField(
            upload_to = '{}/uploads'.format(title), height_field = None,
            width_field = None, max_length = 100
    )
    picture_position = models.CharField(max_length = 5, choices = PICTURE_LOCATION_CHOICES, default=None)
    article_content = models.TextField()
    order = models.IntegerField(default = 0)
    page = models.ForeignKey(Page)

    class Meta:
        ordering = ['order',]

        def __str__(self):
            return self.title
