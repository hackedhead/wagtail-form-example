from django.db import models
from django import forms
from django.shortcuts import render
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailcore.fields import RichTextField


class CarDetail(Page):

    make = models.CharField(max_length=255,
                            help_text="Car Manufacturer")
    model = models.CharField(max_length=255,
                             help_text="Car Model")
    year = models.IntegerField()

    description = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('make'),
        FieldPanel('model'),
        FieldPanel('year'),
        FieldPanel('description')
    ]


class CarDetailForm(forms.ModelForm):
    class Meta:
        model = CarDetail
        fields = ['make',
                  'model',
                  'year',
                  'description']


class CarListingPage(RoutablePageMixin, Page):
    @route('^$')
    def list(self, request):
        context = {'page': self,
                   'list': CarDetail.objects.all()}
        return render(request, 'cars/car_list.html', context)

    @route('^add/')
    def default(self, request):
        form = CarDetailForm
        context = {'page': self,
                   'form': form}
        return render(request, 'cars/new_car.html', context)
