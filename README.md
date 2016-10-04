# maxentpy

[![Build Status](https://travis-ci.org/kepbod/maxentpy.svg?branch=master)](https://travis-ci.org/kepbod/maxentpy)

maxentpy is a python wrapper for MaxEntScan to calculate splice site strength.

It contains two functions. `score5` is adapt from [MaxEntScan::score5ss](http://genes.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq.html) to score 5' splice sites. `score3` is adapt from [MaxEntScan::score3ss](http://genes.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq_acc.html) to score 3' splice sites. They only use Maximum Entropy Model to score.

## Examples

```python
import maxentpy
maxentpy.score5('cagGTAAGT')  # 3 bases in exon and 6 bases in intron
maxentpy.score3('ttccaaacgaacttttgtAGgga')  # 20 bases in the intron and 3 base in the exon
```
## Citation

Yeo G, Burge CB. Maximum entropy modeling of short sequence motifs with applications to RNA splicing signals. Journal of Computational Biology. 2004, 11:377-94.

## License

The original algorithm and perl scripts are under license described in http://genes.mit.edu/burgelab/maxent/download/READTHIS.
The python version of maxent is under the [MIT License](https://opensource.org/licenses/MIT).
