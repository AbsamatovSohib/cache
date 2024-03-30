from django.contrib import admin
from product.models import Product


# @admin.site(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "id", "amount")


admin.site.register(Product, ProductAdmin)
