# Python 3.6.7

import os
import wikipedia
import threading

# Get Current File Path
dir_path = os.path.dirname(os.path.realpath(__file__))

# Allows to call this python file from anywhere
BASE_PATH = dir_path + "/dataset/"

BASE_PAGE = "IFRS_17"

DEPTH_LIMIT = 2

def downloadRecursive(pageTitle, depth=0):
    try:
        wikipediaPage = wikipedia.page(title=pageTitle)
    except Exception as e:
        print("Exception occurred:", str(e),
              "|",
              "Thread:", threading.get_ident())
        return

    try:
        filePath = BASE_PATH + wikipediaPage.title + ".txt"
        if not os.path.exists(path=filePath):
            with open(filePath, "w+") as text_file:
                print("Downloading:", wikipediaPage.title,
                      "|",
                      "Thread:", threading.get_ident())
                text_file.write(wikipediaPage.content)
        else:
            print("Skipping:", wikipediaPage.title,
                  "|",
                  "Thread:", threading.get_ident())
    except Exception as e:
        print("Exception occurred:", str(e),
              "|",
              "Thread:", threading.get_ident())

    # Measure Depth
    depth = depth + 1
    if depth > DEPTH_LIMIT:
        return

    threads = []

    # Apply recursion in parallel
    for link in wikipediaPage.links:
        downloadRecursive(pageTitle=link, depth=depth)
        thread = threading.Thread(target=downloadRecursive, args=(link, depth))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    downloadRecursive(BASE_PAGE)
