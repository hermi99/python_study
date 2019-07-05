import re

content = """
router static
 address-family ipv4 unicast
  0.0.0.0/0 61.78.49.241
  14.34.64.0/18 Null0 tag 9260
  14.35.0.0/19 Null0 tag 9260
  14.35.192.0/20 Null0 tag 9260
  14.36.216.0/21 Null0 tag 9260
  14.36.224.0/20 Null0 tag 9260
  14.36.240.0/21 Null0 tag 9260
  14.38.192.0/18 Null0 tag 9260
  14.51.64.0/18 Null0 tag 9260
  14.51.224.0/19 Null0 tag 9260
  59.14.0.0/16 Null0 tag 9260
"""

p = re.compile(r"(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\/(\d{1,3})\s+Null0\s+tag\s+(\d+)")
# m = p.search(content)
# if m:
#     ip_addr = m.group(1)
#     tag = m.group(2)
#     print(ip_addr, tag)

results = p.findall(content)
for result in results:
    ipaddr, bit, tag = result
    print(ipaddr, bit, tag)

    
