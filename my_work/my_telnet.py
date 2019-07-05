import re
import telnetlib


class MyTelnet:
    def __init__(self, equip_ip, telnet_id, telnet_pw, telnet_en_pw):
        self.equip_ip = equip_ip
        self.telnet_id = telnet_id
        self.telnet_pw = telnet_pw
        self.telnet_en_pw = telnet_en_pw

        self.telnet_logs = []
        self.tn = None
        self.hostname = ""

    def connect(self):
        self.tn = telnetlib.Telnet(self.equip_ip)
        self.tn.read_until(b"sername:")

        self.tn.write(self.encode(self.telnet_id + "\n"))
        self.tn.read_until(b"assword:")

        self.tn.write(self.encode(self.telnet_pw + "\n"))
        log = self.decode(self.tn.read_until(b">"))
        p = re.compile("\n(.*)>")
        m = p.search(log)
        if m:
            self.hostname = m.group(1)

        self.tn.write(self.encode("en" + "\n"))
        self.tn.read_until(b"assword:")

        self.tn.write(self.encode(self.telnet_en_pw + "\n"))
        self.tn.read_until(self.encode(self.hostname + "#"))

        self.tn.write(self.encode("terminal length 0" + "\n"))
        self.tn.read_until(self.encode(self.hostname + "#"))

    def execute(self, cmd):
        self.tn.write(self.encode(cmd + "\n"))
        self.telnet_logs.append(self.decode(self.tn.read_until(b"#")))

    def executes(self, cmds):
        for cmd in cmds:
            self.tn.write(self.encode(cmd + "\n"))
            log = self.decode(self.tn.read_until(self.encode(self.hostname + "#")))
            self.telnet_logs.append(log)

    def disconnect(self):
        self.tn.close()

    def get_telnet_log(self):
        return "\n".join(self.telnet_logs)

    def encode(self, str):
        return str.encode("ascii")

    def decode(self, str):
        return str.decode("ascii")