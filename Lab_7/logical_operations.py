class LogicalOperations:
    @staticmethod
    def perform_disjunction(word1, word2):
        return ''.join(str(int(a) or int(b)) for a, b in zip(word1, word2))

    @staticmethod
    def perform_pierce(word1, word2):
        return ''.join(str(int(not (int(a) or int(b)))) for a, b in zip(word1, word2))

    @staticmethod
    def perform_conjunction_negation(word1, word2):
        return ''.join(str(int(int(a) and not int(b))) for a, b in zip(word1, word2))

    @staticmethod
    def perform_negation_disjunction(word1, word2):
        return ''.join(str(int(not int(a) or int(b))) for a, b in zip(word1, word2))
