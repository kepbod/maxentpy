'''
maxent.py
Calculate splice site strength
Modified from MaxEntScan perl scripts developed by Gene Yeo and Christopher
Burge
Yeo G and Burge C. Maximum entropy modeling of short sequence motifs with
applications to RNA splicing signals. Journal of Computational Biology,
2004, 11:377-94.
'''

import math
from collections import defaultdict
from string import maketrans
import os.path


__all__ = ['score5', 'score3']

dir_path = os.path.dirname(os.path.abspath(__file__))


def score5(fa):
    '''
    Calculate 5' splice site strength
    (exon)XXX|XXXXXX(intron)
              **
    >>> round(score5('cagGTAAGT'), 2)
    10.86
    >>> round(score5('gagGTAAGT'), 2)
    11.08
    >>> round(score5('taaATAAGT'), 2)
    -0.12
    '''
    # for key elements
    key = fa[3:5].upper()
    bgd = {'A': 0.27, 'C': 0.23, 'G': 0.23, 'T': 0.27}
    cons1 = {'A': 0.004, 'C': 0.0032, 'G': 0.9896, 'T': 0.0032}
    cons2 = {'A': 0.0034, 'C': 0.0039, 'G': 0.0042, 'T': 0.9884}
    score = cons1[key[0]] * cons2[key[1]] / (bgd[key[0]] * bgd[key[1]])
    # for rest elements
    rest = (fa[:3] + fa[5:]).upper()
    matrix_f = dir_path + '/data/score5_matrix.txt'
    with open(matrix_f, 'r') as f:
        for line in f:
            entry = line.split()
            if entry[0] == rest:
                rest_score = float(entry[1])
                break
    # final score
    return math.log(score * rest_score, 2)


def score3(fa):
    '''
    Calculate 3' splice site strength
    (intron)XXXXXXXXXXXXXXXXXXXX|XXX(exon)
                              **
    >>> round(score3('ttccaaacgaacttttgtAGgga'), 2)
    2.89
    >>> round(score3('tgtctttttctgtgtggcAGtgg'), 2)
    8.19
    >>> round(score3('ttctctcttcagacttatAGcaa'), 2)
    -0.08
    '''
    # for key elements
    key = fa[18:20].upper()
    bgd = {'A': 0.27, 'C': 0.23, 'G': 0.23, 'T': 0.27}
    cons1 = {'A': 0.9903, 'C': 0.0032, 'G': 0.0034, 'T': 0.0030}
    cons2 = {'A': 0.0027, 'C': 0.0037, 'G': 0.9905, 'T': 0.0030}
    score = cons1[key[0]] * cons2[key[1]] / (bgd[key[0]] * bgd[key[1]])
    # for rest elements
    rest = (fa[:18] + fa[20:]).upper()
    matrix_f = dir_path + '/data/score3_matrix.txt'
    matrix = defaultdict(dict)
    with open(matrix_f, 'r') as f:
        for line in f:
            n, m, s = line.split()
            matrix[int(n)][int(m)] = float(s)
    rest_score = 1
    rest_score *= matrix[0][hashseq(rest[:7])]
    rest_score *= matrix[1][hashseq(rest[7:14])]
    rest_score *= matrix[2][hashseq(rest[14:])]
    rest_score *= matrix[3][hashseq(rest[4:11])]
    rest_score *= matrix[4][hashseq(rest[11:18])]
    rest_score /= matrix[5][hashseq(rest[4:7])]
    rest_score /= matrix[6][hashseq(rest[7:11])]
    rest_score /= matrix[7][hashseq(rest[11:14])]
    rest_score /= matrix[8][hashseq(rest[14:18])]
    # final score
    return math.log(score * rest_score, 2)


def hashseq(fa):
    table = maketrans('ACGT', '0123')
    seq = fa.translate(table)
    return sum(int(j) * 4**(len(seq) - i - 1) for i, j in enumerate(seq))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
