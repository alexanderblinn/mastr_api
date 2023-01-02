# -*- coding: utf-8 -*-
"""A script to demonstrate how to use the MarktstammdatenregisterAPI class."""

from typing import Any

import pandas as pd

from helpers.api_accessor import MarktstammdatenregisterAPI
from helpers.enumeration import Energietraeger, Marktfunktion, MarktTyp


def get_power_units(**kwargs: dict[str, str]) -> dict[str, Any]:
    """
    Get data of power units from the Marktstammdatenregister API.

    Parameters
    ----------
    **kwargs : dict[str, str]
        Additional keyword arguments to pass to the API method.

    Returns
    -------
    dict[str, Any]
        The data returned by the API method, serialized as a dictionary.
    """
    api = MarktstammdatenregisterAPI(MarktTyp.ANLAGE.value)
    data = api.get('GetGefilterteListeStromErzeuger', **kwargs)
    return pd.DataFrame(data['Einheiten'])


def get_market_players(**kwargs: dict[str, str]) -> dict[str, Any]:
    """Get data of market players from the Marktstammdatenregister API.

    Parameters
    ----------
    **kwargs : dict[str, str]
        Additional keyword arguments to pass to the API method.

    Returns
    -------
    dict[str, Any]
        The data returned by the API method, serialized as a dictionary.
    """
    api = MarktstammdatenregisterAPI(MarktTyp.AKTEUR.value)
    return api.get('GetGefilterteListeMarktakteure', **kwargs)


def get_player_info(mastr_nummer: str, **kwargs: dict[str, str]
                    ) -> dict[str, Any]:
    """
    Get information about a market player from the Marktstammdatenregister API.

    Parameters
    ----------
    mastr_nummer : str
        The MaStR number of the market player.
    **kwargs : dict[str, str]
        Additional keyword arguments to pass to the API method.

    Returns
    -------
    dict[str, Any]
        The data returned by the API method, serialized as a dictionary.
    """
    api = MarktstammdatenregisterAPI(MarktTyp.AKTEUR.value)
    return api.get('GetMarktakteur', mastrNummer=mastr_nummer, **kwargs)


if __name__ == '__main__':
    power_units = get_power_units(
        ort='Schiffweiler',
        energietraeger=Energietraeger.SOLAR.value
        )

    # market_akteurs = get_market_players(
    #     ort='Neunkirchen',
    #     # marktfunktion=Marktfunktion.STROMNETZBETREIBER.value
    #     )

    # player_info = get_player_info(mastr_nummer='SNB943841101959')

# %%
# import csv

# keys, values = [], []

# for key, value in power_units.items():
#     keys.append(key)
#     values.append(value)       

# with open("frequencies.csv", "w") as outfile:
#     csvwriter = csv.writer(outfile)
#     csvwriter.writerow(keys)
#     csvwriter.writerow(values)
