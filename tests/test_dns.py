from unittest.mock import patch
import socket
from infra_glass.core.dns import get_ip_addresses


# Test 1: Empty DNS response
def test_get_ip_addresses_empty():
    with patch("infra_glass.core.dns.socket.getaddrinfo", return_value=[]):
        result = get_ip_addresses("example.com")

    assert result == {"IPv4": [], "IPv6": []}


# Test 2: Successful DNS response
def test_get_ip_addresses_success():
    fake_response = [
        (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("192.0.2.1", 0)),
        (socket.AF_INET6, socket.SOCK_STREAM, 6, "", ("2001:db8::1", 0, 0, 0)),
    ]

    with patch("infra_glass.core.dns.socket.getaddrinfo", return_value=fake_response):
        result = get_ip_addresses("example.com")

    assert result == {
        "IPv4": ["192.0.2.1"],
        "IPv6": ["2001:db8::1"]
    }


# Test 3: Duplicate IP addresses
def test_get_ip_addresses_duplicates():
    fake_response = [
        (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("192.0.2.1", 0)),
        (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("192.0.2.1", 0)),
        (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("192.0.2.2", 0)),
    ]

    with patch("infra_glass.core.dns.socket.getaddrinfo", return_value=fake_response):
        result = get_ip_addresses("example.com")

    assert result == {
        "IPv4": ["192.0.2.1", "192.0.2.2"],
        "IPv6": []
    }


# Test 4: DNS resolution failure
def test_get_ip_addresses_failure():
    with patch(
        "infra_glass.core.dns.socket.getaddrinfo",
        side_effect=socket.gaierror
    ):
        result = get_ip_addresses("invalid-domain.test")
