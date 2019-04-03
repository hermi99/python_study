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

    def getCmdResultForL2(self, cmds):
        log_all = ""

        try:
            tn = telnetlib.Telnet(self.telnet_ip, timeout=10)
        except:
            self.error_type = TelnetError.connect_error
            return False

        try:
            tn.read_until(b"ogin:")
            tn.write(self.telnet_id.encode('ascii') + b"\n")

            tn.read_until(b"assword:")
            tn.write(self.telnet_pwd.encode('ascii') + b"\n")

            expect_bytes = [b"ogin:", b"(.*)>"]

            index, match, log = tn.expect(expect_bytes, timeout=10)

            if index == 0:  # 로그인 실패
                self.error_type = TelnetError.login_fail
                tn.close()
                return False
            elif index == 1:
                hostname = match.group(1)
                expect_bytes = [b"ogin:", b"assword:", hostname + b">", hostname + b"#"]

            # log_all += hostname + "\n"
            self.hostname = hostname

            tn.write(b"enable\n")
            index, match, log = tn.expect(expect_bytes, timeout=10)

            if index == 1:  # en password 입력대기 상태
                tn.write(self.telnet_en_pwd.encode('ascii') + b"\n")
                # index_en, _, _ = tn.expect(expect_bytes, timeout=5)
                index_en, _, log = tn.expect(expect_bytes, timeout=5)
                if index_en == 1: # password 다시 물어봄
                    self.error_type = TelnetError.enable_fail
                    tn.close()
                    return False
                elif index_en == 3:  # en login 성공
                    pass
                else:
                    self.error_type = TelnetError.unknown
                    tn.close()
                    return False
            elif index == 3:  # en login 성공
                pass
            else:
                self.error_type = TelnetError.unknown
                tn.close()
                return False

            tn.write(b"terminal length 0\n")
            tn.expect(expect_bytes)

            tn.write(b"\n")
            log = tn.expect(expect_bytes)[2]

            for cmd in cmds:
                tn.write(cmd.encode('ascii') + b"\n")
                log = log + tn.expect(expect_bytes, timeout=15)[2]

                tn.write(b"\n")
                log = log + tn.expect(expect_bytes)[2]

                tn.write(b"\n")
                log = log + tn.expect(expect_bytes)[2]

                tn.write(b"\n")
                log = log + tn.expect(expect_bytes)[2]

            tn.write(b"exit\n")

        except Exception as e:
            self.error_type = TelnetError.unknown
            self.error_desc = "unknown error : {}, {}".format(e, log_all)
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