# -*- coding: utf-8 -*-
"""
Enumerations for the Marktstammdatenregister API.

This file contains enumerations that can be used when interacting with the API
of the Marktstammdatenregister. The enumerations provide a convenient way to
specify certain parameters when making API requests, such as the type of
market data to retrieve or the format of the response.
"""

from enum import Enum


# class Einheiten(Enum):
#     # get unit
#     BIOMASSE = 'GetEinheitBiomasse'
#     GASERZEUGER = 'GetEinheitGasErzeuger'
#     GASSPEICHER = 'GetEinheitGasSpeicher'
#     GASVERBRAUCHER = 'GetEinheitGasVerbraucher'
#     GENEHMIGUNG = 'GetEinheitGenehmigung'
#     KERNKRAFT = 'GetEinheitKernkraft'
#     REST = 'GetEinheitGeoSolarthermieGrubenKlaerschlamm'
#     STROMSPEICHER = 'GetEinheitStromspeicher'
#     STROMVERBRAUCHER = 'GetEinheitStromverbraucher'
#     SOLAR = 'GetEinheitSolar'
#     VERBRENNUNG = 'GetEinheitVerbrennung'
#     WASSER = 'GetEinheitWasser'
#     WIND = 'GetEinheitWind'
#     # filter units by a search query
#     FILTER = 'GetGefilterteListeStromErzeuger'


# Einheiten = {e.name: e.value for e in Einheiten}

class MarktTyp(Enum):
    AKTEUR = 'Akteur'
    ANLAGE = 'Anlage'
    # ALLGEMEINE_FUNKTIONEN = 'AllgemeineFunktionen'
    # NETZANSCHLUSSPUNKT = 'Netzanschlusspunkt'
    # NETZBETREIBERPRUEFUNG = 'Netzbetreiberpruefung'


class Id(Enum):
    BilanzierungsgebietId: int
    EegMastrNummerId: str
    EinheitMastrNummerId: str
    EinsatzverantwortlicherMaStRNummerId: str
    ErtuechtigungId: str
    GasSpeicherMastrNummerId: str
    GenMastrNummerId: str
    KatalogkategorieId: int
    KatalogwertId: int
    KorrekturVorschlagId: int
    KwkMastrNummerId: str
    LokationMastrNummerId: str
    MaStRNummerId: str
    MarktakteurMastrNummerId: str
    ...  # Rest ab S. 710 fehlt


class ErgebniscodeTyp(Enum):
    OK = 'OK'
    OK_WEITERE_DATEN_VORHANDEN = 'OkWeitereDatenVorhanden'
    KEINE_DATEN_VORHANDEN = 'KeineDatenVorhanden'


class AnlagenBetriebsStatus(Enum):
    NONE = 'None'
    INPLANUNG = 'InPlanung'
    INBETRIEB = 'InBetrieb'
    VORUEBERGEHEND_STILLGELEGT = 'VoruebergehendStillgelegt'
    DAUERHAFT_STILLGELEGT = 'DauerhaftStillgelegt'
    INBETRIEBNAHME_VORBEREITEN = 'InBetriebnahmeVorbereiten'


class AnlagenSystemStatus(Enum):
    NONE = 'None'
    AKTIV = 'Aktiv'
    DEAKTIVIERT = 'Deaktiviert'
    UNGEPRUEFT = 'Ungeprueft'
    UNVOLLSTAENDIG = 'Unvollstaendig'
    GELOESCHT = 'Geloescht'


class AnlagenTypStatus(Enum):
    INUEBERTRAGUNG = 'InUebertragung'
    UEBERTRAGUNG = 'Uebertragung'


class AnlagenUebertragungStatus(Enum):
    NotImplementedError


class Anlagenart(Enum):
    NotImplementedError


class AnlagenartSolarAusrichtung(Enum):
    NotImplementedError


class AnlagenartSolarNeigungswinkel(Enum):
    NotImplementedError


class Anlagentyp(Enum):
    SOLARESTRAHLUNGSENERGIE = 'SolareStrahlungsenergie'
    WIND = 'Wind'
    VERBRENNUNGSANLAGE = 'Verbrennungsanlage'
    VERBRENNUNGSANLAGE_BIOMASSE = 'VerbrennungsanlageBiomasse'
    WASSER = 'Wasser'
    SONSTIGE = 'SonstigeAnlage'
    GEOTHERMIE = 'Geothermie'
    KERNENERGIE = 'Kernenergie'
    SPEICHER = 'Speicher'
    GASERZEUGUNGSANLAGE = 'Gaserzeugungsanlage'
    STROMVERBRAUCHSANLAGE = 'Stromverbrauchsanlage'
    GASVERBRAUCHSANLAGE = 'Gasverbrauchsanlage'


class ArtAbschaltbareLast(Enum):
    NONE = 'None'
    SOFORT = 'Sofort'
    SCHNELL = 'Schnell'
    TEMPORAERBEFRISTET = 'Temporaerbefristet'


class ArtDerStilllegung(Enum):
    VORLAEUFIG = 'Vorlaeufig'
    ENDGUELTIG = 'Endgueltig'


class ArtDerWasserkraftanlage(Enum):
    NotImplementedError


class BatterieTechnologie(Enum):
    NONE = 'None'
    LITHIUM = 'LithiumBatterie'
    BLEI = 'BleiBatterie'
    REDOX_FLOW = 'RedoxFlowBatterie'
    HOCHTEMPERATUR = 'Hochtemperaturbatterie'
    NICKEL_CADMIUM_OR_NICKEL_METALLHYDRID = 'NickelCadmiumOrNickelMetallhydridbatterie'
    SONSTIGE = 'SonstigeBatterie'


class BenutzerRollenGruppen(Enum):
    NotImplementedError


class BenutzerStatus(Enum):
    NotImplementedError


class BiomasseArt(Enum):
    NotImplementedError


class BiomasseBrennstoff(Enum):
    NotImplementedError


class BrennstoffLage(Enum):
    NotImplementedError


class BrennstoffSonstige(Enum):
    NotImplementedError


class BrennstoffeVerbrennungsanlagen(Enum):
    NotImplementedError


class BundeslaenderEinheiten(Enum):
    NONE = 'None'
    AUSSCHLIESSLICHE_WIRTSCHAFTSZONE = 'AusschliesslicheWirtschaftszone'
    BADENWUERTTEMBERG = 'BadenWuerttemberg'
    BAYERN = 'Bayern'
    BERLIN = 'Berlin'
    BRANDENBURG = 'Brandenburg'
    BREMEN = 'Bremen'
    HAMBURG = 'Hamburg'
    HESSEN = 'Hessen'
    MECKLENBURG_VORPOMMERN = 'MecklenburgVorpommern'
    NIEDERSACHSEN = 'Niedersachsen'
    NORDRHEIN_WESTFALEN = 'NordrheinWestfalen'
    RHEINLAND_PFALZ = 'RheinlandPfalz'
    SAARLAND = 'Saarland'
    SACHSEN = 'Sachsen'
    SACHSEN_ANHALT = 'SachsenAnhalt'
    SCHLESWIG_HOLSTEIN = 'SchleswigHolstein'
    THUERINGEN = 'Thueringen'


class Bundeslaender(Enum):
    NONE = 'None'
    BADENWUERTTEMBERG = 'BadenWuerttemberg'
    BAYERN = 'Bayern'
    BERLIN = 'Berlin'
    BRANDENBURG = 'Brandenburg'
    BREMEN = 'Bremen'
    HAMBURG = 'Hamburg'
    HESSEN = 'Hessen'
    MECKLENBURG_VORPOMMERN = 'MecklenburgVorpommern'
    NIEDERSACHSEN = 'Niedersachsen'
    NORDRHEIN_WESTFALEN = 'NordrheinWestfalen'
    RHEINLAND_PFALZ = 'RheinlandPfalz'
    SAARLAND = 'Saarland'
    SACHSEN = 'Sachsen'
    SACHSEN_ANHALT = 'SachsenAnhalt'
    SCHLESWIG_HOLSTEIN = 'SchleswigHolstein'
    THUERINGEN = 'Thueringen'


class ClusterNordsee(Enum):
    NotImplementedError


class ClusterOstsee(Enum):
    NotImplementedError


class EegTyp(Enum):
    NotImplementedError


class EinheitArt(Enum):
    STROMERZUEUGUNGSEINHEIT = 'Stromerzeugungseinheit'
    STROMVERBRAUCHSEINHEIT = 'Stromverbrauchseinheit'
    GASERZEUGUNGSEINHEIT = 'Gaserzeugungseinheit'
    GASVERBRAUCHSEINHEIT = 'Gasverbrauchseinheit'


class EinheitSparte(Enum):
    NONE = 'None'
    STROM = 'Strom'
    GAS = 'Gas'


class EinheitTyp(Enum):
    SOLAREINHEIT = 'Solareinheit'
    WINDEINHEIT = 'Windeinheit'
    BIOMASSE = 'Biomasse'
    WASSER = 'Wasser'
    GEOTHERMIE = 'Geothermie'
    VERBRENNUNG = 'Verbrennung'
    KERNENERGIE = 'Kernenergie'
    STROMSPEICHEREINHEIT = 'Stromspeichereinheit'
    STROMVERBRAUCHSEINHEIT = 'Stromverbrauchseinheit'
    GASVERBRAUCHSENHEIT = 'Gasverbrauchseinheit'
    GASERZEUGUNGSEINHEIT = 'Gaserzeugungseinheit'
    GASSPEICHEREINHEIT = 'Gasspeichereinheit'


class EinheitenGruppierungsTyp(Enum):
    NotImplementedError


class Einsatzort(Enum):
    NotImplementedError


class Einspeisungsart(Enum):
    NONE = 'None'
    VOLLEINSPEISUNG = 'Volleinspeisung'
    TEILEINSPEISUNG = 'Teileinspeisung'


class Energietraeger(Enum):
    NONE = 'None'
    ANDERE_GASE = 'AndereGase'
    BIOMASSE = 'Biomasse'
    BRAUNKOHLE = 'Braunkohle'
    ERDGAS = 'Erdgas'
    GEOTHERMIE = 'Geothermie'
    GRUBENGAS = 'Grubengas'
    KERNENERGIE = 'Kernenergie'
    KLAERSCHLAMM = 'Klaerschlamm'
    MINERALOEL_PRODUKTE = 'Mineraloelprodukte'
    NICHT_BIOGENER_ABFALL = 'NichtBiogenerAbfall'
    SOLAR = 'SolareStrahlungsenergie'
    SOLARTHERMIE = 'Solarthermie'
    SPEICHER = 'Speicher'
    STEINKOHLE = 'Steinkohle'
    WAERME = 'Waerme'
    WASSER = 'Wasser'
    WIND = 'Wind'


class ErtuechtigungsmassnahmeWasserkraft(Enum):
    NotImplementedError


class GasSpeicherart(Enum):
    NotImplementedError


class GasartDerErzeugung(Enum):
    NotImplementedError


class Gasqualitaet(Enum):
    NotImplementedError


class Genehmigungsart(Enum):
    NotImplementedError


class KlaerungsGrund(Enum):
    NotImplementedError


class LaenderEinheiten(Enum):
    NotImplementedError


class Land(Enum):
    NotImplementedError


class LeistungsAenderung(Enum):
    NotImplementedError


class LeistungsaenderungsAnlagenart(Enum):
    NotImplementedError


class Leistungsaenderungsart(Enum):
    NotImplementedError


class LokationTyp(Enum):
    NotImplementedError


class MarktakteurStatus(Enum):
    NotImplementedError


class Marktfunktion(Enum):
    STROMNETZBETREIBER = 'Stromnetzbetreiber'
    ANLAGENBETREIBER = 'Anlagenbetreiber'
    AKTEURIMSTROMMARKT = 'AkteurImStrommarkt'
    ORGANISIERTEMARKTPLAETZE = 'OrganisierteMarktplaetze'
    BEHOERDEN = 'Behoerden'
    SONSTIGEMARKTAKTEURE = 'SonstigeMarktakteure'
    BUNDESNETZAGENTUR = 'Bundesnetzagentur'
    GASNETZBETREIBER = 'Gasnetzbetreiber'
    AKTEURIMGASMARKT = 'AkteurImGasmarkt'
    SUPPORTPARTNER = 'Supportpartner'


class MarktfunktionStatus(Enum):
    NotImplementedError


class Marktgebiet(Enum):
    NotImplementedError


class Marktrollen(Enum):
    NetzbetreiberUebertragungsnetzbetreiber = 'NetzbetreiberUebertragungsnetzbetreiber'
    NetzbetreiberAnschlussnetzbetreiberStrom = 'NetzbetreiberAnschlussnetzbetreiberStrom'
    NetzbetreiberBilanzkreisverantwortlicherStrom = 'NetzbetreiberBilanzkreisverantwortlicherStrom'
    NetzbetreiberBilanzkoordinatorStrom = 'NetzbetreiberBilanzkoordinatorStrom'
    NetzbetreiberMessstellenbetreiberStrom = 'NetzbetreiberMessstellenbetreiberStrom'
    NetzbetreiberFernleitungsnetzbetreiberGas = 'NetzbetreiberFernleitungsnetzbetreiberGas'
    NetzbetreiberMarktgebietsverantwortlicheGas = 'NetzbetreiberMarktgebietsverantwortlicheGas'
    NetzbetreiberAnschlussnetzbetreiberGas = 'NetzbetreiberAnschlussnetzbetreiberGas'
    NetzbetreiberMessstellenbetreiberGas = 'NetzbetreiberMessstellenbetreiberGas'
    EnergiemarktakteureStromlieferant = 'EnergiemarktakteureStromlieferant'
    EnergiemarktakteureBilanzkreisverantwortlicherStrom = 'EnergiemarktakteureBilanzkreisverantwortlicherStrom'
    EnergiemarktakteureMessstellenbetreiberStrom = 'EnergiemarktakteureMessstellenbetreiberStrom'
    EnergiemarktakteureBilanzkreisverantwortlicherGas = 'EnergiemarktakteureBilanzkreisverantwortlicherGas'
    EnergiemarktakteureMessstellenbetreiberGas = 'EnergiemarktakteureMessstellenbetreiberGas'
    EnergiemarktakteureGastransportkunden = 'EnergiemarktakteureGastransportkunden'
    OrganisierteMarktplaetzeCaoCasc = 'OrganisierteMarktplaetzeCaoCasc'
    OrganisierteMarktplaetzeBoerse = 'OrganisierteMarktplaetzeBoerse'
    OrganisierteMarktplaetzeOTCPlattform = 'OrganisierteMarktplaetzeOTCPlattform'
    OrganisierteMarktplaetzeBetreiberEinerBuchungsplattformFuerGasspeicher = 'OrganisierteMarktplaetzeBetreiberEinerBuchungsplattformFuerGasspeicher'
    OrganisierteMarktplaetzeBetreiberEinerBuchungsplattformfuerGaskapazitaeten = 'OrganisierteMarktplaetzeBetreiberEinerBuchungsplattformfuerGaskapazitaeten'
    BehoerdenBehoerden = 'BehoerdenBehoerden'
    BehoerdenenergiewirtschaftlicherVerband = 'BehoerdenenergiewirtschaftlicherVerband'
    BehoerdenenergiewirtschaftlicheInstitution = 'BehoerdenenergiewirtschaftlicheInstitution'
    SonstigeMarktakteureDienstleister = 'SonstigeMarktakteureDienstleister'
    SonstigeMarktakteureSonstige = 'SonstigeMarktakteureSonstige'


class MastrZugangStatus(Enum):
    NotImplementedError


class NaceAbschnitt(Enum):
    NotImplementedError


class NaceAbteilung(Enum):
    NotImplementedError


class NaceGruppe(Enum):
    NotImplementedError


class NetzbetreiberpruefungsStatus(Enum):
    NotImplementedError


class NummernkreisTypen(Enum):
    NotImplementedError


class Nutzungsbereich(Enum):
    NotImplementedError


class Personenart(Enum):
    NotImplementedError


class Pumpspeichertechnologie(Enum):
    NotImplementedError


class Regelzone(Enum):
    NotImplementedError


class RegisterNrPraefix(Enum):
    NotImplementedError


class Rollen(Enum):
    NotImplementedError


class Salutation(Enum):
    NotImplementedError


class Seelage(Enum):
    NotImplementedError


class SolarFlaechenart(Enum):
    NotImplementedError


class SolarLage(Enum):
    NotImplementedError


class SolarLeistungsbegrenzung(Enum):
    NotImplementedError


class Spannungsebene(Enum):
    NotImplementedError


class Sparte(Enum):
    NotImplementedError


class SpeicherTyp(Enum):
    NotImplementedError


class Standortangabe(Enum):
    NotImplementedError


class StilllegungsArt(Enum):
    NotImplementedError


class Systemkopplung(Enum):
    NotImplementedError


class TechnologieGasErzeugung(Enum):
    NotImplementedError


class TechnologieKernkraft(Enum):
    NotImplementedError


class TechnologieSpeicher(Enum):
    NotImplementedError


class TechnologieVerbrennungsanlage(Enum):
    NotImplementedError


class TicketProzessKategorie(Enum):
    NotImplementedError


class Titel(Enum):
    NotImplementedError


class VerbrennungArt(Enum):
    NotImplementedError


class VerbrennungBrennstoff(Enum):
    NotImplementedError


class Wechselrichter(Enum):
    NotImplementedError


class WeitereBrennstoffe(Enum):
    NotImplementedError


class WindLage(Enum):
    NotImplementedError


class WindanlageTechnologie(Enum):
    NotImplementedError


class Zuflussart(Enum):
    NotImplementedError
