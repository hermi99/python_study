import telnetlib


class Telnet:
    def __init__(self, telnet_ip, telnet_id, telnet_pwd, telnet_en_pwd=''):
        self.telnet_ip = telnet_ip
        self.telnet_id = telnet_id
        self.telnet_pwd = telnet_pwd
        self.telnet_en_pwd = telnet_en_pwd

        self.hostname = ""

    def getCmdResult(self, cmds):
        log_all = ""

        try:
            tn = telnetlib.Telnet(self.telnet_ip, timeout=5)
        except:
            return False

        try:
            tn.read_until(b"ogin:")
            tn.write(self.telnet_id.encode('ascii') + b"\n")

            tn.read_until(b"assword:")
            tn.write(self.telnet_pwd.encode('ascii') + b"\n")

            expect_bytes = [b"ogin:", b"(.*)>"]

            index, match, log = tn.expect(expect_bytes, timeout=10)

            if index == 0:  # 로그인 실패
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
                if index_en == 1:  # password 다시 물어봄
                    tn.close()
                    return False
                elif index_en == 3:  # en login 성공
                    pass
                else:
                    tn.close()
                    return False
            elif index == 3:  # en login 성공
                pass
            else:
                tn.close()
                return False

            tn.write(b"terminal length 0\n")
            tn.expect(expect_bytes)

            tn.write(b"\n")
            log = tn.expect(expect_bytes)[2]

            for cmd in cmds:
                # tn.write(cmd.encode('utf-8') + b"\n")
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
            tn.close()
            return False

        tn.close()

        # log = log.decode('ascii').replace('\r', '')
        if type(log) != str:
            log = log.decode('euc-kr', 'ignore')

        return log