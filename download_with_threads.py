import threading
import requests
import json


def downloader(i, url, jsons_strings_len):
    jsons_strings_len[i] = len(json.dumps(requests.get(url).json()))
    
def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
     
    jsons_strings_lens = {}
    threads = []
    jsons_strings_sum_total = 0
    
    for i, url in enumerate(urls):
        thread = threading.Thread(target= downloader, args=(i, url, jsons_strings_lens))
        thread.start()
        threads.append(thread)
        
    for thread in threads:
        thread.join()
    
    for i in jsons_strings_lens:
        print("Thread " +  str(i) + " Downloaded " + str(jsons_strings_lens[i]) + " chars from " + urls[i])
        jsons_strings_sum_total += jsons_strings_lens[i]


    print("Total numbers of chars downloaded is " + str(jsons_strings_sum_total))

if __name__  == "__main__":
    main()
   