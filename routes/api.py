import requests
from flask import Blueprint, request

core = Blueprint('core', __name__, url_prefix='/api/v1')
"""Use Postman Mock Server's url instead 
url = 'https://api.housecanary.com/v2/property/details'
"""

url = 'https://df064114-1b02-456a-9fc6-14c98e1d5e52.mock.pstmn.io'


def get_sewer(property_response):
    # NOTE: For simplicity, we assume all properties exist in the data.
    return property_response['property/details']['result']['property']['sewer']


def get_property(params):
    try:
        response = requests.get(url, params=params, timeout=1)
        if response.status_code == 200:
            property_response = response.json()
            sewer = get_sewer(property_response)
            params['has_septic'] = sewer == 'Septic'
            return params, 200
        return {'message': 'Property not found'}, 404
    except requests.exceptions.HTTPError as error:
        LOGGER.error('Http Error:', error)
    except requests.ConnectionError as error:
        LOGGER.error('Error Connecting:', error)


@core.route('/', methods=['GET'])
def check_septic():
    data = request.get_json()
    if data:
        zipcode = data.get('zipcode')
        address = data.get('address')
        if zipcode is None or address is None:
            return {'message': 'Missing field in "{}"'.format(data)}, 422
        return get_property(data)
    return {'Bad Request'}, 400
