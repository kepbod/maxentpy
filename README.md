# maxentpy

maxentpy is a python wrapper for MaxEntScan to calculate splice site strength.

It contains two functions. `score5` is adapt from
[MaxEntScan::score5ss](http://genes.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq.html)
to score 5' splice sites. `score3` is adapt from
[MaxEntScan::score3ss](http://genes.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq_acc.html)
to score 3' splice sites. They only use Maximum Entropy Model to score.

## Examples

```python
import maxentpy
maxentpy.score5('cagGTAAGT')
maxentpy.score3('ttccaaacgaacttttgtAGgga')
```
