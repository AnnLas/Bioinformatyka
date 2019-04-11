class Fasta:
    """
        A class which mimics Fasta files structure.
        Parameters
         ----------
        id : str, represents id of the sequence
        sequence : str, represents sequence included in Fasta file
         """

    def __init__(self, id, sequence):
        self.id = id
        self.sequence = sequence

    def set_id(self, id):
        """Sets Fasta id
                Parameters
                ----------
                id : str, id given to Fasta
                """
        self.id = id

    def set_sequence(self, sequence):
        """Sets Fasta sequence
                Parameters
                ----------
                sequence : str, sequence given to Fasta
                """
        self.sequence = sequence

    def get_id(self):
        """Returns Fasta id
                Returns
                ----------
                id : str, Fasta id
                """
        return self.id

    def get_sequence(self):
        """Returns Fasta sequence
                Returns
                ----------
                id : str, Fasta sequence
                """
        return self.sequence
