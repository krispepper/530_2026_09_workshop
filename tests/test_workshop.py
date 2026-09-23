# Purpose: Unit tests for fetching workshop hosts and locations

from model.workshop import get_all_hosts, get_all_locations

def test_get_all_hosts_returns_list():
    hosts = get_all_hosts()
    # Ensure the return type is a list (even if empty in a fresh test DB)
    assert isinstance(hosts, list)

def test_get_all_locations_returns_list():
    locations = get_all_locations()
    assert isinstance(locations, list)