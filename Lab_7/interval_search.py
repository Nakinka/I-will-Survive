from matrix_operations import MatrixOperations

class IntervalSearch:
    @staticmethod
    def search_values_in_interval(matrix_operations: MatrixOperations, lower_bound, upper_bound):
        result_flags = [1] * len(matrix_operations.matrix[0])
        for column_index in range(len(matrix_operations.matrix[0])):
            word = matrix_operations.read_word_by_index(column_index)
            if int(word, 2) < int(upper_bound, 2):
                result_flags[column_index] = 1
            else:
                result_flags[column_index] = 0

        for column_index in range(len(matrix_operations.matrix[0])):
            word = matrix_operations.read_word_by_index(column_index)
            if int(word, 2) > int(lower_bound, 2) and result_flags[column_index] == 1:
                result_flags[column_index] = 1
            else:
                result_flags[column_index] = 0

        return [i for i, flag in enumerate(result_flags) if flag == 1]
