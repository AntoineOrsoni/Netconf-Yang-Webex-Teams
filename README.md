# Netconf-Yang-Webex-Teams
Getting operational data on a remote IOS XE device using NETCONF Yang, and posting the output in Webex Teams.

## Getting started
You now have to sart ngrok on port 8080. 

```./ngrok http 8080```

Then, use `./webhook_tools/post_webhook.py` to POST the two webhooks. You will need the ngrok URL to do so, and a Webex Teams token to do so.
* One for when the bot is mentioned,
* one for when the bot is added in a room.

Don't forget to edit the `./core/variables.py` file with your bot token.

Then, execute the `./core/main.py` file.

## Tools
In order to facilite the creation and deletion of webhooks, two scripts can be executed. Both files are in `./webhooks_tools/`.
* `post_webhooks` will post two webhooks. One for when the bot is mentioned, one for when the bot is added to a room.
    * mentioned will be sent to `{URL}/newmessage`
    * mentioned will be sent to `{URL}/newroom`
* `delete_webhooks` will delete all active wehbooks.

## Examples

### Interfaces configuration data

Listing the interfaces with their configuration data.

![Interfaces configuration data](https://i.imgur.com/b8w4tCSl.png)