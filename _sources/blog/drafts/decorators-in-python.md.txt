```{post} 2222-02-22
:tags: sphinx
:author: Rajat Sethi
```

# Decorators


## Returning function

```{code-block} python
---
lineno-start: 1
---
def add(x, y):
    return x + y


def outer(func):
    def inner(*args, **kwargs):
        print("Executing")
        return func(*args, **kwargs)
    return inner


add_modified = outer(add)
```

```python
>>> print(add_modified(10, 20))
Executing
30
```






```{code-block} python
---
lineno-start: 1
---
import datetime



def add(x, y):
    return x + y


def timer(func):
    def inner(*args, **kwargs):
        print(f"Executing at {datetime.datetime.now()}")
        return func(*args, **kwargs)
    return inner


add_modified = timer(add)
```

```python
>>> print(add_modified(10, 20))
Executing at 2021-02-22 21:17:06.002724
30
```





```{code-block} python
---
lineno-start: 1
---
import datetime


def timer(func):
    def inner(*args, **kwargs):
        print(f"Executing at {datetime.datetime.now()}")
        return func(*args, **kwargs)
    return inner


@timer
def add(x, y):
    return x + y
```

```python
>>> print(add(10, 20))
Executing at 2021-02-22 21:20:28.247221
30
```





```{code-block} python
---
lineno-start: 1
---
```

```python
```






```{code-block} python
---
lineno-start: 1
---
```

```python
```






```{code-block} python
---
lineno-start: 1
---
```

```python
```






```{code-block} python
---
lineno-start: 1
---
```

```python
```






```{code-block} python
---
lineno-start: 1
---
```

```python
```






```{code-block} python
---
lineno-start: 1
---
```

```python
```






```{code-block} python
---
lineno-start: 1
---
```

```python
```






```{code-block} python
---
lineno-start: 1
---
```

```python
```






```{code-block} python
---
lineno-start: 1
---
```

```python
```






```{code-block} python
---
lineno-start: 1
---
```

```python
```






```{code-block} python
---
lineno-start: 1
---
```

```python
```






```{code-block} python
---
lineno-start: 1
---
```

```python
```





```{code-block} python
---
lineno-start: 1
---
```

```python
```





```{code-block} python
---
lineno-start: 1
---
```

```python
```




```{code-block} python
---
lineno-start: 1
---
```

```python
```





```{code-block} python
---
lineno-start: 1
---
```

```python
```





```{code-block} python
---
lineno-start: 1
---
```

```python
```







```{code-block} python
---
lineno-start: 1
---
```

```python
```