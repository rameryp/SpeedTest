
  
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This example can be run safely as it won't change anything in your box configuration
'''

from freepybox import Freepybox


# Instantiate Freepybox class using default application descriptor 
# and default token_file location
fbx = Freepybox()

# Connect to the freebox with default http protocol
# and default port 80
# Be ready to authorize the application on the Freebox if you use this
# example for the first time
fbx.open('192.168.0.254')


fbx_connection_status_details = fbx.connection.get_status_details()
fbx_dyn_dhcp = fbx.dhcp.get_dynamic_dhcp_lease();

index = 0
while index < len(fbx_dyn_dhcp):
    if fbx_dyn_dhcp[index]['is_static'] == False :
        if index == 0 :
            print('');
            print(' Attributions dhcp dynamiques :');
            print(' ----------------------------');
            
            print(''); 
            print('  Hostname               Adresse MAC            Adresse IP');
            print('  --                     --                     --');
        mac = fbx_dyn_dhcp[index]['mac'];
        hostname = fbx_dyn_dhcp[index]['hostname'];
        ip = fbx_dyn_dhcp[index]['ip'];
        print('  {0:21.21s}  {1:21.21s}  {2:21.21s}'.format(hostname,mac,ip));
    index += 1;


rx = fbx_connection_status_details['rate_down']/1024
rxb = rx*8/1024
tx = fbx_connection_status_details['rate_up']/1024
txb = tx*8/1024
rx_str = '{0:.0f} ko/s ({1:.1f} Mb/s)'.format(rx, rxb)
tx_str = '{0:.0f} ko/s ({1:.1f} Mb/s)'.format(tx, txb)
print('  {0:21.21s}  {1:13.13s}  {2}  {3}'.format('WAN', '', rx_str.ljust(23," "), tx_str.ljust(23," ")));


# Close the freebox session
fbx.close()
