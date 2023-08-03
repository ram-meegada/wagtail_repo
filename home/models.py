from django.db import models
from wagtail.fields import StreamField
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, PageChooserPanel, MultipleChooserPanel, MultiFieldPanel, InlinePanel
from streams import blocks
from django.shortcuts import render
from wagtail.contrib.routable_page.models import RoutablePageMixin, path, route
from modelcluster.fields import ParentalKey

class HomeImages(Orderable):
    page = ParentalKey("home.HomePage", related_name= "home_images")
    photos = models.ForeignKey("wagtailimages.Image", null=True, blank=True,  on_delete=models.SET_NULL, related_name='+')
    panels = [
        FieldPanel('photos')
    ]    

class FooterLinks(Orderable):    
    page = ParentalKey("home.HomePage", related_name= "footer_links")
    name_of_page = models.CharField(max_length=255, null=True, blank=True)
    links = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    panels = [
        FieldPanel("name_of_page"),
        PageChooserPanel('links')
    ]

class HomePage(RoutablePageMixin, Page):
    body = RichTextField(features=['bold', 'italic'], blank=True)
    home_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    some_url = models.ForeignKey("wagtailcore.Page", null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    content = StreamField(
        [
            ("call_action_block", blocks.CallToActionBlock()),
        ], null=True, blank=True, use_json_field=True
    )
    max_count = 1
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('body'),
                FieldPanel('home_image'),
                FieldPanel('some_url')
            ], heading="Main Matter"
        ),
        FieldPanel('content'),
        MultiFieldPanel([InlinePanel('home_images', max_num=7, min_num=1, label='HomeImages')], heading="Home Images"),
        MultiFieldPanel([InlinePanel('footer_links', max_num=15, label='Footer Link')], heading="Footer links"),
    ]
    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

    @route(r'^subscribers/$')
    def add_new(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context['extra'] = "This is a routable page."
        return render(request, "home/add_new.html", context)