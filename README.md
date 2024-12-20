# Currency Converter Microservice

This microservice provides currency conversion functionality. It listens for requests on a specified socket, processes the conversion, and returns the results.

## Features

- Converts a specified amount from one currency to multiple requested currencies.
- Supports sorting of the results based on currency or value.
- Errors are handled by returning an empty response if conversion fails.

## Requirements

- Python 3.x
- `zmq` library
- `json` library
- `currency_converter` library

## Installation

1. Install the required libraries using pip:
    ```bash
    pip install pyzmq currencyconverter
    ```

2. Save the provided script as `CurrencyConversionMicroservice.py`.

## Usage

1. Start the Currency Converter:
    ```bash
    python CurrencyConversionMicroservice.py
    ```

2. The service will start and listen for requests on `tcp://*:5555`. NOTE: Propper Port needs to be open if not on the same system.

# Communication Contract and UML:
## Request Format

Send a JSON object with the following structure:

(NOTE: A list of Currency Abbrevations can be found here in file CurrencyAbbrevation.md)
```json
{
    "SORT": "CURR" or "VALUE" or "",
    "NOW_CURR": "current_currency_code",
    "AMOUNT": amount_to_convert,
    "REQ_CURR": ["currency_code1", "currency_code2", ...]
}
```

- `SORT`: Specifies how to sort the results. Option 1:  is `CURR` (by currency) returns a sort based on Currency abbreviation, Option 2: is `VALUE` (by converted value) returns a sort based on conversion amounts, Option 3: is `` (no sorting) returns the calulations based on order in orignal request.
- `NOW_CURR`: The currency abbreviation code of the amount to be converted.
- `AMOUNT`: The amount to be converted.
- `REQ_CURR`: A list of currency abbreviation codes in list form to which the amount should be converted.

## Response Format

The service returns a JSON object with the following structure:
```json
{
    "CURR": ["currency_code1", "currency_code2", ...],
    "AMOUNT": [converted_amount1, converted_amount2, ...],
    "SORT": "CURR" or "VALUE" or "NONE",
    "REQ_CURR": "current_currency_code",
    "REQ_AMOUNT": amount_to_convert,
    "ADDR": "tcp://*:5555"
}
```

- `CURR`: A list of requested currency abbreviation codes in order of the amounts.
- `AMOUNT`: A list of converted amounts corresponding to the requested currencies.
- `SORT`: The sorting method used.
- `REQ_CURR`: The original currency abbreviation code.
- `REQ_AMOUNT`: The original amount to be converted.
- `ADDR`: The address of the Currency Converter.

## Example

Request:
```json
{
    "SORT": "VALUE",
    "NOW_CURR": "USD",
    "AMOUNT": 100,
    "REQ_CURR": ["EUR", "JPY", "GBP"]
}
```

Response:
```json
{
    "CURR": ["JPY", "EUR", "GBP"],
    "AMOUNT": [10850.0, 85.0, 75.0],
    "SORT": "VALUE",
    "REQ_CURR": "USD",
    "REQ_AMOUNT": 100,
    "ADDR": "tcp://*:5555"
}
```

## Error Handling

If the conversion fails, the service returns an empty response with the same structure but with empty `CURR` and `AMOUNT` lists.


## UML Sequence Diagram

```mermaid

sequenceDiagram
    participant Client
    participant Currency Converter Microservice
    participant Currency Converter
    
    Client->>+Currency Converter Microservice: Send JSON Request
    Currency Converter Microservice->>Currency Converter Microservice: Receive Request
    Currency Converter Microservice->>Currency Converter Microservice: Parse JSON
    Currency Converter Microservice->>Currency Converter: Convert Amounts
    Currency Converter-->>Currency Converter Microservice: Return Converted Amounts
    Currency Converter Microservice->>Currency Converter Microservice: Sort Results
    Currency Converter Microservice->>Currency Converter Microservice: Add Address to Response
    Currency Converter Microservice->>Currency Converter Microservice: Convert Response to JSON
    Currency Converter Microservice-->>-Client: Convert Response to JSON
```
