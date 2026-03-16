#!/usr/bin/env python3
"""Radix tree — compressed trie for strings."""
class RadixNode:
    def __init__(self,label=""): self.label=label;self.children={};self.is_end=False
class RadixTree:
    def __init__(self): self.root=RadixNode()
    def insert(self,word):
        node=self.root;i=0
        while i<len(word):
            found=False
            for key in list(node.children):
                child=node.children[key];j=0
                while j<len(child.label) and i+j<len(word) and child.label[j]==word[i+j]: j+=1
                if j==0: continue
                if j==len(child.label): node=child;i+=j;found=True;break
                # Split
                new=RadixNode(child.label[:j]);new.children[child.label[j]]=child
                child.label=child.label[j:];node.children[key]=new;del node.children[key]
                node.children[word[i]]=new
                if i+j<len(word):
                    leaf=RadixNode(word[i+j:]);leaf.is_end=True;new.children[word[i+j]]=leaf
                else: new.is_end=True
                return
            if not found:
                leaf=RadixNode(word[i:]);leaf.is_end=True;node.children[word[i]]=leaf;return
        node.is_end=True
    def search(self,word):
        node=self.root;i=0
        while i<len(word):
            found=False
            for key in node.children:
                child=node.children[key]
                if word[i:i+len(child.label)]==child.label:
                    node=child;i+=len(child.label);found=True;break
            if not found: return False
        return node.is_end
def main():
    rt=RadixTree()
    for w in ["test","testing","team","toast"]: rt.insert(w)
    print(f"test:{rt.search('test')}, tea:{rt.search('tea')}, team:{rt.search('team')}")
if __name__=="__main__":main()
