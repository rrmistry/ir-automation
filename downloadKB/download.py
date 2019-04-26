# Python 3.6.7

import os
import wikipedia
import multiprocessing

# Get Current File Path (If downloading to local repo)
dir_path = os.path.dirname(os.path.realpath(__file__))

# Set Dataset Path (If downloading external to this repo)
dir_path = 'D:/datasets/Wikipedia/IFRS_17'

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
              "Process:", os.getpid())
        return

    try:
        filePath = BASE_PATH + wikipediaPage.title + ".txt"
        if not os.path.exists(path=filePath):
            with open(filePath, "w+") as text_file:
                print("Downloading:", wikipediaPage.title,
                      "|",
                      "Process:", os.getpid())
                text_file.write(wikipediaPage.content)
        else:
            print("Skipping:", wikipediaPage.title,
                  "|",
                  "Process:", os.getpid())
    except Exception as e:
        print("Exception occurred:", str(e),
              "|",
              "Process:", os.getpid())

    # Measure Depth
    if depth > DEPTH_LIMIT:
        return

    processes = []

    # Apply recursion in parallel
    for link in wikipediaPage.links:
        downloadRecursive(pageTitle=link, depth=depth+1)
        process = multiprocessing.Process(target=downloadRecursive, args=(link, depth))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

if __name__ == "__main__":
    downloadRecursive(BASE_PAGE)
