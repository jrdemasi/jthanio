from django.db import models
from django import forms
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks
from wagtailcodeblock.blocks import CodeBlock

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.snippets.models import register_snippet

class BlogIndexPage(Page):
    intro = models.CharField(max_length=500)


    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        paginator = Paginator(blogpages, 5)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            blogpages = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            blogpages = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            blogpages = paginator.page(paginator.num_pages)
        context['blogpages'] = blogpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

@register_snippet
class BlogPostTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPost',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogPost(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField(
        [
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('page', blocks.PageChooserBlock()),
            ('document', DocumentChooserBlock()),
            ('media', EmbedBlock()),
            ('html', blocks.RawHTMLBlock(label='Raw HTML')),
            ('code', CodeBlock(label='Code')),
        ])
    tags = ClusterTaggableManager(through=BlogPostTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    
    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        InlinePanel('gallery_images', label="Gallery images"),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]

class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPost.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context
        
@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'

class BlogPostGalleryImage(Orderable):
    page = ParentalKey(BlogPost, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
