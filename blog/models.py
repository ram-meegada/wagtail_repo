from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from django.shortcuts import render
from streams import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
# Create your models here.\

#################### -BlogIndexPage- ###########################
class BlogIndexPage(RoutablePageMixin, Page):
    custom_title = models.CharField(max_length=255, blank=False, null=True, help_text="This is blog Index Page")

    content_panels = Page.content_panels + [
        FieldPanel("custom_title")
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        parent = BlogIndexPage.objects.get(custom_title=self.custom_title)
        children = BlogDetailPage.objects.child_of(parent).public()
        context["posts"] = children
        return context
    
    @route(r'^latest-blogs/$', name="latest_blog_posts")
    def latest_blog_posts_view(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context["posts"] = context["posts"][:1]
        return render(request, "blog/latest_blogs.html", context)
    
    def get_sitemap_urls(self, request=None):
        sitemap = super().get_sitemap_urls(request)
        sitemap.append({
            "location": self.full_url + self.reverse_subpage("latest_blog_posts"),
            "lastmod": self.last_published_at
        })
        return sitemap

#################### -BlogDetailPage- ###########################
class BlogDetailPage(Page):
    custom_title = models.CharField(max_length=255, blank=False, null=True, help_text="This is blog details Page")
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL
    )
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("rich_text", blocks.RichTextBlock()),
            ("simple_rich_text", blocks.SimpleRichTextBlock()),
            ("list_display_block", blocks.ListDisplayBlock()),
            ("call_action_block", blocks.CallToActionBlock()),
        ], use_json_field=True, null=True, blank=True
    )
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("blog_image"),
        FieldPanel("content"),
    ]