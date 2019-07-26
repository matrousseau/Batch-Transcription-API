import requests, os

# This code checks for an environment variable with an S0 key.
# Make sure to adjust this with the name of your env variable.
# Feel free to save the key as a string.
if 'SPEECH_S0_KEY' in os.environ:
    subscription_key = os.environ['SPEECH_S0_KEY']
else:
    print('Environment variable for your subscription key is not set.')
    exit()


# Replace with the ID for the transcription you'd like to delete.
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


delete_transcriptions()
