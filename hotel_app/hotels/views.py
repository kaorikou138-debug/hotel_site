from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Hotel, DailyPrice

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    daily_prices = DailyPrice.objects.filter(
        hotel=hotel,
        date__gte=date.today()
    ).order_by('date')

    return render(request, 'hotels/hotel_detail.html', {
        'hotel': hotel,
        'daily_prices': daily_prices,
    })
    
def top(request):
    return render(request, 'hotels/top.html')