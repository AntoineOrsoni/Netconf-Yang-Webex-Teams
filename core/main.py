from core.variables import DevNet_XE_sandbox as xe
from core.variables import better_than_kitty as bot
from core.netconf_functions import *
from core.teams_functions import *
from flask import Flask, request

app = Flask(__name__)

@app.route('/newmessage', methods=['POST'])
def newmessage():

    json_data = request.json

    message_id = json_data["data"]["id"]
    person_id = json_data["data"]["personId"]
    person_email = json_data["data"]["personEmail"]
    room_id = json_data["data"]["roomId"]

    message = get_message(message_id, bot.token)

    # removing the bot name from the message and the space after the bot name
    message_received = message[len(bot.botname_kitty) + 1:]

    # ---
    # I would like to show the operational data of my interfaces
    # ---
    if message_received.lower() == "interface":
        intf_details = get_interfaces(xe)
        message = ""

        for i in range(len(intf_details["interfaces"]["interface"])):
            current_int = intf_details["interfaces"]["interface"][i]

            if i != 0:
                message += "\n\n"

            for key, value in current_int.items():
                if key == "name":
                    message += "### 🖲 {0} 🖲\n".format(value)
                else:
                    if value == "if-state-up":
                        message += "* {0} : `{1}` ✅\n".format(key, value)
                    elif value == "if-state-down":
                        message += "* {0} : `{1}` 🚨\n".format(key, value)
                    else:
                        message += "* {0} : `{1}`\n".format(key, value)


        print(message)
        post_message_markdown(message, room_id, bot.token)

    elif message_received.lower() == "help":
        post_help_bot(room_id, bot.token)

    return("200")

@app.route('/newroom', methods=['POST'])
def newRoom():

    json_data = request.json

    message_id = json_data["data"]["id"]
    person_id = json_data["data"]["personId"]
    person_email = json_data["data"]["personEmail"]
    room_id = json_data["data"]["roomId"]

    post_message_markdown("Hey, I have been added to a new room !", room_id, bot.token)
    post_help_bot(room_id, bot.token)

    return ("message sent")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)