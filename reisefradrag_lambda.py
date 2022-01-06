import json

# øker tot_km for hver reise som er utført
def add_km(tot_km, reiser):
    for reise in reiser:
        km = reise["km"]
        ant = reise["antall"]
        tot_km = tot_km + km * ant
    return tot_km



def lambda_handler(event, context):
    # henter ut body
    try:
        y = json.loads(event['body'])
    except json.JSONDecodeError:
        return {"400": "Bad Request error"}

    # initierer variabler
    ovregrense = 75000
    mellomgrense = 50000
    utgiftgrense = 3400
    egenandel = 22000
    tot_utlegg = 0
    tot_km = 0

    # Sjekker om det gjort reiser og legger til i tot_km
    if 'arbeidsreiser' in y:
        arbeidsreiser = y['arbeidsreiser']
        tot_km = add_km(tot_km, arbeidsreiser)

    if 'besoeksreiser' in y:
        besoeksreiser = y['besoeksreiser']
        tot_km = add_km(tot_km, besoeksreiser)

    # sjekker om det finnes utgifterBomFergeEtc og om utgiftene er større enn utgiftgrensa
    if 'utgifterBomFergeEtc' in y:
        utgifterBomFergeEtc = y['utgifterBomFergeEtc']
        if utgifterBomFergeEtc > utgiftgrense:
            tot_utlegg = tot_utlegg + utgifterBomFergeEtc

    # sjekker om tot_km er større enn ovregrense
    if tot_km - ovregrense >= 0:
        tot_utlegg = tot_utlegg + mellomgrense * 1.5 + (ovregrense - mellomgrense) * 0.7

    # sjekker om tot_km er mellom ovre og midtregrense
    elif tot_km - mellomgrense >= 0:  # tot_km - 50000 >= 0
        tot_utlegg = tot_utlegg + mellomgrense * 1.5 + (tot_km - mellomgrense) * 0.7

    # else tot_km er mindre enn midtregrense
    else:
        tot_utlegg = tot_utlegg + tot_km * 1.5

    # sjekker om det totale utlegget er større enn egenandelen
    if tot_utlegg > egenandel:
        reisefradrag = tot_utlegg - egenandel
    else:
        reisefradrag = 0

    json_reisefradrag = json.dumps({"reisefradrag": int(reisefradrag)})

    return json_reisefradrag