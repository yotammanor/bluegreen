from django.shortcuts import get_object_or_404
from core.models import Book
from django.http.response import JsonResponse


def chapters(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    data = [{"name": x.__str__()} for x in book.chapters.all()]
    return JsonResponse(data=data, safe=False)
