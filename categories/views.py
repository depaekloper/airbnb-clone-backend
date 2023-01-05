from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category


@api_view()
def cotegories(request):
    return Response(
        {
            "ok": True,
        },
    )
