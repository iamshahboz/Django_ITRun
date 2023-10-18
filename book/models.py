from django.db import models
from .validators import validate_decimal, validate_integer,validate_string 
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


# book model
class Book(models.Model):
    class GenreChoices(models.TextChoices):
        CRIME = 'C'
        NON_FICTION = 'N'
        SCI_FICTION = 'S'
        PSYCHOLOGY = 'P'
        OTHER = 'O'
    title = models.CharField(max_length=255,validators=[validate_string])
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    isbn_number = models.PositiveIntegerField(validators=[validate_integer])
    genre = models.CharField(max_length=1, choices=GenreChoices.choices)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=5, decimal_places=2, \
        validators= [validate_decimal] )
    cover_image = models.ImageField(upload_to='books/',blank=True,null=True)
    

    def delete(self):
        self.cover_image.delete()
        super().delete()

    def __str__(self):
        return self.title

# author model
class Author(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

# rating model
class Rating(models.Model):
    book = models.ForeignKey('Book',on_delete=models.CASCADE, related_name='ratings')
    class RatingChoices(models.IntegerChoices):
        POOR = 1 #"P"
        FAIR = 2
        GOOD = 3 
        VERY_GOOD = 4
        EXCELLENT = 5
    rating = models.IntegerField(choices=RatingChoices.choices)

    def __str__(self):
        return str(self.book)
    
class UserProfileManager(BaseUserManager):
    """ Manager for user profiles """

    def create_user(self, email, name, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        """ Return string representation of our user """
        return self.email
    




