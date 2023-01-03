# -*- coding: utf-8 -*-
"""
A simple class for accessing the API of the Marktstammdatenregister.

To use this class, you must first register as a Webdienstnutzer/Marktakteur on
the Marktstammdatenregister website:
    https://test.marktstammdatenregister.de/MaStR

Once you have registered, you will receive a marktakteurMastrNummer and an
apiKey, which you can use to access the API.
"""

import os
from typing import Any

from zeep import Client, Settings, Transport
from zeep.cache import SqliteCache
from zeep.helpers import serialize_object

from src.config_reader import ConfigReader
from src.enumeration import MarktTyp


class MarktstammdatenregisterAPI:
    """A class for accessing the API of the Marktstammdatenregister."""

    def __init__(self, market_type: MarktTyp) -> None:
        """Initialize the MarktstammdatenregisterAPI object.

        Parameters
        ----------
        market_type : MarktTyp
            The type of market to retrieve data for.

        Returns
        -------
        None
        """
        # Read config data from file.
        config_path = os.path.join('src', 'config.json')
        config = ConfigReader(config_path).read_config()

        # Assign data in config file to variables.
        self.marktakteurMastrNummer = config['MARKTAKTEUR_MASTR_NUMBER']
        self.api_key = config['API_KEY']
        self.market_type = market_type

        # Set up the client object to make API requests.
        api_endpoint = \
            "https://www.marktstammdatenregister.de/MaStRAPI/wsdl/mastr.wsdl"
        transport = Transport(cache=SqliteCache())
        settings = Settings(strict=False, xml_huge_tree=True)
        self.client = Client(
            wsdl=api_endpoint, transport=transport, settings=settings)
        self.client_bind = self.client.bind(
            'Marktstammdatenregister', self.market_type)

    def get(self, method_name: str, **kwargs: dict[str, Any]
            ) -> dict[str, Any] | list[dict[str, Any]]:
        """Retrieve data from the Marktstammdatenregister API.

        Parameters
        ----------
        method_name : str
            The name of the API method to call.
        **kwargs : dict[str, Any]
            Additional keyword arguments to pass to the API method. See the
            documentation to learn more about the valid keyword arguments.

        Returns
        -------
        dict[str, Any] | list[dict[str, Any]]
            The data returned by the API method, serialized as a dictionary
            or list of dictionaries.
        """
        # Get the specified method from the client binding.
        method = getattr(self.client_bind, method_name)
        # Call the method and pass the required arguments.
        data = method(
            apiKey=self.api_key,
            marktakteurMastrNummer=self.marktakteurMastrNummer,
            **kwargs)
        # Serialize the data and return it.
        return serialize_object(data)
