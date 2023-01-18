from dadata import Dadata
from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import render, redirect


def hello(request):
    return redirect('admin/')


@staff_member_required()
def index(request):
    # if not request.user.is_authenticated:
    #     return redirect('admin/')
    if request.method == 'POST' and request.POST['address']:
        address = request.POST['address']
        token = "2ab84f15eba521cc63cf605cfc04c03ce22139bd"
        secret = "48197a7131162e9a1006457d11fb97e222efae51"
        dadata = Dadata(token, secret)
        result = dadata.clean("address", address)
        context = {
            'postal_code': result['postal_code'] or '',
            'region': result['region'] or '',
            'city': result['city'] or result['region'] or '',
            'street_with_type': result['street_with_type'] or '',
            'house': result['house'] or '',
            'geo_lat': result['geo_lat'] or '',
            'geo_lon': result['geo_lon'] or '',
            'city_fias_id': result['city_fias_id'] or '',
            'street_fias_id': result['street_fias_id'] or '',
            'house_fias_id': result['house_fias_id'] or '',
            'flat_fias_id': result['flat_fias_id'] or '',
            'house_cadnum': result['house_cadnum'] or '',
            'flat_cadnum': result['flat_cadnum'] or '',
            'kladr_id': result['kladr_id'] or '',
            'okato': result['okato'] or '',
            'oktmo': result['oktmo'] or '',
            'tax_office': result['tax_office'] or '',
            'tax_office_legal': result['tax_office_legal'] or '',
            'address': address,
            'get_info': 'Информация по запросу:',
            'title': 'Поиск сведений по адресу',
        }
    else:
        context = {
            'result': 'Введите пожалуйста адрес',
            'title': 'Поиск сведений по адресу',

        }

    return render(request, 'form.html', context)
