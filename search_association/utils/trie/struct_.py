"""
前缀树
https://oi-wiki.org/string/trie/
https://pdai.tech/md/algorithm/alg-basic-tree-trie.html
利用词典的公共前缀减少查询时间，减少字符串比较次数

前缀树 vs 哈希树
"""

class BooleanResponse:
    def __init__(self, flag=False, data=None):
        self.flag = flag
        self.data = data



class TrieNode:
    def __init__(self):
        # 是否是某个单词的末尾字符
        self.is_end = False
        # 字典用于记录节点的子节点,以字符作为key，子节点作为value
        self.children = {}


    def add_child_node(self, ch):
        """
        判断
        :param node:
        :return:
        """
        self.children[ch] = TrieNode()



class TrieTree:
    """
    经过索引的字符串集合
    """
    root = None

    def __init__(self):
        self.root = TrieNode()

    @classmethod
    def from_word_list(cls, word_list):
        # 构造Trie树
        tree = TrieTree()
        for word in word_list:
            tree.insert(word)
        return tree

    def insert(self, word):
        """
        将单词加入字符串集合
        :param word:
        :return:
        """
        # TODO 特殊情况处理，word为空或者为其他对象（不可迭代）
        if word is None or word == "":
            return
        assert isinstance(self.root, TrieNode)
        cur_node = self.root
        for ch in word:
             # 如果未识别到ch边，则新增
            if cur_node.children.get(ch, None) is None:
                cur_node.add_child_node(ch)
            # 如果识别到/新增ch边，则将当前节点指向下一节点
            cur_node = cur_node.children[ch]
        # 标记为词尾
        cur_node.is_end = True

    def search(self, word):
        """
        查询单词是否在字符串集合中
        :param word:
        :return:
        """
        pass

    def has_prefix(self, prefix):
        """
        是否有prefix作为前缀的字符串，若无，返回False，若有，返回True以及prefix末尾所在节点
        :param prefix:
        :return:
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            else:
                node = node.children[ch]
                continue

        return True

    def startwith(self, keyword):
        """
        返回以keyword为前缀的字符串列表
        :param keyword:
        :return:
        """
        result_list = []
        node = self.root
        for ch in keyword:
            if ch not in node.children:
                return []
            else:
                node = node.children[ch]
                continue
        # 到这里还没返回，说明找到
        # 便利子节点，返回所有候选字符串
        def dfs(node, prefix=""):
            """
            返回以prefix作为前缀的字符串列表
            :param node:
            :return:
            """
            if len(node.children) == 0:
                result_list.append(prefix)
            elif node.is_end:
                result_list.append(prefix)
            for child_char in node.children:
                dfs(node.children[child_char], prefix + child_char)
        dfs(node, keyword)
        return result_list









    def plot(self):
        """
        TODO: Trie树可视化
        :return:
        """
        pass

if __name__ == "__main__":
    # 测试用例
    word_list_test = ["塞尔达公主","塞尔达","《塞尔达公主》", "《异度神剑","《xxxx》", "人鱼传说", "人鱼故事", "人传说", "塞尔达传说2", "塞尔达传说"]
    t = TrieTree.from_word_list(word_list_test)
    print(t.startwith("塞尔达"))
    print(t.startwith("人鱼"))
    print(t.startwith("人"))
    print(t.startwith("《人鱼"))
    print(t.startwith("《"))