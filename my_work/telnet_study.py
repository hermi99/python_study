import csv

import pythonping

from my_work.analyzer import PortAnalyzer
from my_work.my_telnet import MyTelnet

if __name__ == '__main__':
    equip_ip = "192.168.0.100"
    telnet_id = "admin"
    telnet_pw = "admin"
    telnet_en_pw = "admin"

    # telnet = MyTelnet(equip_ip, telnet_id, telnet_pw, telnet_en_pw)
    # telnet.connect()
    # telnet.executes(["show ip int br", "show ip route", "show run"])
    # # telnet.executes(["show run"])
    # telnet.disconnect()
    # log = telnet.get_telnet_log()
    #
    # with open("..\\log\\telnet_log.txt", "w", newline='') as f:
    #     f.write(log)

    with open("..\\log\\telnet_log.txt", "r") as f:
        log = f.read()

    analyzer = PortAnalyzer(log)
    analyzer.do_analyze()

    for port in analyzer.ports:
        if port.ip_addr != "unassigned":
            print("ping check : {}".format(port.ip_addr))
            ping_result = pythonping.ping(port.ip_addr, timeout=1)
            if ping_result.rtt_avg_ms >= 1000:
                port.ping_result = "fail"
            else:
                port.ping_result = "success"

    with open("..\\file\\ports.txt", "w") as f:
        for port in analyzer.ports:
            line = "{}\t{}\t{}\t{}\t{}\n".format(port.port_name, port.ip_addr, port.link_status, port.ping_result, port.ethernet)
            f.write(line)

    with open('..\\file\\output.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["port명", "IP주소", "Link Status", "Ping Check", "ethernet"])
        for port in analyzer.ports:
            writer.writerow([port.port_name, port.ip_addr, port.link_status, port.ping_result, port.ethernet])

    print("done")









