# Netconf-Yang-Webex-Teams
Getting operational data on a remote IOS XE device using NETCONF Yang, and posting the output in Webex Teams.

### Webex Teams webhooks

A webhook is an HTTP callback, or an HTTP POST, to a specified URL that notifies your app when a particular activity or “event” has occurred in one of your resources on the Webex Teams platform. The benefit of using webhooks is that they allow your application to receive real-time data from Webex Teams, so you can keep up with the state of your resources (i.e. rooms, messages, memberships, etc.).

[More information about Webex Teams wehbooks](https://developer.webex.com/docs/api/guides/webhooks)

## Getting started

### Creating a Virtual env and install the required packages.
Run the commands below to create a virtual environment and activate it. Commands might slightly differ depending of your OS. Commands below are for Unix kernerls.
```bash
python -m venv venv
source ./venv/bin/activate
```
Then, install the required packages
```bash
pip install -r requirements.txt
```

### ngrok
If you run the bot directly on your computer, you can use ngrok to make it publicly accessible via a public URL.

Sart ngrok on port 8080. 

```./ngrok http 8080```

### Launching the bot
Then, execute the `./core/main.py` file.

### Capabilities

Capabilities of the bot are listed in the `./core/bot_capabilities.py` file.

## Webhooks tools

### Webex Teams webhooks

A webhook is an HTTP callback, or an HTTP POST, to a specified URL that notifies your app when a particular activity or “event” has occurred in one of your resources on the Webex Teams platform. The benefit of using webhooks is that they allow your application to receive real-time data from Webex Teams, so you can keep up with the state of your resources (i.e. rooms, messages, memberships, etc.).

[More information about Webex Teams wehbooks](https://developer.webex.com/docs/api/guides/webhooks)

### post_webhooks.py
Post Webhooks for when my bot is mentioned, and when my bot is added to a new room.
* mentioned will be sent to `{URL}/newmessage`
* mentioned will be sent to `{URL}/newroom`

Usage: `python post_webhooks.py [-h] -t TOKEN -u URL`

To avoid errors, if the URL giving as a parameter ends with a "/", removes it.

### delete_webhooks.py
Deletes all active webhooks for a specific Webex Teams token.

Usage: `delete_webhooks.py [-h] -t TOKEN`

### function.py
Set of functions used by the files in this folder.

## Examples

### Interfaces configuration data

Listing the interfaces with their configuration data.

![Interfaces configuration data](https://i.imgur.com/b8w4tCSl.png)

### ARP data

Listing the ARP table of the device.

![ARP data](https://i.imgur.com/57RrMlxl.png)
