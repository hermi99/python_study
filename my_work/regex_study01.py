import re

content = """
    xxx 192.168.0.1 xxx 
"""

p = re.compile("\d{1,3}.\d{1,3}.\d{1,3}.(\d{1,3})")
m = p.search(content)
if m:
    ip_addr = m.group(0)
    last_num = m.group(1)
