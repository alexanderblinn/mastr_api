# -*- coding: utf-8 -*-
"""
A simple script for reading configuration data from a JSON file.

It defines a ConfigReader class with a method for reading the
configuration data from the JSON file.
"""

import json


class ConfigReader:
    """Class for reading configuration data from a JSON file."""

    def __init__(self, config_file: str) -> None:
        """
        Initialize the ConfigReader object.

        Parameters
        ----------
        config_file : str
            The file path of the JSON configuration file.

        Returns
        -------
        None
        """
        self.config_file = config_file

    def read_config(self) -> dict:
        """
        Read the configuration data from the JSON file.

        Returns
        -------
        dict
            The configuration data in the JSON file..
        """
        with open(self.config_file, 'r') as json_file:
            config = json.load(json_file)
        return config
