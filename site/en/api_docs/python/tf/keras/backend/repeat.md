

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.repeat

``` python
repeat(
    x,
    n
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/keras/_impl/keras/backend.py).

Repeats a 2D tensor.

if `x` has shape (samples, dim) and `n` is `2`,
the output will have shape `(samples, 2, dim)`.

#### Arguments:

* <b>`x`</b>: Tensor or variable.
* <b>`n`</b>: Python integer, number of times to repeat.


#### Returns:

A tensor.