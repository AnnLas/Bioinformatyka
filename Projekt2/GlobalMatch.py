import matplotlib.pyplot as plt
import numpy


class GlobalMatch:
    """
           A class which represents implementation of Needleman-Wunsch algorithm to compute the optimal
           global aligment of two sequences.

           """

    def __init__(self, missmatch, match, gap):
        """Returns instance of GlobalMatch

                             Parameters
                             ----------
                             missmatch: int, value returned when substitution happens
                             match: int, value returned when nucleotides match
                             gap: int, value returned when deletion happens
                              """
        self.missmatch = missmatch
        self.match = match
        self.gap = gap
        self.sequence1 = ''
        self.sequence2 = ''
        self.sim = ""
        self.resultSequence1 = ""
        self.resultSequence2 = ""
        self.score = None

    def sequence_match(self, sequence1, sequence2):
        """Compares two sequences to each other

                             Parameters
                             ----------
                             sequence1: str, first sequence
                             sequence2: str, second sequence

                             Returns
                             ----------
                             roadMatrix; matrix which represents the way from given value come from:
                             # cross - 100 - 4
                             # up - 010 - 2
                             # left - 001 - 1
                             matrix: matrix with punctation for GlobalMatch
                              """
        self.sequence1 = sequence1
        self.sequence2 = sequence2
        matrix = numpy.zeros((len(sequence2) + 1, len(sequence1) + 1), dtype="float")
        roadMatrix = numpy.zeros((len(sequence2) + 1, len(sequence1) + 1), dtype="int")

        for i in range(len(sequence1) + 1):
            matrix[0][i] = i * self.gap

        for j in range(len(sequence2) + 1):
            matrix[j][0] = j * self.gap

        for j in range(1, matrix.shape[0]):
            for i in range(1, matrix.shape[1]):
                self.evaluate_transformations(i, j, matrix, roadMatrix)

        return roadMatrix, matrix

    def evaluate_transformations(self, i, j, matrix, roadMatrix):
        """Scores best way of transformation, add points of most profitable transformation to previous value from matrix

                                    Parameters
                                    ----------
                                    i: int, y coordinate of matrix
                                    j: int, x coordinate of matrix
                                    matrix: matrix with scores for GlobalMatch
                                    roadMatrix: matrix which tells what transformation happened

                                     """
        substitution = matrix[j - 1][i - 1] + self.similarity(self.sequence2[j - 1], self.sequence1[i - 1])
        deletion1 = matrix[j - 1][i] + self.similarity(self.sequence1[i - 1], '-')
        deletion2 = matrix[j][i - 1] + self.similarity('-', self.sequence2[j - 1])
        matrix[j][i] = max(substitution, deletion1, deletion2)

        if max(substitution, deletion1, deletion2) == substitution:
            roadMatrix[j][i] = 4
        if max(substitution, deletion1, deletion2) == deletion1:
            roadMatrix[j][i] = 2
        if max(substitution, deletion1, deletion2) == deletion2:
            roadMatrix[j][i] = 1

        self.score = roadMatrix[-1][-1]

    def similarity(self, a, b):
        """Compares two nucleotides and returns score for similarity

                                    Parameters
                                    ----------
                                    a: char, first nucleotide
                                    b: char, second nucleotide

                                    Returns
                                    ----------
                                    int, similarity score

                                     """
        if a == '-':
            return self.gap
        if b == '-':
            return self.gap
        if a == b:
            return self.match
        if a != b:
            return self.missmatch

    def mark_path(self, roadMatrix, matrix, sequence1, sequence2):
        """Checks the best way of transformation, based on roadMatrix, begins from the end of the GlobalMatch score matrix.

                                         Parameters
                                         ----------
                                         roadMatrix: matrix which tells what transformation happened
                                         matrix: global match score matrix
                                         sequence1: str, first sequence
                                         sequence2: str, second sequence

                                         Returns
                                         ----------
                                         marix: global match score matrix with best path marked by Nans

                                          """

        j = roadMatrix.shape[0] - 1
        i = roadMatrix.shape[1] - 1

        seq1 = ''
        seq2 = ''
        self.sim = ''
        matrix[j, i] = float(numpy.nan)

        while i > 0 and j > 0:

            if roadMatrix[j][i] == 4:
                i -= 1
                j -= 1
                seq1 = seq1 + sequence1[i]
                seq2 = seq2 + sequence2[j]
                if sequence1[i] == sequence2[j]:
                    self.sim += "|"
                else:
                    self.sim += " "

            elif roadMatrix[j][i] == 2:
                j -= 1
                seq1 = seq1 + "-"
                seq2 = seq2 + sequence2[j]
                self.sim += " "

            elif roadMatrix[j][i] == 1:
                i -= 1
                seq1 = seq1 + sequence1[i]
                seq2 = seq2 + "-"
                self.sim += " "

            matrix[j][i] = float(numpy.nan)

        self.resultSequence1 = seq1[::-1]
        self.resultSequence2 = seq2[::-1]
        self.sim = self.sim[::-1]

        self.get_stats()
        return matrix

    def show_plot(self, matrix, seq1, seq2):
        """Shows global match plot with path
                                               """
        plt.matshow(matrix)
        plt.colorbar()
        plt.xlabel(seq1)
        plt.ylabel(seq2)
        plt.title("Global Match")
        plt.show()

    def get_stats(self):
        """Creates String with statistics such as number of gaps, identity....

                                              Returns
                                              ----------
                                              statistics: str with statistics

                                               """
        statistics = ''
        length = len(self.resultSequence1)
        statistics += "# 1:" + self.sequence1 + '\n' + "# 2:" + self.sequence2 + '\n'
        statistics += "# Mode: " + "distance" + '\n'
        statistics += "# Match: " + str(self.match) + '\n'
        statistics += "# Mismatch: " + str(self.missmatch) + '\n'
        statistics += "# Gap: " + str(self.gap) + '\n'
        statistics += "# Score: " + str(self.score) + '\n'
        statistics += "# Length: " + str(length) + '\n'
        statistics += "# Idenity: " + str(self.sim.count('|')) + "/" + str(length) + ' (' + str(
            int((self.sim.count('|')) * 100 / length)) + '%)' + '\n'

        statistics += "# Gaps: " + str(
            (self.resultSequence1.count('-')) + (self.resultSequence2.count('-'))) + '/' + str(length) + ' (' + \
                      str(int(((self.resultSequence1.count('-')) + (
                          self.resultSequence2.count('-'))) * 100 / length)) + '%)' + '\n'

        statistics += self.resultSequence1 + '\n'
        statistics += self.sim + '\n'
        statistics += self.resultSequence2 + '\n'

        with open("Stats.txt", "w") as text_file:
            print(statistics, file=text_file)

        return statistics
