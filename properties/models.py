from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Property(models.Model):
    """
    A class to represnt a property eligible for review.
    """
    # Specifiy choices for dropdown option
    FLAT = 'Flat'
    TERRACE = 'Terrace house'
    SEMI = 'Semi-detached house'
    DETACHED = 'Detached house'
    BUNGALOW = 'Bungalow'
    SHARE = 'House share'
    HOUSING_CHOICES = [
        (FLAT, 'Flat'),
        (TERRACE, 'Terrace house'),
        (SEMI, 'Semi-detached house'),
        (DETACHED, 'Detached house'),
        (BUNGALOW, 'Bungalow'),
        (SHARE, 'House share'),
    ]
    DRAFT = '0'
    PUBLISHED = '1'
    STATUS = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    ]
    # Model fields
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    street_address = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Address Line 1'
    )
    address_street2 = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Address Line 2'
    )
    address_town = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Town'
    )
    address_county = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='County/Province/State'
    )
    address_postcode = models.CharField(
        max_length=35,
        verbose_name='Postal Code/Zip Code'
    )
    address_country = models.CharField(
        max_length=75,
        null=True,
        blank=True,
        verbose_name='Country'
    )
    num_of_bedrooms = models.PositiveIntegerField(null=True, blank=True)
    num_of_bathrooms = models.PositiveIntegerField(null=True, blank=True)
    type_of_property = models.CharField(
        max_length=30,
        choices=HOUSING_CHOICES,
        default=0,
        blank=False
    )
    for_rent = models.BooleanField(default=False)
    images = CloudinaryField(
        'image',
        default='placeholder',
        blank=True,
        null=True
    )
    ll_or_ea = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Landlord/Estate Agent'
        )
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=30,
        choices=STATUS,
        default=1,
        blank=False
    )
    likes = models.ManyToManyField(
        User, related_name='property_like', blank=True)

    class Meta:
        """
        Class to add Metadata, in this instance the ordering options
        """
        ordering = ['-created_on', 'title']
        verbose_name_plural = 'Properties'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + self.address_postcode)
        super(Property, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

    def number_of_likes(self):
        """Method counts the number of likes for each property
        entry in the database"""
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('property_detail', kwargs={'slug': self.slug})
