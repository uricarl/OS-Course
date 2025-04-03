import threading
import requests
import time

def downloader(i, url, returns):
    time_start = time.time()
    requests.get(url).json()
    time_end = time.time()
    returns[i] = time_end - time_start   # Total time for download

def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
     
    threads = []
    threads_returns = {}
    threads_names = []
    
    for i, url in enumerate(urls):
        thread = threading.Thread(target= downloader, args=(i, url, threads_returns))
        thread.start()
        threads.append(thread)
        threads_names.append(thread.name)
    
    for thread in threads:
        thread.join()
    
    print("The runtime for each thread (Download):")
    for thread in threads_returns:
        print(str(threads_names[thread]) + ": " + str(threads_returns[thread]) + " sec  |  URL: " + urls[thread])


if __name__  == "__main__":
    start = time.time()
    main()
    end = time.time()
    total_time = end - start
    print("Toatl time of program is: " + str(total_time) + " sec")