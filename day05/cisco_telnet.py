import re
import telnetlib


class CiscoTelnet:

    def __init__(self, equip_ip, telnet_id, telnet_pw, telnet_enpw):
        self.equip_ip = equip_ip
        self.telnet_id = telnet_id
        self.telnet_pw = telnet_pw
        self.telnet_enpw = telnet_enpw

        self.tn = None
        self.hostname = ""
        self.wait_str = ""
        self.logs = []

    def connect(self):
        self.tn = telnetlib.Telnet(self.equip_ip)

        #username 대기
        self.tn.read_until(b"sername:")

        # username 입력
        self.tn.write("{}\n".format(self.telnet_id).encode("ascii"))
        self.tn.read_until(b"assword:")

        # password 입력
        self.tn.write("{}\n".format(self.telnet_pw).encode("ascii"))
        log = self.tn.read_until(b">").decode("ascii")
        p = re.compile("(.+)>")
        m = p.search(log)
        if m:
            self.hostname = m.group(1)
            self.wait_str = "{}#".format(self.hostname).encode("ascii")

        # enable 입력
        self.tn.write(b"enable\n")
        self.tn.read_until(b"assword:")

        # enable password 입력
        self.tn.write("{}\n".format(self.telnet_enpw).encode("ascii"))
        self.tn.read_until(self.wait_str)

        # terminal length 0
        self.tn.write(b"terminal length 0\n")
        self.tn.read_until(self.wait_str)

    def disconnect(self):
        self.tn.close()

    def execute(self, cmds):
        for cmd in cmds:
            self.tn.write("{}\n".format(cmd).encode("ascii"))
            log = self.tn.read_until(self.wait_str).decode("ascii")
            self.logs.append(log)

    def get_log(self):
        return "\n".join(self.logs)


