from pythonping import ping

ping_response = ping("127.0.0.1", timeout=1)


print(ping_response.rtt_avg_ms)
