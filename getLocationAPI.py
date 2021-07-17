from flask import Flask, request
from flask_cors import CORS
from json import dumps
from Localizador import Finder

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return 'Locate by IP API<br>view the documentation <a href="#">here</a>  '


@app.route('/geolocation', methods=['GET'])
def get():
    location = Finder()
    location.IP = request.args.get('ip')
    location.get_location()
    json = {
        'isValid': location.valid_IP,
        'ip': location.IP,
        'city': location.city,
        'country': location.country,
        'latitude': location.latitude,
        'longitude': location.longitude,
        'reliability': (location.longitude_reliability + location.latitude_reliability) / 2
    }

    return dumps(json, ensure_ascii=False).encode('utf8')


if __name__ == "__main__":
    try:
        app.run()
    except Exception as error:
        print(error)
