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

   