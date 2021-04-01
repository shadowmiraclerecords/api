import json
from googleapiclient import discovery
from google.oauth2 import service_account


# def lambda_handler(event, context):
def store():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = service_account.Credentials.from_service_account_file('client_secret.json')
    service = discovery.build('sheets', 'v4', credentials=creds)

    spreadsheet_id = '161e3gc2zXWdpbL6y3tOQ3Z7Fm6819jrfNeuTeHt45zg'
    range_ = 'Sheet1!A:A'
    value_input_option = 'RAW'
    major_dimension_option = "ROWS"
    insert_data_option = 'INSERT_ROWS'
    # Assume the body is present
    # loading = json.loads(event)

    # value = [event['email']]

    value = ['api@gmail.com']

    # value = [loading['email']]
    value_range_body = {
        "majorDimension": major_dimension_option,
        "values": [value]
    }
    

    request = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range_,
        valueInputOption=value_input_option,
        insertDataOption=insert_data_option,
        body=value_range_body
    )

    response = request.execute()
    # print(json.dumps(response))
    return {
        "statusCode": 200,
        "body": value,
        "headers": {
            "Content-Type": "application/json", 
            "Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods": "OPTIONS,POST",
            "Access-Control-Allow-Credentials": True,
            "Access-Control-Allow-Origin": "*",
            "X-Requested-With": "*"
        }
    }


# debug
# if __name__ == '__main__':
#     lambda_handler({"email": 'sweet'}, None)
