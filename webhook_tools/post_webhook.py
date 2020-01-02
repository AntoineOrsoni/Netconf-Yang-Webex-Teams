# SOURCE : https://github.com/CiscoDevNet/spark-webhooks-sample/blob/master/postwebhook.py
# Post Webhooks for when my bot is mentioned, and when my bot is added to a new room.
# mentioned will be sent to {url}/newmessage
# mentioned will be sent to {url}/newroom

import requests
from datetime import date
from argparse import ArgumentParser
from functions import *


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
