#!/usr/bin/env python3
"""
function that Define filter_datum & returns an obfuscated log message
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate specified fields in the log message.

    Arguments:
        fields: List of strings representing fields to obfuscate.
        redaction: String representing the obfuscation for the fields.
        message: String representing the log line.
        separator: String representing the character separating fields.

    Returns:
        String: Log message with specified fields obfuscated.
    """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message


if __name__ == "__main__":
    main()
