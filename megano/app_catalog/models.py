from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Product(models.Model):
    class Meta:
        ordering = ['title']

    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    count = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=False, blank=True)
    fullDescription = models.TextField(max_length=1000, null=False, blank=True)
    freeDelivery = models.BooleanField(default=False)
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='products')
    # images = models.OneToOneField(Image, on_delete=models.CASCADE)
    # images = models.ImageField(upload_to='product_images_directory_path')
    # tags
    # reviews
    # rating


class Category(MPTTModel):
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True,
                            related_name='children', db_index=True)

    def __str__(self):
        return self.title
