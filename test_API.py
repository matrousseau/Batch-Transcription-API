# import requests
#
# transcriptions_api_url = 'https://francecentral.cris.ai/api/speechtotext/v2.0/transcriptions'
#
headers={'content-type' : 'application/json'}
    # 'Ocp-Apim-Subscription-Key  ':'3be8da2f97244571b75dc28b7f50a931',
    # 'Authorization' : '[Iwif9itooIx4f.sgx14@TbKNRTGkds_',
    # 'Content-Type': 'application/json'}

#
# file = open("test_voix.wav", "rb")
#
# response = requests.post(transcriptions_api_url, headers=headers, data=file)
# response.raise_for_status()

import requests

transcriptions_api_url = 'https://prod-110.westus.logic.azure.com:443/workflows/0cc468c026274e28ac2553150149cd0a/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=KtpLpxD91GDI21sxzxfesoLYKW4CwZfKP7_oHF4CLaQ'

body={"content-type" : "application/json",
    "text": "im so happy"}

response = requests.post(transcriptions_api_url,  data=body)
response.raise_for_status()
