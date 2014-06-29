#!/usr/local/bin/python

##
# This file contains an interface for Trulia's TruliaStats Library.
#
# @package     trulia
# @author      Matt Koskela <mattkoskela@gmail.com>
##

"""
stats.py

This file contains an interface for Trulia's TruliaStats Library.

Documentation about Trulia's TruliaStats Library can be found here:
http://developer.trulia.com/docs/read/TruliaStats
"""

import requests
import xmltodict


class TruliaStats(object):
    """
    The TruliaStats class is used to retrieve stats data from the Trulia API
    """

    def __init__(self, api_key):
        self.api_key = api_key

    def get_city_stats(self, city, state, start_date, end_date, stat_type="all"):
        """This method returns an OrderedDict of all stats for a city"""

        url = "http://api.trulia.com/webservices.php"
        payload = {
            "library": "TruliaStats",
            "function": "getCityStats",
            "city": city,
            "state": state,
            "startDate": start_date,
            "endDate": end_date,
            "statType": stat_type,
            "apikey": self.api_key
        }
        xml = requests.get(url, params=payload)

        results = xmltodict.parse(xml.content)
        city_stats = results["TruliaWebServices"]["response"]["TruliaStats"]

        return city_stats

    def get_county_stats(self, county, state, start_date, end_date, stat_type="all"):
        """This method returns an OrderedDict of all stats for a county"""

        url = "http://api.trulia.com/webservices.php"
        payload = {
            "library": "TruliaStats",
            "function": "getCountyStats",
            "county": county,
            "state": state,
            "startDate": start_date,
            "endDate": end_date,
            "statType": stat_type,
            "apikey": self.api_key
        }
        xml = requests.get(url, params=payload)

        results = xmltodict.parse(xml.content)
        county_stats = results["TruliaWebServices"]["response"]["TruliaStats"]

        return county_stats

    def get_neighborhood_stats(self, neighborhood_id, start_date, end_date, stat_type="all"):
        """This method returns an OrderedDict of all stats for a neighborhood"""

        url = "http://api.trulia.com/webservices.php"
        payload = {
            "library": "TruliaStats",
            "function": "getCountyStats",
            "neighborhoodId": neighborhood_id,
            "startDate": start_date,
            "endDate": end_date,
            "statType": stat_type,
            "apikey": self.api_key
        }
        xml = requests.get(url, params=payload)

        results = xmltodict.parse(xml.content)
        neighborhood_stats = results["TruliaWebServices"]["response"]["TruliaStats"]

        return neighborhood_stats
