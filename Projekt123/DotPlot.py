import numpy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class DotPlot:
    """
        A class used to represent a Dotplot

        """
    def __init__(self, mismatch, match, gap):
        """Returns instance of GlobalMatch

                             Parameters
                             ----------
                             mismatch: int, value returned when substitution happens
                             match: int, value returned when nucleotides match
                             gap: int, value returned when deletion happens
                              """
        self.missmatch = mismatch
        self.match = match
        self.gap = gap


    @classmethod
    def make_dotplot(self, seq1, seq2):

        """Makes two-dimensional array which represents match between two sequences.

                Parameters
                ----------
                seq1: str, first sequence
                seq2: str, second sequence

                Returns
                ------
                two-dimensional array of zeros and ones
                """

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
    def show_dotplot(self, matrix, id1, id2):

        """Shows dotplot

                    Parameters
                    ----------
                    matrix: Array of zeros and ones
                    fasta1ID: str, ID of the first sequence
                    fasta2ID: str, ID of the second sequence
                    title: str, Dotplot title


                    """

        data = numpy.array(matrix)
        values = numpy.unique(data.ravel())
        plt.figure()
        im = plt.imshow(data, cmap='Greys')
        colors = [im.cmap(im.norm(value)) for value in values]
        states = ['mismatch', 'match']
        patches = [mpatches.Patch(color=colors[i], label="{l}".format(l=states[i])) for i in range(len(values))]
        plt.legend(handles=patches, bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
        plt.ylabel(id1)
        plt.xlabel(id2)
        plt.title("Filtered Dotplot")
        plt.show()

    @classmethod
    def filter_dotplot(self, matrix, error, window):
        """Makes two-dimensional array which represents filtered
        (with given treshold and window) match between two sequences.

                        Parameters
                        ----------
                        matrix: Array, which is result of first match between two sequences
                        error: int, number which represents acceptable difference of sequences in given window
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

                    if (counter + error) >= window:

                        for k in range(window):
                            if (arr.shape[0] >= diagCounter):
                                filteredArray[arr.shape[0] - diagCounter + k + i][k + i] = n[k + i]
                            else:

                                filteredArray[k + i][(diagCounter - arr.shape[0] + k + i)] = n[k + i]

            diagCounter = diagCounter + 1

        return filteredArray




