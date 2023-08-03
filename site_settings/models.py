from django.db import models
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
# Create your models here.

@register_setting
class SocialMediaSettings(BaseSiteSetting):
    facebook = models.URLField(null=True, blank=True, help_text="Facebook url")
    google = models.URLField(null=True, blank=True, help_text="Google url")
    twitter = models.URLField(null=True, blank=True, help_text="twitter url")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("google"),
            FieldPanel("twitter")
        ], heading="Social Media Settings")
    ]