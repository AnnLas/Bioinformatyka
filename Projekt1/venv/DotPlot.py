import numpy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class Dotplot:
    """
        A class used to represent a Dotplot

        """

    @classmethod
    def make_dotplot(self, fasta1, fasta2):

        """Makes two-dimensional array which represents match between two sequences.

                Parameters
                ----------
                fasta1, fasta2: Fasta
                    Structure which contains id and analysed sequence

                Returns
                ------
                two-dimensional array of zeros and ones
                """

        seq1 = fasta1.get_sequence()
        seq2 = fasta2.get_sequence()

        n = len(seq1)
        m = len(seq2)

        matrix = [[0 for x in range(m)] for y in range(n)]
        for i in range(n):
            for j in range(m):
                if seq1[i] == seq2[j]:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 0

        return matrix


@classmethod
def filter_dotplot(self, matrix, treshold, window):
    """Makes two-dimensional array which represents filtered
    (with given treshold and window) match between two sequences.

                    Parameters
                    ----------
                    matrix: Array, which is result of first match between two sequences
                    treshold: int, number which represents acceptable difference of sequences in given window
                    window: int, length of diagonal section which is analysed one at a time

                    Returns
                    ------
                    two-dimensional filtered array of zeros and ones
                    """

    arr = numpy.array(matrix)

    diags = [arr.diagonal(i) for i in range(-arr.shape[0] + 1, arr.shape[1])]

    filteredArray = numpy.zeros((arr.shape[0], arr.shape[1]), dtype=int)

    diagCounter = 1

    for n in diags:

        if len(n) >= window:
            for i in range((len(n) + 1) - window):
                counter = 0
                for j in range(window):
                    if n[j + i] == 1:
                        counter = counter + 1

                if (counter + treshold) >= window:

                    for k in range(window):
                        if (arr.shape[0] >= diagCounter):
                            filteredArray[arr.shape[0] - diagCounter + k + i][k + i] = n[k + i]
                        else:

                            filteredArray[k + i][(diagCounter - arr.shape[0] + k + i)] = n[k + i]

        diagCounter = diagCounter + 1

    return filteredArray