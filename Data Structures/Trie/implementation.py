import random
class TrieNode:
    def __init__(self,char):
        # Character stored in this node
        self.char = char

        # A flag that marks if the word ends on this particular node.
        self.end_of_word = False

        # A dictionary of child nodes where the keys are the characters (letters) 
        # and values are the nodes
        self.children = {}
    
class Trie:

    def __init__(self):
        """
        The root node of a trie is empty and does not store any character.
        """
        self.root = TrieNode("")

    def Insert (self, string):
        """Insert a string i.e a word into the trie"""
        node = self.root

        # Check each character in the string 
        # If none of the children of the current node contains the character, 
        # create a new child of the current node for storing the character.
        for char in string:
            if char in node.children:
                node = node.children[char]
            else:
                # As the character is not found, create a new trie node
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a word
        node.end_of_word = True 

    def delete(self,string):
        
 T without s {
search the compressed trie for s

if s is not found then
 return False

else

 let u be the node where s was found
 if s is not equal to the whole string ended at u or u has a child
  return False // we cannot delete an internal node
 let v be the parent of u
 delete u

 if v has a child c then

  // p.string denotes the string stored at a node p

  v.string ← v.string + c.string

  delete node c // merg*e v and c into a single node

 return True // successful deletion