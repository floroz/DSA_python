from trie import Trie


def test_insert_word():
    trie = Trie()
    trie.add("hello")
    assert trie.find("hello") is True


def test_delete_word():
    trie = Trie()
    trie.add("hello")
    trie.delete("hello")
    assert trie.find("hello") is False


def test_not_find_word():
    trie = Trie()
    trie.add("hello")
    assert trie.find("hello") is True
    assert trie.find("world") is False


def test_delete_prefix_word():
    trie = Trie()
    trie.add("hello")
    trie.add("helloworld")
    assert trie.find("hello") is True
    trie.delete("hello")
    assert trie.find("hello") is False
    assert trie.find("helloworld") is True


def test_insert_multiple_words():
    trie = Trie()
    trie.add("hello")
    trie.add("world")
    trie.add("helloworld")
    assert trie.find("hello") is True
    assert trie.find("world") is True
    assert trie.find("helloworld") is True


def test_delete_multiple_words():
    trie = Trie()
    trie.add("hello")
    trie.add("world")
    trie.add("helloworld")
    trie.delete("hello")
    trie.delete("world")
    trie.delete("helloworld")
    assert trie.find("hello") is False
    assert trie.find("world") is False
    assert trie.find("helloworld") is False


def test_delete_prefix_words():
    trie = Trie()
    trie.add("hello")
    trie.add("helloworld")
    trie.delete("hello")
    assert trie.find("hello") is False
    assert trie.find("helloworld") is True


def test_delete_prefix_words2():
    trie = Trie()
    trie.add("hello")
    trie.add("helloworld")
    trie.delete("helloworld")
    assert trie.find("hello") is True
    assert trie.find("helloworld") is False
