class Exceptions(BaseException) : ...
import os, sys, threading, requests, bs4

get = requests.get

__structure__ = "UserName = "
__structure_answer__ = []

def __structure_methods__(*data):
    try:
        for i in range(0, 14):
            __structure_answer__.append(":::%s:::" % (data[i]))
    except IndexError : pass
    finally : return __structure_answer__

def load_pyc_files(filepath):
    path, fname = os.path.split(filepath)
    module, _ = os.path.splitext(fname)
        
    if path not in sys.path:            
        sys.path.insert(0, path)
        
    return __import__(module)
from json import load, loads, dump

def clear():
    import os
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def path_os(way):
    if os.sys.platform == "win32":
        new_way=way.replace("/", "\\")
    else:
        new_way=way.replace("\\", "/")
    return new_way

def __reconfig__(username):
    if '"' in username : raise Exceptions("Please, enter only text")

    try:
        with open(r'username.py', 'w') as userNfile: userNfile.write(__structure__+f"\"{username}\"")
        return True
    except : return False

class _config:
    UserName = load_pyc_files(r'username.py').UserName
    def __proxy_file_live__(self):
        try: 
            with open(r'proxy.json', 'r') : return True
        except: 
            return False

# Скан портов
class scan_port:
    def __scan__(self, host, port):
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            connect = sock.connect((host, port))
            sock.close()
            print(f'Open port : {port}')
        except : pass
    def __thread__(self, host):
        for list_ports in range(0, 50000):
            thread = threading.Thread(target=self.__scan__, args=(host, list_ports))
            thread.start()
            thread.join(0.5)

# Главный класс с методами
class Main:
# _console[ Пробив ip, mac, number. Генерация прокси ]
    class _console(_config):
        def __init__(self):
            try:
                while True:
                    choice = input(super().UserName + "> ")
                    if choice == "reconfig":
                        new_name = input("NewName> ")
                        if __reconfig__(username=new_name) == True : print('Exit'), quit()
                        else : print('Error')
                    elif choice == "scan_port_simple":
                        host = input("Enter host> ")
                        for list_ports in range(0, 50000):
                            scan_port().__scan__(host, list_ports)
                    elif choice == "scan_port_thread":
                        host = input("Enter host> ")
                        scan_port().__thread__(host)
                    elif choice == "ip":
                        self._methods().ip()
                    elif choice == "number":
                        self._methods().number()
                    elif choice == "mac":
                        self._methods().mac()
                    elif choice == "generation_proxy":
                        self._methods().generation_proxy()
                    elif choice == "help":
                        self.help()
                    elif choice == "exit" : sys.exit(1)
                    else : print(f"Not found command -> {choice}. If you have show list with command, enter \"help\"")
            except KeyboardInterrupt : print("Exit")
        def help(self):
            print("""
reconfig - reconfig file with username,
scan_port_simple - scan port without method \"threading\",
scan_port_thread - scan port with method \"threading\",
ip - break IP-Address,
number - break number phone,
mac - break MAC-Address,
generation_proxy - generate proxy for user,
exit - exit\n""")
        class _methods(_config):
            def ip(self):
                clear()
                print("Enter IP-Address")
                ip = input("> ")
                if super().__proxy_file_live__() == True:
                    with open(r'proxy.json', 'r') as proxy_file : proxy = load(proxy_file)
                else : proxy = None
                if proxy is not None : send_request = get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting", proxies=proxy)
                elif proxy == None : send_request = get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting")
                answer = send_request
                soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json = loads(soup_json)
                Handler = site_json
                info = len(__structure_methods__(Handler["continent"], Handler["country"], Handler["regionName"], Handler["city"], str(Handler["lat"]), str(Handler["lon"]), str(Handler["isp"]), Handler["org"], Handler["as"], Handler["asname"], Handler["reverse"], Handler["mobile"], Handler["proxy"], Handler["hosting"]))
                try:
                    for i in range(0, info):
                        print(__structure_answer__[i], end='\n')
                except : print(':::Not found:::')
                finally : __structure_answer__.clear()
            def number(self):
                clear()
                print("Enter number phone")
                number = input("> ")
                if super().__proxy_file_live__() == True:
                    with open(r'proxy.json', 'r') as proxy_file : proxy = load(proxy_file)
                else : proxy = None
                if proxy is not None : send_request = get(f"https://htmlweb.ru/json/mnp/phone/{number}", proxies=proxy)
                elif proxy == None : send_request = get(f"https://htmlweb.ru/json/mnp/phone/{number}")
                answer = send_request
                soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json = loads(soup_json)
                Handler = site_json
                info = len(__structure_methods__(Handler["oper"]["name"], Handler["oper"]["mnc"], Handler["oper"]["brand"], Handler["oper"]["inn"], Handler["mobile"], Handler["region"]["name"]))
                try:
                    for i in range(0, info):
                        print(__structure_answer__[i], end="\n")
                except : print(":::Not found:::")
                finally : __structure_answer__.clear()
            def mac(self):
                clear()
                print("Enter MAC-Address")
                mac = input("> ")
                if super().__proxy_file_live__() == True:
                    with open(r'proxy.json', 'r') as proxy_file : proxy = load(proxy_file)
                else : proxy = None
                if proxy is not None : send_request = get(f"https://api.2ip.ua/mac.json?mac={mac}", proxies=proxy)
                elif proxy == None : send_request = get(f"https://api.2ip.ua/mac.json?mac={mac}")
                answer = send_request
                soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json = loads(soup_json)
                Handler = site_json
                info = len(__structure_methods__(Handler["company"], Handler["address"], Handler["block_size"]))
                try:
                    for i in range(0, info):
                        print(__structure_answer__[i], end="\n")
                except : print(":::Not found:::")
                finally : __structure_answer__.clear()
            def generation_proxy(self):
                clear()
                print("Enter protocol proxy [\"http\", \"https\", \"socks4\", \"socks5\"]")
                protocol = input("> ")
                if 'http' or 'https' or 'socks4' or 'socks5' in protocol : pass
                else : raise Exceptions(f"Not found protocol -> {protocol}")
                send_request = get(f"https://www.proxyscan.io/api/proxy?type={protocol}")
                answer = send_request
                soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json = loads(soup_json)
                Handler = site_json
                for proxies in Handler:
                    host = proxies["Ip"]
                    port = proxies["Port"]
                data_proxy = {f"{protocol}": f"{protocol}://{host}:{port}"}
                with open('proxy.json', 'w') as proxy_ready : dump(data_proxy, proxy_ready)
                print("Proxy generated!")
if __name__ == "__main__":
    Main._console()
else:
    print("You have import this is file????")
    quit()
