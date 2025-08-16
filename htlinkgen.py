import argparse
import webbrowser
import pyperclip

parser = argparse.ArgumentParser(
    description="hitomi.la ID Tool",
    epilog="https://github.com/lesipepsiman/htlinkgen"
)
parser.add_argument("id", type=int, help="gallery ID")
parser.add_argument("-c", "--copy", action="store_true", help="Copy link to clipboard")
parser.add_argument("-p", "--print", action="store_true", help="Print link to console")
args = parser.parse_args()

ID = str(args.id)
url = "https://hitomi.la/reader/"+ID+".html"

if not args.copy and not args.print:
    webbrowser.open(url)
if args.copy:
    pyperclip.copy(url)
if args.print:
    print(url)
