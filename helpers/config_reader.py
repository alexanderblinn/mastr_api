# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:32:17 2022

@author: s13c2d
"""

import json

class ConfigReader:
    """Class to read configuration data from a JSON file."""

    def __init__(self, config_file: str):
        """Initialize the ConfigReader object."""
        self.config_file = config_file

    def read_config(self):
        """Read the configuration data from the JSON file."""
        with open(self.config_file, 'r') as json_file:
            config = json.load(json_file)
        return config
