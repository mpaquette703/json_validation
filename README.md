This repository uses the Pydantic V2 python library to validate and process data coming from a simple json file. 
The `process_records.py` script does all of the business logic validation and processing while the pytest, `test_process_records.py` can be run to validate those requirements.

Pydantic was choosen for this task as it seems to be a standard in data engineering, and is very simple to use. I found that consolidating all of the validators into one function made the code run faster, as well as make it easier to maintain and debug. 

If this were going to be used on much larger datasets, I would consider the following updates:
  - batch processing in chunks
  - asynchronous processing
  - log errors to a file rather than printing them 
  - Experiment with validating unique IDs using sets or dictionaries rather than lists

Using this code as a baseline for working with semi or unstructured data could require some changes such as:
  - adding different validators for different data sources 
  - pre-processing the data into dictionaries or other structures that can work more easily with model
  - incorporate schema inference tools
  - experiement with schema inference via language models
