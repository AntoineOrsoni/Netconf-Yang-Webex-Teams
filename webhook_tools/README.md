# Webhooks tools

## Webex Teams webhooks

A webhook is an HTTP callback, or an HTTP POST, to a specified URL that notifies your app when a particular activity or “event” has occurred in one of your resources on the Webex Teams platform. The benefit of using webhooks is that they allow your application to receive real-time data from Webex Teams, so you can keep up with the state of your resources (i.e. rooms, messages, memberships, etc.).

[More information about Webex Teams wehbooks](https://developer.webex.com/docs/api/guides/webhooks)

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
