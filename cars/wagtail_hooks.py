from django.utils.safestring import mark_safe
from wagtail.wagtailcore import hooks
from cars.models import CarDetail


class CarSummary(object):
    order = 50

    def render(self):
        print("Making a Car Summary")
        car_count = CarDetail.objects.count()
        message = """
        <section class="panel summary nice-padding">
          <h3>There are {car_count} car{plural}.</h3>
        </section>
        """.format(car_count=car_count, plural='s' if car_count > 1 else '')
        return mark_safe(message)


@hooks.register('construct_homepage_panels')
def add_another_panel(request, panels):
    return panels.append(CarSummary())
