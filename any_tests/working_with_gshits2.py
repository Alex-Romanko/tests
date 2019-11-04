from pprint import pprint
import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


# here is a start point to working with google sheets

# autorization
CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = '16Ox7jX0ljQ5r6Zc7492uaW583-3wDS9HlREXVRNCY9Q'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)

# Пример чтения файла
values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='sheet2',
    majorDimension='COLUMNS'
).execute()
pprint(values)

# Пример записи в файл
values1 = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "sheet1", "majorDimension": "ROWS", "values": [["This is B3", "This is C3"], ["This is B4", "This is C4"], ["This is dvdcscsdv", "This is 12345464"], ["This is 23rrdf", "This is dfv324"]]},
            {"range": "sheet1", "majorDimension": "COLUMNS", "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
                ]
        }
).execute()


# here is how to insert data to the particular line
# now data must be in format of a como separated string
insert_data = "a777, na, 32, na, na, 33, 32, 32, 34, 22, 23"  # the data

# forming http request
batch_update_spreadsheet_request_body = {
    "requests": [
        {
            "insertRange": {
                "range": {
                    "sheetId": 1288123411,
                    "startRowIndex": 1,
                    "endRowIndex": 2
                },
                "shiftDimension": "ROWS"
            }
        },
        {
            "pasteData": {
                "data": f'{insert_data}',  # inserting data in request
                "type": "PASTE_NORMAL",
                "delimiter": ",",
                "coordinate": {
                    "sheetId": 1288123411,
                    "rowIndex": 1  # the nomber of row to insert data
                }
            }
        }
    ]
}

# making a request
request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=batch_update_spreadsheet_request_body)
response = request.execute()
print(response)  # its work

# other afforts
'''
sheet = service.spreadsheets()
result = sheet.values().batchUpdate(
                            spreadsheetId=spreadsheet_id,
                            # range='sheet2',
                            body={
                                "valueInputOption": "RAW",
                                "data": [
                                    {"range": "sheet2",
                                    "majorDimension": "COLUMNS",
                                    'values': [['dfw', 'dwfwd', 'wdwfws'], ['qwerwf', 'wwfdscds'], [234342, 654432], ['wer'], ['qwerwf'], [234342]]
                                    }
                                    ]
                                }
                            ).execute()

[['dfw', 'dwfwd', 'wdwfws'], ['qwerwf', 'wwfdscds'], [234342, 654432], ['wer'], ['qwerwf'], [234342]]

"'dfw', 'dwfwd', 'wdwfws', 'qwerwf', 'wwfdscds', 234342, 654432, 'wer', 'qwerwf', 234342"



values = result.get('values', [])

if not values:
    print('No data found.')
else:
    print('Name, Major:')
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s' % (row[0], row[4]))
'''