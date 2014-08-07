class strFind:
    def __init__(self, child, matrix):
        self.child = list(child)
        self.matrix = list(matrix)
        self.part_num = []
        self.part_list = []

    def part_match(self):
        matrix_len = len(self.matrix)
        child_len = len(self.child)
        matrix_part = []
        i = 0
        if self.part_list:
            return
        while i < matrix_len:
            i += 1
            matrix_part.append(self.child[0:i])

        for i in matrix_part:
            prefix = []
            postfix = []
            j = 1
            while j < len(i):
                prefix.append(''.join(i[0:j]))
                postfix.append(''.join(i[j:len(i)]))
                j += 1
            pre = set(prefix)
            post = set(postfix)
            self.part_num.append(len(''.join(pre & post)))
        j = 0
        for i in self.child:
            self.part_list.append(self.part_num[j])    
            j += 1

    def find(self):
        self.part_match()
        j = 0
        equals = 0
        for i in self.matrix:
            if i == self.child[j]:
                equals += 1
                j += 1
                if equals == len(self.child):
                    return True
            else:
                if equals:
                    move_num = equals - self.part_list[equals-1]
                else:
                    move_num = 1
                self.matrix = self.matrix[move_num:len(self.matrix)]
                if len(self.matrix) < len(self.child):
                    return False     

                return self.find()
