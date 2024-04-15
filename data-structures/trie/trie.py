class TrieNode:
    def __init__(self, value: str):
        self.valye = value
        self.children = {}
        self.is_end_of_word = False

    def add(self, word: str, node: 'TrieNode' = None):
        if not word:
            node.is_end_of_word = True
            return

        char = word[0]

        if char not in node.children:
            node.children[char] = TrieNode(char)

        self.add(word[1:], node.children[char])

    def find(self, word: str, node: 'TrieNode' = None):
        if not node:
            return False

        if not word:
            return node.is_end_of_word

        char = word[0]

        if char in node.children:
            return self.find(word[1:], node.children[char])

        return False

    def delete(self, word: str, node: 'TrieNode' = None):
        if not node:
            return
        # we exhausted the characters, since a node exists, we mark is as
        # not end of word anymore
        if not word:
            node.is_end_of_word = False
            return

        # next char is not present - trying to delete a word that doesn't exist
        if not word[0] in node.children:
            return
        # move to next char to delete
        return self.delete(word[1:], node.children[word[0]])


class Trie:
    root = TrieNode("")

    def add(self, word: str):
        return self.root.add(word, self.root)

    def find(self, word: str) -> bool:
        return self.root.find(word, self.root)

    def delete(self, word: str):
        return self.root.delete(word, self.root)
