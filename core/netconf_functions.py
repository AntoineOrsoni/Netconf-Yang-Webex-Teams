from ncclient import manager
import xmltodict


def get_interfaces_conf(device):
    # NETCONF filter to use
    netconf_filter = open("interface.xml").read()

    with manager.connect(host=device.hostname,
                         port=device.netconf_port,
                         username=device.username,
                         password=device.password,
                         hostkey_verify=False) as m:
        # Get Configuration and State Info for Interface
        netconf_reply = m.get(netconf_filter)

        # Process the XML and store in useful dictionaries
        # Converting XML into dictionnaries, and access the node ["rpc-reply"]["data"]
        intf_details = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]

        return intf_details


def message_get_interface(interfaces):
    message = ""

    for i in range(len(interfaces["interfaces"]["interface"])):
        current_int = interfaces["interfaces"]["interface"][i]

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

    return message
