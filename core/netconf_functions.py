from ncclient import manager
import xmltodict

def get_interfaces(device):

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

# def message_get_interface(...)