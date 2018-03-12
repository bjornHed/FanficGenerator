from urllib.request import urlopen
from os import path
import json
import editdistance

TEXT_URL = "https://archive.org/stream/Book5TheOrderOfThePhoenix/Book%201%20-%20The%20Philosopher's%20Stone_djvu.txt"
SAVED_TEXT_PATH = "text.txt"


def fetchText(url):
    with urlopen(url) as response:
        return response.read().decode('utf-8')


def clean(text):
    startStr = '<pre>'
    start = text.index(startStr)
    end = text.index('</pre>')
    clean = text[start + len(startStr):end]
    clean = clean.splitlines()
    clean = list(filter(lambda x: not x.startswith("Page"), clean))
    clean = "".join(clean)
    clean = clean.lower()
    clean = filter(lambda c: not c in "-—\"”“■•\\/()", clean)
    return "".join(clean)


def uniqueChars(text):
    table = {}
    for c in text:
        if c not in table:
            table[str(c)] = 1
        else:
            table[str(c)] += 1
    return table


def doMachineLearning(text):
    pass


def main():
    if path.exists(SAVED_TEXT_PATH):
        text = open(SAVED_TEXT_PATH).read()
    else:
        text = fetchText(TEXT_URL)
        textfile = open(SAVED_TEXT_PATH, "w+")
        text = clean(text)
        textfile.write(text)
    frequencyCount = uniqueChars(text)
    print(json.dumps(frequencyCount, sort_keys=True, indent=4))
    print("Unique char count: %d" % len(frequencyCount))


if __name__ == "__main__":
    # execute only if run as a script
    main()
