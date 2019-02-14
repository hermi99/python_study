import telnetlib

from day05.cisco_telnet import CiscoTelnet

equip_ip = "192.168.0.100"
telnet_id = "admin"
telnet_pw = "admin"
telnet_enpw = "admin"

telnet = CiscoTelnet(equip_ip, telnet_id, telnet_pw, telnet_enpw)
telnet.connect()
telnet.execute(['show ip int br', 'show ip route', 'show run'])
telnet.disconnect()

log = telnet.get_log()
print(log)




