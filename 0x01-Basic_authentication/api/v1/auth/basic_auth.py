#!/usr/bin/env python3
""" class BasicAuth
"""
from flask import request
from api.v1.auth.auth import Auth
import re


class BasicAuth(Auth):
    """class BasicAuth that inherits from Auth
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization header
        for a Basic Authentication
        """
        if authorization_header is None or type(authorization_header) is not str:
            return None

        if authorization_header.split(' ')[0] != 'Basic':
            return None

        return authorization_header.split(' ')[1]
