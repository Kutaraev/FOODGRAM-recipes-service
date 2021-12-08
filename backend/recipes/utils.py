from django.db.models import Sum
from django.http import HttpResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas

from .models import Amount


def from_cart_to_pdf(user):
    shopping_list = Amount.objects.filter(
        recipe__shoplist__user=user).values(
            'ingredient__name',
            'ingredient__measurement_unit'
    ).annotate(amount=Sum('amount')).order_by()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = (
        'attachment; filename="shopping_list.pdf"'
    )
    pdfmetrics.registerFont(
        TTFont('DejaVuSerif', 'DejaVuSerif.ttf', 'UTF-8')
    )
    page = Canvas(filename=response)
    page.setFont('DejaVuSerif', 24)
    page.drawString(210, 800, 'Список покупок')
    page.setFont('DejaVuSerif', 16)
    height = 760
    for idx, ingr in enumerate(shopping_list, start=1):
        page.drawString(60, height, text=(
            f'{idx}. {ingr["ingredient__name"]} - {ingr["amount"]} '
            f'{ingr["ingredient__measurement_unit"]}'
        ))
        # height -= 30
        page.showPage()
    page.showPage()
    page.save()
    return response
