import argparse
import threading
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from colorama import init, Fore, Style

init()

INFO = Fore.YELLOW + 'CHECKING'.ljust(8)
SUCCESS = Fore.GREEN + 'SUCCESS'.ljust(8)
ABNORMAL = Fore.CYAN + 'ABNORMAL'.ljust(8)
ERROR = Fore.RED + 'FAILED'.ljust(8)


def print_message(url, message, end='\n'):
    """Print status message"""

    print(
        Style.BRIGHT +
        Fore.WHITE + '[',
        message,
        Fore.WHITE + ']',
        Style.RESET_ALL,
        Fore.WHITE + url,
        end=end
    )


def fix_url(url):
    """Fix broken url"""

    url = url.strip()
    if not url.__contains__('http'):
        url = 'http://' + url
    return url


def check(url):
    """Check if url is ok, abnormal or not healthy"""

    print_message(url, INFO, end='\r')
    try:
        request = Request(url=url, method="GET")
        response = urlopen(request)
        if response.status == 200:
            print_message(url, SUCCESS)
        else:
            print_message(url, ABNORMAL)
    except HTTPError:
        print_message(url, ABNORMAL)
    except:
        print_message(url, ERROR)


def get200ok(url_list):
    """Start status checker"""

    for url in url_list:
        url = fix_url(url)
        threading.Thread(target=lambda: check(url)).start()


parser = argparse.ArgumentParser(
    description="Check website status, get 200 ok response"
)
parser.add_argument(
    "-f",
    "--files",
    nargs='+',
    help="One or more word list files",
    type=argparse.FileType('r')
)

parser.add_argument(
    "-u",
    "--urls",
    nargs='+',
    help="One or more website urls",
    type=str
)

if __name__ == '__main__':
    urls = []
    args = parser.parse_args()
    if args.files:
        for file in args.files:
            urls.extend(file.readlines())

    if args.urls:
        urls.extend(args.urls)

    get200ok(url_list=urls)
