from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from streams import blocks
    
class FlexPage(Page):
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("speciality_and_habits", blocks.SpecialityAndHabitsBlock()),
            ("rich_text", blocks.RichTextBlock()),
            ("simple_rich_text", blocks.SimpleRichTextBlock()),
            ("list_display_block", blocks.ListDisplayBlock()),
            ("call_action_block", blocks.CallToActionBlock()),
        ], use_json_field=True, null=True, blank=True
    )
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('content'),
    ]    

class ContactUsPage(Page):
    text = models.TextField(null=False, blank=False)
    max_count = 1 
    content_panels = Page.content_panels + [
        FieldPanel('text')
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        contacts = ContactUsPage.objects.all()
        context["title"] = contacts.first().title
        return context