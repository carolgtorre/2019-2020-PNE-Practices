from pathlib import Path
class Seq:
    """A class for representing sequences"""
    NULL_SEQUENCE = 'NULL'
    INVALID_SEQUENCE = 'ERROR'
    def __init__(self, strbases=NULL_SEQUENCE):
        self.strbases = strbases
        if strbases == Seq.NULL_SEQUENCE:
            print('Null seq created')
            self.strbases = strbases
        else:
            if self.is_valid_sequence():
                self.strbases = strbases
                print('New sequence created!')
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print('INVALID Seq!')
    def is_valid_sequence(self):
        for i in self.strbases:
            if i != 'A' and i != 'C' and i != 'G' and i != 'T':
                return False
        return True

    @staticmethod
    def is_valid_sequence_2(bases):
        for i in strbases:
            if i != 'A' and i != 'C' and i != 'G' and i != 'T':
                return False
        return True
    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = 'Sequence' + str(i) + ': (Length:' + str(list_sequences[i].len()) + ')'+ str(list_sequences[i])
            termcolor.cprint(text, 'yellow')
    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if not (self.strbases == Seq.NULL_SEQUENCE) and not(self.strbases == Seq.INVALID_SEQUENCE):
            for i in self.strbases:
                if i == 'A':
                    a += 1
                elif i == 'C':
                    c += 1
                elif i == 'G':
                    g += 1
                else:
                    t += 1
        return a, c, g, t
    def count(self):
        a, c, g, t = self.count_bases()
        return {'A': a, 'C': c, 'G': g, 'T': t}

    # def info(argument, cs, list_sequence):
    #     termcolor.cprint("INFO", "yellow")
    #     s = Seq(argument)
    #     count_dict = s.count_genes_info()
    #     a = count_dict['A'][0]
    #     pa = count_dict['A'][1]
    #     c = count_dict['C'][0]
    #     pc = count_dict['C'][1]
    #     g = count_dict['G'][0]
    #     pg = count_dict['G'][1]
    #     t = count_dict['T'][0]
    #     pt = count_dict['T'][1]
    #     first = 'Total length: ' + str(len(argument)) + '\n'
    #     cs.send(first.encode())
    #     second = 'A: ' + str(a) + ' ' + str(pa) + '%' + '\n'
    #     cs.send(second.encode())
    #     third = 'C: ' + str(c) + ' ' + str(pc) + '%' + '\n'
    #     cs.send(third.encode())
    #     fourth = 'G: ' + str(g) + ' ' + str(pg) + '%' + '\n'
    #     cs.send(fourth.encode())
    #     fifth = 'T: ' + str(t) + ' ' + str(pt) + '%' + '\n'
    #     cs.send(fifth.encode())
    #     print(first, second, third, fourth, fifth)

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return 'NULL'
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return 'ERROR'
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            complement = ''
            for i in self.strbases:
                if i == 'A':
                    complement += 'T'
                elif i == 'C':
                    complement += 'G'
                elif i == 'G':
                    complement += 'C'
                elif i == 'T':
                    complement += 'A'
            return complement

    def info_seq(self):
        a, c, g, t = self.count_bases()
        sum_all = a + c + g + t
        ap = a * 100 / sum_all
        cp = c * 100 / sum_all
        gp = g * 100 / sum_all
        tp = t * 100 / sum_all
        return {'A': [a, ap], 'C': [c, cp], 'G': [g, gp], 'T': [t, tp]}

    @staticmethod
    def take_out_first_line(sequence):
        return sequence[sequence.find("\n") + 1:].replace("\n", "")

    def read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())

    def most_frequent_base(self, count_dict):
        most_frequent = max(count_dict.values())
        for k, v in count_dict.items():
            if v == most_frequent:
                return k

    def seq_count(self):
        a, c, g, t = self.count_bases(self)
        return {'A': a, 'C': c, 'G': g, 'T': t}

def test_sequences():
    s1 = Seq()
    s2 = Seq('ACTGA')
    s3 = Seq('Invalid Sequence')
    return s1, s2, s3