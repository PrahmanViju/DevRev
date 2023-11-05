from django.contrib import admin

from .models import Order
from .models import Order, User, Company, UserInField

admin.site.register(Order)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'password')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'company_id', 'order_description', 'company_address', 'status')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'company_address', 'city')


class UserInFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_number', 'company_id', 'address_id', 'status')


admin.site.register(Order, OrderAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Company, CustomerAdmin)
admin.site.register(UserInField, UserInFieldAdmin)