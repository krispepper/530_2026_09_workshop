# Purpose: Unit tests to verify the workshop timeslot filtering logic for enrollments.

from model.enroll import get_available_timeslots

def test_get_available_timeslots_returns_list():
    # Test that passing a sample user ID returns available slots as a list
    slots = get_available_timeslots(1)
    assert isinstance(slots, list)