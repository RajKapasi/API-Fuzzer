import argparse
import sys
import requests
import time
import json
import threading
from queue import Queue
from colorama import Fore, Style, init


init(autoreset=True)
# Default threads = 10
THREADS = 10

def fuzz_worker(queue,args,results):
    # Use while loop to read word from Queue
    while not queue.empty():
        word = queue.get().strip()
        # If there is no word then continue
        if not word:
            continue
        # Replace FUZZ word enter in target url with wordlist
        if "FUZZ" in args.target:
            url = args.target.replace("FUZZ",word)
        elif args.data and "FUZZ" in args.data:
            url=args.target
        else:
            url=f"{args.target.rstrip('/')}/{word}"

        headers={}
        if args.headers:
            for h in args.headers.split(","):
                if":" in h:
                    k, v = h.split(":", 1)
                    headers[k.strip()] = v.strip()

        try:
            if args.data:
                data = args.data.replace("FUZZ",word)
                # Send http or https requests
                res = requests.request(args.method, url , headers=headers, timeout=5)

            else:
                res = requests.request(args.method , url, headers=headers, timeout=5)

            status = res.status_code
            color=(
                Fore.GREEN if status ==200 else
                Fore.YELLOW if status in (301,302) else
                Fore.RED if status == 403 else
                Fore.MAGENTA if status >=500 else
                Fore.WHITE
            )

            if status != 404 :
                try:
                    data = res.json()
                except Exception:
                    data = res.text[:100]
                line = f"[{status}] {url} -> {data}"
                print(color + line + Style.RESET_ALL)
                results.append({"payload" : word, "url" : url, "status" : status, "response" : data})

        except Exception as e:
            print(Fore.CYAN + f"[!] Error on '{word}':{e}")
        finally:
            queue.task_done()

        if args.delay:
            time.sleep(args.delay)


def main():
    #This is a tool description shows how tool works and take arguments on command line interface
    parser=argparse.ArgumentParser(description ="API FUZZER")
    parser.add_argument("target",help="Target URL/FUZZ (FUZZ will replace by wordlist)")
    parser.add_argument("-w", "--wordlist" , help="Wordlist File", required=False)
    parser.add_argument("-H","--headers", help="Custom headers (e.g : 'Auth:Bearer TOKEN , User-Agent=Test')", required=False)
    parser.add_argument("-X", "--method", help="HTTP method", default="GET")
    parser.add_argument("-d","--data", help="POST, PUT data", required=False)
    parser.add_argument("-t","--threads", help="Number of threads (default=10)",type=int,default=10)
    parser.add_argument("--delay",help="Delay between  requests (seconds)" , type=float, default=0)
    parser.add_argument("-o", "--output",help="Save result to JSON file", required=False)
    args =parser.parse_args()

#In this stage wordlist is read and put every word it into a Queue
    result=[]
    queue=Queue()
    if args.wordlist:
        with open(args.wordlist,"r",encoding="utf-8",errors="ignore") as f:
            for line in f:
                queue.put(line.strip())

    else :
        for line in sys.stdin:
            queue.put(line.strip())

    print(Fore.CYAN + f"[+] Starting Fuzzing on {args.target} with {args.threads} threads")

# Start the threads and call the function fuzz_worker
    threads=[]
    for _ in range(args.threads):
        t= threading.Thread(target=fuzz_worker, args=(queue, args, result))
        t.daemon = True
        t.start()
        threads.append(t)

    queue.join()
# In this stage the result of output is store in Json file given by user
    if args.output:
        with open (args.output, "w") as f:
            json.dump(result, f ,indent=2)
        print(Fore.CYAN + f"[+] Results Save in {args.output}")

# main function the program start with this function
if __name__ == "__main__":
    main()