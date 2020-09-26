# Generated by Django 3.0.8 on 2020-09-03 21:58

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailgeowidget.blocks
import wagtailstreamforms.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('basic_page', '0003_auto_20200903_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('BlockQuoteBlock', wagtail.core.blocks.BlockQuoteBlock()), ('URLBlock', wagtail.core.blocks.URLBlock()), ('EmailBlock', wagtail.core.blocks.EmailBlock()), ('DateBlock', wagtail.core.blocks.DateBlock()), ('TimeBlock', wagtail.core.blocks.TimeBlock()), ('DateTimeBlock', wagtail.core.blocks.DateBlock()), ('PageChooserBlock', wagtail.core.blocks.PageChooserBlock()), ('DocumentChooserBlock', wagtail.documents.blocks.DocumentChooserBlock()), ('EmbedBlock', wagtail.embeds.blocks.EmbedBlock()), ('form', wagtail.core.blocks.StructBlock([('form', wagtailstreamforms.blocks.FormChooserBlock()), ('form_action', wagtail.core.blocks.CharBlock(help_text='The form post action. "" or "." for the current page or a url', required=False)), ('form_reference', wagtailstreamforms.blocks.InfoBlock(help_text='This form will be given a unique reference once saved', required=False))])), ('map', wagtail.core.blocks.StructBlock([('address', wagtailgeowidget.blocks.GeoAddressBlock(required=True)), ('map', wagtailgeowidget.blocks.GeoBlock(address_field='address'))], icon='user', template='basic_page/blocks/map.html')), ('bookClub', wagtail.core.blocks.StructBlock([('book_club_name', wagtail.core.blocks.CharBlock()), ('book_club_day_of_the_week', wagtail.core.blocks.TextBlock()), ('book_club_PDF', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('book_club_time', wagtail.core.blocks.TimeBlock()), ('books', wagtail.core.blocks.StreamBlock([('book', wagtail.core.blocks.StructBlock([('book_name', wagtail.core.blocks.CharBlock()), ('author_name', wagtail.core.blocks.CharBlock()), ('reading_date', wagtail.core.blocks.DateBlock()), ('book_description', wagtail.core.blocks.RichTextBlock()), ('book_cover', wagtail.images.blocks.ImageChooserBlock(required=False))], template='basic_page/blocks/books.html'))]))], icon='openquote', template='basic_page/blocks/book_club.html')), ('panel', wagtail.core.blocks.StructBlock([('panel_name', wagtail.core.blocks.CharBlock()), ('show_by_default', wagtail.core.blocks.BooleanBlock(help_text='Display Panel as open by default', required=False)), ('panel_body', wagtail.core.blocks.StreamBlock([('panel_items', wagtail.core.blocks.StructBlock([('panel_item_title', wagtail.core.blocks.CharBlock()), ('panel_link', wagtail.core.blocks.URLBlock(help_text='Use this for images you wish to link', required=False)), ('panel_image', wagtail.images.blocks.ImageChooserBlock(help_text='Use this for images you wish to link', required=False)), ('panel_description', wagtail.core.blocks.RichTextBlock())], template='basic_page/blocks/panel_items.html'))]))], icon='collapse-down', template='basic_page/blocks/panel.html'))], blank=True),
        ),
    ]