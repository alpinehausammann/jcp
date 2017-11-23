
from django.db import models

PICTURE_LOCATION_CHOICES = (
    ('Top','Top'),
    ('Left','Left'),
    ('Right','Right'),
    ('Bottom','Bottom'),
)

# Create your models here.
class Page(models.Model): #creates pages on website
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, default=None)

class Picture(models.model):
    upload = models.ImageField(
        upload_to='{}/uploads'.format(title),
        height_field=None,
        width_field=None,
        max_length=100
        )
    picture_position = models.CharField(
        max_length=5,
        choices=PICTURE_LOCATION_CHOICES,
        default=None
        )
    description = models.TextField()
    #if object is page:
    #page = models.ForeignKey()
    #elif object is content:
    #Content = models.ForeignKey(Content)

    def __str__(self):
        return self.title
class Content(models.model):
    title = models.CharField(max_length=255,default=None)
    body = models.TextField()

        #def contains_picture():
            #if radio button is pressed
            #access picture class
            #upload picture

class Post(models.Model):


    def service_request():
        SERVICE_CHOICES = (
            ('Carpentry', 'Carpentry'),
            ('Landscaping', 'Landscaping'),
            ('Maintenance', 'Maintenance'),
            ('Other','Other'),
            )

        f_name = models.CharField(max_length=50)
        l_name = models.CharField(max_length=50)
        email_address = models.CharField(max_length=100)
        phone = re.findallmodels.CharField(max_length=10)
        address = models.CharField(max_length=255)
        category = models.CharField(
            max_length=15,
            choices=SERVICE_CHOICES,
            default=None
            )
            if category == "Other":
                category_description = Models.CharField(max_length=20)
        description = models.TextField()
    def testimonials():
    def __str__(self):
        return self.title

# class Article(models.Model):
#     created_at = models.DateTimeField(auto_now_add = True)
#     title = models.CharField(max_length = 255)
#     upload = models.ImageField(
#             upload_to = '{}/uploads'.format(title), height_field = None,
#             width_field = None, max_length = 100
#     )
#     picture_position = models.CharField(max_length = 5, choices = PICTURE_LOCATION_CHOICES, default=None)
#     article_content = models.TextField()
#     order = models.IntegerField(default = 0)
#     page = models.ForeignKey(Page)
#
#     class Meta:
#         ordering = ['order',]
#
#         def __str__(self):
#             return self.title
