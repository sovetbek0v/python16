from django.db import models
from django.db.models import Choices
from model_utils.fields import StatusField

from account.models import User


class CreatedAtModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,
                                      null=True)

    class Meta:
        abstract = True


class Product(CreatedAtModel):
    # STATUS = Choices("Available", "Not existed")
    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    # status = StatusField()
    description = models.TextField()

    class Meta:
        ordering = ['title', 'price']

    def __str__(self):
        return self.title


class ProductReview(CreatedAtModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True)
    text = models.TextField()
    rating = models.PositiveIntegerField(default=1)

