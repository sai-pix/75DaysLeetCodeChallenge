class Trie:
    def __init__(self):
        self.child={}
        self.end=False
class WordDictionary:
    
    def __init__(self):
        self.root=Trie()
        
    def addWord(self, word: str) -> None:
        node=self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch]=Trie()
            node=node.child[ch]
        node.end=True
    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i==len(word):
                return node.end
            ch=word[i]
            if ch!='.':
                if ch not in node.child:
                    return False
                return dfs(node.child[ch],i+1)
            for child in node.child.values():
                if dfs(child,i+1):
                    return True
            return False
        return dfs(self.root,0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)