from django.urls import path

from .views import (
    BottleCapDetailView,
    BottleCapListView,
    PreformDetailView,
    PreformListView
)

urlpatterns = [
    path(
        'preforms',
        PreformListView.as_view(),
        name='preforms-list'
    ),
    path(
        'preforms/<slug:slug>',
        PreformDetailView.as_view(),
        name='preforms-detail'
    ),
    path(
        'bottle-caps',
        BottleCapListView.as_view(),
        name='bottlecaps-list'
    ),
    path(
        'bottle-caps/<slug:slug>',
        BottleCapDetailView.as_view(),
        name='bottlecap-detail'
    )
]
