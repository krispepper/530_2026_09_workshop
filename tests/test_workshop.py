# Purpose: Unit tests for fetching workshop hosts, locations, and workshops

from model.workshop import get_all_hosts, get_all_locations, get_all_workshops

def test_get_all_hosts():
    hosts = get_all_hosts()
    assert isinstance(hosts, list)

def test_get_all_locations():
    locations = get_all_locations()
    assert isinstance(locations, list)

def test_get_all_workshops():
    workshops = get_all_workshops()
    assert isinstance(workshops, list)