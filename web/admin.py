from django.contrib import admin
from .models import *


class HomeAdmin(admin.ModelAdmin):
	list_display = ('name','img','position','name_1','img_1','position_1','name_2','img_2','position_2',)
	list_filter = ("name","name_1","name_2",)


class Home_1Admin(admin.ModelAdmin):
	list_display = ('heading','image',)
	list_filter = ("heading",)
	search_fields = ['heading']


class AboutAdmin(admin.ModelAdmin):
	list_display = ('image','title','content',)
	list_filter = ("title",)
	list_editable = ['title']
	search_fields = ['title']


class EventsAdmin(admin.ModelAdmin):
	list_display = ('image','title','text',)
	list_filter = ("title",)
	search_fields = ['title']


class MinistriesAdmin(admin.ModelAdmin):
	list_display = ('image','title','content',)
	list_filter = ("title",)
	search_fields = ['title']


class PrayerAdmin(admin.ModelAdmin):
	list_display = ('name','email','subject','message',)
	list_filter = ("name",)
	search_fields = ['subject']


class Ben_testAdmin(admin.ModelAdmin):
	list_display = ('name','image','bio')
	list_filter = ("name",)
	search_fields = ['subject']



admin.site.register(Ben_test,Ben_testAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Login)
admin.site.register(Prayer, PrayerAdmin)
admin.site.register(Ministries, MinistriesAdmin)
admin.site.register(Gallary)
admin.site.register(About, AboutAdmin)
admin.site.register(Home_1, Home_1Admin)
admin.site.register(Events, EventsAdmin)
admin.site.register(Construction_history)
