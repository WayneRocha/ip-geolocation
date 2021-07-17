import json
import requests
from statistics import mode
from threading import Thread
from unicodedata import normalize
from deep_translator.exceptions import NotValidPayload


class Finder:
    def __init__(self):
        self.IP = ''
        self.valid_IP = False
        self.HG_geoip_key = ''
        self.ipstack_key = ''

        self.extreme_ip_lookup_response = {}
        self.geoplugin_response = {}
        self.ip_api_response = {}
        self.ipapi_response = {}
        self.HG_geoip_response = {}
        self.ipstack_response = {}

        self.latitude = []
        self.longitude = []
        self.city = []
        self.country = []

    def extreme_ip_lookup(self):
        request = f'http://extreme-ip-lookup.com/json/{self.IP}'
        response = requests.get(request)

        if response.status_code != 200:
            print('ERRO EXTREME_IP_LOOKUP! Status Code:{response.status_code}')
        else:
            response = response.text
            response = json.loads(response)
            try:
                response = {'city': response['city'],
                            'country': response['country'],
                            'latitude': response['lat'],
                            'longitude': response['lon']}
                self.extreme_ip_lookup_response = response
                self.valid_IP = True

            except KeyError:
                pass
            except NotValidPayload:
                pass

    def geoplugin(self):
        local_request = f'http://www.geoplugin.net/json.gp?ip='
        local_response = requests.get(local_request)

        if local_response.status_code != 200:
            print('ERRO GEOPLUGUIN! Status Code:{response.status_code}')
        else:
            local_response = local_response.text
            local_response = json.loads(local_response)

        request = f'http://www.geoplugin.net/json.gp?ip={self.IP}'
        response = requests.get(request)

        if response.status_code != 200:
            print('ERRO GEOPLUGUIN! Status Code:{response.status_code}')
        else:
            response = response.text
            response = json.loads(response)

        if self.IP != '':
            if local_response['geoplugin_request'] == response['geoplugin_request']:
                pass
        else:
            try:
                response = {'city': response['geoplugin_city'],
                            'country': response['geoplugin_countryName'],
                            'latitude': response['geoplugin_latitude'],
                            'longitude': response['geoplugin_longitude']}
                self.geoplugin_response = response
                self.valid_IP = True

            except KeyError:
                pass
            except NotValidPayload:
                pass

    def ip_api(self):
        request = f'http://ip-api.com/json/{self.IP}'
        response = requests.get(request)

        if response.status_code != 200:
            print('ERRO IP_API! Status Code:{response.status_code}')
        else:
            response = response.text
            response = json.loads(response)
            try:
                response = {'city': response['city'],
                            'country': response['country'],
                            'latitude': response['lat'],
                            'longitude': response['lon']}
                self.ip_api_response = response
                self.valid_IP = True
            except KeyError:
                pass
            except NotValidPayload:
                pass

    def ipapi(self):
        request = f'https://ipapi.co/{self.IP}/json/'
        response = requests.get(request)

        if response.status_code != 200:
            print(f'ERRO IPAPI! Status Code:{response.status_code}')
        else:
            response = json.loads(response.content)
            try:
                response = {'city': response['city'],
                            'country': response['country'],
                            'latitude': response['latitude'],
                            'longitude': response['longitude']}
                self.ipapi_response = response
                self.valid_IP = True
            except KeyError:
                pass
            except NotValidPayload:
                pass

    def HG_geoip(self):
        request = f'https://api.hgbrasil.com/geoip?key={self.HG_geoip_key}&address={self.IP}'
        response = requests.get(request)

        if response.status_code != 200:
            print(f'ERRO HG_geopi! Status Code:{response.status_code}')
        else:
            response = response.text
            response = json.loads(response)
            response = response['results']
            try:
                response = {'city': response['city'],
                            'country': response['country_name'],
                            'latitude': response['latitude'],
                            'longitude': response['longitude']}
                self.HG_geoip_response = response
                self.valid_IP = True
            except KeyError:
                pass
            except NotValidPayload:
                pass

    def ipstack(self):
        request = f'http://api.ipstack.com/{self.IP}?access_key={self.ipstack_key}'
        response = requests.get(request)

        if response.status_code != 200:
            print(f'ERRO IPSTACK! Status Code:{response.status_code}')
        else:
            response = response.text
            response = json.loads(response)
            if response["type"] != None:
                try:
                    response = {'city': response['city'],
                                'country': response['country_name'],
                                'latitude': response['latitude'],
                                'longitude': response['longitude']}
                    self.ipstack_response = response
                    self.valid_IP = True
                except KeyError:
                    pass
                except NotValidPayload:
                    pass

    def get_location(self):

        extreme_ip_lookup_thread = Thread(target=self.extreme_ip_lookup)
        geoplugin_thread = Thread(target=self.geoplugin)
        ip_api_thread = Thread(target=self.ip_api)
        ipapi_thread = Thread(target=self.ipapi)
        HG_geoip_thread = Thread(target=self.HG_geoip)
        ipstack_thread = Thread(target=self.ipstack)

        threads = [extreme_ip_lookup_thread,
                   geoplugin_thread, ip_api_thread, ipapi_thread]

        for thread in threads:
            thread.start()

        if self.HG_geoip_key != '' and self.IP != '':
            HG_geoip_thread.start()
            threads.append(HG_geoip_thread)
        if self.ipstack_key != '' and self.IP != '':
            ipstack_thread.start()
            threads.append(ipstack_thread)

        for thread in threads:
            thread.join()

        responses = [self.extreme_ip_lookup_response, self.geoplugin_response,
                     self.ip_api_response, self.ipapi_response, self.HG_geoip_response, self.ipstack_response]

        for _ in range(6):
            for response in responses:
                response_as_str = str(response)
                if response == {} or "''" in response_as_str or 'None' in response_as_str:
                    responses.remove(response)

        for response in responses:
            self.latitude.append(str(response['latitude']))
            self.longitude.append(str(response['longitude']))
            self.city.append(response['city'])
            self.country.append(response['country'])

        if self.latitude != [] and self.valid_IP != False:
            latitude_for_comparation = []
            for latitude in self.latitude:
                latitude_for_comparation.append(latitude[0:6])

            latitude_mode = str(mode(latitude_for_comparation))
            self.latitude_reliability = float(f'{round(latitude_for_comparation.count(latitude_mode[0:6]) / len(latitude_for_comparation), 4) * 100}')
            self.latitude = str(mode(self.latitude))
        else:
            print('IP inválido.')

        if self.longitude != [] and self.valid_IP != False:
            longitude_for_comparation = []
            for longitude in self.longitude:
                longitude_for_comparation.append(longitude[0:6])

            longitude_mode = str(mode(longitude_for_comparation))
            self.longitude_reliability = float(f'{round(longitude_for_comparation.count(longitude_mode[0:6]) / len(longitude_for_comparation), 4) * 100}')
            self.longitude = str(mode(self.longitude))

        if self.city != [] and self.valid_IP != False:
            city_mode = mode(self.city)
            city_index = self.city.index(city_mode)
            city_mode_without_accents = normalize('NFKD', city_mode).encode(
                'ASCII', 'ignore').decode('ASCII')

            city_without_accents = []
            for city in self.city:
                city = normalize('NFKD', city).encode(
                    'ASCII', 'ignore').decode('ASCII')
                city_without_accents.append(city)

            self.city_reability = round(city_without_accents.count(city_mode_without_accents) / len(city_without_accents), 4) * 100
            self.city = city_mode

        if self.country != [] and self.valid_IP != False:
            self.country = self.country[city_index]
