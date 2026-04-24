class TrieNode:
    def __init__(self):
        self.child={}
        self.end=False
class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        node=self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch]=TrieNode()
            node=node.child[ch]
        node.end=True
    def search(self, word: str) -> bool:
        node=self.root
        for ch in word:
            if ch not in node.child:
                return False
            node=node.child[ch]
        return node.end
    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for ch in prefix:
            if ch not in node.child:
                return False
            node=node.child[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)