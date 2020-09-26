from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtailstreamforms.blocks import WagtailFormBlock
from wagtail.core import blocks
from wagtail.core.blocks import DateBlock, DateTimeBlock, URLBlock, EmailBlock, TimeBlock, StreamBlock, ChoiceBlock
from wagtail.core.blocks import DateTimeBlock, TimeBlock, BlockQuoteBlock, PageChooserBlock, ListBlock, BooleanBlock, TextBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.search import index
from wagtailgeowidget.blocks import GeoBlock, GeoAddressBlock
from wagtailgeowidget.edit_handlers import GeoPanel
from wagtail.embeds.oembed_providers import youtube, vimeo

class BasicPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('table', TableBlock()),
        ('BlockQuoteBlock', BlockQuoteBlock()),
        ('URLBlock', URLBlock()),
        ('EmailBlock', EmailBlock()),
        ('DateBlock', DateBlock()),
        ('TimeBlock', TimeBlock()),
        ('DateTimeBlock', DateBlock()),
        ('PageChooserBlock', PageChooserBlock()),
        ('DocumentChooserBlock', DocumentChooserBlock()),
        ('IframeBlock', TextBlock()),
        ('EmbedBlock', EmbedBlock()),
        ('form', WagtailFormBlock()),
        ('show_business_hours', BooleanBlock(required=False, help_text="If checked, the library hours will display on the page", template='basic_page/blocks/business_hours.html', icon='user')),
        ('show_next_closure', BooleanBlock(required=False, help_text="If checked, the next library closure will display", template='basic_page/blocks/next_closure.html', icon='user')),
        ('show_all_closures', BooleanBlock(required=False, help_text="If checked, all upcoming library closures will be shown", template='basic_page/blocks/all_closures.html', icon='user')),
        ('map', blocks.StructBlock([
            ('address', GeoAddressBlock(required=True)),
            ('map', GeoBlock(address_field='address')),
        ], template='basic_page/blocks/map.html', icon='user')),
        ('bookClub', blocks.StructBlock([
            ('book_club_name', blocks.CharBlock()),
            ('book_club_day_of_the_week', blocks.TextBlock()),
            ('book_club_PDF', DocumentChooserBlock(required=False)),
            ('book_club_time', blocks.TimeBlock()),
            ('books', blocks.StreamBlock(
                [
                    ('book', blocks.StructBlock([
                        ('book_name', blocks.CharBlock()),
                        ('author_name', blocks.CharBlock()),
                        ('reading_date', blocks.DateBlock()),
                        ('book_description', blocks.RichTextBlock()),
                        ('book_cover', ImageChooserBlock(required=False)),
                    ],template='basic_page/blocks/books.html'),),
                ]
            ))
            ], template='basic_page/blocks/book_club.html', icon='openquote')),
        ('panel', blocks.StructBlock([
            ('panel_name', blocks.CharBlock()),
            ('show_by_default', blocks.BooleanBlock(required=False, help_text="Display Panel as open by default")),
            ('panel_body', blocks.StreamBlock(
                [
                    ('panel_items', blocks.StructBlock([
                        ('panel_item_title', blocks.CharBlock()),
                        ('panel_link', URLBlock(required=False, help_text="Use this for images you wish to link")),
                        ('panel_image', ImageChooserBlock(required=False, help_text="Use this for images you wish to link")),
                        ('panel_description', blocks.RichTextBlock()),
                    ],template='basic_page/blocks/panel_items.html'),),
                ]
            ))
            ], template='basic_page/blocks/panel.html', icon='collapse-down')),
            ], blank=True)

    def get_context(self, request):
        data = super(BasicPage, self).get_context(request)
        return data


    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]
