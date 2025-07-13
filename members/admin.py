from django.contrib import admin
from .models import Trainer, Membership, ClassSchedule, Contact, Payment, Profile

# ✅ 1. Trainers
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 20

# ✅ 2. Memberships
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'plan', 'joined_at')
    search_fields = ('full_name', 'email', 'phone')
    list_filter = ('plan',)
    date_hierarchy = 'joined_at'
    list_per_page = 25

# ✅ 3. Class Schedules
@admin.register(ClassSchedule)
class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'trainer', 'date', 'time')
    list_filter = ('trainer', 'date')
    search_fields = ('title',)
    date_hierarchy = 'date'
    list_per_page = 20

# ✅ 4. Contact Enquiries
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at')
    search_fields = ('name', 'email')
    date_hierarchy = 'sent_at'
    list_per_page = 20

# ✅ 5. Payments
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'amount', 'payment_id', 'paid', 'created_at')
    list_filter = ('paid',)
    search_fields = ('full_name', 'payment_id')
    date_hierarchy = 'created_at'
    list_per_page = 25

# ✅ 6. Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_premium')
    search_fields = ('user__username', 'user__email')
    list_filter = ('is_premium',)
    list_per_page = 20

# ✅ 7. Users (Django User model)
# Django ka default User already included hota hai — koi custom register ki zarurat nahi!
