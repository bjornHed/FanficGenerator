import editdistance
import sys

text = "hiy were soiekiig an the saik, herdione  soe paid and she peater the saale and the seat whse the siat oe thing to the moaker bnors and then hed hesd oo the siat hn the corriror  and they were soieking ano hir hend and the seat whse the siat oe thing to the moaker bnors and then hed hesd oo the siat hn the corriror  and they were soieking ano hir hend and the seat whse the siat oe thing to the moaker bnors and then hed hesd oo the siat hn the corriror  and they were soieking ano hir hend and the seat whse the siat oe thing to the moaker bnors and then hed hesd oo the siat hn the corriror  and they were soieking ano hir hend and the seat whse the siat oe thing to the moaker bnors and then hed hesd oo the siat hn the corriror  and they were soieking ano hir hend and the seat whse the siat oe thing to the moaker bnors and then hed hesd oo the siat hn the corriror  and they were soieking ano hir hend and the seat whse the siat oe thing to the moaker bnors and then hed hesd oo the siat hn th"

def create_dictionary(text):
    table = {}
    words = text.split(" ")
    for w in words:
        if w not in table:
            table[w] = 1
        else:
            table[w] += 1
    return table

def spellcheck_word(word, dictionary):
    words = dictionary.keys()
    distances = []

    for w in words:
        distances += [editdistance.eval(word,w)]
    index = distances.index(min(distances))
    return list(dictionary.keys())[index]

def correct_text(text, dictionary):
    lines = text.splitlines()
    words = []
    for line in lines:
        words += line.split(" ")
    new_text = []
    for w in words:
        new_text += [spellcheck_word(w,dictionary)]
    return new_text


if __name__ == "__main__":
    # execute only if run as a script
    
    content = open("text.txt").read()    
    wordDict = create_dictionary(content)

    generatedContent = open("gen.txt").read()
    
    sys.stdout.write(" ".join(correct_text(generatedContent, wordDict)))
    