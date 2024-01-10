#!/usr/bin/env python3
"""
Define a hash_password function & return a hashed password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes the provided password using bcrypt with a salt.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The salted, hashed password as a byte string.
    """
    b = password.encode()
    hashed = hashpw(b, bcrypt.gensalt())
    return hashed
