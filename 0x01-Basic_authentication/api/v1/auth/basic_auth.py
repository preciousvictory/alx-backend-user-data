#!/usr/bin/env python3
""" class BasicAuth
"""
from flask import request
from api.v1.auth.auth import Auth
import base64
import binascii
import re


class BasicAuth(Auth):
    """class BasicAuth that inherits from Auth
    """
    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        """ returns the Base64 part of the Authorization header
        for a Basic Authentication
        """
        if authorization_header is None or \
                type(authorization_header) is not str:
            return None

        if authorization_header.split(' ')[0] != 'Basic':
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """ returns the decoded value of a Base64 string
        base64_authorization_header
        """
        if base64_authorization_header is None or \
                type(base64_authorization_header) is not str:
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
        except binascii.Error:
            return None

        return decoded.decode('utf-8')

    def extract_user_credentials(self, decoded_base64_authorization_header: str)\
            -> (str, str):
        """returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None or \
                type(decoded_base64_authorization_header) is not str:
            return None, None

        if not re.search(r':', decoded_base64_authorization_header):
            return None, None

        credentials = decoded_base64_authorization_header.split(':')
        return credentials[0], credentials[1]
