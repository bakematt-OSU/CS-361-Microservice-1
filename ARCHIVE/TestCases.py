# FUNCTIONALITY TEST CASES:
# TEST CASE: BASE FUNCTIONALITY "SHOULD RETURN EXACT SAME AMOUNT"
Case1 = {
    "REQ_CURR": ["USD"],
    "SORT": "",
    "NOW_CURR": "USD",
    "AMOUNT": 100.00
    }

# SORT TEST CASES:
# TEST CASE: "SORT BASED ON VALUES RETURNED"
Case2 = {
    "REQ_CURR": ["EUR", "CAD", "AUD", "CHF", "JPY"],
    "SORT": "VALUE",
    "NOW_CURR": "USD",
    "AMOUNT": 100.00
    }

# TEST CASE: "NO SORT SPECIFIED"
Case3 = {
    "REQ_CURR": ["EUR", "CAD", "AUD", "CHF", "JPY"],
    "SORT": "",
    "NOW_CURR": "USD",
    "AMOUNT": 100.00
    }

# TEST CASE: "SORT BASED ON CURR NAME"
Case4 = {
    "REQ_CURR": ["EUR", "CAD", "AUD", "CHF", "JPY"],
    "SORT": "CURR",
    "NOW_CURR": "USD",
    "AMOUNT": 100.00
    }

# TEST CASE: "GARBAGE"
Case5 = {
    "REQ_CURR": ["EUsR", "CAD", "AUD", "CHF", "JPY"],
    "SORT": "CURR",
    "NOW_CURR": "USD",
    "AMOUNT": 100.00
    }


Tests= [Case1, Case2, Case3, Case4, Case5]


