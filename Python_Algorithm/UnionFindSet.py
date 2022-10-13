input_set = [[0,1],[2,3],[4,6],[2,5],[5,4],[1,6],[10,11],[7,9],[8,10],[7,11]]

class UnionFindSet(object):
    def __init__(self, relation_list):
        self.father_dict = {}
        self.size_dict = {}

        for node in relation_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1
    
    def find(self, node):
        father = self.father_dict[node]
        if(node != father):
            if(father != self.father_dict[father]):
                self.size_dict[father] -= 1
            father = self.find(father)
        
        self.father_dict[node] = father
        return father


    def union(self, node_1, node_2):
        if node_1 is None or node_2 is None:
            return
        
        head_1 = self.find(node_1)
        head_2 = self.find(node_2)

        if(head_1 != head_2):
            set1_size = self.size_dict[head_1]
            set2_size = self.size_dict[head_2]
            if(set1_size >= set2_size):
                self.father_dict[head_2] = head_1
                self.size_dict[head_1] = set1_size + set2_size
            else:
                self.father_dict[head_1] = head_2
                self.size_dict[head_2] = set1_size + set2_size

    def get_root(self):
        root_list = []
        for i in range(len(self.father_dict)):
            if(self.father_dict[i] == i):
                root_list.append(i)
        return root_list

local_max = 0
for i in input_set:
    if max(i) > local_max:
        local_max = max(i)

ufs = UnionFindSet(range(local_max+1))

for i in input_set:
    ufs.union(i[0], i[1])

print(ufs.get_root())