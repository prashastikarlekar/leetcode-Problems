from collections import defaultdict  # Default dict to avoid key error while inserting

class TrieNode:
    def _init_(self, end_of_string=False):
        """
        This class implements a single node
        of a compressed trie that we are going to
        implement.        
       
          end_of_string: True if the current node represents end of any string else False
        """
        self.end_of_string = end_of_string
        self.children = defaultdict(TrieNode)


class CompressedTrie:
    def _init_(self):
        self.root = TrieNode()
    
    def __insert_word(self, word):
        """
        To insert a word in the Trie data structure.
        
        Input:
          word: a string containing characters
        """
        current = self.root
        for i, char in enumerate(word):
            current = current.children[char]
            if i == len(word) - 1:
                current.end_of_string = True
    
    def __compress_trie(self, node, prefix=''):
        """
        Compresses this trie into another object, ie. collapses each sequence
        of non-terminal nodes with one child into a single nodes whose key is
        concatenation of the original keys.
        The method is idempotent, ie. calling it repeatedly produces the same
        result.
        The implementation is recursive (first a top-down pass, then bottom-up
        backtracking).
        Compresses a (sub)trie with given key prefix. In the top-down pass
        the original keys in single-child sequences are concatenated and in
        the backtracking the result is returned back.
        
        Input:
          node: current Node object involved in recursion
          prefix: prefix of the current non-terminal string
        
        Returns:
          res_node: Node object representing new child node
          key: str which contains new information to be added as child
        """
        children, end_of_string = node.children, node.end_of_string
        if len(children)==0:
            return node, prefix
        elif len(children)==1:
            for key, child in children.items():
                nxt = key if end_of_string else prefix + key
                n_child, n_key = self.__compress_trie(child, nxt)
                if prefix == '' or end_of_string:
                    res_node = TrieNode(n_child.end_of_string or end_of_string)
                    res_node.children[n_key] = n_child
                else:
                    res_node = n_child
                    res_node.end_of_string = res_node.end_of_string or end_of_string
                return res_node, prefix if end_of_string else n_key
        else:
            new_children = defaultdict(TrieNode)
            for key, child in children.items():
                n_child, n_key = self.__compress_trie(child, key)
                new_children[n_key] = n_child
            res_node = TrieNode(end_of_string)
            res_node.children = new_children
            return res_node, prefix
    
    def build_trie(self, words):
        """
        This function is utility for client functions to utilize
        the data structure. It builds compressed trie with words.
        
        Input:
          words: list of strings containing word
        """
        for word in words:
            self.__insert_word(word)
        self.root, _ = self.__compress_trie(self.root, '')
    
    def __deletion_utility(self, node, word, index):
        """
        This is a utility method which recursively deletes a word
        from compressed trie.
        
        Input:
          node: current node inside trie
          word: string to be deleted
          index: current index of the string
        
        Returns: True if child key needs deletion else False
        """
        keys = list(node.children.keys())
        for key in keys:
            if key not in node.children:
                continue
            if word[index:].startswith(key):
                l = len(key)
                if index + l == len(word):
                    node.children[key].end_of_string = False
                    if len(node.children[key].children)>0:
                        return False
                    del node.children[key]
                    if len(node.children)>0:
                        return False
                    return True
                toDelete = self.__deletion_utility(node.children[key], word, index+l)
                if toDelete:
                    del node.children[key]
                if len(node.children)>0:
                    return False
                return True
        return False
                
    def delete_word(self, word):
        """
        This method is user consumable method with which
        the client function can delete any string from
        compressed trie.
        
        Input:
          word: string to be deleted
        """
        if len(word)>0:
            self.__deletion_utility(self.root, word, 0)
    
    def collect_stored_words(self):
        """
        This method traverse the Trie data structure recursively
        and collect all the words stored inside.
        
        Returns: list of strings
        """
        words = set()
        def recursive_utility(node, prefix):
            nonlocal words
            if node.end_of_string:
                words.add(prefix)
            for key, child in node.children.items():
                recursive_utility(child, prefix + key)
        recursive_utility(self.root, '')
        return list(words)



if __name__=='__main__':
    # Test case: 1
    print('###### Test Case: 1 ######')
    words = ['tiger', 'eat', 'tea', 'meat', 'tigeress', 'eaten']
    wordToDelete = 'eat'
    print('Words in Testcase: {}'.format(words))
    print('Word to Delete: {}'.format(wordToDelete))
    cTrie = CompressedTrie()
    cTrie.build_trie(words)
    print('Building Trie...')
    print('Words in Trie before deletion: {}'.format(cTrie.collect_stored_words()))
    print('Deleting word: {}'.format(wordToDelete))
    cTrie.delete_word(wordToDelete)
    print('Words in Trie after deletion: {}'.format(cTrie.collect_stored_words()))
    print()
    
    # Test case: 2
    print('###### Test Case: 2 ######')
    words = ['tiger', 'eat', 'tea', 'meat', 'tigeress', 'eaten']
    wordToDelete = 'tea'
    print('Words in Testcase: {}'.format(words))
    print('Word to Delete: {}'.format(wordToDelete))
    cTrie = CompressedTrie()
    cTrie.build_trie(words)
    print('Building Trie...')
    print('Words in Trie before deletion: {}'.format(cTrie.collect_stored_words()))
    print('Deleting word: {}'.format(wordToDelete))
    cTrie.delete_word(wordToDelete)
    print('Words in Trie after deletion: {}'.format(cTrie.collect_stored_words()))
    print()