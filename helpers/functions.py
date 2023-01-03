# -*- coding: utf-8 -*-
"""Some helper functions for the MarktstammdatenregisterAPI class."""

from typing import Any

from datetime import datetime, date

from src.api_accessor import MarktstammdatenregisterAPI
from src.enumeration import (
    AnlagenBetriebsStatus,
    BrennstoffLage,
    BundeslaenderEinheiten,
    EEG_Einheiten,
    Einheiten,
    Energietraeger,
    Marktfunktion,
    Marktrollen,
    MarktTyp,
    Regelzone,
    Spannungsebene,
    TechnologieVerbrennungsanlage
    )


# %% get a specific unit

def get_eeg_unit(unit_type: EEG_Einheiten, unit_number: str) -> dict[str, Any]:
    """
    Get data of power units from the Marktstammdatenregister API.

    Parameters
    ----------
    unit_type: EEG_Einheiten
        Value of the enum `EEG_Einheiten`.
    unit_number: str
       The MaStR number of the desired EEG unit.

    Returns
    -------
    dict[str, Any]
        The data returned by the API method, serialized as a dictionary.
    """
    api = MarktstammdatenregisterAPI(MarktTyp.ANLAGE.value)
    return api.get(unit_type, eegMastrNummer=unit_number)


def get_unit(unit_type: Einheiten, unit_number: str) -> dict[str, Any]:
    """
    Get data of power units from the Marktstammdatenregister API.

    Parameters
    ----------
    unit_type: Einheiten
        Value of the enum `Einheiten`.
    unit_number: str
       The MaStR number of the desired unit.

    Returns
    -------
    dict[str, Any]
        The data returned by the API method, serialized as a dictionary.
    """
    api = MarktstammdatenregisterAPI(MarktTyp.ANLAGE.value)
    return api.get(unit_type, einheitMastrNummer=unit_number)


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


# %% get filtered units

def get_power_units(
        startAb: int | None = None,
        datumAb: datetime | None = None,
        limit: int | None = None,
        einheitBetriebsstatus: AnlagenBetriebsStatus | None = None,
        name: str | None = None,
        energietraeger: Energietraeger | None = None,
        postleitzahl: str | None = None,
        ort: str | None = None,
        einheitBundesland: BundeslaenderEinheiten | None = None,
        bruttoleistung: float | None = None,
        bruttoleistungKleiner: float | None = None,
        bruttoleistungGroesser: float | None = None,
        nettoleistung: float | None = None,
        nettoleistungKleiner: float | None = None,
        nettoleistungGroesser: float | None = None,
        hauptbrennstoff: BrennstoffLage | None = None,
        inbetriebnahmedatum: date | None = None,
        inbetriebnahmedatumKleiner: date | None = None,
        inbetriebnahmedatumGroesser: date | None = None,
        technologie: TechnologieVerbrennungsanlage | None = None,
        lokationNetzbetreiber: str | None = None,
        lokationSpannungsebene: Spannungsebene | None = None,
        eegInbetriebnahmedatum: date | None = None,
        eegInbetriebnahmedatumKleiner: date | None = None,
        eegInbetriebnahmedatumGroesser: date | None = None,
        zuschlagsnummer: str | None = None,
        speicherNutzbareSpeicherkapazität: float | None = None,
        speicherNutzbareSpeicherkapazitätKleiner: float | None = None,
        speicherNutzbareSpeicherkapazitätGroesser: float | None = None,
        Registrierungsdatum: date | None = None,
        RegistrierungsdatumKleiner: date | None = None,
        RegistrierungsdatumGroesser: date | None = None,
        netzRegelzone: Regelzone | None = None,
        AnlagenbetreiberMastrNummer: str | None = None
        ) -> dict[str, Any]:
    """Get data of power units from the Marktstammdatenregister API."""
    api = MarktstammdatenregisterAPI(MarktTyp.ANLAGE.value)
    return api.get(
        'GetGefilterteListeStromErzeuger',
        startAb=startAb,
        datumAb=datumAb,
        limit=limit,
        einheitBetriebsstatus=einheitBetriebsstatus,
        name=name,
        energietraeger=energietraeger,
        postleitzahl=postleitzahl,
        ort=ort, einheitBundesland=einheitBundesland,
        bruttoleistung=bruttoleistung,
        bruttoleistungKleiner=bruttoleistungKleiner,
        bruttoleistungGroesser=bruttoleistungGroesser,
        nettoleistung=nettoleistung, nettoleistungKleiner=nettoleistungKleiner,
        nettoleistungGroesser=nettoleistungGroesser,
        hauptbrennstoff=hauptbrennstoff,
        inbetriebnahmedatum=inbetriebnahmedatum,
        inbetriebnahmedatumKleiner=inbetriebnahmedatumKleiner,
        inbetriebnahmedatumGroesser=inbetriebnahmedatumGroesser,
        technologie=technologie,
        lokationNetzbetreiber=lokationNetzbetreiber,
        lokationSpannungsebene=lokationSpannungsebene,
        eegInbetriebnahmedatum=eegInbetriebnahmedatum,
        eegInbetriebnahmedatumKleiner=eegInbetriebnahmedatumKleiner,
        eegInbetriebnahmedatumGroesser=eegInbetriebnahmedatumGroesser,
        zuschlagsnummer=zuschlagsnummer,
        speicherNutzbareSpeicherkapazität=speicherNutzbareSpeicherkapazität,
        speicherNutzbareSpeicherkapazitätKleiner=speicherNutzbareSpeicherkapazitätKleiner,
        speicherNutzbareSpeicherkapazitätGroesser=speicherNutzbareSpeicherkapazitätGroesser,
        Registrierungsdatum=Registrierungsdatum,
        RegistrierungsdatumKleiner=RegistrierungsdatumKleiner,
        RegistrierungsdatumGroesser=RegistrierungsdatumGroesser,
        netzRegelzone=netzRegelzone,
        AnlagenbetreiberMastrNummer=AnlagenbetreiberMastrNummer
        )


def get_market_players(
        startAb: int | None = None,
        datumAb: datetime | None = None,
        limit: int | None = None,
        name: str | None = None,
        postleitzahl: str | None = None,
        ort: str | None = None,
        bundesland: BundeslaenderEinheiten | None = None,
        marktfunktion: Marktfunktion | None = None,
        Marktrollen: Marktrollen | list[Marktrollen] | None = None,
        MarktrolleMastrNummerIds: str | list[str] | None = None
        ) -> dict[str, Any]:
    """Get data of market players from the Marktstammdatenregister API."""
    api = MarktstammdatenregisterAPI(MarktTyp.AKTEUR.value)
    return api.get(
        'GetGefilterteListeMarktakteure',
        startAb=startAb,
        datumAb=datumAb,
        limit=limit,
        name=name,
        postleitzahl=postleitzahl,
        ort=ort,
        bundesland=bundesland,
        marktfunktion=marktfunktion,
        Marktrollen=Marktrollen,
        MarktrolleMastrNummerIds=MarktrolleMastrNummerIds
        )
