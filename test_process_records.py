# test_validation.py
import pytest
from process_records import *

@pytest.fixture(autouse=True)
def reset_records():
    records.clear()

test_data_opened = {
    "id": 1,
    "code": "code1",
    "description": "An opened record",
    "status": "OPENED",
    "date_opened": "2023-01-01",
    "date_closed": None
}

test_data_closed = {
    "id": 2,
    "code": "code2",
    "description": "A closed record",
    "status": "CLOSED",
    "date_opened": None,
    "date_closed": "2023-01-02"
}

test_data_both = {
    "id": 3,
    "code": "code3",
    "description": "A record with both dates",
    "status": "BOTH",
    "date_opened": "2023-01-01",
    "date_closed": "2023-01-03"
}

test_data_both_invalid = {
    "id": 4,
    "code": "code4",
    "description": "",  # Should be converted to None
    "status": "BOTH",
    "date_opened": None,  # Invalid as BOTH requires both dates
    "date_closed": "2023-01-04"
}

test_data_opened_invalid = {
    "id": 5,
    "code": "code5",
    "description": "",  # Should be converted to None
    "status": "OPENED",
    "date_opened": None,  # Invalid as OPENED requires date_opened
    "date_closed": "2023-01-04"
}

test_data_closed_invalid = {
    "id": 6,
    "code": "code6",
    "description": "",  # Should be converted to None
    "status": "CLOSED",
    "date_opened": "2023-01-04",  # Invalid as CLOSED requires date_closed
    "date_closed": None # Invalid as CLOSED requires date_closed
}

test_data_empty_str = {
    "id": 7,
    "code": "code7",
    "description": "",  # Should be converted to None
    "status": "BOTH",
    "date_opened": "2023-01-04", 
    "date_closed": "2023-01-04"
}

test_data_unique_id = {
    "id": 8,
    "code": "code8",
    "description": "",  # Should be converted to None
    "status": "BOTH",
    "date_opened": "2023-01-04", 
    "date_closed": "2023-01-04"
}

#test opened record has open date
def test_record_opened():
    record = Record(**test_data_opened)
    assert record.date_opened is not None


#test closed record has open date
def test_record_closed():
    record = Record(**test_data_closed)
    assert record.date_closed is not None


#test both record has both dates
def test_record_both():
    record = Record(**test_data_both)
    assert record.date_opened is not None and record.date_closed is not None

#test both record without both dates raises error
def test_record_both_invalid():
    with pytest.raises(ValidationError):
        Record(**test_data_both_invalid)

#test opened record without opened date raises error
def test_record_opened_invalid():
    with pytest.raises(ValidationError):
        Record(**test_data_opened_invalid)

#test closed record without closed date raises error
def test_record_closed_invalid():
    with pytest.raises(ValidationError):
        Record(**test_data_closed_invalid)

#test empty description string is converted to null
def test_record_empty_str():
    record = Record(**test_data_empty_str)
    assert record.description is None

#test record must have unique id
def test_record_unique_id():
     record=Record(**test_data_unique_id)
     records.append(record)
     with pytest.raises(ValidationError):
         Record(**test_data_unique_id)
