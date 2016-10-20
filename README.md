# maxentpy

[![Build Status](https://travis-ci.org/kepbod/maxentpy.svg?branch=master)](https://travis-ci.org/kepbod/maxentpy)
[![Coverage Status](https://coveralls.io/repos/github/kepbod/maxentpy/badge.svg)](https://coveralls.io/github/kepbod/maxentpy)

maxentpy is a python wrapper for MaxEntScan to calculate splice site strength.

It contains two functions. `score5` is adapt from [MaxEntScan::score5ss](http://genes.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq.html) to score 5' splice sites. `score3` is adapt from [MaxEntScan::score3ss](http://genes.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq_acc.html) to score 3' splice sites. They only use Maximum Entropy Model to score.

## Examples

```python
>>> from maxentpy import score5, score3
>>> score5('cagGTAAGT')  # 3 bases in exon and 6 bases in intron
10.858313101356437
>>> score3('ttccaaacgaacttttgtAGgga')  # 20 bases in the intron and 3 base in the exon
10.858313101356437
>>> from maxentpy import load_matrix5, load_matrix3  # preloading matrix will speed up
>>> timeit score5('cagGTAAGT')
10 loops, best of 3: 23.2 ms per loop
>>> matrix5 = load_matrix5()
>>> timeit score5('cagGTAAGT', matrix=matrix5)
100000 loops, best of 3: 2.56 µs per loop
>>> timeit score3('ttccaaacgaacttttgtAGgga')
1 loop, best of 3: 260 ms per loop
>>> matrix3 = load_matrix3()
>>> timeit score3('ttccaaacgaacttttgtAGgga', matrix=matrix3)
10000 loops, best of 3: 99.4 µs per loop
```
## Citation

Yeo G, Burge CB. Maximum entropy modeling of short sequence motifs with applications to RNA splicing signals. Journal of Computational Biology. 2004, 11:377-94.

## License

The original algorithm and perl scripts are under license described in http://genes.mit.edu/burgelab/maxent/download/READTHIS.
The python version of maxent is under the [MIT License](https://opensource.org/licenses/MIT).
