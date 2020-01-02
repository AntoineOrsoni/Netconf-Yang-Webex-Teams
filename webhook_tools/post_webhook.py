# SOURCE : https://github.com/CiscoDevNet/spark-webhooks-sample/blob/master/postwebhook.py
# Post Webhooks for when my bot is mentioned, and when my bot is added to a new room.
# mentioned will be sent to {url}/newmessage
# mentioned will be sent to {url}/newroom

import requests
from datetime import date
from argparse import ArgumentParser


def webhook_new_message(webhook_url, token):
    # create request body
    payload_new_message = {
        "resource": "messages",
        "event": "created",
        "filter": "mentionedPeople=me",
        "targetUrl": "{url}/newmessage".format(url=webhook_url),
        "name": "Webhook NETCONF-Yang - New Message -- {0}".format(date.today())
    }

    # header
    header = {"Authorization": "Bearer {token}".format(token=token), "content-type": "application/json"}

    # send the POST request resource and do not verify SSL certificate for simplicity of this example
    api_response = requests.post("https://api.ciscospark.com/v1/webhooks", json=payload_new_message, headers=header,
                                 verify=False)

    # get the response status code
    response_status = api_response.status_code

    # print the status code
    print("/newmessage -- {response}".format(response=response_status))

    return "webhook new message sent"


def webhook_new_room(webhook_url, token):
    # create request body
    payload_new_message = {
        "resource": "memberships",
        "event": "created",
        "targetUrl": "{url}/newroom".format(url=webhook_url),
        "name": "Webhook NETCONF-Yang - New Room -- {0}".format(date.today())
    }

    # header
    header = {"Authorization": "Bearer {token}".format(token=token), "content-type": "application/json"}

    # send the POST request resource and do not verify SSL certificate for simplicity of this example
    api_response = requests.post("https://api.ciscospark.com/v1/webhooks", json=payload_new_message, headers=header,
                                 verify=False)

    # get the response status code
    response_status = api_response.status_code

    # print the status code
    print("/newmroom -- {response}".format(response=response_status))

    return "webhook new message sent"


if __name__ == "__main__":
    parser = ArgumentParser(description='Usage:')
    parser.add_argument('-t', '--token', type=str, required=True,
                        help="Token of the Webex Teams bot.")
    parser.add_argument('-u', '--url', type=str, required=True,
                        help="URL the Webhook.\n"
                             "/newmessage will be added for bot mentions,\n"
                             "/newroom will be added for room adding.")
    args = parser.parse_args()

    requests.packages.urllib3.disable_warnings()

    webhook_new_message(args.url, args.token)
    webhook_new_room(args.url, args.token)
