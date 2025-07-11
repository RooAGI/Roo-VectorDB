## Our Test Environment Setup

Our testing was conducted on a high-performance server equipped with an Intel® Xeon® Gold 6212U CPU running at up to 3.9 GHz, featuring 48 threads across 24 cores. The system supports both 32-bit and 64-bit operation modes and includes 512 GB of RAM, with over 500 GB available during testing. 


### CPU Information
```
$ lscpu
Architecture:             x86_64
  CPU op-mode(s):         32-bit, 64-bit
  Address sizes:          46 bits physical, 48 bits virtual
  Byte Order:             Little Endian
CPU(s):                   48
  On-line CPU(s) list:    0-47
Vendor ID:                GenuineIntel
  Model name:             Intel(R) Xeon(R) Gold 6212U CPU @ 2.40GHz
    CPU family:           6
    Model:                85
    Thread(s) per core:   2
    Core(s) per socket:   24
    Socket(s):            1
    Stepping:             7
    CPU(s) scaling MHz:   27%
    CPU max MHz:          3900.0000
    CPU min MHz:          1000.0000
    BogoMIPS:             4800.00
```

### Memory Information

```
$ free -m
               total        used        free      shared  buff/cache   available
Mem:          515418       11412      502491        2645        7591      504006
Swap:           2047         895        1152
```

## Benchmark Setup

We use ANN-benchmarks to test evaluate our query performance.

