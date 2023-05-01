class Solution:
    def duplicateSubtreeNaryTree(self, root):
        subtrees_count = {}
        
        def find_duplicate_subtrees(root):
            if root is None:
                return ""
            
            subtree_str = root.__str__()
            
            for child in root.children:
                subtree_str = subtree_str + "#" + find_duplicate_subtrees(child)
            
            subtrees_count[subtree_str] = subtrees_count.get(subtree_str, 0) + 1
            
            return subtree_str
        
        find_duplicate_subtrees(root)
        
        duplicate_count = 0
        for count in subtrees_count.values():
            if count > 1:
                duplicate_count += 1
        
        return duplicate_count