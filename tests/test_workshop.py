# Purpose: Unit tests to verify that workshop, host, and location query functions return valid lists.

from model.workshop import get_all_hosts, get_all_locations, get_all_workshops

def test_get_all_hosts():
    # Test that fetching all hosts returns a list structure
    hosts = get_all_hosts()
    assert isinstance(hosts, list)

def test_get_all_locations():
    # Test that fetching all locations returns a list structure
    locations = get_all_locations()
    assert isinstance(locations, list)

def test_get_all_workshops():
    # Test that fetching all workshops returns a list structure
    workshops = get_all_workshops()
    assert isinstance(workshops, list)