import matplotlib.pyplot as plt
import numpy


class LocalMatch:
    ACROSS = 4
    UP = 2
    LEFT = 1

    def __init__(self, gap, G, L, substitutionMatrix):
        """Returns instance of LocalMatch

                             Parameters
                             ----------
                             G: int, value returned when first deletion happens
                             L: int, value returned when next deletion happens
                             substitutionMatrix: int[][], array of values for different substitutions
                              """
        self.dictionary = self.punctation_dict(substitutionMatrix)
        self.G = G
        self.gap = gap
        self.L = L
        self.lastTransformation = None
        self.sequence1 = ''
        self.sequence2 = ''
        self.sim = ""
        self.resultSequence1 = ""
        self.resultSequence2 = ""
        self.score = None
        self.last = []
        self.first = []

    def punctation_dict(self, inputMatrix):
        """Creates dictionary of scores for different types of substitution

                                     Parameters
                                     ----------
                                     inputMatrix: matrix with values for substitution for different nucleotides.
                                     Returns
                                     ----------
                                     dict(listOfPairs): dict, dictionary with values for substitution for different nucleotides.

                                      """
        listOfPairs = []
        matrix = numpy.asarray(inputMatrix)
        for j in range(1, matrix.shape[0]):
            for i in range(1, matrix.shape[1]):
                listOfPairs.append([matrix[0][i] + matrix[j][0], int(matrix[j][i])])

        return dict(listOfPairs)

    def match(self, seq1, seq2, gaps_len_count):

        self.sequence1 = seq1
        self.sequence2 = seq2

        matrix = numpy.zeros((len(seq2) + 1, len(seq1) + 1), dtype="float")
        roadMatrix = numpy.zeros((len(seq2) + 1, len(seq1) + 1), dtype="int")

        if gaps_len_count:
            for j in range(1, matrix.shape[0]):
                for i in range(1, matrix.shape[1]):
                    if (i != 0 and j != 0):
                        self.calculate_score(i, j, matrix, roadMatrix)

        else:
            for j in range(1, matrix.shape[0]):
                for i in range(1, matrix.shape[1]):
                    if (i != 0 and j != 0):
                        self.calculate_score_gap_penalising(i, j, matrix, roadMatrix)

        return matrix, roadMatrix

    def max_coordinates(self, matrix):
        coordinates = numpy.where(matrix == numpy.amax(matrix))
        return coordinates

    def compute_path(self, roadMatrix, matrix, sequence1, sequence2, i, j):
        """Checks the best way of transformation, based on roadMatrix, begins from the maximum value in LocalMatch score matrix.

                                         Parameters
                                         ----------
                                         roadMatrix: matrix which tells what transformation happened
                                         matrix: local match score matrix
                                         sequence1: str, first sequence
                                         sequence2: str, second sequence

                                         Returns
                                         ----------
                                         marix: local match score matrix with best path marked by Nans

                                          """

        seq1 = ''
        seq2 = ''
        self.sim = ''
        self.score = matrix[j][i]
        matrix[j, i] = float(numpy.nan)
        self.first.append(i)
        self.first.append(j)
        while i > 0 and j > 0:

            if roadMatrix[j][i] == LocalMatch.ACROSS:
                i -= 1
                j -= 1
                seq1 = seq1 + sequence1[i]
                seq2 = seq2 + sequence2[j]
                if sequence1[i] == sequence2[j]:
                    self.sim += "|"
                else:
                    self.sim += " "

            elif roadMatrix[j][i] == LocalMatch.UP:
                j -= 1
                seq1 = seq1 + "-"
                seq2 = seq2 + sequence2[j]
                self.sim += " "

            elif roadMatrix[j][i] == LocalMatch.LEFT:
                i -= 1
                seq1 = seq1 + sequence1[i]
                seq2 = seq2 + "-"
                self.sim += " "

            matrix[j][i] = float(numpy.nan)

        self.resultSequence1 = seq1[::-1]
        self.resultSequence2 = seq2[::-1]
        self.sim = self.sim[::-1]
        matrix[j][i] = float(numpy.nan)
        self.last.append(i)
        self.last.append(j)

        return matrix

    def calculate_score(self, i, j, matrix, roadMatrix):
        """Scores best way of transformation, add points of most profitable transformation to previous value from matrix

                                    Parameters
                                    ----------
                                    i: int, y coordinate of matrix
                                    j: int, x coordinate of matrix
                                    matrix: matrix with scores for LocalMatch
                                    roadMatrix: matrix which tells what transformation happened

                                     """
        substitution = matrix[j - 1][i - 1] + self.dictionary.get(self.sequence2[j - 1] + self.sequence1[i - 1])
        deletion1 = matrix[j - 1][i] + self.gap
        deletion2 = matrix[j][i - 1] + self.gap
        matrix[j][i] = max(substitution, deletion1, deletion2, 0)

        if max(substitution, deletion1, deletion2) == substitution:
            roadMatrix[j][i] = LocalMatch.ACROSS
        if max(substitution, deletion1, deletion2) == deletion1:
            roadMatrix[j][i] = LocalMatch.UP
        if max(substitution, deletion1, deletion2) == deletion2:
            roadMatrix[j][i] = LocalMatch.LEFT

    def calculate_score_gap_penalising(self, i, j, matrix, roadMatrix):
        """Alternative version of calculating score, includes the length of the gap.
        Scores best way of transformation, add points of most profitable transformation to previous value from matrix

                                    Parameters
                                    ----------
                                    i: int, y coordinate of matrix
                                    j: int, x coordinate of matrix
                                    matrix: matrix with scores for LocalMatch
                                    roadMatrix: matrix which tells what transformation happened

                                     """
        substitution = matrix[j - 1][i - 1] + self.dictionary.get(self.sequence2[j - 1] + self.sequence1[i - 1])
        if self.lastTransformation != 'deletion':
            deletion1 = matrix[j - 1][i] + self.G
            deletion2 = matrix[j][i - 1] + self.G
        else:
            deletion1 = matrix[j - 1][i] + self.L
            deletion2 = matrix[j][i - 1] + self.L

        matrix[j][i] = max(substitution, deletion1, deletion2, 0)

        if max(substitution, deletion1, deletion2) == substitution:
            roadMatrix[j][i] = LocalMatch.ACROSS
            self.lastTransformation = 'substitution'
        if max(substitution, deletion1, deletion2) == deletion1:
            roadMatrix[j][i] = LocalMatch.UP
            self.lastTransformation = 'deletion'
        if max(substitution, deletion1, deletion2) == deletion2:
            roadMatrix[j][i] = LocalMatch.LEFT
            self.lastTransformation = 'deletion'

    def show_plot(self, matrix, seq1, seq2):
        """Shows local match plot with path
                                               """
        plt.matshow(matrix)
        plt.colorbar()
        plt.xlabel(seq1)
        plt.ylabel(seq2)
        plt.title("Local Match")
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
        statistics += "# Mode: " + "similarity" + '\n'
        statistics += "# Punctation: " + str(self.dictionary) + '\n'
        statistics += "# Gap: " + str(self.gap) + '\n'
        statistics += "# G: " + str(self.G) + '\n'
        statistics += "# L: " + str(self.L) + '\n'
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
        statistics += 'Fasta Format:' + '\n'
        statistics += '>seq1 '
        statistics += str(self.last[0] + 1) + '-' + str(self.first[0]) + '\n'
        statistics += self.resultSequence1 + '\n'
        statistics += '>seq2 '
        statistics += str(self.last[1] + 1) + '-' + str(self.first[1]) + '\n'
        statistics += self.resultSequence2 + '\n'

        with open("Stats.txt", "w") as text_file:
            print(statistics, file=text_file)

        return statistics
