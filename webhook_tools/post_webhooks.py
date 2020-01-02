# Post Webhooks for when my bot is mentioned, and when my bot is added to a new room.
# mentioned will be sent to {url}/newmessage
# mentioned will be sent to {url}/newroom

import requests
import argparse
import functions


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Usage:')
    parser.add_argument('-t', '--token', type=str, required=True,
                        help="Token of the Webex Teams bot.")
    parser.add_argument('-u', '--url', type=str, required=True,
                        help="URL the Webhook.\n"
                             "/newmessage will be added for bot mentions,\n"
                             "/newroom will be added for room adding.")
    args = parser.parse_args()

    requests.packages.urllib3.disable_warnings()

    functions.create_webhook_new_message(args.url, args.token)
    functions.create_webhook_new_room(args.url, args.token)
