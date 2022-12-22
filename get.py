# -*- coding: utf-8 -*-
"""
In order to access the API of the Marktstammdatenregister, registration as a Webdienstnutzer/Marktakteur is required.
Link: https://test.marktstammdatenregister.de/MaStR
After registration a marktakteurMastrNummer and an apiKey are available for use.
"""


import pandas as pd
import numpy as np


from zeep import Client, Settings, Transport
from zeep.cache import SqliteCache
from zeep.helpers import serialize_object

from config.enumeration import *

MARKTAKTEUR_MASTR_NUMBER = 'SOM935513419707'
API_KEY = '163rm88xn4NjDa88mGXnfA9wuFSgf8+OACy3ff4ja1plquCy8/671NiTa72GxbwZ/1EWOmjoI0tqbhOIM5kx5DMoWEuUQRyz4jnziXG8GeVjessIrxlpy8AxVkOxvGaNwCzcmXjUhec7mlEwhe3Df3OgtGr6w7V1tO+nIyJxfYFd3bDZ5rIW+bPSEzQ0OH4CbAUZBitthc6PGnuGQ7kdkwqh/lPvdARS1+HjTUGrOois8SUEmp0xG278gF4+Tg0O6SWf+JnN08NuqrgWL39b6tAaLEACRmkLdfGZWllsyAn8YvSY/vzW+2tyxDAN643/9SI18rhVAfHkTHu5DdXyqvCYLTd/RKAuMchYob+riESTSnBssg9R14xxP8mfmc4mJvM94xEyvx0trq3rSoOsxVr5relYrs95J/zOWzj2zGXvL3feC+bTgcUpi6L4iT6TWJxhAKQEpHpIaHEENVGg2bhCAMHL4CCf0nrr0ioNVK32mIlkDZJSj9LzHnSCZFUasBKXhJLfjHgag4ICmqEP1B5Y/cs='



class MarktstammdatenregisterAPI:
    """Simple class to access the API of the Marktstammdatenregister."""

    def __init__(self, marktakteurMastrNummer: str,
                 api_key: str,
                 market_type: str
                 ):
        """
        Initialize the MarktstammdatenregisterAPI object.

        Parameters
        ----------
        marktakteurMastrNummer : str
            The Mastr number of the market participant.
        api_key : str
            The API key to use for authenticating requests.
        """
        self.marktakteurMastrNummer = marktakteurMastrNummer
        self.api_key = api_key
        self.market_type = market_type

        # Set up the client object to make API requests.
        api_endpoint = \
            "https://www.marktstammdatenregister.de/MaStRAPI/wsdl/mastr.wsdl"
        transport = Transport(cache=SqliteCache())
        settings = Settings(strict=False, xml_huge_tree=True)
        self.client = Client(
            wsdl=api_endpoint, transport=transport, settings=settings
            )
        self.client_bind = self.client.bind(
            'Marktstammdatenregister', self.market_type
            )

    def get(self, method_name: str, **kwargs):
        """
        Retrieve data from the Marktstammdatenregister API.

        Parameters
        ----------
        method_name : str
            The name of the method to use for retrieving data for the unit/-s.

        Returns
        -------
        object
            The data for the unit/-s, in the format returned by the API.
        """
        method = getattr(self.client_bind, method_name)
        data = method(apiKey=self.api_key,
                      marktakteurMastrNummer=self.marktakteurMastrNummer,
                      **kwargs)
        return serialize_object(data)


def get_power_units(**kwargs):
    api = MarktstammdatenregisterAPI(
        MARKTAKTEUR_MASTR_NUMBER, API_KEY, MarketType.ANLAGE.value)
    return api.get('GetGefilterteListeStromErzeuger', **kwargs)


def get_market_players(**kwargs):
    api = MarktstammdatenregisterAPI(
        MARKTAKTEUR_MASTR_NUMBER, API_KEY, MarketType.AKTEUR.value)
    return api.get('GetGefilterteListeMarktakteure', **kwargs)


def get_player_info(mastrNummer: str, **kwargs):
    api = MarktstammdatenregisterAPI(
        MARKTAKTEUR_MASTR_NUMBER, API_KEY, MarketType.AKTEUR.value)
    return api.get('GetMarktakteur', mastrNummer=mastrNummer, **kwargs)


power_units = get_power_units(ort='Schiffweiler',
                              energietraeger=Energietraeger.WIND.value)

market_akteurs = get_market_players(ort='Trier',
                                    # marktrollen=Marktfunktion.STROMNETZBETREIBER.value
                                    )

player_info = get_player_info('SNB966813503780')

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
