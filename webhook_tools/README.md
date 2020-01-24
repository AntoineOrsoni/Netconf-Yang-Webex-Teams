# Webhooks tools

## post_webhooks.py
Post Webhooks for when my bot is mentioned, and when my bot is added to a new room.
* mentioned will be sent to `{URL}/newmessage`
* mentioned will be sent to `{URL}/newroom`

Usage: `python post_webhooks.py [-h] -t TOKEN -u URL`

To avoid errors, if the URL giving as a parameter ends with a "/", removes it.

## delete_webhooks.py
Deletes all active webhooks for a specific Webex Teams token.

Usage: `delete_webhooks.py [-h] -t TOKEN`

## function.py
Set of functions used by the files in this folder.
