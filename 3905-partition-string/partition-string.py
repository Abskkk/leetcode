class TrieNode:
    def __init__(self, letter='', children=None, seen=False):
        self.letter = letter
        self.children = children if children != None else {}
        self.seen = seen

class Solution:
    def partitionString(self, s: str) -> List[str]:
        root = TrieNode()
        curr = root
        res = []
        currSeg = []
        for ch in s:
            currSeg.append(ch)
            node = TrieNode(ch)
            if ch not in curr.children:
                curr.children[ch] = node
            curr = curr.children[ch]
            if not curr.seen:
                res.append(''.join(currSeg))
                currSeg = []
                curr.seen = True
                curr = root
        return res
            
        