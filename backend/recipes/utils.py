from io import BytesIO

from django.db.models import Sum
from django.http import HttpResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas

from .models import Amount


def from_cart_to_pdf(user):
    """Преобразование списка покупок в pdf-файл"""
    # не стал использовать values_list, т.к. изменил вывод списка покупок
    # и мне кажется, что понятнее, когда идет обращение к ключам словаря values
    # а не к индексам кортежа values_list
    shopping_basket = Amount.objects.filter(
        recipe__shoplist__user=user).values(
            'ingredient__name',
            'ingredient__measurement_unit'
    ).annotate(amount=Sum('amount')).order_by()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = (
        'attachment; filename="somefilename.pdf"')

    buffer = BytesIO()
    canvas_page = canvas.Canvas(buffer)
    fname = 'a010013l'
    facename = 'URWGothicL-Book'
    cyrface = pdfmetrics.EmbeddedType1Face(fname+'.afm', fname+'.pfb')
    cyrenc = pdfmetrics.Encoding('CP1251')

    cp1251 = (
            'afii10051', 'afii10052', 'quotesinglbase', 'afii10100',
            'quotedblbase', 'ellipsis', 'dagger', 'daggerdbl', 'Euro',
            'perthousand', 'afii10058', 'guilsinglleft', 'afii10059',
            'afii10061', 'afii10060', 'afii10145', 'afii10099', 'quoteleft',
            'quoteright', 'quotedblleft', 'quotedblright', 'bullet',
            'endash', 'emdash', 'tilde', 'trademark', 'afii10106',
            'guilsinglright', 'afii10107', 'afii10109', 'afii10108',
            'afii10193', 'space', 'afii10062', 'afii10110', 'afii10057',
            'currency', 'afii10050', 'brokenbar', 'section', 'afii10023',
            'copyright', 'afii10053', 'guillemotleft', 'logicalnot',
            'hyphen', 'registered', 'afii10056', 'degree', 'plusminus',
            'afii10055', 'afii10103', 'afii10098', 'mu1', 'paragraph',
            'periodcentered',
            'afii10071', 'afii61352', 'afii10101', 'guillemotright',
            'afii10105', 'afii10054', 'afii10102', 'afii10104',
            'afii10017', 'afii10018', 'afii10019', 'afii10020', 'afii10021',
            'afii10022', 'afii10024', 'afii10025', 'afii10026', 'afii10027',
            'afii10028', 'afii10029', 'afii10030', 'afii10031', 'afii10032',
            'afii10033', 'afii10034', 'afii10035', 'afii10036', 'afii10037',
            'afii10038', 'afii10039', 'afii10040', 'afii10041', 'afii10042',
            'afii10043', 'afii10044', 'afii10045', 'afii10046', 'afii10047',
            'afii10048', 'afii10049', 'afii10065', 'afii10066', 'afii10067',
            'afii10068', 'afii10069', 'afii10070', 'afii10072', 'afii10073',
            'afii10074', 'afii10075', 'afii10076', 'afii10077', 'afii10078',
            'afii10079', 'afii10080', 'afii10081', 'afii10082', 'afii10083',
            'afii10084', 'afii10085', 'afii10086', 'afii10087', 'afii10088',
            'afii10089', 'afii10090', 'afii10091', 'afii10092', 'afii10093',
            'afii10094', 'afii10095', 'afii10096', 'afii10097'
    )

    for counter in range(128, 256):
        cyrenc[counter] = cp1251[counter-128]

    pdfmetrics.registerEncoding(cyrenc)
    pdfmetrics.registerTypeFace(cyrface)
    pdfmetrics.registerFont(
        pdfmetrics.Font(facename+'1251', facename, 'CP1251'))
    canvas_page.setFont(facename+'1251', 20)

    canvas_page.drawString(60, 800, 'Список покупок')
    y_coord = 760
    list_counter = 1
    page_end_flag = False
    for ingredient in shopping_basket:
        canvas_page.drawString(60, y_coord, text=(
            f'{list_counter}. {ingredient["ingredient__name"]} - '
            f'{ingredient["amount"]} '
            f'{ingredient["ingredient__measurement_unit"]}'
        ))
        y_coord -= 30
        list_counter += 1
        if y_coord <= 30:
            canvas_page.showPage()
            page_end_flag = True
    if not page_end_flag:
        canvas.page.showPage()
    canvas_page.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
