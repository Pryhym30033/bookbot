def Words (book):
    finalcount = []
    words = book.split()
    return words

def LetterCount (words):
    letterTotal ={}
    for word in words:
        for letter in word:
            low = letter.lower()
            if low in letterTotal:
                letterTotal[low] = letterTotal[low] + 1
            else:
                letterTotal[low] = 1

    return letterTotal

def dictSort (dict):
    return dict["count"]


def report (file):
    wordCount = Words(file)
    letters = LetterCount(wordCount)  
    letterList = []

    for letter in letters:
        if letter.isalpha():
            letterList.append({"let":letter, "count":letters[letter]}) 

    letterList.sort(reverse=True, key=dictSort)
    
    print("----- Book report begins -----")
    print(f"{len(wordCount)} words found in the document\n")

    for lib in letterList:
        print(f"The '{lib["let"]}' character was found {lib["count"]} times")
    


def main():

    with open("/home/pryhym/workspace/github.com/Pryhym30033/bookbot/books/frankenstein.txt") as f:
        file_contents =f.read()

    report(file_contents)
    
main()
