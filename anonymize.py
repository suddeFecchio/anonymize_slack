import requests
import subprocess
import json
import urllib.parse


def main(params):
    # # Get the content of the POST request
    # payload = args.get('payload')
    #
    # # Get the text message from the payload
    # message = payload.get('text')

    # Get the payload from the POST request
    payload_str = params.get('text')
    if payload_str is None:
        return {"body": "Payload not found", "statusCode": 400}

    # Construct the curl command with the message as an argument
    curl_command = f'curl -X POST -H "Content-type: application/json" -d \'{{"text":"{payload_str}"}}\' {"https://hooks.slack.com/services/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"}'

    # Execute the curl command
    subprocess.run(curl_command, shell=True, check=True)

    return {'message': 'Curl command executed successfully'}
