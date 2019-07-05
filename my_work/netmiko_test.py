import netmiko

device = {
    'device_type': 'cisco_ios_telnet',
    'ip': "192.168.0.100",
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}

# net_connect = netmiko.ConnectHandler(device_type="cisco_ios_telnet", ip="192.168.0.100",
#                                      username="cisco", password="cisco")

net_connect = netmiko.ConnectHandler(**device)

net_connect.enable()

result = net_connect.find_prompt() + "\n"
print(result)

# print(net_connect.send_command_expect("show ip int br"))
# print(net_connect.send_command_expect("show run"))


print(net_connect.send_command_expect("show ip int br"))

print(net_connect.find_prompt() + "\n")


print(net_connect.send_command_expect("show interfaces"))

print(net_connect.find_prompt() + "\n")