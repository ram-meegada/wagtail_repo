from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import PageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=255, help_text="Add your title", null=True, blank=True)
    text = blocks.TextBlock(help_text="Add additional text", null=True, blank=True)

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "user"
        label = "Title And Text"
class SpecialityAndHabitsBlock(blocks.StructBlock):
    speciality = blocks.CharBlock(max_length=255, help_text="Add speciality", null=True, blank=True)
    habits = blocks.CharBlock(max_length=255, help_text="Add habits", null=True, blank=True)

    class Meta:
        template = "streams/speciality_habits_Block.html"
        icon = "edit"
        label = "Speciality And Habits"

class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        template = "streams/rich_text_block.html"
        icon = "doc-full"
        label = "Full Rich Text Comment"

class SimpleRichTextBlock(blocks.RichTextBlock):
    def __init__(
        self,
        required=True,
        help_text=None,
        editor="default",
        features=None,
        max_length=None,
        validators=(),
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.features = ['bold', 'italic', 'link']
    class Meta:
        template = "streams/rich_text_block.html"
        icon = "comment"
        label = "Simple Rich Text Comment"

class ListDisplayBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=255)
    list_blocks = blocks.ListBlock(blocks.StructBlock(
        [
            ("image", ImageChooserBlock(required=True)),
            ("title", blocks.CharBlock(required=True)),
            ("text", blocks.CharBlock(required=False)),
            ("link", blocks.URLBlock(required=False)),
        ]
    ))
    class Meta:
        template = "streams/list_display_block.html"
        icon = "bars"
        label = "list display block"

class CallToActionValue(blocks.StructValue):
    def button(self):
        internal_page = self.get('internal_page')
        external_url = self.get('external_url')    
        if internal_page:
            return internal_page.url
        elif external_url:
            return external_url
        return None

class CallToActionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    text = blocks.RichTextBlock(required=False, features=["bold", "italic"])
    internal_page = PageChooserBlock(required=False)
    external_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default="Learn More")
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        return context
    class Meta:
        template = "streams/call_action_block.html"
        icon = "cog"
        label = "Call to Action block"
        value_class = CallToActionValue