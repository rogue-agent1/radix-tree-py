"""Radix Tree (Patricia Trie) — compressed prefix tree."""
class RadixNode:
    def __init__(self, prefix="", is_end=False):
        self.prefix = prefix; self.children = {}; self.is_end = is_end

class RadixTree:
    def __init__(self): self.root = RadixNode()
    def insert(self, word):
        node = self.root
        while word:
            found = False
            for key in list(node.children):
                cp = self._common_prefix(word, key)
                if not cp: continue
                if cp == key:
                    word = word[len(cp):]; node = node.children[key]; found = True; break
                child = node.children.pop(key)
                split = RadixNode(cp)
                split.children[key[len(cp):]] = child
                if len(cp) == len(word):
                    split.is_end = True
                else:
                    split.children[word[len(cp):]] = RadixNode(word[len(cp):], True)
                node.children[cp] = split; return
            if not found:
                node.children[word] = RadixNode(word, True); return
        node.is_end = True
    def _common_prefix(self, a, b):
        i = 0
        while i < len(a) and i < len(b) and a[i] == b[i]: i += 1
        return a[:i]
    def search(self, word):
        node = self.root
        while word:
            found = False
            for key in node.children:
                if word.startswith(key):
                    word = word[len(key):]; node = node.children[key]; found = True; break
            if not found: return False
        return node.is_end

if __name__ == "__main__":
    rt = RadixTree()
    for w in ["test","testing","tester","team","tea"]:
        rt.insert(w)
    assert rt.search("test") and rt.search("testing") and rt.search("tea")
    assert not rt.search("tes") and not rt.search("teax")
    print("Radix tree: all lookups correct")
    print("All tests passed!")
