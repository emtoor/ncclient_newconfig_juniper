# Importing required libraries
import ncclient
from ncclient import manager
import xml.dom.minidom

# Connect to the Juniper device
conn = manager.connect(
    host="juniper_device_ip",
    port=22,
    username="juniper_username",
    password="juniper_password",
    hostkey_verify=False,
    device_params={'name': 'junos'},
    allow_agent=False,
    look_for_keys=False
)

# Define the configuration in XML format
config = '''
<configuration>
  <system>
    <host-name>new-host-name</host-name>
  </system>
</configuration>
'''

# Send the configuration to the device
result = conn.edit_config(target='running', config=config)

# Parse the XML response
xml_response = xml.dom.minidom.parseString(str(result))

# Print the response
print(xml_response.toprettyxml())

# Close the connection
conn.close_session()
