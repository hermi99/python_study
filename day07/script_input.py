import ipaddress
import sys

from PyQt5 import uic
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QApplication

from day07.dialog_script import DialogScript

uifile = r'.\qt\script_input.ui'
form, base = uic.loadUiType(uifile)


class ScriptInput(form, base):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setup_data()

    def setup_data(self):
        self.combo_interface.addItem("ge0/1")
        self.combo_interface.addItem("ge0/2")
        self.combo_interface.addItem("ge0/3")
        self.combo_interface.addItem("ge0/4")
        self.combo_interface.addItem("ge0/5")

        self.btn_script.clicked.connect(self.btn_script_clicked)

        # 전용회선번호 체크
        linenum_check = QRegExpValidator(QRegExp("[\d]{8}-[\d]{4}"))
        self.text_line_number.setValidator(linenum_check)

        # 고객명은 영문만 허용
        reg_ex = QRegExp("[A-Za-z0-9_\`\~\!\@\#\$\%\^\&\*\(\)\-\=\+\\\{\}\[\]\'\"\;\:\<\,\>\.\?\/\s]*")
        custNameValidator = QRegExpValidator(reg_ex)
        self.text_custname.setValidator(custNameValidator)

        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
        bitRange = "(?:(?:[2][0-9]|[3][0-2]))"
        ipRegex = QRegExp("^" + ipRange + "\\." + ipRange + "\\." + ipRange
                          + "\\." + ipRange + "\/" + bitRange + "$")

        ipValidator = QRegExpValidator(ipRegex)
        self.text_serial_ip.setValidator(ipValidator)
        self.text_ethernet_ip.setValidator(ipValidator)

    def btn_script_clicked(self):
        interface = self.combo_interface.currentText()
        custname = self.text_custname.text()
        line_number = self.text_line_number.text()
        serial_ip = self.text_serial_ip.text()
        ethernet_ip = self.text_ethernet_ip.text()

        print(interface, custname, line_number, serial_ip, ethernet_ip)

        try:
            # serial ip 의 subnetmask, netxhop 을 구한다.
            serial_net = ipaddress.ip_network(serial_ip, strict=False)
            serial_netmask = serial_net.netmask
            serial_nexthop = list(serial_net.hosts())[1]
            serial_address = ipaddress.ip_interface(serial_ip).ip

            # ethernet ip 의 subnetmask 를 구한다.
            ethernet = ipaddress.ip_network(ethernet_ip, strict=False)
            ethernet_netmask = ethernet.netmask
            ehternet_address = ipaddress.ip_interface(ethernet_ip).ip

            print("serial_netmask:", serial_netmask)
            print("serial_nexthop:", serial_nexthop)
            print("ethernet_netmask:", ethernet_netmask)
        except Exception as e:
            print(e)

        script_lines = []

        line = "interface {}".format(interface)
        script_lines.append(line)

        line = "description ## {}, {} ##".format(line_number, custname)
        script_lines.append(line)

        line = "ip address {} {}".format(serial_address, serial_netmask)
        script_lines.append(line)

        script_lines.append("")

        line = "ip route {} {}".format(ehternet_address, ethernet_netmask)
        script_lines.append(line)

        print("\n".join(script_lines))

        dialog = DialogScript("\n".join(script_lines))
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    script_input = ScriptInput()
    script_input.show()
    app.exec()
