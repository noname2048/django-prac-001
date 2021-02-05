from django.urls import path, re_path, register_converter
from . import views
from .converters import YearConverter, MonthConverter, DayConverter

register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

app_name = 'instagram'  # URL Reverse

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    # path('', views.post_list, ),
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/detele/', views.post_delete, name='post_delete'),

    # re_path(r'(?P<pk>\d+)/$', views.post_detail),
    path('archives/<year:year>/', views.archives_year, name='archive_year'),
    # re_path(r'archives/(?P<year>\d+)/$', views.archives_year),
    # re_path(r'archives/(?P<year>\\d+)/$', views.archives_year),
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
    path('archive/<year:year>/<month:month>/<day:day>/', views.post_archive_year_month_day,
         name='post_archive_year_month_day'),
    path('test/', views.test_detail),
]
