from django.db.models import Sum
from django.http import HttpResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas

from .models import Amount


def from_cart_to_pdf(user):
    shopping_basket = Amount.objects.filter(
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
    canvas_page = Canvas(filename=response)
    canvas_page.setFont('DejaVuSerif', 24)
    canvas_page.drawString(210, 800, 'Список покупок')
    canvas_page.setFont('DejaVuSerif', 16)
    y_coord = 760
    list_counter = 1
    for ingredient in shopping_basket:
        canvas_page.drawString(60, y_coord, text=(
            f'{list_counter}. {ingredient["ingredient__name"]} - '
            f'{ingredient["amount"]} '
            f'{ingredient["ingredient__measurement_unit"]}'
        ))
        list_counter += 1
        y_coord -= 30
        if y_coord <= 30:
            canvas_page.showPage()
            canvas_page.setFont('DejaVuSerif', 16)
            y_coord = 760
    canvas_page.showPage()
    canvas_page.save()
    return response
