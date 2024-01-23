#!/usr/bin/env python3
"""
Definition of _hash_password function
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash the input password with bcrypt
    Args:
        password (str): password in string format
    """
    passwd = password.encode('utf-8')
    return bcrypt.hashpw(passwd, bcrypt.gensalt())
