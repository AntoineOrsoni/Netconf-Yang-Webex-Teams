# Netconf-Yang-Webex-Teams
Getting operational data on a remote IOS XE device using NETCONF Yang, and posting the output in Webex Teams.

## Tools
In order to facilite the creation and deletion of webhooks, two scripts can be executed. Both files are in `./webhooks_tools/`.
* `post_webhooks` will post two webhooks. One for when the bot is mentioned, one for when the bot is added to a room.
    * mentioned will be sent to `{url}/newmessage`
    * mentioned will be sent to `{url}/newroom`
* `delete_webhooks` will delete all active wehbooks.