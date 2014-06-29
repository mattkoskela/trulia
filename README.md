# trulia

Python library for accessing Trulia's REST API

## Installation

    pip install trulia

## Usage

    import trulia.location

    TRULIA_KEY = "RELACE_WITH_YOUR_API_KEY"
    # Get all cities in California
    cities = trulia.location.LocationInfo(TRULIA_KEY).get_cities_in_state("CA")

    # Get all counties in California
    counties = trulia.location.LocationInfo(TRULIA_KEY).get_counties_in_state("CA")

    # Get all neighborhoods in Los Angeles
    neighborhoods = trulia.location.LocationInfo(TRULIA_KEY).get_neighborhoods_in_city("Los Angeles", "CA")

    # Get all states in the United States
    states = trulia.location.LocationInfo(TRULIA_KEY).get_states()

    # Get all zip codes in California
    zip_codes = trulia.location.LocationInfo(TRULIA_KEY).get_zip_codes_in_state("CA")

## Documentation

Trulia's API documentation can be found here: http://developer.trulia.com/docs
