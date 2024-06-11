from furniture_webshop import asgi

asgi.get_asgi_application()

import requests
from bs4 import BeautifulSoup
from store.models import *
from random import randint


BASE_URL = "https://www.amazon.es/s?k=furniture&ref=nb_sb_noss"


# This URL_ROOT is for the first page only
URL_ROOT = "rh=n%3A4204397031%2Cp_n_feature_six_browse-bin%3A4221270031%2Cp_n_feature_two_browse-bin%3A4221244031"

params = {
	"i": "lighting&rh=n%3A4204397031%2Cp_n_feature_six_browse-bin%3A4221270031%2Cp_n_feature_two_browse-bin%3A4221244031&",
	"page": 1, # increasing + 1
	"qid": "1717654030", # this is the base number, we need to add 3 more digits
	"ref": "sr_pg_1" # the number in the end increasing + 1
}

def create_cattegories():
      
      for category in CATEGORY_CHOICES:
            
            Category(
				nombre=CATEGORY_CHOICES[category],
		).save()

def get_category(description: str):
      
      for category in CATEGORY_CHOICES:
            
            if CATEGORY_CHOICES[category].lower() in description.lower():
                  
                  return CATEGORY_CHOICES[category]
      
      return CATEGORY_CHOICES['Otros']


def generate_url(pages, params: dict):
      
      current_params = params.copy()
      
      for i in range(2, (pages + 1)):
            
            current_params['page'] += 1
            current_params['qid'] = current_params['qid'][0:-3] + str(randint(100, 299))
            current_params['ref'] = current_params['ref'].replace(current_params['ref'][-1:], str(int(current_params['ref'][-1:]) + 1))
            
            yield current_params
            
            

def populate_furniture(pages: int, BASE_URL: str, URL_ROOT: str):
      
      
      print(f"Scraping data from {BASE_URL} ...")
      
      url_params = generate_url(pages=pages, params=params)
      i = 1
      
      for param in url_params:
            
            custom_headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
			'Accept-Language': 'es-ES,es;q=0.9',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
			'Referer': 'https://www.google.com/'
            }
            
            if i == 1:
                  url = BASE_URL + URL_ROOT
            else:
                  url = BASE_URL + "i=" + param['i'] + "page=" + str(param['page']) + "&qid=" +  param['qid'] + "&ref=" + param['ref']
            
            
            response = requests.get(url, headers=custom_headers)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            products = soup.find_all("div", {'data-component-type': 's-search-result'})
            
            for product in products:
                  
                  
                  imagen = product.img.get('src')
                  description = product.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'})
                  assessment = product.find('span', {'class': 'a-icon-alt'})
                  price_whole = product.find('span', {'class': 'a-price-whole'})
                  price_fraction = product.find('span', {'class': 'a-price-fraction'})
                  delivery = DELIVERY_CHOICES["Gratis"] if randint(0, 1) == 0 else DELIVERY_CHOICES["Prime gratis"]
                  
                  Furniture(
					imagen=imagen if imagen else "",
					descripcion=description.get_text() if description else "",
					valoracion=assessment.get_text() if assessment else "",
					precio=float(str(price_whole.get_text()[:-1].replace(".", "")) + "." + str(price_fraction.get_text())) if price_whole and price_fraction else 0,
					entrega=delivery,
					categoria=Category.objects.filter(nombre=get_category(description.get_text())).first()
			).save()
      
            i += 1
            
      print("Data was saved succesfully!")
        
        
create_cattegories()
populate_furniture(pages=10, BASE_URL=BASE_URL, URL_ROOT=URL_ROOT)