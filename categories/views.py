from django.http import JsonResponse
from .models import Category


def cotegories(request):
    all_categories = Category.objects.all()
    return JsonResponse({"ok": True})
