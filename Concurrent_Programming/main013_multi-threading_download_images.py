# Download Images (multi-threaded) # 3.63 s
import threading
import time
import requests


def get_urls():
    filename = 'coco_img_urls.txt'
    lines = open(filename, 'r').readlines() # list of urls
    lines = [line.strip() for line in lines]
    return lines


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[-1]
    img_file = open(f'images/{img_name}', "wb")
    img_file.write(img_bytes)
    img_file.close()
    print(f'{img_name} was downloaded...')


if __name__ == '__main__':
    start = time.perf_counter()
    img_urls = get_urls()[:100]
    # The threads list is used to keep track of all newly created threads
    threads = []
    for url in img_urls:
        t = threading.Thread(target=download_image, args=[url])
        t.start()
        threads.append(t)

    # wait for all threads to complete by calling the join() method
    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
