from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.value = val
        self.left_child = left
        self.right_child = right

root = TreeNode('A')
root.left_child = TreeNode('B')
root.right_child = TreeNode('C')
root.left_child.left_child = TreeNode('D')
root.left_child.right_child = TreeNode('E')
root.right_child.left_child = TreeNode('F')
root.right_child.right_child = TreeNode('G')


def bfs(root: TreeNode) -> None:
    q = deque()
    if root:
        q.append(root)

    while q:
        for _ in range(len(q)):
            node: TreeNode = q.popleft()

            if node is not None:
                print(node.value, end=', ')
                if node.left_child is not None:
                    q.append(node.left_child)
                if node.right_child is not None:
                    q.append(node.right_child)



bfs(root)