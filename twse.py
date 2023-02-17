__author__ = "https://vk.com/twse_newsoffc, https://github.com/Sos1ska, https://vk.com/nikitasos1ska"
__version__ = "0.2"
class Exceptions(BaseException) : ...
import os, sys, threading, requests, bs4, datetime
from json import load, loads, dump

# Новый модуль 11:42 14.02.2023
def __create__():
    with open("settings.json", 'w') as create_file : dump(__structure__, create_file)
    sys.exit(1)

get = requests.get

__structure__ = {"Program":{"Language":"ENG", "UserName":"TWSEUser", "Proxy":"No"}, "System":{"ClearWindow":"Yes", "ClearEveryTime":"Yes", "InputDebugInFile":"Yes"}}
__structure_answer__ = []

# Новый класс 13:32 14.02.2023
class micro_logger:
    date = str(datetime.datetime.now())
    def __init__(self, mode, text):
        self.text = text
        if mode == "error":
            if os.path.exists(r'log') == True:
                with open(r'log', 'a') as file_log : file_log.write(self.__error__() +'\n')
            else:
                print("Created file \"log\"")
                with open(r'log', 'w') as file_log : file_log.write(self.__error__() +'\n')
        elif mode == "info":
            if os.path.exists(r'log') == True:
                with open(r'log', 'a') as file_log : file_log.write(self.__info__() +'\n')
            else:
                print("Created file \"log\"")
                with open(r'log', 'w') as file_log : file_log.write(self.__info__() +'\n')
        elif mode == "warning":
            if os.path.exists(r'log') == True:
                with open(r'log', 'a') as file_log : file_log.write(self.__warn__() +'\n')
            else:
                print("Created file \"log\"")
                with open(r'log', 'w') as file_log : file_log.write(self.__warn__() +'\n')
        elif mode == "debug":
            if os.path.exists(r'log') == True:
                with open(r'log', 'a') as file_log : file_log.write(self.__deb__() +'\n')
            else:
                print("Created file \"log\"")
                with open(r'log', 'w') as file_log : file_log.write(self.__deb__() +'\n')
    def __error__(self):
        return f"[ root ] - [ [ ERROR ] {self.text} ] {self.date}"
    def __info__(self):
        return f"[ root ] - [ [ INFO ] {self.text} ] {self.date}"
    def __warn__(self):
        return f"[ root ] - [ [ WARNING ] {self.text} ] {self.date}"
    def __deb__(self):
        return f"[ root ] - [ [ DEBUG ] {self.text} ] {self.date}"
    
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

# Новый модуль 11:47 14.02.2023
def __replace_nick__(username):
    try:
        if '"' in username or '\'' in username : raise Exceptions(f"You entered special symbol in username")
        with open(r'settings.json', 'r') as old_version_file : old_data = load(old_version_file)
        old_data["Program"]["UserName"] = username
        with open(r'settings.json', 'w') as new_version_file : dump(old_data, new_version_file, sort_keys=True)
    except : return False
    finally : return True

# Новый модуль 12:07 14.02.2023
def __replace_lang__(lang):
    list_rus = ["RUS", "rus", "rUS", "ruS", "Rus"]
    list_eng = ["ENG", "eng", "eNG", "enG", "Eng"]
    if lang in list_rus:
        language = lang.replace(lang, "RUS")
    elif lang in list_eng:
        language = lang.replace(lang, "ENG")
    with open(r'settings.json', 'r') as old_version_file : old_data = load(old_version_file)
    old_data["Program"]["Language"] = language
    with open(r'settings.json', 'w') as new_version_file : dump(old_data, new_version_file, sort_keys=True)

# Новый класс 13:07 14.02.2023
class __replaces_system__:
    def __init__(self, _answer, _branch):
        self.local_data = _answer
        if _branch == "ClearEveryTime":
            self.__single_replaces__().__clear_every_time__(self.__check_answer__())
        elif _branch == "ClearWindow":
            self.__single_replaces__().__clear_window__(self.__check_answer__())
        elif _branch == "InputDebugInFile":
            self.__single_replaces__().__input_debug_in_file__(self.__check_answer__())
        else:
            print(f"Not found branch -> {_branch}")
    def __check_answer__(self):
        yes_list = ["YES", "YeS", "yEs", "Yes", "yES", "y", "Y", "yes"]
        no_list = ["NO", "nO", "No", "n", "N", "no"]
        if self.local_data in yes_list:
            new_data = self.local_data.replace(self.local_data, "Yes")
        elif self.local_data in no_list:
            new_data = self.local_data.replace(self.local_data, "No")
        return new_data
    class __single_replaces__:
        def __clear_every_time__(self, _answer):
            with open(r'settings.json', 'r') as old_version_file : old_data = load(old_version_file)
            old_data["System"]["ClearEveryTime"] = _answer
            with open(r'settings.json', 'w') as new_version_file : dump(old_data, new_version_file)
        def __clear_window__(self, _answer):
            with open(r'settings.json', 'r') as old_version_file : old_data = load(old_version_file)
            old_data["System"]["ClearWindow"] = _answer
            with open(r'settings.json', 'w') as new_version_file : dump(old_data, new_version_file)
        def __input_debug_in_file__(self, _answer):
            with open(r'settings.json', 'r') as old_version_file : old_data = load(old_version_file)
            old_data["System"]["InputDebugInFile"] = _answer
            with open(r'settings.json', 'w') as new_version_file : dump(old_data, new_version_file)

# Новый модуль 13:20 14.02.2023
def __return_nick__():
    with open(r'settings.json', 'r') as file_with_nick : data = load(file_with_nick)
    nick = data["Program"]["UserName"]
    return nick

# Новый класс 13:23 14.02.2023
def _config():
    try:
        with open(r'settings.json', 'r') as file_settings : data = load(file_settings)
    except FileNotFoundError : print('Set default settings'), __create__()
    return data

# Новый модуль 13:53 14.02.2023
def __proxy_file_live__():
    try:
        with open(r'proxy.json', 'r') : return True
    except : return False

# Новый модуль 20:37 14.02.2023
def __check_proxy__():
    with open(r'proxy.json', 'r') as proxy_file : data=load(proxy_file)
    send_request = get("http://ip-api.com/json/")
    soup_json = bs4.BeautifulSoup(send_request.text, "html.parser").text.strip()
    site_json = loads(soup_json)
    user_ip = site_json["query"]
    send_request_p = get("http://ip-api.com/json/", proxies=data)
    soup_json_p = bs4.BeautifulSoup(send_request_p.text, "html.parser").text.strip()
    site_json_p = loads(soup_json_p)
    user_ip_p = site_json_p["query"]
    if user_ip == user_ip_p:
        return False
    else:
        return True

config = _config()

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
# Дописать проверку работы через прокси в методах
    class _console:
        def __init__(self):
            if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Starting work \"_console.__init__\"")
            try:
                while True:
                    choice = input(__return_nick__() + "> ")
                    if choice == "reconfig":
                        new_name = input("NewName> ")
                        if __replace_nick__(username=new_name) == True : print('Exit'), quit()
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
                    elif choice == "replace_value_config":
                        self._methods().replace_mode()
                    elif choice == "exit" : sys.exit(1)
                    else : print(f"Not found command -> {choice}. If you have show list with command, enter \"help\"")
            except KeyboardInterrupt : print("Exit")
        def help(self):
            if config["Program"]["Language"] == "ENG" : print("""
reconfig - reconfig file with username,
scan_port_simple - scan port without method \"threading\",
scan_port_thread - scan port with method \"threading\",
ip - break IP-Address,
number - break number phone,
mac - break MAC-Address,
generation_proxy - generate proxy for user,
replace_value_config - Change settings in settings,
exit - exit\n""")
            if config["Program"]["Language"] == "RUS" : print("""
reconfig - файл реконфигурации с именем пользователя,
scan_port_simple - сканировать порт без метода \"threading\",
scan_port_thread - сканировать порт методом \"threading\",
ip - пробить IP-адрес,
number - пробить номер телефона,
mac - пробить MAC-адрес,
generation_proxy - сгенерировать прокси для пользователя,
replace_value_config - Поменять значения в настройках,
exit - выход\n""")
        class _methods:
            def ip(self):
                if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Starting work \"_methods.ip\"")
                if config["System"]["ClearEveryTime"] == "Yes" : clear()
                if config["Program"]["Language"] == "ENG" : print("Enter IP-Address")
                if config["Program"]["Language"] == "RUS" : print("Введите IP-адрес")
                ip = input("> ")
                if config["Program"]["Proxy"] == "Yes":
                    if __proxy_file_live__() == True:
                        with open(r'proxy.json', 'r') as proxy_file : proxy = load(proxy_file)
                    else : proxy = None
                    if proxy is not None:
                        if __check_proxy__() == True:
                            send_request = get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting", proxies=proxy)
                            if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Send request with proxy")
                        else:
                            send_request = get(f"http://ip-api.com/json/")
                            if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Send request1")
                    elif proxy == None: 
                        send_request = get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting")
                        if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Send request")
                else: 
                    send_request = get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting")
                    if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Send request")
                answer = send_request
                soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json = loads(soup_json)
                Handler = site_json
                info = len(__structure_methods__(Handler["continent"], Handler["country"], Handler["regionName"], Handler["city"], str(Handler["lat"]), str(Handler["lon"]), str(Handler["isp"]), Handler["org"], Handler["as"], Handler["asname"], Handler["reverse"], Handler["mobile"], Handler["proxy"], Handler["hosting"]))
                try:
                    for i in range(0, info):
                        print(__structure_answer__[i], end='\n')
                except: 
                    if config["Program"]["Language"] == "ENG" : print(':::Not found:::')
                    if config["Program"]["Language"] == "RUS" : print(':::Не найдено:::')
                finally: 
                    __structure_answer__.clear()
                    if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "End working \"_methods.ip\"")
            def number(self):
                if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Starting work \"_methods.number\"")
                if config["System"]["ClearEveryTime"] == "Yes" : clear()
                if config["Program"]["Language"] == "ENG" : print("Enter number phone")
                if config["Program"]["Language"] == "RUS" : print("Введите номер телефона")
                number = input("> ")
                if config["Program"]["Proxy"] == "Yes":
                    if __proxy_file_live__() == True:
                        with open(r'proxy.json', 'r') as proxy_file : proxy = load(proxy_file)
                    else : proxy = None
                    if proxy is not None:
                        if __check_proxy__() == True:
                            send_request = get(f"https://htmlweb.ru/json/mnp/phone/{number}", proxies=proxy)
                            if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Send request with proxy")
                        else:
                            send_request = get(f"http://ip-api.com/json/")
                            if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Send request1")
                    elif proxy == None: 
                        send_request = get(f"https://htmlweb.ru/json/mnp/phone/{number}")
                        if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Send request")
                else: 
                    send_request = get(f"https://htmlweb.ru/json/mnp/phone/{number}")
                    if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Send request")
                answer = send_request
                soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json = loads(soup_json)
                Handler = site_json
                info = len(__structure_methods__(Handler["oper"]["name"], Handler["oper"]["mnc"], Handler["oper"]["brand"], Handler["oper"]["inn"], Handler["mobile"], Handler["region"]["name"]))
                try:
                    for i in range(0, info):
                        print(__structure_answer__[i], end="\n")
                except: 
                    if config["Program"]["Language"] == "ENG" : print(':::Not found:::')
                    if config["Program"]["Language"] == "RUS" : print(':::Не найдено:::')
                finally: 
                    __structure_answer__.clear()
                    if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "End working \"_methods.number\"")
            def mac(self):
                if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Starting work \"_methods.mac\"")
                if config["System"]["ClearEveryTime"] == "Yes" : clear()
                if config["Program"]["Language"] == "ENG" : print("Enter MAC-Address")
                if config["Program"]["Language"] == "RUS" : print("Введите MAC-адрес")
                mac = input("> ")
                if config["Program"]["Proxy"] == "Yes":
                    if __proxy_file_live__() == True:
                        with open(r'proxy.json', 'r') as proxy_file : proxy = load(proxy_file)
                    else : proxy = None
                    if proxy is not None:
                        if __check_proxy__() == True:
                            send_request = get(f"https://api.2ip.ua/mac.json?mac={mac}", proxies=proxy)
                            if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Send request with proxy")
                        else:
                            send_request = get(f"http://ip-api.com/json/")
                            if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Send request1")
                    elif proxy == None: 
                        send_request = get(f"https://api.2ip.ua/mac.json?mac={mac}")
                        if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Send request")
                else: 
                    send_request = get(f"https://api.2ip.ua/mac.json?mac={mac}")
                    if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Send request")
                answer = send_request
                soup_json = bs4.BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json = loads(soup_json)
                Handler = site_json
                info = len(__structure_methods__(Handler["company"], Handler["address"], Handler["block_size"]))
                try:
                    for i in range(0, info):
                        print(__structure_answer__[i], end="\n")
                except: 
                    if config["Program"]["Language"] == "ENG" : print(':::Not found:::')
                    if config["Program"]["Language"] == "RUS" : print(':::Не найдено:::')
                finally: 
                    __structure_answer__.clear()
                    if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "End working \"_methods.mac\"")
            def generation_proxy(self):
                if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Starting work \"_methods.generation_proxy\"")
                if config["System"]["ClearEveryTime"] == "Yes" : clear()
                if config["Program"]["Language"] == "ENG" : print("Enter protocol proxy [\"http\", \"https\", \"socks4\", \"socks5\"]")
                if config["Program"]["Language"] == "RUS" : print("Введите протокол прокси [\"http\", \"https\", \"socks4\", \"socks5\"]")
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
                if config["Program"]["Language"] == "ENG" : print("Proxy generated")
                if config["Program"]["Language"] == "RUS" : print("Прокси сгенерирован")
                if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "End working \"_methods.generation_proxy\"")
                sys.exit(1)
            # Новый модуль 13:28 14.02.2023
            def replace_mode(self):
                if config["System"]["InputDebugInFile"] == "Yes" : micro_logger("debug", "Starting work \"replace_mode\"")
                list_modes_system = ["ClearEveryTime", "ClearWindow", "InputDebugInFile"]
                list_modes_program = ["Language", "UserName"]
                if config["Program"]["Language"] == "ENG":
                    print("Select branch [\"System\", \"Program\"]")
                    choice = input('> ')
                    if choice == "System":
                        print(f"Select mode {list_modes_system}")
                        mode = input("> ")
                        if mode == "ClearEveryTime":
                            print("Enter Value [\"Yes\", \"No\"]")
                            value = input("> ")
                            __replaces_system__(value, mode)
                            sys.exit(1)
                        elif mode == "ClearWindow":
                            print("Enter Value [\"Yes\", \"No\"]")
                            value = input("> ")
                            __replaces_system__(value, mode)
                            sys.exit(1)
                        elif mode == "InputDebugInFile":
                            print("Enter Value [\"Yes\", \"No\"]")
                            value = input("> ")
                            __replaces_system__(value, mode)
                            sys.exit(1)
                        else:
                            print("Not found mode. Exit")
                            sys.exit(1)
                    elif choice == "Program":
                        print(f"Select mode {list_modes_program}")
                        mode = input("> ")
                        if mode == "Language":
                            print("Enter language [\"RUS\", \"ENG\"]")
                            value = input("> ")
                            __replace_lang__(value)
                            sys.exit(1)
                        elif mode == "UserName":
                            print("Enter new UserName")
                            new_name = input("> ")
                            if __replace_nick__(new_name) == True : print("NickName changed.\n Exit"), sys.exit(1)
                            else : raise Exceptions("Error after trying change NickName")
                        else:
                            print("Not found mode. Exit")
                            sys.exit(1)
                    else:
                        print("Not found branch. Exit")
                        sys.exit(1)
                elif config["Program"]["Language"] == "RUS":
                    print("Выберите ветвь [\"System\", \"Program\"]")
                    choice = input('> ')
                    if choice == "System":
                        print(f"Выберите мод {list_modes_system}")
                        mode = input("> ")
                        if mode == "ClearEveryTime":
                            print("Введите значение [\"Yes\", \"No\"]")
                            value = input("> ")
                            __replaces_system__(value, mode)
                            sys.exit(1)
                        elif mode == "ClearWindow":
                            print("Введите значение [\"Yes\", \"No\"]")
                            value = input("> ")
                            __replaces_system__(value, mode)
                            sys.exit(1)
                        elif mode == "InputDebugInFile":
                            print("Введите значение [\"Yes\", \"No\"]")
                            value = input("> ")
                            __replaces_system__(value, mode)
                            sys.exit(1)
                        else:
                            print("Такого мода нету. Exit")
                            sys.exit(1)
                    elif choice == "Program":
                        print(f"Выберите ветвь {list_modes_program}")
                        mode = input("> ")
                        if mode == "Language":
                            print("Введите язык [\"RUS\", \"ENG\"]")
                            value = input("> ")
                            __replace_lang__(value)
                            sys.exit(1)
                        elif mode == "UserName":
                            print("Введите новый UserName")
                            new_name = input("> ")
                            if __replace_nick__(new_name) == True : print("NickName изменён.\n Exit"), sys.exit(1)
                            else : raise Exceptions("Error after trying change NickName")
                        else:
                            print("Такого мода нету. Exit")
                            sys.exit(1)
                    else:
                        print("Такой ветви нету. Exit")
                        sys.exit(1)
    # Новый класс 20:04 14.02.2023
    class _methods_fast:
        def __ip__(self, ip):
            micro_logger("debug", "Starting work \"_methods_fast.__ip__\"")
            if config["Program"]["Proxy"] == "Yes":
                if __proxy_file_live__() == True:
                    with open(r'proxy.json', 'r') as proxy_file : proxy = load(proxy_file)
                else : proxy=None
                if proxy is not None : send_request = get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting", proxies=proxy)
                elif proxy == None : send_request = get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting")
            else:
                send_request = get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting")
            soup_json = bs4.BeautifulSoup(send_request.text, "html.parser").text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            info = len(__structure_methods__(Handler["continent"], Handler["country"], Handler["regionName"], Handler["city"], str(Handler["lat"]), str(Handler["lon"]), str(Handler["isp"]), Handler["org"], Handler["as"], Handler["asname"], Handler["reverse"], Handler["mobile"], Handler["proxy"], Handler["hosting"]))
            for i in range(0, info):
                print(__structure_answer__[i], end='\n')
            input()
            micro_logger("debug", "End work \"_methods_fast.__ip__\"")
            sys.exit(1)
        def __number__(self, number):
            micro_logger("debug", "Starting work \"_methods_fast.__number__\"")
            if config["Program"]["Proxy"] == "Yes":
                if __proxy_file_live__() == True:
                    with open(r'proxy.json', 'r') as proxy_file : proxy = load(proxy_file)
                else : proxy=None
                if proxy is not None : send_request = get(f"https://htmlweb.ru/json/mnp/phone/{number}", proxies=proxy)
                elif proxy == None : send_request = get(f"https://htmlweb.ru/json/mnp/phone/{number}")
            else:
                send_request = get(f"https://htmlweb.ru/json/mnp/phone/{number}")
            soup_json = bs4.BeautifulSoup(send_request.text, "html.parser").text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            info = len(__structure_methods__(Handler["oper"]["name"], Handler["oper"]["mnc"], Handler["oper"]["brand"], Handler["oper"]["inn"], Handler["mobile"], Handler["region"]["name"]))
            for i in range(0, info):
                print(__structure_answer__[i], end='\n')
            input()
            micro_logger("debug", "End work \"_methods_fast.__number__\"")
            sys.exit(1)
        def __mac__(self, mac):
            micro_logger("debug", "Starting work \"_methods_fast.__mac__\"")
            if config["Program"]["Proxy"] == "Yes":
                if __proxy_file_live__() == True:
                    with open(r'proxy.json', 'r') as proxy_file : proxy = load(proxy_file)
                else : proxy=None
                if proxy is not None : send_request = get(f"https://api.2ip.ua/mac.json?mac={mac}", proxies=proxy)
                elif proxy == None : send_request = get(f"https://api.2ip.ua/mac.json?mac={mac}")
            else:
                send_request = get(f"https://api.2ip.ua/mac.json?mac={mac}")
            soup_json = bs4.BeautifulSoup(send_request.text, "html.parser").text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            info = len(__structure_methods__(Handler["company"], Handler["address"], Handler["block_size"]))
            for i in range(0, info):
                print(__structure_answer__[i], end='\n')
            input()
            micro_logger("debug", "End work \"_methods_fast.__mac__\"")
            sys.exit(1)

if __name__ == "__main__":
    Main._console()
else:
    print("You have import this is file????")
    quit()
