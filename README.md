# trulia

Python library for accessing Trulia's REST API

## Installation

    pip install trulia

## Usage

    from trulia import trulia

    # Get all cities in California
    cities = trulia.Trulia("RELACE_WITH_YOUR_API_KEY").get_cities_in_state("CA")

    # Get all counties in California
    counties = trulia.Trulia("RELACE_WITH_YOUR_API_KEY").get_counties_in_state("CA")

    # Get all neighborhoods in Los Angeles
    neighborhoods = trulia.Trulia("RELACE_WITH_YOUR_API_KEY").get_neighborhoods_in_city("Los Angeles", "CA")

    # Get all states in the United States
    states = trulia.Trulia("RELACE_WITH_YOUR_API_KEY").get_states()

    # Get all zip codes in California
    zip_codes = trulia.Trulia("RELACE_WITH_YOUR_API_KEY").get_zip_codes_in_state("CA")

## Documentation

Trulia's API documentation can be found here: http://developer.trulia.com/docs
