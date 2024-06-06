from matrix_operations import MatrixOperations

class MatrixLogicalOperations:
    def __init__(self, matrix_operations: MatrixOperations):
        self.matrix_operations = matrix_operations

    def apply_and_paste(self, index1, index2, target_column_index, operation):
        word1 = self.matrix_operations.read_word_by_index(index1)
        word2 = self.matrix_operations.read_word_by_index(index2)
        result_word = operation(word1, word2)
        self.matrix_operations.write_word_to_column(result_word, target_column_index)
        return self.matrix_operations.matrix
