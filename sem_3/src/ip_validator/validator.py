# src/ip_validator/validator.py
"""Валидация IPv4-адресов."""

import re

_OCTET = r"(?:0|[1-9][0-9]{0,2})"  # без ведущих нулей
_IPV4_RE = re.compile(rf"{_OCTET}(?:\.{_OCTET}){{3}}\Z", re.ASCII)


def is_valid_ipv4(ip: str) -> bool:
    """Проверяет, является ли строка корректным IPv4-адресом в виде a.b.c.d.

    Каждый октет — число 0..255 без ведущих нулей.

    Examples:
        >>> is_valid_ipv4("192.168.0.1")
        True
        >>> is_valid_ipv4("256.1.1.1")
        False
    """
    if not isinstance(ip, str):
        return False
    if _IPV4_RE.match(ip) is None:
        return False
    return all(int(part) <= 255 for part in ip.split("."))
