#!/usr/bin/env python3
""" class Auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ a class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth"""
        if path is None or excluded_paths is None:
            return True

        for excluded_path in excluded_paths:
            if path[-1] != '/':
                path = '{}/'.format(path)

            if path in excluded_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header """
        if request is None:
            return None

        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user """
        return None
