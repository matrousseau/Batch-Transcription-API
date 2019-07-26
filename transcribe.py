import requests, os

# This code checks for an environment variable with an S0 key.
# Make sure to adjust this with the name of your env variable.
# Feel free to save the key as a string.

subscription_key = 'c9******************b'
# Function to start Batch Transcription asynchronously.
def speech_to_text():
    base_url = 'https://westus.cris.ai/api/speechtotext/v2.0/'
    path = 'transcriptions'
    constructed_url = base_url + path

    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key
    }
    # The downside is that only Azure Blob is supported right now.
    body = {
  "description": "An optional description of the transcription.",
  "locale": "fr-FR",
  "models": [],
  "name": "Transcription using locale fr",
  "properties": {
    "ProfanityFilterMode": "Masked",
    "PunctuationMode": "DictatedAndAutomatic"
    },
  "recordingsUrl": "https://transcriptionblob.blob.core.windows.net/input/test_voix.wav"
}




    response = requests.post(constructed_url, headers=headers, json=body)
    # Print the response. Should just be status.
    # You'll need to use get_transcriptions.py to get the transcription result.
    print(response)

speech_to_text()
