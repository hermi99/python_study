import re

# content = "my phone is 010-9650-0502 !!!"
#
# p = re.compile(".+[ ](\d{3}-\d{4}-\d{4})[ ][!]{3}")
# m = p.search(content)
# if m:
#     print(m.group(0))
#     phone_number = m.group(1)
#     print(phone_number)

content = "my phone is 010-9650-0502 !!! 010-9650-0503"
p = re.compile("(\d{3}-\d{4}-\d{4})")
phone_numers = p.findall(content)
for phone in phone_numers:
    print(phone)






