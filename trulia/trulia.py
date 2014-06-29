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

    def get_counties_in_state(self, state):
        """This function returns an OrderedDict of all counties in a state"""

        url = "http://api.trulia.com/webservices.php"
        payload = {
            "library": "LocationInfo",
            "function": "getCountiesInState",
            "state": state,
            "apikey": self.api_key
        }
        xml = requests.get(url, params=payload)

        results = xmltodict.parse(xml.content)
        counties = results["TruliaWebServices"]["response"]["LocationInfo"]["county"]

        return counties

    def get_neighborhoods_in_city(self, city, state):
        """This function returns an OrderedDict of all neighborhoods in a city"""

        url = "http://api.trulia.com/webservices.php"
        payload = {
            "library": "LocationInfo",
            "function": "getNeighborhoodsInCity",
            "city": city,
            "state": state,
            "apikey": self.api_key
        }
        xml = requests.get(url, params=payload)

        results = xmltodict.parse(xml.content)
        neighborhoods = results["TruliaWebServices"]["response"]["LocationInfo"]["neighborhood"]

        return neighborhoods

    def get_states(self):
        """This function returns an OrderedDict of all states in the US"""

        url = "http://api.trulia.com/webservices.php"
        payload = {
            "library": "LocationInfo",
            "function": "getStates",
            "apikey": self.api_key
        }
        xml = requests.get(url, params=payload)

        results = xmltodict.parse(xml.content)
        states = results["TruliaWebServices"]["response"]["LocationInfo"]["state"]

        return states

    def get_zip_codes_in_state(self, state):
        """This function returns an OrderedDict of all zipcodes in a state"""

        url = "http://api.trulia.com/webservices.php"
        payload = {
            "library": "LocationInfo",
            "function": "getZipCodesInState",
            "state": state,
            "apikey": self.api_key
        }
        xml = requests.get(url, params=payload)

        results = xmltodict.parse(xml.content)
        zip_codes = results["TruliaWebServices"]["response"]["LocationInfo"]["zipCode"]

        return zip_codes
