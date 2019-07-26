import requests, json, os

# This code checks for an environment variable with an S0 key.
# Make sure to adjust this with the name of your env variable.
# Feel free to save the key as a string.
if 'SPEECH_S0_KEY' in os.environ:
    subscription_key = os.environ['SPEECH_S0_KEY']
else:
    print('Environment variable for your subscription key is not set.')
    exit()

# List of transcription ids that will be deleted.
list_of_ids = []

def delete_transcriptions(id):
    base_url = 'https://westus.cris.ai/api/speechtotext/v2.0/'
    path = 'transcriptions/' + id
    constructed_url = base_url + path

    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key
    }

    request = requests.delete(constructed_url, headers=headers)
    print(request)

# Iterate over the list of transcriptions created by get_transcriptions.py
# Append each id in the file to list_of_ids
# Then delete the transcription for each id
with open('response.json') as batch_transcription_results:
    data = json.load(batch_transcription_results)
    for transcription in data:
        if transcription['id']:
            id = transcription['id']
            list_of_ids.append(id)
            delete_transcriptions(id)
            print(str(id) + " has been deleted.")
