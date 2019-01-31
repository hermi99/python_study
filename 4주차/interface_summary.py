import re

content = """
interface vlan11
 description ##ts(117-2585)## 
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 ip address 121.170.126.9/30
 service-policy rate_50M
!
interface vlan12
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
!
interface vlan13
 description korail-university(117-0420) 
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 service-policy rate_20M
!
interface vlan14
 description sicc(117-0055) 
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 ip address 112.170.144.85/30
 service-policy rate_10M
!
interface vlan21
 description korail-university(117-2585) 
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 service-policy rate_100M
!
interface vlan22
 description bugok(117-2427) 
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 service-policy rate_10M
!
interface vlan23
 description trueinfo(117-2261) 
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 service-policy rate_100M
!
interface vlan24
 description uuc(117-2472) 
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 ip address 221.163.99.37/30
 service-policy rate_50M
!
interface vlan31
 description ##Korail_Uni(117-0420)## 
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 ip address 221.163.99.205/30
 service-policy rate_50M
!
interface vlan32
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 service-policy rate_30M
!
interface vlan33
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
!
interface vlan34
 description ##MOBIS(117-2580)## 
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 ip address 121.170.126.105/30
 service-policy rate_50M
!
interface vlan41
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
!
interface vlan42
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
!
interface vlan43
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 service-policy rate_100M
!
interface vlan44
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 service-policy rate_100M
!
interface vlan51
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 service-policy rate_100M
!
interface vlan52
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 service-policy rate_100M
!
interface vlan53
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 service-policy rate_100M
!
interface vlan54
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 service-policy rate_100M
!
interface vlan61
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 service-policy rate_100M
!
interface vlan62
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 service-policy rate_100M
!
interface vlan63
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
 service-policy rate_100M
!
interface vlan64
 cpu-mac-filter multicast
 cpu-mac-filter broadcast
!
"""

p = re.compile(r"interface\s+[\w]+(?:\n.+)*?\n!")
interface_configs = p.findall(content)

print(interface_configs[0])

for config in interface_configs:
    pattern = r"""
        interface\s+([\w]+)    # interface vlan63
        (?:\n.+)*?           # 모든 라인
        \n\s+(?:description\s+(.*)\s*)* # description bugok(117-2427)
        (?:\n.+)*?           # 모든 라인
        \n!                  # !(종료)
        """
    p = re.compile(pattern, re.VERBOSE)
    m = p.search(config)
    if m:
        print(m.group(1))
        print(m.group(2))