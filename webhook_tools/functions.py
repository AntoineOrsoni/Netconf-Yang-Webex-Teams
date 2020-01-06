# Post Webhooks for when my bot is mentioned, and when my bot is added to a new room.
# mentioned will be sent to {url}/newmessage
# mentioned will be sent to {url}/newroom

import requests
import datetime
import json

# returns the person_id for a specific token. Used to filter the /newroom webhook to only the bot.
def get_person_id(token):
    headers = {'Authorization': 'Bearer ' + token,
               'Content-Type': 'application/json'}

    response = json.loads(requests.request("GET", "https://api.ciscospark.com/v1/people/me", headers=headers).text)

    return response["id"]


# create a webhook for the bot mentions
def create_webhook_new_message(webhook_url, token):
    # create request body
    payload_new_message = {
        "resource": "messages",
        "event": "created",
        "filter": "mentionedPeople=me",
        "targetUrl": "{url}/newmessage".format(url=webhook_url),
        "name": "Webhook NETCONF-Yang - New Message -- {0}".format(datetime.date.today())
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


# create a webhook when a bot is added to a room
def create_webhook_new_room(webhook_url, token):
    # create request body
    payload_new_message = {
        "resource": "memberships",
        "event": "created",
        "filter": "personId={bot_id}".format(bot_id=get_person_id(token)),
        "targetUrl": "{url}/newroom".format(url=webhook_url),
        "name": "Webhook NETCONF-Yang - New Room -- {0}".format(datetime.date.today())
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


# Returns a list with all the webhooks id
def list_webhook(token):
    list_webhook_id = []

    header = {"Authorization": "Bearer {token}".format(token=token)}
    response = requests.request("GET", "https://api.ciscospark.com/v1/webhooks", headers=header)
    data = json.loads(response.text)

    for item in range(len(data["items"])):
        list_webhook_id.append(data["items"][item]["id"])

    return list_webhook_id


# Deletes a specific webhook id
def delete_wehbook(list_webhook_id, token):
    header = {"Authorization": "Bearer {token}".format(token=token)}

    if len(list_webhook_id) == 0:
        print("No active webhooks.")
    else:
        for item in range(len(list_webhook_id)):
            requests.request("DELETE",
                             "https://api.ciscospark.com/v1/webhooks/{webhook_id}"
                             .format(webhook_id=list_webhook_id[item]), headers=header)
            print("Webhook [\"{webhook_id}\"] has been deleted !".format(webhook_id=list_webhook_id[item]))

        print("All webhooks have been deleted successfuly !")

    return True
