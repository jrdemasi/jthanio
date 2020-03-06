from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    body = StreamField(
        [
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('page', blocks.PageChooserBlock()),
            ('document', DocumentChooserBlock()),
            ('media', EmbedBlock()),
            ('html', blocks.RawHTMLBlock(label='Raw HTML')),
        ])


    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
