from django.contrib import admin

from expenses_tracker.models import Profile, Expense

admin.site.register(Profile)
admin.site.register(Expense)
