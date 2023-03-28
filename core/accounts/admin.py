from django.contrib import admin
from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'birth_date')
    list_filter = ('id', 'email')
    search_fields = ('email',)
    fields = ('email', 'gender', 'birth_date', 'subscriptions', 'commented_post')
    readonly_fields = ('id', 'birth_date')


admin.site.register(Account, AccountAdmin)
