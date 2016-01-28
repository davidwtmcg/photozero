from django.contrib import admin

# Register your models here.
from .models import Photo, UserProfile

class PhotoModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp", "user"]
	#list_display_links = ["title"]
	list_filter = ["updated", "timestamp"]
	#list_editable = ["draft"]
	search_fields = ["title", "desription"]
	change_form_template = 'progressbarupload/change_form.html'
	add_form_template = 'progressbarupload/change_form.html'

	class Meta:
		model = Photo


class UserProfileModelAdmin(admin.ModelAdmin):
	class Meta:
		model = UserProfile


admin.site.register(Photo, PhotoModelAdmin)
admin.site.register(UserProfile, UserProfileModelAdmin)