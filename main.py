# -*- coding: utf-8 -*-
"""A script to demonstrate how to use the MarktstammdatenregisterAPI class."""

import pandas as pd

from src.enumeration import (
    BundeslaenderEinheiten,
    EEG_Einheiten,
    Einheiten,
    Marktfunktion
    )
from helpers.functions import (
    get_eeg_unit,
    get_unit,
    get_player,
    get_units,
    get_players
    )


if __name__ == '__main__':
    # Usage example to get data of a specific EEG unit.
    eeg_unit = get_eeg_unit(EEG_Einheiten.WASSER.value, 'EEG961283324996')

    # Usage example to get data of a specific power unit.
    unit = get_unit(Einheiten.KERNKRAFT.value, 'SEE943690268513')
    unit = get_unit(Einheiten.WASSER.value, 'SEE904976795352')

    # Usage example to get data of a specific power unit.
    player = get_player(mastr_nummer='SNB943841101959')

    # Usage example to get data of power units that match a filter.
    units = get_units(ort='Birkenfeld')
    units = pd.DataFrame(units['Einheiten'])

    # Usage example to get data of market players that match a filter.
    players = get_players(
        bundesland=BundeslaenderEinheiten.SAARLAND.value,
        marktfunktion=Marktfunktion.STROMNETZBETREIBER.value
        )
    players = pd.DataFrame(players['Marktakteure'])
