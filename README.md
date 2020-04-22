# maxentpy

[![Build Status](https://travis-ci.org/kepbod/maxentpy.svg?branch=master)](https://travis-ci.org/kepbod/maxentpy)
[![Coverage Status](https://coveralls.io/repos/github/kepbod/maxentpy/badge.svg)](https://coveralls.io/github/kepbod/maxentpy)
[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat-square)](http://bioconda.github.io/recipes/maxentpy/README.html)
[![download](https://anaconda.org/bioconda/maxentpy/badges/downloads.svg)](https://anaconda.org/bioconda/maxentpy)

maxentpy is a python wrapper for MaxEntScan to calculate splice site strength.

It contains two functions. `score5` is adapt from [MaxEntScan::score5ss](http://hollywood.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq.html) to score 5' splice sites. `score3` is adapt from [MaxEntScan::score3ss](http://hollywood.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq_acc.html) to score 3' splice sites. They only use Maximum Entropy Model to score.

## Prerequisites

* Cython
* msgpack-python

## Examples

```python
>>> from maxentpy import maxent  # use normal version of maxent
>>> maxent.score5('cagGTAAGT')  # 3 bases in exon and 6 bases in intron
10.858313101356437
>>> maxent.score3('ttccaaacgaacttttgtAGgga')  # 20 bases in the intron and 3 base in the exon
2.8867730651152104
>>> from maxentpy.maxent import load_matrix5, load_matrix3  # preloading matrix will speed up
>>> timeit maxent.score5('cagGTAAGT')
10 loops, best of 3: 23.5 ms per loop
>>> matrix5 = load_matrix5()
>>> timeit maxent.score5('cagGTAAGT', matrix=matrix5)
100000 loops, best of 3: 3.27 µs per loop
>>> timeit maxent.score3('ttccaaacgaacttttgtAGgga')
1 loop, best of 3: 259 ms per loop
>>> matrix3 = load_matrix3()
>>> timeit maxent.score3('ttccaaacgaacttttgtAGgga', matrix=matrix3)
10000 loops, best of 3: 103 µs per loop
>>> from maxentpy import maxent_fast  # fast version could further speed up
>>> timeit maxent_fast.score5('cagGTAAGT')
100 loops, best of 3: 5.04 ms per loop
>>> timeit maxent_fast.score3('ttccaaacgaacttttgtAGgga')
100 loops, best of 3: 9.3 ms per loop
>>> from maxentpy.maxent_fast import load_matrix  # support preloading matrix
>>> matrix5 = load_matrix(5)
>>> timeit maxent_fast.score5('cagGTAAGT', matrix=matrix5)
100000 loops, best of 3: 3.61 µs per loop
>>> matrix3 = load_matrix(3)
>>> timeit maxent_fast.score3('ttccaaacgaacttttgtAGgga', matrix=matrix3)
100000 loops, best of 3: 7.76 µs per loop
```

## Benchmark

### score5

  score5      |maxentpy.maxent|maxentpy.maxent_fast
--------------|---------------|--------------------
without matrix|     23.5 ms   |   5.04 ms          
with matrix   |     3.27 µs   |   3.61 µs          

### score3

 score3       |maxentpy.maxent|maxentpy.maxent_fast
--------------|---------------|--------------------
without matrix|     259 ms    |   9.3 ms           
with matrix   |     103 µs    |   7.76 µs          

## Citation

Yeo G, Burge CB. Maximum entropy modeling of short sequence motifs with applications to RNA splicing signals. Journal of Computational Biology. 2004, 11:377-94.

## License

The original algorithm and perl scripts are under license described in http://genes.mit.edu/burgelab/maxent/download/READTHIS.
The python version of maxent is under the [MIT License](https://opensource.org/licenses/MIT).
