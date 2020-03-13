# Generated by Django 3.0.3 on 2020-03-13 04:21

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200310_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'code', 'strikethrough', 'superscript', 'subscript', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'blockquote', 'hr', 'embed', 'link', 'document-link', 'image'])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('page', wagtail.core.blocks.PageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('media', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock(label='Raw HTML')), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Code')), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='blog/table_template.html'))]),
        ),
    ]
