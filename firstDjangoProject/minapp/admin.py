from django.contrib import admin
from .models import MiniAppCategory, MiniAppReview, Organization, UserProfile
# Register your models here.
class MiniAppReviewInline(admin.TabularInline):
    model = MiniAppReview
    extra = 2
    
class MiniApCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [MiniAppReviewInline]
    
class MiniAppOrganization(admin.ModelAdmin):
    list_display = ('name', 'location', )
    filter_horizontal = ('app_varieties',)
    
class MiniAppUserProfile(admin.ModelAdmin):
    list_display = ('user', 'user_name', 'bio')
    
    
    
    
admin.site.register(MiniAppCategory, MiniApCategoryAdmin)
admin.site.register(MiniAppReview)
admin.site.register(Organization, MiniAppOrganization)
admin.site.register(UserProfile, MiniAppUserProfile)



