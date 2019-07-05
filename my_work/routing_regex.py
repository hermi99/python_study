import re

config = """
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

p = re.compile(r"\s+(\d+.\d+.\d+.\d+\/\d+)\s+Null0\s+tag\s+(\d+)")

# 1. search : 첫번째 나오는것만 리턴
# m = p.search(config)
# if m:
#     print(m.group()) # => 전체 문자열
#     print(m.group(0)) # => 전체 문자열
#     print(m.group(1)) # => 1번째 그룹
#     ipaddr = m.group(1)

# 2. findall : 전체 리턴
results = p.findall(config)
print(results)

for result in results:
    ipaddr, tag = result
    print("ipaddr={}, tag={}".format(ipaddr, tag))





