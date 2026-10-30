# tests/test_validator.py
from ip_validator import is_valid_ipv4


def test_all_valid_fixture_ips(valid_ips):
    for ip in valid_ips:
        assert is_valid_ipv4(ip) is True, f"должен быть валидным: {ip!r}"


def test_all_invalid_fixture_ips(invalid_ips):
    for ip in invalid_ips:
        assert is_valid_ipv4(ip) is False, f"должен быть невалидным: {ip!r}"


def test_non_string():
    assert is_valid_ipv4(None) is False
    assert is_valid_ipv4(1234) is False
