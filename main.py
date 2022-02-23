from english_words import english_words_set

def chronWords(text, minLength):
    wordList = []
    chronFunc("", text, wordList, minLength)
    wordList.sort()
    return wordList

def chronFunc(startLetters, text, wordList, minLength):
        index = 0
        temp = ""
        stored = startLetters
        for letter in text:
            index = index + 1
            temp = chronFunc(startLetters + letter, text[index:], wordList, minLength)
            if len(temp) >= minLength and temp in english_words_set and temp not in wordList:
                wordList.append(temp)
                stored = temp
        return stored

print(chronWords("unions", 3))