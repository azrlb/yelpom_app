from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os


def get_businesses(location):
    auth = Oauth1Authenticator(
        consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ['CONSUMER_SECRET'],
        token=os.environ['TOKEN'],
        token_secret=os.environ['TOKEN_SECRET']
    )

    client = Client(auth)

    params = {
        'term': 'food',
        'lang': 'en',
        'limit': 3
    }

    response = client.search(location, **params)

    businesses = []

    for business in response.businesses:
        # print(business.name, business.rating, business.phone)
        businesses.append({"rating": business.rating,
        "phone": business.phone,
        "name": business.name


        })

    return businesses

# "Name:{}, Rating:{} and Phone:{}".format(business.name, business.rating, business.phone)
# businesses = get_businesses('New York City')

# print(businesses)
