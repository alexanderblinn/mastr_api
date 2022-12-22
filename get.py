# -*- coding: utf-8 -*-
"""
In order to access the API of the Marktstammdatenregister, registration as a Webdienstnutzer/Marktakteur is required.
Link: https://test.marktstammdatenregister.de/MaStR
After registration a marktakteurMastrNummer and an apiKey are available for use.
"""


from helpers.api_accessor import MarktstammdatenregisterAPI
from helpers.enumeration import *



def get_power_units(**kwargs):
    api = MarktstammdatenregisterAPI(MarketType.ANLAGE.value)
    return api.get('GetGefilterteListeStromErzeuger', **kwargs)


def get_market_players(**kwargs):
    api = MarktstammdatenregisterAPI(MarketType.AKTEUR.value)
    return api.get('GetGefilterteListeMarktakteure', **kwargs)


def get_player_info(mastrNummer: str, **kwargs):
    api = MarktstammdatenregisterAPI(MarketType.AKTEUR.value)
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
