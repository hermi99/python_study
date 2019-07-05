import ipaddress

import netaddr


class IPUtil:
    def __init__(self):
        pass

    @classmethod
    def prefixmask_to_netmask(self, ipaddr, prefixmask):
        bitmask = netaddr.IPAddress(prefixmask).netmask_bits()
        network = ipaddress.ip_network("{}/{}".format(ipaddr, bitmask))
        return str(network)
