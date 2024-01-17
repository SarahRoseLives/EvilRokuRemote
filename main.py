from kivymd.app import MDApp
from localroku.core import Roku
import socket
import ipaddress
import localre as re
from kivymd.uix.list import ThreeLineListItem, OneLineListItem
from threading import Thread

configFile = 'config.conf'

class MainApp(MDApp):
    def build(self):
        # Setting theme to my favorite theme
        self.theme_cls.primary_palette = "DeepPurple"

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
        except:
            self.root.ids.label_network.text = "[size=35][b]Check WiFi[/b][/size]"


    def scan_network(self):
        #trying some dumb shit
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
        except OSError:
            pass
        sockname = s.getsockname()[0]
        s.close()
        ipaddr = re.findall('(.*\.)', sockname)
        network = [str(ip) for ip in ipaddress.IPv4Network(ipaddr[0] + '0/24')]
        f = open(configFile, 'w')
        f.write('')
        f.close()
        result = []
        count = 0
        for i in network:
            self.root.ids.button_networkscan.text = 'Scanning \r\n' + str(i)
            try:
                roku = Roku(i, timeout=0.1)
                roku.device_info
                count = count + 1
                result += [i]
                f = open(configFile, "a")
                f.write(str(i) + '\r\n')
                f.close()
            except:
                pass
        self.root.ids.button_networkscan.text = 'Complete'

 #       for i in result:
 #           self.root.ids.list_devices.add_widget(
 #               OneLineListItem(text=f"{i}")
 #           )

        #print(count)
        #print(result)


        #self.root.ids.label_discover.text = " Rokus found: " + str(count)
    def btn_scan(self):
        Thread(target=lambda: self.scan_network()).start()



    def load_list(self):
        self.root.ids.list_devices.clear_widgets()
        try:
            with open(configFile) as f:
                line = f.read().split()
                for i in line:
                    device_info = self.lookup_deviceinfo(ip=i)
                    device_name = device_info.splitlines()[0]
                    device_model = device_info.splitlines()[1] + ' ' + device_info.splitlines()[2]
                    self.root.ids.list_devices.add_widget(
                        ThreeLineListItem(text=f"{device_name}",
                                          secondary_text=f'{device_model}',
                                          tertiary_text=f'{i}',
                                          on_release=self.remove_ip)
                    )
        except:
            line = ['No Devices, Please Scan for Some']
            self.root.ids.list_devices.add_widget(
                OneLineListItem(text=f"{line[0]}")
            )
    def add_ip(self):
        inputip = self.root.ids.input_manualip.text
        with open(configFile, 'a') as file:
            file.write(inputip + '\r\n')
            file.close()
        self.load_list()

    def remove_ip(self, item):
        itemtoremove = item.tertiary_text

        with open(configFile, 'r') as file:
            data = file.read()
            file.close()
            data = data.replace(itemtoremove, '')
        with open(configFile, 'w') as file:
            file.write(data)
            file.close()
        self.load_list()





        #with open(configFile, 'r') as f:
        #    lines = f.read()
        #    f.close()
        #    print(lines)

    def lookup_deviceinfo(self, ip):
        roku = Roku(ip)
        return str(roku.device_info)

    def get_iplist(self):
        with open(configFile) as f:
            line = f.read().split()
            f.close()
            return line

    # ['back', 'backspace', 'channel_down', 'channel_up',
    # 'down', 'enter', 'find_remote', 'forward', 'home', 'info', 'input_av1',
    # 'input_hdmi1', 'input_hdmi2', 'input_hdmi3', 'input_hdmi4', 'input_tuner',
    # 'left', 'literal', 'play', 'power', 'poweroff', 'poweron', 'replay', 'reverse',
    # 'right', 'search', 'select', 'up', 'volume_down', 'volume_mute', 'volume_up']
    def update_status(self, command, ip):
        device_name = self.lookup_deviceinfo(ip=ip).splitlines()[0]
        self.root.ids.list_status.add_widget(
            OneLineListItem(text=f"Sent {command} to {ip} | {device_name}")
        )




    def run_command(self, command):
        try:
            line = self.get_iplist()
            for i in line:
                roku = Roku(i)
                if command == 'select':
                    roku.select()
                    self.update_status(command, ip=i)
                if command == 'back':
                    roku.back()
                    self.update_status(command, ip=i)
                if command == 'backspace':
                    roku.backspace()
                    self.update_status(command, ip=i)
                if command == 'channel_down':
                    roku.channel_down()
                    self.update_status(command, ip=i)
                if command == 'channel_up':
                    roku.channel_up()
                    self.update_status(command, ip=i)
                if command == 'down':
                    roku.down()
                    self.update_status(command, ip=i)
                if command == 'enter':
                    roku.enter()
                    self.update_status(command, ip=i)
                if command == 'find_remote':
                    roku.find_remote()
                    self.update_status(command, ip=i)
                if command == 'forward':
                    roku.forward()
                    self.update_status(command, ip=i)
                if command == 'home':
                    roku.home()
                    self.update_status(command, ip=i)
                if command == 'info':
                    roku.info()
                    self.update_status(command, ip=i)
                if command == 'input_av1':
                    roku.input_av1()
                    self.update_status(command, ip=i)
                if command == 'input_hdmi1':
                    roku.input_hdmi1()
                    self.update_status(command, ip=i)
                if command == 'input_hdmi2':
                    roku.input_hdmi2()
                    self.update_status(command, ip=i)
                if command == 'input_hdmi3':
                    roku.input_hdmi3()
                    self.update_status(command, ip=i)
                if command == 'input_hdmi4':
                    roku.input_hdmi4()
                    self.update_status(command, ip=i)
                if command == 'input_tuner':
                    roku.input_tuner()
                    self.update_status(command, ip=i)
                if command == 'left':
                    roku.left()
                    self.update_status(command, ip=i)
                if command == 'literal':
                    roku.litteral()
                    self.update_status(command, ip=i)
                if command == 'play':
                    roku.play()
                    self.update_status(command, ip=i)
                if command == 'power':
                    roku.power()
                    self.update_status(command, ip=i)
                if command == 'poweroff':
                    roku.poweroff()
                    self.update_status(command, ip=i)
                if command == 'poweron':
                    roku.poweron()
                    self.update_status(command, ip=i)
                if command == 'replay':
                    roku.replay()
                    self.update_status(command, ip=i)
                if command == 'reverse':
                    roku.reverse()
                    self.update_status(command, ip=i)
                if command == 'right':
                    roku.right()
                    self.update_status(command, ip=i)
                if command == 'search':
                    roku.search()
                    self.update_status(command, ip=i)
                if command == 'up':
                    roku.up()
                    self.update_status(command, ip=i)
                if command == 'volume_down':
                    roku.volume_down()
                    self.update_status(command, ip=i)
                if command == 'volume_mute':
                    roku.volume_mute()
                    self.update_status(command, ip=i)
                if command == 'volume_up':
                    roku.volume_up()
                    self.update_status(command, ip=i)
                else:
                    pass
        except:
            self.root.ids.list_status.add_widget(
                OneLineListItem(text=f"FAILED TO CONNECT, CHECK NETWORK!")
            )

            #roku.find_remote()

        #self.root.ids.drop_item.text = str(roku.apps[0])


if __name__ == '__main__':
    app = MainApp()
    app.run()