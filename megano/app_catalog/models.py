from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from app_auth.models import Profile


def images_dir_path(instance: "Product", filename: str) -> str:
    return "products/product_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename
    )


class Images(models.Model):
    images = models.ImageField(upload_to=images_dir_path, null=True, max_length=255)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')


class ProductReviews(models.Model):
    author = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    text = models.TextField(max_length=1000, null=False, blank=True)
    rate = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews')


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
    # images = models.ForeignKey(Images, on_delete=models.CASCADE, null=True, related_name='product')
    # images = models.ImageField(upload_to='product_images_directory_path')
    # tags
    # rating


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Category(MPTTModel):
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True,
                            related_name='children', db_index=True)

    def __str__(self):
        return self.title
