import urllib.request


class FastaReader:
    """
               A class which reads fastas in various ways.

               """

    @classmethod
    def fasta_from_url(self, id):
        """Returns fastas from web ncbi database by id.

                        Parameters
                        ----------
                        id: str, fasta's identifier

                        Returns
                        ----------
                        content; str which contains fastas
                         """
        URL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
        response = urllib.request.urlopen(URL + '?db=nucleotide&rettype=fasta&id=' + id)
        content = response.read().decode("utf-8", "ignore")
        return content

    @classmethod
    def fasta_from_file(self, filePath):
        """Returns fastas from file

                        Parameters
                        ----------
                        filePath: str, path to file with fastas

                        Returns
                        ----------
                        content; str which contains fastas
                        """
        response = open(filePath, "r")  # r - READ
        content = response.read()
        response.close()
        return content

    @classmethod
    def fasta_from_user(self):
        """Returns fastas from user input, it can be used in console version of the program

                        Returns
                        ----------
                        content; str which contains fastas
                        """
        content = ''
        content += '>' + input("id:\n") + '\n'
        content += input("sequence:\n")
        return content
