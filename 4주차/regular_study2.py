import re

content = """
Uiwang-EXP038# show ip int br
 IFNAME   LPROTO IP-ADDRESS         SIP POLICY-NAME
------------------------------------------------------------
 vlan11   up     121.170.126.9/30       rate_50M
 vlan14   up     112.170.144.85/30      rate_10M
 vlan24   up     221.163.99.37/30       rate_50M
 vlan31   up     221.163.99.205/30      rate_50M
 vlan34   up     121.170.126.105/30     rate_50M
 vlan71   up     112.189.154.38/30      security_filter
 vlan72   up     112.189.154.90/30      security_filter
 eth0     up     192.168.0.1/24  
"""

p = re.compile("""
    ([\w\-\_]+)\s+       #vlan72
    (up|down)\s+       #up
    ((?:\d{1,3}.){3}\d{1,3}\/\d{1,2})\s+ #192.168.0.1/24
    ([\w\-\_]*)
""", re.VERBOSE)
results = p.findall(content)

for result in results:
    (interface, status, ipaddr, policy) = result
    print("interface={}, status={}, ipaddr={}, policy={}"
          .format(interface, status, ipaddr, policy))