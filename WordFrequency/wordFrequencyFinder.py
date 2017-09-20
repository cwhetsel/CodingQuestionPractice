# Question: Design a method to find the frequency of occurences of any given word in a book. What if we were running this agorithm multiple times?
# Time: 10 min
# Complexity: O(n) where n is the number of words in your file for the initial setup. Looking up frequency is O(1) after.
# 9/20/19
# 
# First thought: read every word in the "book" or text file and compare if it is the word we are counting. 
# If we are running it multiple times, depending on how many times, it may be worth counting every word in the book on the first 
# go through. Then any subsequent time the method is called, it can be looked up in a hash table in constant time. 
# 

class WordFrequencyFinder():
    def __init__(self, book: "list of strings"):
        self.book = book
        self.freq = {'a': 0}
    

    def __intiFreq__(self):
        for word in self.book:
            word.lower()
            word.strip()
            if word in self.freq:
                self.freq[word] += 1
            else:
                self.freq[word] = 1
    
    def getFrequency(self, word):
        if word in self.freq:
            return self.freq[word]; 
        else:
            return 0

book = ["String", "Word", "Carrot", "Carrot", "This", "Is", "A" "Bad", "Book"]
finder = WordFrequencyFinder(book)
finder.__intiFreq__()

freq = finder.getFrequency(book[1])
print("Word: %d" % (freq))

freq = finder.getFrequency(book[2])
print("Carrot: %d" % (freq))
    