from __future__ import absolute_import, unicode_literals

from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel)
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailforms.edit_handlers import FormSubmissionsPanel
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailimages.blocks import ImageChooserBlock

COLOUR_CHOICES = [
    ('bg-white', 'Geen'),
    ('bg-primary', 'Primair'),
]


class OneColumnBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(choices=COLOUR_CHOICES, default="bg-white")
    center_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
        # ('google_map', GoogleMapBlock()),
    ], icon='user', label='Center column')

    class Meta:
        template = 'home/blocks/one_column_block.html'
        icon = 'placeholder'
        label = 'One Column'


class TwoColumnBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(choices=COLOUR_CHOICES, default="bg-white")
    left_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
        # ('google_map', GoogleMapBlock()),
    ], icon='arrow-left', label='Left column content')

    right_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
        # ('google_map', GoogleMapBlock()),
    ], icon='arrow-right', label='Right column content')

    class Meta:
        template = 'home/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class ThreeColumnBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(choices=COLOUR_CHOICES, default="bg-white")
    left_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
        # ('google_map', GoogleMapBlock()),
    ], icon='arrow-left', label='Left column content')

    column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
        # ('google_map', GoogleMapBlock()),
    ], icon='user', label='Center column')

    right_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
        # ('google_map', GoogleMapBlock()),
    ], icon='arrow-right', label='Right column content')

    class Meta:
        template = 'home/blocks/three_column_block.html'
        icon = 'placeholder'
        label = 'Three Columns'


class JumbotronBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    body = blocks.RichTextBlock()

    class Meta:
        template = 'home/blocks/jumbotron.html'
        icon = 'user'


class HomePage(Page):
    body = StreamField([
        ('one_column', OneColumnBlock()),
        ('two_columns', TwoColumnBlock()),
        ('three_columns', ThreeColumnBlock()),
        ('jumbotron', JumbotronBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]
