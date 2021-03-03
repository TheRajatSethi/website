```{post} 2021-03-02
:tags: python
:author: Rajat Sethi
```


# First Class Functions in Python

## What are first class functions?

A language is set to support first class functions when they can be treated like any other value. You can pass them to functions as arguments, return them from functions, and save them in variables.

First-class functions are important because they’re a basic requirement for writing higher-level abstractions with functions. First class functions are used in various abstractions like closures, decorator and more. First class functions also facilitate metaprogramming.

## Storing functions in a variable

Functions can be stored as a value can inside a variable. Few examples below.

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

In the above example `foo` function is stored in `y` variable. `y` can be executed exactly like `foo` can.


```{code-block} python
---
lineno-start: 1
---
double_it = lambda x : x * 2
```


```python
>>> double_it(10)
20

>>> double_it
<function <lambda> at 0x0000019EF46DA790>
```

Its not just named functions that can be stored in variables, even the anonymous lambda functions can be stored inside a variable.


## Passing functions as arguments

Functions can also be passed into arguments just like a Integer or String value is passed in an argument.

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

In the above example the function `foo` is passed as an argument inside the `bar` function.

## Returning function

A function can also return a function as shown below. The `bar` function returns the `foo` function which was defined above. The `foo` function could also have been defined inside the `bar` function which would have made it a nested function which you will see described below.


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

Having the above stated capabilities open up a lot of coding paradigms, one of them being the functional programming. The functional programming makes heavy use of the `map()`, `filter()` and `reduce()` functions.

In this section lets try and attempt to replicate some of the functionality of Python's map function.

Before we jump over to see how can we replicate the map function and create our own version of it lets check out the standard implementation. The standard `map` function takes in an iterable(s) and applies a specified function to each element in that iterable.


E.g. lets multiply everything in a list by 2.

```python
>>> list(map(lambda x: x*2, [10, 20]))
[20, 40]
```

Calculate the length of each element in the list.

```python
>>> tuple(map(len, ["USA", "Canada", "Australia", "Egypt", "Sweden"]))
(3, 6, 9, 5, 6)
```

Multiple iterators can be supplied. Here I have given two lists, they will be zipped and supplied as arguments to the function. Thus if you are providing two lists make sure the function is able to take in two arguments.

```python
>>> list(map(lambda x,y: x**y, [10, 20], [2, 3]))
[100, 8000]
```

I hope the above code snippets gave you some sense of the `map` function which you see accepts functions as arguments i.e. making use of functions as first class citizens. In the remainder of this section let build our own version of the `map` function. I'll call it `my_map`.

The below `my_map` function can take in a function and single iterable and apply that function to all the elements of that iterable. Note the line 2 is a generator expression in case the sequence is very long. Even the standard `map` does not do eager calculation.

```{code-block} python
---
lineno-start: 1
emphasize-lines: 2, 2
---
def my_map(func, l):
    return (func(element) for element in l)  # Generator Expression


def double(x):
    return 2*x
```

```python
>>> l = [10, 20]
>>> list(my_map(double, l))
[20, 40]
```

While our replica `my_map` took in a function and applied it to every element it still lacks the ability to take in multiple iterables as the standard `map` does. In the below attempt lets make the `my_map` function generic enough to handle multiple iterables.

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

As you see above our version of the `map` function is starting to behave a lot like the standard function. If you are interested you can attempt to create the following functions which make use of first class functions yourself as an exercise.

- `my_sort(iterable, custom_function)` - Replicates the behaviour of the sort function. The `custom_function` can be optional which defines the custom sort criteria.
- `my_reduce` - Replicates the behaviour of reduce.
- `my_filter` - Replicates the behaviour of filter.

## Simple Function Dispatcher

An another interesting use case of first class functions can be to create a function dispatcher. A function dispatcher calls a function based on some arguments/logic

Lets consider a use case where based on the value of the argument a particular function needs to call a different function dynamically i.e. we are not creating a bunch of if conditions and calling functions by name inside those if conditions.

Below are 3 functions and a dispatcher dictionary. The `dispatcher` function can call any function listed in the dictionary based on the `num` argument it receives. This makes the `dispatcher` function generic enough to call a particular function based on the arguments it receives. This is possible due to the Python programming language supporting functions as first class citizens.

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


## Building a Data Pipe Line generator

Before we jump into creating a data pipeline generator take a look at nested functions below. Python allows the creation of a function within a function (i.e. nested function). In this example we are just returning a function `func` which was created within the function `func_maker`. It applies a random power to the argument supplied.



```{code-block} python
---
lineno-start: 1
---
import random


def func_maker():
    def func(x: int):
        return x**random.randint(1, 10)
    return func


surprise_power = func_maker()
```

```python
>>> surprise_power(10)
1000
```

Below code is a quick demonstration of the power of first class functions. Using the `pipeline_creator` function the user has the ability to create linear pipelines which process data in sequence.

In data engineering it is common to clean, transform and store data. Thus I created 3 simple functions to do the same which act on string data. These functions can then be arranged in any order by calling the `pipeline_creator` function which gives the user ability to generate data transformation pipelines using simple functions.

```{code-block} python
---
lineno-start: 1
---
from itertools import zip_longest
import uuid
import json


def clean(data: str) -> str:
    exclude = ".,!()[]*'\n"
    maketrans_dict = str.maketrans(dict(zip_longest(exclude, "")))
    return data.translate(maketrans_dict)


def transform(data: str) -> dict:
    return {str(uuid.uuid4()) : data.lower()}


def store(data: dict):
    serialized_data = json.dumps(data)
    # actual storage omitted
    return serialized_data


def pipeline_creator(funcs: list):
    def func(data: str):
        pipeline = []
        for f in funcs:
            pipeline.append(f)
        for f in pipeline:
            data = f(data)
        return data
    return func

```

Lets create two pipelines `full_pipeline` and `partial_pipeline` which take in 3 and 2 functions respectively.

```python
>>> full_pipeline = pipeline_creator([clean, transform, store])
>>> partial_pipeline = pipeline_creator([clean, store])
>>> full_pipeline("Today. is monday!! () and tomorrow is tuesday")
{"b0571f93-c654-471c-be08-134eb52737a2": "today is monday  and tomorrow is tuesday"}

>>> partial_pipeline("Today. is monday!! () and tomorrow is tuesday")
'"Today is monday  and tomorrow is tuesday"'
```

## Conclusion

First class functions can be treated like any other value i.e. stored in a variable, returned from a function or passed as an argument. They can be used to build powerful programming constructs. 