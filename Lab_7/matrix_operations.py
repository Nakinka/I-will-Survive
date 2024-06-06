class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix

    def read_word_by_index(self, column_index):
        word = ""
        for row_index in range(len(self.matrix)):
            if row_index + column_index < len(self.matrix):
                word += str(self.matrix[row_index + column_index][column_index])
            else:
                word += str(self.matrix[row_index + column_index - len(self.matrix)][column_index])
        return word

    def write_word_to_column(self, word, column_index):
        for row_index in range(len(self.matrix)):
            if row_index + column_index < len(self.matrix):
                self.matrix[row_index + column_index][column_index] = int(word[row_index])
            else:
                self.matrix[row_index + column_index - len(self.matrix)][column_index] = int(word[row_index])
        return self.matrix

    def find_word(self, word):
        if len(word) != len(self.matrix[0]):
            return None

        for column_index in range(len(self.matrix[0])):
            word_in_matrix = self.read_word_by_index(column_index)
            if word_in_matrix == word:
                return (column_index, column_index)
        return None

    def print_matrix(self):
        for row in self.matrix:
            print(row)
