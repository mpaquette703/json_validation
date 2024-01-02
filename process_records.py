from typing import Optional
from pydantic import BaseModel, model_validator, ValidationError
import json

records = []

# Define the Pydantic model
class Record(BaseModel):
    id: int
    code: str
    description: Optional[str] = None
    status: str
    date_opened: Optional[str] = None
    date_closed: Optional[str] = None

    #Convert any empty strings to null
    def __init__(self, **data):
        # Check and set 'description', 'date_opened', and 'date_closed' to None if they are empty strings
        for field in ['code','description','status', 'date_opened', 'date_closed']:
            if field in data and isinstance(data[field], str) and not data[field].strip():
                data[field] = None

        super().__init__(**data)

    #Validate that "opened" records have opened dates
    @model_validator(mode='after')
    def validators(self) -> 'Record':
        #Check for unique ID
        for record in records:
            if record.id == self.id:
                raise ValueError('id must be unique')
        #Check date_opened not null when status is "OPENED"
        if self.status == 'OPENED' and not self.date_opened:
            raise ValueError('date_opened cannot be null with status equal to "OPENED"')
        #Check date_closed not null when status is "CLOSED"
        if self.status == 'CLOSED' and not self.date_closed:
            raise ValueError('date_closed cannot be null with status equal to "CLOSED"')
        #Check date_openedand date_closed not null when status is "BOTH"
        if self.status == 'BOTH':
            if not self.date_opened or not self.date_closed:
                raise ValueError('date_opened and date_closed cannot be null with status equal to "BOTH"')
        return self
    
# Read JSON file
with open('example_dataset.json') as file:
    data = json.load(file)

#Validate data
for item in data:
    try:
        record = Record(**item)
        records.append(record)
    except ValidationError as e:
        print(f"Error in record {item['id']}: {e}")

# Write to a new-line delimited JSON file
with open('output.json', 'w') as file:
    for record in records:
        file.write(record.model_dump_json() + '\n')
