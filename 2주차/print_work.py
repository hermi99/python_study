
def print_script(vprn, desc, rd, vlan, address):
    print("/configure service vprn {} customer 1 create".format(vprn))
    print("/configure service vprn {} customer 1 description \"{}\"".format(vprn, desc))
    print("/configure service vprn {} customer 1 route-distinguisher {}".format(vprn, rd))
    print("/configure service vprn {} customer 1 interface \"{}\" create".format(vprn, vlan))
    print("/configure service vprn {} customer 1 interface \"{}\" enable-ingress-stats"
          .format(vprn, vlan))
    print("/configure service vprn {} customer 1 interface \"{}\" address {}"
          .format(vprn, vlan, address))

    """
    => 결과물은 아래와 같아야 합니다
    /configure service vprn 1201 customer 1 create
/configure service vprn 1201 customer 1 description "##02191111-1111, kt##"
/configure service vprn 1201 customer 1 route-distinguisher 125.141.249.195:1201
/configure service vprn 1201 customer 1 interface "vlan-1201" create
/configure service vprn 1201 customer 1 interface "vlan-1201" enable-ingress-stats
/configure service vprn 1201 customer 1 interface "vlan-1201" address 192.168.1.254
    :return:
    """

vprn = "1201"

print_script(vprn, "##02191111-1111, kt##", "125.141.249.195:1201", "vlan-1201", "192.168.1.254")

