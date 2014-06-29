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

    def get_city_stats(self, city, state, start_date=None, end_date=None, stat_type="all"):
        """This method returns an OrderedDict of all cities in a state"""

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
