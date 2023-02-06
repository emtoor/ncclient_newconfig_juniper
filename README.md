# ncclient_newconfig_juniper

This script is an example of automating the configuration of a Juniper network device using the ncclient library in Python. The script does the following:

Imports the required libraries ncclient and xml.dom.minidom
Connects to a Juniper device using the manager.connect method and the provided device parameters.
Defines the desired configuration in XML format
Sends the configuration to the device using the edit_config method of the ncclient connection.
Parses the XML response from the device.
Prints the parsed response.
Closes the connection to the device using conn.close_session().
This script demonstrates the basic steps to automate the configuration of a Juniper device using Python and the ncclient library.
