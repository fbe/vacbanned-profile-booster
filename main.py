import concurrent.futures
import requests
from fake_useragent import UserAgent
import random
from colorama import init, Fore, Style
import os
import subprocess
import ctypes

init()

def get_single_proxy(proxies):
    REMOVE_PROXY = True
    with open('proxies.txt', 'r+') as file:
        proxy_list = [line.replace('\n', '') for line in file]
        if len(proxy_list) == 0:
            print("Proxy list is empty.")
            return None
        ctypes.windll.kernel32.SetConsoleTitleW(f"vbBoost        ~        Target: {steamid}        ~        Proxies: {len(proxy_list)}")
        proxy = random.choice(proxy_list)
        if REMOVE_PROXY:
            proxy_list.remove(proxy)
            file.seek(0)
            file.truncate()
            file.write('\n'.join(proxy_list))
    return proxy

def send_request(steamid, proxies, session):
    headers = {
        'User-Agent': UserAgent().random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'http://vacbanned.com/engine/check',
        'Upgrade-Insecure-Requests': '1',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0'
    }

    proxy = get_single_proxy(proxies)
    data = {'qsearch': steamid}
    url = "http://vacbanned.com/engine/check"

    try:
        response = session.post(url, data=data, headers=headers, proxies={'http': proxy}, timeout=5)
        if response.status_code == 200:
            result = f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Attempt successful. [{Fore.GREEN}{proxy.replace('http://', '')}{Fore.WHITE}]{Fore.RESET}"
        else:
            result = f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Attempt failed. [{Fore.RED}{proxy.replace('http://', '')}{Fore.WHITE}]{Fore.RESET}"
    except (requests.exceptions.Timeout, requests.exceptions.ProxyError, requests.exceptions.ConnectionError):
        result = f"{Fore.WHITE}[{Fore.BLUE}?{Fore.WHITE}] Attempt timed out. [{Fore.BLUE}{proxy.replace('http://', '')}{Fore.WHITE}]{Fore.RESET}"

    return result.strip()

def main_func(steamid, amount):
    request_buffer = []
    logo = f"""{Fore.LIGHTMAGENTA_EX}
     ██▒   █▓ ▄▄▄▄    ▄▄▄▄    ▒█████   ▒█████    ██████ ▄▄▄█████▓
    ▓██░   █▒▓█████▄ ▓█████▄ ▒██▒  ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒
     ▓██  █▒░▒██▒ ▄██▒██▒ ▄██▒██░  ██▒▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░
      ▒██ █░░▒██░█▀  ▒██░█▀  ▒██   ██░▒██   ██░  ▒   ██▒░ ▓██▓ ░ 
       ▒▀█░  ░▓█  ▀█▓░▓█  ▀█▓░ ████▓▒░░ ████▓▒░▒██████▒▒  ▒██▒ ░ 
       ░ ▐░  ░▒▓███▀ ░▒▓███▀▒░ ▒░▒ ▒  ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   
       ░ ░    ░▒   ░ ▒░    ░   ░        ░ ▒  ░ ░  ▒    ░        
    """

    centered_text = f"{Fore.LIGHTMAGENTA_EX}            github.com/fbe {Fore.RED}♥ \n{Fore.RESET}"
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print(centered_text.center(os.get_terminal_size().columns))
    print()

    proxy_list = [line.replace('\n', '') for line in open('proxies.txt', 'r')]

    with requests.Session() as session:
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            futures = []
            for _ in range(amount):
                futures.append(executor.submit(send_request, steamid, proxy_list, session))
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                request_buffer.append(result)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(logo)
                print(centered_text.center(os.get_terminal_size().columns))
                for request in request_buffer[-5:]:
                    print(request)

if __name__ == "__main__":
    ctypes.windll.kernel32.SetConsoleTitleW(f"vbBoost        ~        Target: ?        ~        Proxies: ?")
    subprocess.run(['mode', 'con:', 'cols=70', 'lines=17'], shell=True)
    os.system('cls')
    steamid = input(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}?{Fore.WHITE}] What SteamID do you want to boost?: \n{Fore.WHITE}[{Fore.YELLOW}>{Fore.WHITE}] ")
    retries = input(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}?{Fore.WHITE}] How many retries?: \n{Fore.WHITE}[{Fore.YELLOW}>{Fore.WHITE}] ")
    main_func(steamid, int(retries))