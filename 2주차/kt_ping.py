from pythonping import ping


def ping_test(ip):
    print("Ping {} \t시도중 ...".format(ip))
    ping_res = ping(ip, timeout=1)
    if ping_res.rtt_avg_ms >= 1000:
        ping_result = "fail"
    else:
        ping_result = "success"

    return ping_result

