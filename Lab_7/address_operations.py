class AddressOperations:
    @staticmethod
    def adres_row(matrix, number):
        print("Адреса столбцов:")
        for column_index in range(len(matrix[0])):
            if (column_index + number <= 15):
                print(matrix[column_index + number][column_index], end="")
            else:
                print(matrix[column_index + number - 16][column_index], end="")
