import re


class FastaParser:
    """
           A class which parses given content to a Fasta format.

           """

    @classmethod
    def check_letter_match(self, sequence):
        """Checks if given sequence contains only A,C,T,G,U letters

                Parameters
                ----------
                sequence: str, sequence which is parsed

                Returns
                ----------
                boolean; True - if sequence contains only permitted letters
                 """
        search = re.compile(r'[^ACTGU ]').search
        return not bool(search(sequence))

    @classmethod
    def parse_fasta(self, content):
        """Splits given content into list of fastas, when content contains not permitted letters program exits.

                Parameters
                ----------
                content: str from which, fastas are selected

                Returns
                ----------
                fastas; List of fastas
                 """

        global fasta
        sequence = ''

        lines = content.splitlines()
        fastas = list()
        for line in lines:
            if '>' in line:
                id = line
                fasta = {"id": id, "sequence": id}
                fastas.append(fasta)
            elif line == '':
                sequence = ''
                continue
            else:
                if self.check_letter_match(line):
                    sequence = sequence + line
                    fasta["sequence"] = sequence
                else:
                    raise Exception('Sequence contains unpermitted signs')

        return fastas
