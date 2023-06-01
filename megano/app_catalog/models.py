from django.db import models
from django.db.models import Sum
from mptt.models import MPTTModel, TreeForeignKey

from app_auth.models import Profile


def images_dir_path(instance: "Images", filename: str) -> str:
    return "products/product_{pk}/{filename}".format(
        pk=instance.product.pk,
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

    def save(self, *args, **kwargs):
        """
        Пересчет рейтинга после добавления нового отзыва.
        """
        if not self.pk:
            res = self.product.reviews.all().aggregate(Sum('rate'))
            rate_sum = res['rate__sum']
            rate_num = self.product.reviews.all().count()
            rate_sum += int(self.rate)
            rate_num += 1
            self.product.rating = round((rate_sum/rate_num), 1)
            self.product.save()
        super(ProductReviews, self).save(*args, **kwargs)


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
    tags = models.ManyToManyField('Tag', null=True)
    specifications = models.ManyToManyField('Specifications', null=True)
    rating = models.DecimalField(default=3, max_digits=2, decimal_places=1)
    products_limited = models.BooleanField(default=False)
    banner = models.BooleanField(default=False)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True,
                            related_name='children', db_index=True)
    image = models.ImageField(upload_to='categories', null=True, max_length=255)

    def __str__(self):
        return self.title


class Specifications(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name


