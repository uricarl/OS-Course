import multiprocessing
import requests
import json


def downloader(i, url, queue):
    queue.put({i: len(json.dumps(requests.get(url).json()))})
    
def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
     
    jsons_strings_sum_total = 0
    processes = []
    queue = multiprocessing.Queue()

    for i, url in enumerate(urls):
        process = multiprocessing.Process(target= downloader, args=(i, url, queue))
        process.start()
        processes.append(process)
       
    for process in processes:
        process.join()
    

    for i in urls:
        next_in_line = queue.get()
        key = list(next_in_line)[0]
        jsons_strings_sum_total += next_in_line[key]
        print("Process " +  str(key) + " Downloaded " + str(next_in_line[key]) + " chars from " + urls[key])
   
    print("Total numbers of chars downloaded is " + str(jsons_strings_sum_total))

if __name__  == "__main__":
    main()
   