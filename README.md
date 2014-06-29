# trulia

Python library for accessing Trulia's REST API

## Installation

    pip install trulia

## Usage

    from trulia import trulia
    cities = trulia.Trulia("RELACE_WITH_YOUR_API_KEY").get_cities_in_state("CA")
    counties = trulia.Trulia("RELACE_WITH_YOUR_API_KEY").get_counties_in_state("CA")
    neighborhoods = trulia.Trulia("RELACE_WITH_YOUR_API_KEY").get_neighborhoods_in_city("Los Angeles", "CA")
    states = trulia.Trulia("RELACE_WITH_YOUR_API_KEY").get_states()

## Documentation

Trulia's API documentation can be found here: http://developer.trulia.com/docs
