# trulia

Python library for accessing Trulia's REST API

## Installation

    pip install trulia

## Usage

    import trulia.stats
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

    # Get all traffic and listing stats for the city of Los Angeles in January 2014
    city_stats = trulia.stats.TruliaStats(TRULIA_KEY).get_city_stats(city="Los Angeles", state="CA", start_date="2014-01-01", end_date="2014-01-31")

    # Get all traffic and listing stats for Santa Clara county in January 2014
    county_stats = trulia.stats.TruliaStats(TRULIA_KEY).get_county_stats(city="Santa Clara", state="CA", start_date="2014-01-01", end_date="2014-01-31")

## Documentation

Trulia's API documentation can be found here: http://developer.trulia.com/docs
