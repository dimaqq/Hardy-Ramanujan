## peformance test results
```
test_cubes.py N used 9000000000
time used 9.743118
memory used 1146880
```


## estimated
### memory
```
In [1]: 800 * 9000000000 ** (1/3)
Out[1]: 1664067.0584415228
```

(off by a factor of 1.5)

### run time
original estimation (no. of function calls) was waaay wrong
reason is, solution*() only calls generator for each result,
thus density of results matters

```
new estimation N**(2/3) * function call cost * C
In [1]: 9000000000**(2/3) * 365e-9
Out[1]: 1.5792632794866108
```

(off by a factor of 6)
