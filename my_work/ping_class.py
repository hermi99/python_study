import pythonping


class Ping:
    def __init__(self, ip):
        self.ip = ip
        self.ping_result = ""

    def do_ping_test(self):
        print("ping : {} ...".format(self.ip))

        ping_res = pythonping.ping(self.ip, timeout=1)
        if ping_res.rtt_avg_ms >= 1000:
            ping_result = "fail"
        else:
            ping_result = "success"
        self.ping_result = ping_result


if __name__ == '__main__':
    ping = Ping("168.126.63.1")
    ping.do_ping_test()

    # ips = ["168.126.63.1", "8.8.8.8", "192.168.0.5", "223.1.1.1"]
    # ping_objects = []
    # for ip in ips:
    #     ping = Ping(ip)
    #     ping_objects.append(ping)

    ping_objects = [Ping("168.126.63.1"), Ping("168.126.63.1"),
                    Ping("168.126.63.1"),
                    Ping("168.126.63.1")]

    for ping in ping_objects:
        ping.do_ping_test()


    for ping in ping_objects:
        print("{} ping result : {}".format(ping.ip, ping.ping_result))

