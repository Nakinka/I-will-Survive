from matrix_operations import MatrixOperations

class MatchingOperations:
    @staticmethod
    def add_fields_for_matching_v(matrix_operations: MatrixOperations, v_key):
        for column_index in range(len(matrix_operations.matrix[0])):
            word = matrix_operations.read_word_by_index(column_index)
            v_field = int(word[:3], 2)
            a_field = int(word[3:7], 2)
            b_field = int(word[7:11], 2)

            if v_field == int(v_key, 2):
                result = a_field + b_field
                new_s_field = format(result, '05b')
                new_word = word[:11] + new_s_field
                matrix_operations.write_word_to_column(new_word, column_index)

        return matrix_operations.matrix
