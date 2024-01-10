#!/usr/bin/env python3
"""
function that Define filter_datum & returns an obfuscated log message
"""
import re
from typing import List
import logging


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record and redact specified fields.

        Args:
            record (LogRecord): The log record to be formatted.

        Returns:
            str: The formatted log message.
        """
        message = super(RedactingFormatter, self).format(record)
        redacted = filter_datum(self.fields, self.REDACTION,
                                message, self.SEPARATOR)
        return redacted


if __name__ == "__main__":
    main()
