from typing import List


class Street:
    """
    An object that represents a collection of houses that use electricity
    """

    def total_usage(self) -> int:
        """
        :return: the total electricity units of use in the street (i.e. all the houses)
        """
        pass

    def total_charge(self):
        """
        :return: the total charge for the all the electricity use in the street (i.e. all the houses)
        """
        pass


def street_with(houses: List[object]) -> Street:
    """
    Returns a Street object containing the houses
    :param houses: a sequence of house objects
    :return: a Street object
    """
    pass


class Tariff:
    """
    An object that figures out charging for a house
    """

    def charge_for(self, units_per_quarter: List[int]) -> int:
        """
        returns charge for a given usage
        :param units_per_quarter: units of use by quarter
        :return: total charging amount
        """
        pass


def house_with(units_per_quarter: List[int], tariff: Tariff) -> object:
    """
    Returns a House object that will be used to create a street.
    :param units_per_quarter: a sequence of units for each quarter of the usage of the house
    :param tariff: how this house should be charged for its electricity
    :return: A House object
    """
    pass


def constant_tariff(pence_per_unit: int) -> Tariff:
    """
    A Tariff object that will be used for house charging at a constant rate throughout the day
    :param pence_per_unit: the rate per unit
    :return: A Constant Tariff object
    """
    pass


def variable_rate_tariff(unit_charges: List[int]) -> Tariff:
    """
    A Night Rate Tariff object will be used for house charging, with a different unit price later in the day
    :param unit_charges: a sequence of unit prices, one for each quarter
    :return: a Night Rate Tariff object
    """
    pass


def low_high_tariff(threshold, low_rate, high_rate) -> Tariff:
    """
    A Low High Tariff object that has a low price up to a threshold of total units used, then a high price
    :param threshold: how many units at the lower rate
    :param low_rate: lower rate per unit
    :param high_rate: higher rate per unit
    :return: A Low High Tariff object
    """
    pass
