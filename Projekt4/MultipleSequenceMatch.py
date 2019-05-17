import numpy


class MultipleSequenceMatch:
    ACROSS = 4
    UP = 2
    LEFT = 1

    def __init__(self, gap, substitutionMatrix):
        """Returns instance of LocalMatch

                             Parameters
                             ----------
                             G: int, value returned when first deletion happens
                             L: int, value returned when next deletion happens
                             substitutionMatrix: int[][], array of values for different substitutions
                              """
        self.dictionary = self.punctation_dict(substitutionMatrix)
        self.gap = gap
        self.sequence1 = ''
        self.sequence2 = ''
        self.sim = ""
        self.resultSequence1 = ""
        self.resultSequence2 = ""
        self.aligmentMatrix = []
        self.centerSeq = 0
        self.sequencesMatrix = []
        self.idList = []

    def calculate_star_centre(self, matrix):
        scores = []
        for i in range(0, matrix.shape[0]):
            rowSum = 0
            for j in range(0, matrix.shape[0]):
                rowSum += matrix[i][j]
            scores.append(rowSum)
        return scores

    def match_multiple_arrays(self, sequences):
        matrix = numpy.zeros((len(sequences), len(sequences)), dtype="float")

        for i in range(0, len(sequences)):
            for j in range(0, len(sequences)):
                if j != i:
                    results = self.match(sequences[i].get('sequence'), sequences[j].get('sequence'))
                    matrix[i][j] = self.score
                    self.insert_gaps(results[0], results[1], self.sequence1, self.sequence2)
                    self.aligmentMatrix.append(self.resultSequence1)
                    self.aligmentMatrix.append(self.resultSequence2)

            self.idList.append(sequences[i].get('id'))
            self.sequencesMatrix.append(sequences[i].get('sequence'))

        return matrix

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

    def match(self, seq1, seq2):
        """Compares two sequences to each other

                                  Parameters
                                  ----------
                                  seq1: str, first sequence
                                  seq2: str, second sequence

                                  Returns
                                  ----------
                                  roadMatrix; matrix which represents the way from given value come from:
                                  # cross - 100 - 4
                                  # up - 010 - 2
                                  # left - 001 - 1
                                  matrix: matrix with punctation for GlobalMatch
                                   """

        self.sequence1 = seq1
        self.sequence2 = seq2

        matrix = numpy.zeros((len(seq2) + 1, len(seq1) + 1), dtype="float")
        roadMatrix = numpy.zeros((len(seq2) + 1, len(seq1) + 1), dtype="int")

        for i in range(len(seq1) + 1):
            matrix[0][i] = i * self.gap
            roadMatrix[0][i] = self.LEFT

        for j in range(len(seq2) + 1):
            matrix[j][0] = j * self.gap
            roadMatrix[j][0] = self.UP

        for j in range(1, matrix.shape[0]):
            for i in range(1, matrix.shape[1]):
                if (i != 0 and j != 0):
                    self.calculate_score(i, j, matrix, roadMatrix)

        self.score = matrix[-1][-1]
        return roadMatrix, matrix

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
        matrix[j][i] = min(substitution, deletion1, deletion2)

        if min(substitution, deletion1, deletion2) == substitution:
            roadMatrix[j][i] = MultipleSequenceMatch.ACROSS
        if min(substitution, deletion1, deletion2) == deletion1:
            roadMatrix[j][i] = MultipleSequenceMatch.UP
        if min(substitution, deletion1, deletion2) == deletion2:
            roadMatrix[j][i] = MultipleSequenceMatch.LEFT

    def insert_gaps(self, roadMatrix, matrix, sequence1, sequence2):
        """Checks the best way of transformation, based on roadMatrix, begins from the end of the GlobalMatch score matrix and inserts gaps to sequences.

                                         Parameters
                                         ----------
                                         roadMatrix: matrix which tells what transformation happened
                                         matrix: global match score matrix
                                         sequence1: str, first sequence
                                         sequence2: str, second sequence

                                          """

        j = roadMatrix.shape[0] - 1
        i = roadMatrix.shape[1] - 1

        seq1 = ''
        seq2 = ''
        while i > 0 or j > 0:

            if roadMatrix[j][i] == MultipleSequenceMatch.ACROSS:
                i -= 1
                j -= 1
                seq1 = seq1 + sequence1[i]
                seq2 = seq2 + sequence2[j]

            elif roadMatrix[j][i] == MultipleSequenceMatch.UP:
                j -= 1
                seq1 = seq1 + "-"
                seq2 = seq2 + sequence2[j]


            elif roadMatrix[j][i] == MultipleSequenceMatch.LEFT:
                i -= 1
                seq1 = seq1 + sequence1[i]
                seq2 = seq2 + "-"

            matrix[j][i] = float(numpy.nan)

        self.resultSequence1 = seq1[::-1]
        self.resultSequence2 = seq2[::-1]

    def aligment_to_center(self):

        """Make aligment to center sequence in star algorithm


                                       Returns
                                       ----------
                                       aligment; list of sequecnes aligned to center sequence:

                                        """

        aligment = []
        sequencesNumber = len(self.sequencesMatrix)
        sequences = self.aligmentMatrix[
                    (self.centerSeq * 2 * (sequencesNumber - 1)):(self.centerSeq * 2 * (sequencesNumber) + 2)]

        aligment.append(sequences[0])
        aligment.append(sequences[1])

        for i in range(3, len(sequences)):
            if (i % 2 == 1):
                j = 0

                while len(sequences[i - 1]) > j or len(sequences[0]) > j:

                    if not len(sequences[i - 1]) > j:
                        sequences[i] = sequences[i][:j] + '-' + sequences[i][j:]
                        sequences[i - 1] = sequences[i - 1][:j] + '-' + sequences[i - 1][j:]

                    if not len(sequences[0]) > j:
                        sequences[0] = sequences[0][:j] + '-' + sequences[0][j:]

                    if sequences[i - 1][j] == sequences[0][j]:
                        j = j + 1

                    elif sequences[0][j] == '-':
                        sequences[i] = sequences[i][:j] + '-' + sequences[i][j:]
                        sequences[i - 1] = sequences[i - 1][:j] + '-' + sequences[i - 1][j:]
                        j = j + 1

                    elif sequences[i - 1][j] == '-':
                        self.insert_gap_to_array(j, aligment)
                        sequences[0] = sequences[0][:j] + '-' + sequences[0][j:]
                        j = j + 1

                    else:
                        j = j + 1

                aligment.append(sequences[i])

        return aligment

    def insert_gap_to_array(self, index, sequences):
        """Inserts gaps to array
                                        Parameters
                                         ----------
                                        index: indicates place of gap insertion
                                        sequences: list of sequences where gap is inserted

                                        """
        for i in range(0, len(sequences)):

            if len(sequences[i]) > index:
                if not sequences[i][index] == '-':
                    sequences[i] = sequences[i][:index] + '-' + sequences[i][index:]
            else:
                sequences[i] = self.insert_gap_to_seq(index, sequences[i])

    def insert_gap_to_seq(self, index, sequence):
        """Inserts gaps to sequence
                                               Parameters
                                                ----------
                                               index: indicates place of gap insertion
                                               sequence: sequence where gap is inserted

                                               """
        return sequence[0][:index] + '-' + sequence[0][index:]

    def calculate_total_score(self, matrix):
        """Calculate total score of star aligment algorithm
                                                Parameters
                                                 ----------
                                                matrix: matrix of transformed sequences

                                                """
        score = 0

        for i in range(0, len(matrix[0])):
            for j in range(0, len(matrix)):
                if '-' == matrix[j][i]:
                    score = score + 2
                for k in range(j + 1, len(matrix)):

                    if matrix[j][i] != matrix[k][i] and '-' != matrix[j][i] and '-' != matrix[k][i]:
                        score = score + 1

        return score

    def print_result(self, aligment):
        """Returns String with result of star aligment
                                                        Parameters
                                                         ----------
                                                        aligment: list of  transformed sequences

                                                        """

        self.idList.insert(0, self.idList[self.centerSeq])
        self.idList.__delitem__(self.centerSeq + 1)
        result = ''
        result = result + '\n'.join(self.idList) + '\n'
        stars = numpy.empty(len(aligment[0]), dtype=object)
        for k in range(0, len(aligment)):
            result = result + aligment[k] + '\n'
        for i in range(0, len(aligment[0])):
            codon = aligment[0][i]
            stars[i] = '*'

            for j in range(0, len(aligment)):
                if aligment[j][i] != codon:
                    stars[i] = ' '

        result = result + ''.join(stars) + '\n'
        print(result)
        return result

    def print_fasta(self, aligment):
        """Returns fasta with result of star aligment
                                                        Parameters
                                                         ----------
                                                        aligment: list of  transformed sequences

                                                        """
        self.idList.insert(0, self.idList[self.centerSeq])
        self.idList.__delitem__(self.centerSeq + 1)
        result = ""

        for k in range(0, len(aligment)):
            result = result + self.idList[k] + '\n'
            result = result + aligment[k] + '\n'

        return result
