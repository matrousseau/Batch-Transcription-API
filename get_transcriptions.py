import requests, json, os

# This code checks for an environment variable with an S0 key.
# Make sure to adjust this with the name of your env variable.
# Feel free to save the key as a string.
if 'SPEECH_S0_KEY' in os.environ:
    subscription_key = os.environ['SPEECH_S0_KEY']
else:
    print('Environment variable for your subscription key is not set.')
    exit()

subscription_key = 'c93cbfbf3b1f4ccdaa1e9e627e34ac6b'

def get_transcriptions():
    base_url = 'https://westus.cris.ai/api/speechtotext/v2.0/'
    path = 'transcriptions'
    constructed_url = base_url + path

    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key
    }

    request = requests.get(constructed_url, headers=headers)
    response = request.json()
    # Write the response to file.
    with open('response.json', 'w') as outfile:
        json.dump(response, outfile, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))

    print("See response.json for results.")

get_transcriptions()
