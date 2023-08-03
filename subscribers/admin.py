from django.contrib import admin
from .models import (Subscriber,)
from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)
# Register your models here.

class SubscriberModelAdmin(ModelAdmin):
    model = Subscriber
    menu_label = 'Subscribers'  # ditch this to use verbose_name_plural from model
    menu_icon = 'placeholder'  # change as required
    menu_order = 300  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('email', 'full_name')
    list_filter = ('email', 'full_name')
    search_fields = ('email', 'full_name')


modeladmin_register(SubscriberModelAdmin)    