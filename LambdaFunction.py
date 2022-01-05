import json

def lambda_handler(event, context):
    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']

    transactionResponse = {}
    transactionResponse['transactionId'] = transactionId
    transactionResponse['type'] = transactionType
    transactionResponse['amount'] = transactionAmount
    transactionResponse['message'] = "hellooo"

    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    return responseObject


    # # 1. Parse out query string params
    # arbeidsreiser = event['queryStringParameters']['arbeidsreiser']
    # besoeksreiser = event['queryStringParameters']['besoeksreiser']
    # utgifterBomFergeEtc = event['queryStringParameters']['utgifterBomFergeEtc']
    #
    # print('arbeidsreiser' + arbeidsreiser)
    # print('besoeksreiser' + besoeksreiser)
    # print('utgifterBomFergeEtc' + utgifterBomFergeEtc)
    #
    # # construct the body of the response object
    # reisefradragResponse = {}
    # reisefradragResponse['arbeidsreiser'] = arbeidsreiser
    # reisefradragResponse['besoeksreiser'] = besoeksreiser
    # reisefradragResponse['utgifterBomFergeEtc'] = utgifterBomFergeEtc
    #
    # # construct a http response object
    # responseObject = {}
    # responseObject['statusCode'] = 200
    # responseObject['headers'] = {}
    # responseObject['headers']['Content-type'] = 'application/json'
    # responseObject['body'] = json.dumps(reisefradragResponse)
    #
    # #return the response object
    # return responseObject

    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }


    # ?transactionId=5&type=PURCHASE&amount=500