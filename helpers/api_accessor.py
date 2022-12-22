"""..."""

import json
import os

from zeep import Client, Settings, Transport
from zeep.cache import SqliteCache
from zeep.helpers import serialize_object

from helpers.config_reader import ConfigReader


class MarktstammdatenregisterAPI:
    """Simple class to access the API of the Marktstammdatenregister."""

    def __init__(self, market_type: str):
        """Initialize the MarktstammdatenregisterAPI object."""
        # Use os.path.join to construct a file path by joining together a
        # sequence of path components.
        config_path = os.path.join('helpers', 'config.json')

        # Pass the constructed file path to the ConfigReader.
        config = ConfigReader(config_path).read_config()

        # assign data in config to variables
        self.marktakteurMastrNummer = config['MARKTAKTEUR_MASTR_NUMBER']
        self.api_key = config['API_KEY']
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
