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


class Trulia(object):
    """The Trulia class is used to interact with the Trulia API"""

    def __init__(self, api_key):
        self.api_key = api_key

    def get_cities_in_state(self, state):
        """This function returns an OrderedDict of all cities in a state"""

        url = "http://api.trulia.com/webservices.php"
        payload = {
            "library": "LocationInfo",
            "function": "getCitiesInState",
            "state": state,
            "apikey": self.api_key
        }
        xml = requests.get(url, params=payload)

        results = xmltodict.parse(xml.content)
        cities = results["TruliaWebServices"]["response"]["LocationInfo"]["city"]

        return cities
