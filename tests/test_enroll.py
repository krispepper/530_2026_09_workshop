# Purpose: Unit tests for checking available workshop slots and enrollment logic

from model.enroll import get_available_timeslots

def test_get_available_timeslots_returns_list():
    # Test passing a mock user ID (e.g., ID 1) to verify query structure
    slots = get_available_timeslots(1)
    assert isinstance(slots, list)