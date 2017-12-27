
from django.urls import path
from core.views import chapters

urlpatterns = [
    path('book/<int:book_id>/', chapters)
]
