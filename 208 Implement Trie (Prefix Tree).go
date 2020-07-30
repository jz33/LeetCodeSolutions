/*
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
*/
type Node struct {
    isWord bool
    children map[rune]*Node
}

func newNode() *Node {
    return &Node{false, make(map[rune]*Node)}
}

type Trie struct {
    root *Node
}

/** Initialize your data structure here. */
func Constructor() Trie {
    return Trie{newNode()}
}


/** Inserts a word into the trie. */
func (this *Trie) Insert(word string)  {
    node := this.root
    for _, r := range word {
        _, existed := node.children[r]
        if !existed {
            node.children[r] = newNode()
        }
        node = node.children[r]
    }
    node.isWord = true
}


/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
    node := this.root
    for _, r := range word {
        child, existed := node.children[r]
        if !existed {
            return false
        }
        node = child
    }
    return node.isWord
}


/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
    node := this.root
    for _, r := range prefix {
        child, existed := node.children[r]
        if !existed {
            return false
        }
        node = child
    }
    return true
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
