#!/usr/local/bin/python

##
# This file contains functions for each Trulia API call
#
# @package     trulia
# @author      Matt Koskela <mattkoskela@gmail.com>
##

"""
trulia.py

This file contains functions for each Trulia API call
"""

import requests
import xmltodict

API_KEY = "b9735tmvu3y3w9qs8hajydbe"


def get_cities_by_state(state):
    """This function returns an OrderedDict of all cities in a state"""

    url = "http://api.trulia.com/webservices.php"
    payload = {
        "library": "LocationInfo",
        "function": "getCitiesInState",
        "state": state,
        "apikey": API_KEY
    }
    xml = requests.get(url, params=payload)

    results = xmltodict.parse(xml.content)
    cities = results["TruliaWebServices"]["response"]["LocationInfo"]["city"]

    return cities
