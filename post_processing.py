import editdistance

def create_dictionary(text):
    table = {}
    words = text.split(" ")
    for w in words:
        if w not in table:
            table[w] = 1
        else:
            table[w] += 1
    return table

def spellcheck_word(word,dictionary):
    words = dictionary.keys()
    distances = []
    for w in words:
        distances += editdistance.eval(word,w)
    index = distances.index(max(distances))
    return words[index]

def correct_text(text,dictionary):
    lines = text.splitlines()
    words = []
    for line in lines:
        words += line.split(" ")
    new_text = []
    for w in words:
        new_text += [spellcheck_word(w,dictionary)]
    return new_text
