### Reisefradrag API

### Usage
Calculate your reisefradag using a POST request to the url: https://bjzvvrj95h.execute-api.us-east-1.amazonaws.com/reisefradrag

example body:
 
person = {
    "arbeidsreiser": [
        {"km": 91, "antall": 180},
        {"km": 378, "antall": 4}
    ],
    "besoeksreiser": [
        {"km": 580, "antall": 4}
    ],
    "utgifterBomFergeEtc": 4850
}

### Contains
- reisefradrag_lambda.py -> lambda function used at server side
- test_reisefradrag.py -> includes assert tests to verify that reisefradrag API correct output values. Compares the reisefradrag API to the solution API.


### dependencies
- pip install requests (required to run test_reisefradrag.py)