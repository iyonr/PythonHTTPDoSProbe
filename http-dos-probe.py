import threading
import requests
import argparse

def send_request(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Request sent, status code: {response.status_code}")
        except Exception as e:
            print(f"Request failed: {e}")

def main(url, num_threads):
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=send_request, args=(url,))
        t.start()
        threads.append(t)

    # To keep the script running, join all threads
    for t in threads:
        t.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HTTP Request Sender')
    parser.add_argument('url', type=str, help='URL to send requests to')
    parser.add_argument('num_threads', type=int, help='Number of concurrent threads')

    args = parser.parse_args()

    main(args.url, args.num_threads)