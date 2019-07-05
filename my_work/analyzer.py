import ipaddress
import re

from my_work.ipaddr_util import IPUtil


class PortAnalyzer:
    def __init__(self, log):
        self.log = log
        self.ports = []

    def do_analyze(self):
        pattern = r"""
            \n([\w\/]+)\s+
            ((?:(?:\d{1,3}\.){3}\d{1,3})|unassigned)\s+
            (?:YES|NO)\s+
            (?:manual|NVRAM|unset)\s+
            (?:up|administratively down)\s+
            (up|down)
        """
        p = re.compile(pattern, re.VERBOSE)
        results = p.findall(self.log)
        for result in results:
            port_name, ip_addr, link_status = result
            port = Port(port_name, ip_addr, link_status)
            self.ports.append(port)

        pattern = r"""
            ip\s+route\s+
            ((?:\d{1,3}\.){3}\d{1,3})\s+
            ((?:\d{1,3}\.){3}\d{1,3})\s+
            ((?:\d{1,3}\.){3}\d{1,3})
        """
        p = re.compile(pattern, re.VERBOSE)
        results = p.findall(self.log)
        for result in results:
            ipaddr, prefixmask, nexthop = result
            network = IPUtil.prefixmask_to_netmask(ipaddr, prefixmask)
            for port in self.ports:
                serial_net = ipaddress.ip_network("{}/30".format(port.ip_addr), strict=False)
                nexthop_addr = ipaddress.ip_address(nexthop)
                if nexthop_addr in serial_net:
                    port.ethernet = str(network)
                    break




class Port:
    def __init__(self, port_name, ip_addr, link_status):
        self.port_name = port_name
        self.ip_addr = ip_addr
        self.link_status = link_status
        self.ping_result = ""
        self.ethernet = ""

