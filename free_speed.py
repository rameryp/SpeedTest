'''
This example can be run safely as it won't change anything in your box configuration
'''
from freepybox import Freepybox
from pprint import pprint

# Instantiate Freepybox class using default application descriptor 
# and default token_file location
fbx = Freepybox()

# Connect to the freebox with default http protocol
# and default port 80
# Be ready to authorize the application on the Freebox if you use this
# example for the first time
fbx.open('192.168.0.254',80)

# Extract WAN interface status (GET /api/v6/connection/full) using connection API
pprint(dir(fbx.lan))


# Close the freebox session
fbx.close()