from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    import requests
    import json

    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD,EUR")
    price = json.loads(price_request.content)

    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)

    return render(request, 'crypto/home.html', {'api': api, 'price' : price})

def prices(request):
    import requests
    import json
    flag = False

    if request.method == 'POST' :
        quote = request.POST['quote'].upper()
        quote_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ quote +"&tsyms=USD,EUR")
        price = json.loads(quote_request.content)
        flag = True

        return render(request, 'crypto/price.html', {'price': price, 'flag': flag})
    else:
        flag = False
        return render(request, 'crypto/price.html', {'price': 'This is the prices page', 'flag': flag})
    

