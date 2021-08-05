from django.urls import path
from cbv import views
urlpatterns=[
    path('funcview/',views.funcview,name="funcview"),
    path('funcdisplay/',views.funcdisplay,name="funcdisplay"),
    path('clsview/',views.clsview.as_view(),name="clsview"),
    path('clsdisplay/',views.clsdisplay.as_view(),name="clsdisplay"),
]

