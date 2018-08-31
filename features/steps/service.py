"""
This module contains step definitions for service.feature.
It uses the requests package:
http://docs.python-requests.org/
"""

import requests
from behave import *

# "Constants"

REGISTER_API = 'https://onboarding.jyve.com/api/register/'

# Whens

@when('the Registration API is queried with')
def step_impl(context):
    first_row = context.table[0]
    params = {'zipcode': first_row['zipcode']}
    context.response = requests.get(REGISTER_API, params=params)

# Thens

@then('the API returns a result of {expected_result}')
def step_impl(context, expected_result):
    assert expected_result == str(context.response.json()['result'])
