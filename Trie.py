
# insert(word): Inserts a new word into the trie
# search(word):  Returns true or false if the word is found in the trie
# startsWith(prefix): Returns true or false if any word in the trie begins with prefix

# [“a”,”are”,”as”,”do”,”dot”,”new”,”news”,”no”,”not”,”zen”]

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.is_end = False 
        self.children = {}


class Trie:
    
    def __init__(self, words=[]):
        self.root = TrieNode("")
        
        if words:
            for word in words:
                self.insert(word)
    
    def insert(self, word):
        node = self.root
        
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode(val=letter)
            node = node.children[letter]
        
        node.is_end = True
        
    
    def search(self, word):
        node = self.root
        
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        
        return node.is_end
            
    # news -> new
    def startsWith(self, prefix):
        node = self.root
        
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        
        return True


trie = Trie(["are", "as", "no", "not", "news", "zen"])

trie.insert("foo")

print(trie.search("news"))
print(trie.search("new"))

print(trie.startsWith("news"))