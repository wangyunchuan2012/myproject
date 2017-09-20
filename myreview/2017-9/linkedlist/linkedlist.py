class Node:
    def __init__(self, data):
        """
        初始化节点
        """
        self.data = data
        self.pnext = None

    def __repr__(self):
        return str(self.data)


class Linkedlist:
    def __init__(self):
        """
        初始化链表
        """
        self.length = 0
        self.head = None

    def is_empty(self):
        """
        判断链表是否为空
        """
        return self.length == 0

    def append(self, this_node):
        """
        向链表尾部添加值，如果是Node对象则直接添加，否则先转为node对象
        """
        if isinstance(this_node, Node):
            pass
        else:
            this_node = Node(data=this_node)
        if self.is_empty():
            self.head = this_node
        else:
            node = self.head
            while node.pnext:
                node = node.pnext
            node.pnext = this_node
        self.length += 1

    def insert(self, value, index):
        """
        向链表中插入
        :param value: 插入的值
        :param index: 插入的位置
        :return: None
        """
        if type(index) is int:
            if index > self.length:
                print("index value is out of range")
                return
            else:
                this_node = Node(data=value)      # 插入的节点
                current_node = self.head     # 头节点

                if index == 0:          # 如果插入的节点index为0，则他的pnext为之前的头结点
                    self.head = this_node
                    this_node.pnext = current_node
                    return

                while index-1:          # 如果插入的节点index不为0，将索引为index-1和index分开
                    current_node = current_node.pnext
                    index -= 1

                this_node.pnext = current_node.pnext      # 插入节点的下一个节点为index
                current_node.pnext = this_node            # index-1的下一个节点为插入的数据
                self.length += 1
                return
        else:
            print('index is not int!')
            return

    def delete(self, index):
        """
        删除链表中指定位置的节点
        :param index: 要删除位置的索引
        :return:
        """

        if type(index) is int:
            if index > self.length:
                print('index is out of range!')
                return
            else:
                if index == 0:
                    self.head = self.head.pnext
                else:
                    current_node = self.head
                    while index-1:
                        current_node = current_node.pnext
                        index -= 1
                    current_node.pnext = current_node.pnext.pnext
                    self.length += 1
                    return
        else:
            print('index value is not int!')

    def print_linked_list(self):
        """
        打印整个链表
        :return:
        """
        if self.is_empty():
            print('linked list is empty!')
        else:
            node = self.head
            print('Head---->', node.data, end=' ')
            while node.pnext:
                node = node.pnext
                print('---->', node.data, end=' ')
            print('---> None. Linked node finished!')

    def update(self, value, index):
        """
        修改指定位置的值
        :param value: 要修改的值
        :param index: 位置
        :return:
        """
        if type(index) is int:
            if index > self.length:
                print('index is out of range!')
                return
            else:
                this_node = Node(data=value)
                if index == 0:
                    this_node.pnext = self.head.pnext
                    self.head = this_node
                else:
                    current_node = self.head
                    while index-1:
                        current_node = current_node.pnext
                        index -= 1
                    this_node.pnext = current_node.pnext.pnext
                    current_node.pnext = this_node
                    return
        else:
            print('index value is not int!')
            return


    def get_value(self, index):
        """
        获取链表中某个位置的值
        :param index: 索引位置
        :return: int
        """
        if type(index) is int:
            if index > self.length:
                print('index is out of range!')
                return
            else:
                if index == 0:
                    return self.head.data
                else:
                    current_node = self.head
                    while index-1:
                        current_node = current_node.pnext
                        index -= 1
                    return current_node.pnext.data

    def get_length(self):
        """
        获取链表长度
        :return: int
        """
        current_node = self.head
        if current_node:
            i = 1
            while current_node.pnext:
                current_node = current_node.pnext
                i += 1
            return i
        else:
            return 0


    def clear(self):
        """
        清空链表
        :return:None
        """
        self.head = None
        self.length = 0
        print('clear the linked list finished!')


if __name__ == '__main__':
    node1 = Node(data='node1')
    node2 = Node(data='node2')
    linked_list = Linkedlist()
    linked_list.append(node1)
    linked_list.append(node2)
    linked_list.print_linked_list()
    linked_list.insert('abc', 2)
    linked_list.insert('bde', 0)
    linked_list.print_linked_list()
    linked_list.delete(0)
    linked_list.print_linked_list()
    linked_list.update(value='updata_test', index=2)
    linked_list.print_linked_list()
    print(linked_list.get_value(index=2))
    print(linked_list.get_length())