class Telnet:
    def __init__(self, telnet_ip, telnet_id, telnet_pwd, telnet_en_pwd=''):
        self.telnet_ip = telnet_ip
        self.telnet_id = telnet_id
        self.telnet_pwd = telnet_pwd
        self.telnet_en_pwd = telnet_en_pwd

        self.error_type = None
        self.error_desc = ""
        self.hostname = ""
		
		
	def getCmdResult(self, cmds):
        try:
            tn = telnetlib.Telnet(self.telnet_ip, timeout=5)
        except:
            self.error_type = TelnetError.connect_error
            return False

        tn.read_until(b"ogin:")  # login id 입력 대기상태
        tn.write(self.telnet_id.encode('ascii') + b"\n")

        tn.read_until(b"assword:")  # password 대기상태
        tn.write(self.telnet_pwd.encode('ascii') + b"\n")

        expect_bytes = [b"ogin:", b"\w\:(.*)\#"]
        try:
            index, match, log = tn.expect(expect_bytes, timeout=5)

            if index == 0:  # 로그인 실패
                self.error_type = TelnetError.login_fail
                tn.close()
                return False
            elif index == 1:
                hostname = match.group(1)
                # print(hostname)
                expect_bytes = [hostname + b"#", hostname + b">"]

            tn.write(b"environment no more\n")
            tn.expect(expect_bytes)

            for cmd in cmds:
                tn.write(cmd.encode('ascii') + b"\n")
                log = log + tn.expect(expect_bytes)[2]

                tn.write(b"\n")
                log = log + tn.expect(expect_bytes)[2]

                tn.write(b"\n")
                log = log + tn.expect(expect_bytes)[2]

                tn.write(b"\n")
                log = log + tn.expect(expect_bytes)[2]

        except:
            self.error_type = TelnetError.unknown
            tn.close()
            return False

        tn.close()

        log = log.decode('ascii').replace('\r', '')

        return log
		
		
class TelnetError(enum.Enum):
    connect_error = 1
    login_fail = 2
    enable_fail = 3
    unknown = 10