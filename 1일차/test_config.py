
# 기가오피스 컨피그를 만드는 function #
def make_script(vprn, desc, gw_ip, qos, filter):
    vprn_prefix = "/configure service vprn {}".format(vprn)
    print("{} customer 1 create".format(vprn_prefix))
    print("{} customer 1 description \"{}\"".format(vprn_prefix, desc))

    interface_prefix = "{} customer 1 interface \"vlan-{}\"".format(vprn_prefix, vprn)
    print("{} create".format(interface_prefix))
    print("{} enable-ingress-stats".format(interface_prefix))
    print("{} address {}".format(interface_prefix, gw_ip))
    print("{} icmp no mask-reply".format(interface_prefix))
    print("{} icmp no redirects".format(interface_prefix))
    print("{} icmp no unreachables".format(interface_prefix))
    print("{} icmp no ttl-expired".format(interface_prefix))
    print("{} sap lag-:{} create".format(interface_prefix, vprn))
    print("{} sap lag-:{} ingress qos {}".format(interface_prefix, vprn, qos))
    print("{} sap lag-:{} ingress filter ip {}".format(interface_prefix, vprn, filter))
    print("{} sap lag-:{} egress qos {}".format(interface_prefix, vprn, qos))

    #/configure service vprn 1201 customer 1 grt-lookup enable-grt
    print("{} customer 1 grt-lookup enable-grt".format(vprn_prefix))
    print("{} customer 1 grt-lookup static-route 0.0.0.0/0 grt".format(vprn_prefix))
    print("{} customer 1 grt-lookup enable-grt \"VPRN_to_Global\"".format(vprn_prefix))
    print("{} customer 1 grt-lookup export-limit 20".format(vprn_prefix))
    print("{} customer 1 no shutdown".format(vprn_prefix))



vprn = "1101"
desc = "##02191111-1111, kt##"
gw_ip = "192.168.1.254"
qos = 500
filter = 101
make_script(vprn, desc, gw_ip, qos, filter)

