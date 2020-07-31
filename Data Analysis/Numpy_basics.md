
`import numpy as np`

Generate some random data
```python
data = np.random.randn(2, 3)
data
array([[-0.2047,  0.4789, -0.5194],
       [-0.5557,  1.9658,  1.3934]])
```

Multiplying data by 10
```python
data * 10

array([[-2.0471,   4.7894,  -5.1944],
       [-5.5573,  19.6578,  13.9341]])
```

```python
data + data

array([[-0.4094,  0.9579, -1.0389],
       [-1.1115,  3.9316,  2.7868]])
```

In the first example, all of the elements have been multiplied by 10. In the second, the corresponding values in each “cell” in the array have been added to each other.

