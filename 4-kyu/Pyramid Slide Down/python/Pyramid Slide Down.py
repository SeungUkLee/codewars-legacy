# My Solution using generator
def longest_slide_down(pyramid):
    pyramid = pyramid[::-1]
    current_line = pyramid[0]
    for next_line in pyramid[1:]:
        line_1 = [sum(x) for x in zip(current_line, next_line)]
        line_2 = [sum(x) for x in zip(current_line[1:], next_line)]
        current_line = [max(x) for x in zip(line_1, line_2)]
    return current_line[0]


# Best Practice & Clever
def longest_slide_down(p):
    res = p.pop()
    while p:
        tmp = p.pop()
        res = [tmp[i] + max(res[i],res[i+1])  for i in range(len(tmp))] 
    return res.pop()

# Best Practice & Clever 2
def back_slide(x, y):
    return [y[i] + max(x[i], x[i+1]) for i in range(len(y))]

def longest_slide_down(pyramid):
    return reduce(back_slide, reversed(pyramid))[0]


# ------

class Tree(object):
    value = summ = None
    left = right = None

    def __init__(self, value):
        self.value = value

def iter_pairs(level):
    it = iter(level)
    a, b = Tree(next(it)), Tree(next(it))
    while b.value is not None:
        yield a, b
        a, b = b, Tree(next(it, None))

def build_tree(pyramid):
    it = iter(pyramid)
    root = Tree(next(iter(next(it))))
    prev_level = iter([root])
    for level in it:
        tree_level = []
        parent = next(prev_level)

        for left_tree, right_tree in iter_pairs(level):
            tree_level.append(left_tree)

            parent.left = left_tree
            parent.right = right_tree
            parent = next(prev_level, None)

        tree_level.append(right_tree)
        prev_level = iter(tree_level)

    return root


def calc_max_sums(root):
    if root is None:
        return 0

    if root.summ is not None:
        return root.summ

    root.summ = root.value + max(calc_max_sums(root.left), calc_max_sums(root.right))
    return root.summ


def find_max_slide(root):
    if root is None:
        return 0

    if not (root.left and root.right):
        return root.value

    if root.left.summ >= root.right.summ:
        return root.value + find_max_slide(root.left)

    if root.left.summ < root.right.summ:
        return root.value + find_max_slide(root.right)


def longest_slide_down(pyramid):
    tree = build_tree(pyramid)
    calc_max_sums(tree)
    return find_max_slide(tree)
