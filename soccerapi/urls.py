"""soccerapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings


admin.autodiscover()



schema_view = get_schema_view(
   openapi.Info(
      title="Soccer API",
      default_version='v1',
      description="This is soccer API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
from django.contrib.staticfiles.views import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('v1/', include('team.urls', namespace='team')),
    # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # url(r'^static/$', serve(), kwargs={'path': 'index.html', 'document_root': settings.STATIC_ROOT}),
    # url(r'^static/$', TemplateView.as_view(template_name='index.html'), name="home"),

    # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    # 'django.contrib.staticfiles.views',
    # url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'index.html'}),
    # url(r'^(?P<path>(?:js|css|img)/.*)$', 'serve'),
    # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

