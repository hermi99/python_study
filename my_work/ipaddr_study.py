import ipaddress
import netaddr

from my_work.ipaddr_util import IPUtil

if __name__ == '__main__':
    # addr = ipaddress.ip_address("192.168.1.0 255.255.255.0")
    # print(addr)
    ipaddr = "192.168.1.0"
    subnet_mask = "255.255.255.0"
    # bitmask = netaddr.IPAddress(subnet_mask).netmask_bits()
    #
    #
    # addr = ipaddress.ip_network("{}/{}".format(ipaddr, bitmask))
    # print(addr)

    # network = IPUtil.prefixmask_to_netmask(ipaddr, subnet_mask)
    # print(network)

    ipaddr = ipaddress.ip_address("192.168.1.0")
    print(ipaddr)
    print(ipaddr.is_private)

    network1 = ipaddress.ip_network("192.168.0.0/24")
    network2 = ipaddress.ip_network("192.168.1.1/24", strict=False)
    print(network1)
    print(network2)

    addr1 = ipaddress.ip_address("192.168.1.1")
    addr2 = ipaddress.ip_address("192.168.1.2")
    if addr1 < addr2:
        print("{} is less than {}".format(str(addr1), str(addr2)))

    print(addr1 + 3)
    print(addr1 - 3)

    print("==========network=============")

    network3 = ipaddress.ip_network("192.168.1.0/255.255.255.0")
    print(network3)
    network4 = ipaddress.ip_network("192.168.1.0/0.0.0.255")
    print(network4)


    for host in network1.hosts():
        print(host)

    print(network1.network_address)
    print(network1.broadcast_address)

    print(list(network1.subnets()))
    print(list(network1.subnets(new_prefix=27)))


    network1 = ipaddress.ip_network("192.168.0.0/24")
    network2 = ipaddress.ip_network("192.168.0.0/24")

    print(network2.overlaps(network1))
    print(network1.overlaps(network2))

    if network1.compare_networks(network2) == 1:
        print("networ1가 network2에 속한다")
    elif network1.compare_networks(network2) == -1:
        print("networ2가 network1에 속한다")
    else:
        print("networ1 = network2")





    net1 = "192.168.1.0/25"
    net2 = "192.168.1.128/25"
    list_net = [net1, net2]

    print(netaddr.cidr_merge(list_net))









