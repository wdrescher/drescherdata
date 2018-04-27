from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'emails'
urlpatterns =[
    url(r"^$", views.ContactFormView.as_view(), name="index"),
    url(r"^getback/$",
        TemplateView.as_view(template_name='pages/getback.html'),
        name="getback"),
]
