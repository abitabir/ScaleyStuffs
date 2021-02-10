# Information about electricity pricing on a street
# A street has a set of houses and we have their electricity use per quarter (3 month period).
# Electricity is measured in "units" (integers)
# Charges are measured in integers

# Houses may be on different tariffs
# The constant tariff means a user pays the same amount for each unit of electricity across each quarter
# The low/high tariff means a user pays a low amount for each unit of electricity until they exceed a yearly threshold,
# after which they pay at a higher rate
# The variable tariff means a user might pay a different amount per unit of electricity for each quarter of the year

# Scroll down to the first test to get started

# Hints.
# - Look at python itertools
# - If you're running in an IDE, you might need to configure it to run pytest

from app.electricitypricing import house_with, constant_tariff, street_with, low_high_tariff, variable_rate_tariff

CONSTANT_TARIFF = constant_tariff(pence_per_unit=2)
NO_USAGE_HOUSE = house_with(units_per_quarter=[0, 0, 0, 0], tariff=CONSTANT_TARIFF)
CONSTANT_HOUSE_1 = house_with(units_per_quarter=[10, 11, 12, 13], tariff=CONSTANT_TARIFF)
CONSTANT_HOUSE_2 = house_with(units_per_quarter=[21, 22, 23, 24], tariff=CONSTANT_TARIFF)

LOW_HIGH_TARIFF = low_high_tariff(threshold=16, low_rate=2, high_rate=7)

VARIABLE_RATE_TARIFF = variable_rate_tariff(unit_charges=[5, 5, 2, 2])
VARIABLE_RATE_HOUSE = house_with(units_per_quarter=[10, 11, 12, 13], tariff=VARIABLE_RATE_TARIFF)


# Start here!
# There are two parts to this first test, you need to implement the total_usage and street_with methods.
# Remember, the goal is to pass each test, so you don't need to do all the work for total_usage now, just pass in this
# one case, more complexity will come later.
# Hint! You will need to write a constructor for the street class.

# However far you get please make sure to submit your work and don't be discouraged if you don't feel you've completed
# too much, this is a hard problem and we know it!
def test_no_usage():
    assert street_with(houses=[NO_USAGE_HOUSE, NO_USAGE_HOUSE]).total_usage() == 0


def test_sums_usage():
    assert street_with(houses=[CONSTANT_HOUSE_1, CONSTANT_HOUSE_2]).total_usage() == 136


def test_no_charge_for_no_usage():
    assert street_with(houses=[NO_USAGE_HOUSE, NO_USAGE_HOUSE]).total_charge() == 0


def test_sums_charges_for_constant_tariff():
    assert street_with(houses=[CONSTANT_HOUSE_1, CONSTANT_HOUSE_2]).total_charge() == 272


def test_charges_remain_low_under_threshold():
    assert street_with(houses=[house_with([4, 4, 4, 4], LOW_HIGH_TARIFF)]).total_charge() == 32


def test_charges_high_after_threshold():
    assert street_with(houses=[house_with([8, 4, 4, 4], LOW_HIGH_TARIFF)]).total_charge() == 60


def test_high_charge_applies_within_quarter():
    assert street_with(houses=[house_with([8, 6, 4, 4], LOW_HIGH_TARIFF)]).total_charge() == 74


def test_sums_charges_for_variable_tariffs():
    assert street_with(houses=[VARIABLE_RATE_HOUSE]).total_charge() == 155


def test_different_houses_have_different_tariffs():
    assert street_with(houses=[VARIABLE_RATE_HOUSE, CONSTANT_HOUSE_1]).total_charge() == 247
