from django.db import models


# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return f"{self.id}: {self.name}"
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=150)
#     price = models.DecimalField(max_digits=12, decimal_places=4)  # 9,999,999.9999
#     c_date = models.DateTimeField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.id}: {self.name}"

class Brand(models.Model):
    name = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    WARRANTY_INFORMATION = [('no_warranty', 'No warranty'),
                            ('six_months_warranty', '6 months warranty'),
                            ('one_week_warranty', '1 week warranty'),
                            ('three_year_warranty', '3 year warranty'),
                            ('three_months_warranty', '3 months warranty'),
                            ('lifetime warranty', 'Lifetime warranty'),
                            ('two_year_warranty', '2 year warranty'),
                            ('one_month_warranty', '1 month warranty'),
                            ('five_year_warranty', '5 year warranty'),
                            ('one_year_warranty', '1 year warranty')]
    SHIPPING_INFORMATION = [('ships_overnight', 'Ships overnight'),
                            ('ships_in_2_weeks', 'Ships in 2 weeks'),
                            ('ships_in_1_month', 'Ships in 1 month'),
                            ('ships_in_3_5_business_days', 'Ships in 3-5 business days'),
                            ('ships_in_1_2 business_days', 'Ships in 1-2 business days'),
                            ('ships_in_1_week', 'Ships in 1 week')]

    AVAILABILITY_STATUS = [('in_stock', 'In Stock'),
                           ('low_stock', 'Low Stock'),
                           ('out_of_stock', 'Out of Stock')]

    RETURN_POLICY = [('no_return_policy', 'No return policy'),
                     ('thirty_days_return_policy', '30 days return policy'),
                     ('ninety_days_return_policy', '90 days return policy'),
                     ('sixty_days_return_policy', '60 days return policy'),
                     ('seven_days_return_policy', '7 days return policy')]

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discountPercentage = models.DecimalField(max_digits=4, decimal_places=2)
    stock = models.IntegerField()
    sku = models.CharField(max_length=255)
    weight = models.FloatField()
    warrantyInformation = models.CharField(max_length=255, choices=WARRANTY_INFORMATION, default='no_warranty')
    shippingInformation = models.CharField(max_length=255, choices=SHIPPING_INFORMATION, default='ships_overnight')
    availabilityStatus = models.CharField(max_length=255, choices=AVAILABILITY_STATUS, default='in_stock')
    returnPolicy = models.CharField(max_length=255, choices=RETURN_POLICY, default='no_return_policy')
    minimumOrderQuantity = models.IntegerField()
    thumbnail = models.URLField()
    width = models.FloatField()
    height = models.FloatField()
    depth = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    barcode = models.CharField(max_length=255)
    qrCode = models.URLField(null=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name="products", on_delete=models.CASCADE)


class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField()
    reviewerName = models.CharField(max_length=255)
    reviewerEmail = models.EmailField()
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=25)
    product = models.ForeignKey(Product, related_name="tags", on_delete=models.CASCADE)


class ProductImage(models.Model):
    imagePath = models.URLField()
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
