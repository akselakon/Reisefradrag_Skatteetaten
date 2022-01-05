import json
import requests

person1 = {
    "arbeidsreiser": [
        {"km": 91, "antall": 180},
        {"km": 378, "antall": 4}
    ],
    "besoeksreiser": [
        {"km": 580, "antall": 4}
    ],
    "utgifterBomFergeEtc": 4850
}

person2 = {
    "arbeidsreiser": [
        {"km": 600, "antall": 180},
        {"km": 378, "antall": 4}
    ],
    "besoeksreiser": [
        {"km": 0, "antall": 4}
    ],
    "utgifterBomFergeEtc": 1500
}

person3 = {
    "arbeidsreiser": [
        {"km": 50, "antall": 10},
        {"km": 378, "antall": 4}
    ],
    "besoeksreiser": [
        {"km": 200, "antall": 2},
        {"km": 200, "antall": 2}
    ],
    "utgifterBomFergeEtc": 0
}

person_list = [person1, person2, person3]

for person in person_list:
    print(1)
    r = requests.post("https://bjzvvrj95h.execute-api.us-east-1.amazonaws.com/reisefradrag", json=person)
    fasit = requests.post("https://9f22opit6e.execute-api.us-east-2.amazonaws.com/default/reisefradrag", json=person)
    assert json.loads(r.text)["reisefradrag"] == json.loads(fasit.text)["reisefradrag"] #sjekker om reisefradraget er likt mellom min API mot fasit API
