from pythonping import ping

ip_list = ["127.0.0.1", "168.126.63.1", "193.168.0.1",
           "168.126.63.2", "193.123.0.1"]

ping_results = {}

def do_ping_test(ip):
    print("ping : {} ...".format(ip))

    ping_res = ping(ip, timeout=1)
    if ping_res.rtt_avg_ms >= 1000:
        ping_result = "fail"
    else:
        ping_result = "success"
    ping_results[ip] = ping_result


if __name__ == '__main__':
    for ip in ip_list:
        do_ping_test(ip)

    print(" ######## ping test 결과 : ###### ")
    for ip in ip_list:
        print("ip {} => {}".format(ip, ping_results[ip]))
