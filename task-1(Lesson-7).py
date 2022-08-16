class Matrix:
    def _init_(self, array):
        self.matrix = array
        self.height = len(array)
        self.width = len(array[0])

    def _str_(self):
        return "\n".join(" ".join(str(str(self.matrix[i])[1:-1]).split(", ")) for i in range(self.height))

    def _add_(self, other):
        new_array = []
        for i in range(self.height):
            new_array.append([])
            for j in range(self.width):
                new_array[i].append((int(self.matrix[i][j]) + int(other.matrix[i][j])))
        return "\n".join(" ".join(str(str(new_array[i])[1:-1]).split(", ")) for i in range(self.height))


mm = Matrix([[31, 22], [37, 43], [51, 86]])
mm2 = Matrix([[18, 27], [9, 3], [51, 12]])
mm3 = mm + mm2
print(mm3)
