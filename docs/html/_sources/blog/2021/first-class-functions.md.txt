```{post} 2022-02-20
:tags: sphinx
:author: Rajat Sethi
```


# First Class Functions

## TODO ==> Add more examples with lambda

## What are first class functions?

A language is set to support first class functions when they can be treated like any other value. You can pass them to functions as arguments, return them from functions, and save them in variables.

First-class functions are important because they’re a basic requirement for writing higher-level abstractions with functions. First class functions are used in various abstractions like closures, decorator and more. First class functions also facilitate metaprogramming.

## Storing functions in a variable


```{code-block} python
---
lineno-start: 1
---
def foo():
    print("foo")
```


```python
>>> y = foo
>>> y is foo
True
>>> y == foo
True
>>> y()
foo
```

## Passing functions as arguments

```{code-block} python
---
lineno-start: 1
---
def bar(my_func):
    print(my_func.__qualname__)


def foo():
    pass
```

```python
>>> bar(foo)
foo
```


## Returning function

```{code-block} python
---
lineno-start: 1
---
def foo():
    pass

def bar():
    return foo
```

```python
>>> y = bar()
>>> y == foo
True
```


## Re-building Python's `map` function


```{code-block} python
---
lineno-start: 1
emphasize-lines: 2, 2
---
def my_map(l, func):
    return (func(element) for element in l)  # Generator Expression


def double(x):
    return 2*x
```

```python
>>> l = [10, 20]
>>> list(my_map(l, double))
[20, 40]
```

Making it generic enough to handle multiple iteratbles.

```{code-block} python
---
lineno-start: 1
---
def my_map(func, *args):
    return (func(*element) for element in zip(*args))


def double(x):
    return 2*x

def add(*args):
    return sum(args)
```

```python
>>> tuple(my_map(add, [10,20], [1, 2], [.1, .2]))
(11.1, 22.2)
```


## Simple Function Dispatcher


```{code-block} python
---
lineno-start: 1
---
def one():
    print("one")
    
    
def two():
    print("one")
    
    
def three():
    print("one")
    

DISPATCH = {1: one, 2: two, 3: three}


def dispatcher(num):
    DISPATCH[num]()
    
    

```

```python
>>> dispatcher(1)
one
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
