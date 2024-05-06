
import csv

class WordBreak(object):
    def word_break(self, s, wordDict):
        
        # initializing our TrieNode class
        class TrieNode(object):
            def __init__(self):
                self.children = []
                self.leafNode = False

            # implementing the method for getting a 
            # TrieNode from our implemented TrieNode 
            def getTrieNode(self):
                temp = TrieNode()
                temp.children = []
                
                # 26 represents the number 
                # of alphabets present 
                # in the English
                for i in range(26):
                    temp.children.append(None)
                temp.leafNode = False
                return temp

            # to search a node into our TrieNode
            def search(self, root, x):
                tNode = root
                for i in x:
                    idx = ord(i)-97
                    if(tNode.children[idx] == None):
                        return False
                    tNode = tNode.children[idx]
                if(tNode and tNode.leafNode):
                    return True

            # to insert a TrieNode into our Trie
            def insertTrieNode(self, root, x):
                x = str(x)
                tNode = root
                for i in x:
                    index = ord(i)-97
                    if(tNode.children[index] == None):
                        # node has to be initialised
                        tNode.children[index] = self.getTrieNode()
                    tNode = tNode.children[index]
                tNode.leafNode = True # marking end of word

        
        # this function checks if it is possible 
        # to do a wordbreak
        def isPossibleWordBreak(strr, root):
            l = len(strr)
            if(l == 0):
                return True
            for i in range(1, l+1):
                if(root.search(root, strr[:i]) and isPossibleWordBreak(strr[i:], root)):
                    return True
            return False
        
#driver code
for i in str:
if i == ' ':
	i='\0'
        
with open('anctamDict.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# creating object of WordBreak() class
ob = WordBreak()
# displaying results
ans = ob.wordBreak(str,data)

