```{post} 2021-02-21
:tags: sphinx
:author: Rajat Sethi
```

# Blogging with Sphinx

## What is Sphinx?

Sphinx is a document generator tool which was originally written for generating Python documentation. Sphinx uses reStructuredText as its markup language but you can write in markdown too.

## Blogging using Sphinx

I have created this blog using [Sphinx](https://www.sphinx-doc.org/en/master/) and its related technologies with inspiration from [Predictably Noisy](https://predictablynoisy.com/posts/2020/sphinx-blogging/). While there are many static site generators available such as Hugo, Jekyll and others I am familiar with Python's ecosystem the most which led to my decision of using Sphinx. The bonus is that using [myst_nb](https://myst-nb.readthedocs.io/en/latest/) or [nbsphinx](http://nbsphinx.readthedocs.io/) [Jupyter notebooks](https://jupyter.org/) can be directly rendered into articles or pages for the website. As per my knowledge none of the other popular static site generators provide ability to render Jupyter notebooks directly into blog posts. In addition to that Sphinx gives you a rich markup to write your articles.

```{image} https://www.sphinx-doc.org/en/master/_static/sphinxheader.png
:class: bg-dark
:target: https://www.sphinx-doc.org/en/master/
```


Tools used in this blog.
- Sphinx - [Docs](https://www.sphinx-doc.org/en/master/)
- Ablog - [Docs](https://ablog.readthedocs.io/)
- MyST{NB} - [Docs](https://myst-nb.readthedocs.io/en/latest/) 
- Pydata theme - [Docs](https://pydata-sphinx-theme.readthedocs.io/en/latest/index.html)
- Github Pages - Hosting Platform
- Domain name provider of your choice e.g. GoDaddy

Using the above tools the user has the ability to write in the markdown syntax or the restructured text syntax. You can use myst_nb or nbsphinx to parse the markdown syntax in both markdown files and Jupyter notebooks.

There are many different themes available for Sphinx but I am using the Pydata theme. It should be fairly easy for someone to set up a similar structure who is familiar with the aforementioned tools.

## The power of ReStructured Text

ReStructured text gives you the power to write and express complex markups easily which includes the below listed directives.
- admonitions
- code blocks
- tables
- footnotes
- references 
- and more ...


A brief demonstration of the rich markup capability. For more details you can refer to [this link](https://myst-parser.readthedocs.io/en/latest/) for writing in markdown files and [this link](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) for writing in ReStructured text files. I am bit biased towards writing in markdown as I have been doing so for years thus I have chosen the MySt parser but both are equally good choices. ReStructured is widely used in the Python community.

**Code Block**

Code blocks for various languages are supported. You can put in line numbers and emphasise selected lines as well. You can also include code from source files if needed.


Python Code

```{code-block} python
---
lineno-start: 1
emphasize-lines: 1, 3
---
# Python demo.py

class X:
    
    def __init__(self,foo):
        self.foo = foo
```

C Code

```{code-block} c
---
lineno-start: 10
emphasize-lines: 1, 3
---
// C demo.c 

#include <stdio.h>
int addition(int num1, int num2)
{
     int sum;
     /* Arguments are used here*/
     sum = num1+num2;

     /* Function return type is integer so we are returning
      * an integer value, the sum of the passed numbers.
      */
     return sum;
}
```

**Admonitions**

Admonition styles and directives.

```{note} My markdown link
Here is [markdown link syntax](https://jupyter.org)
```

```{warning} My markdown link
Here is [markdown link syntax](https://jupyter.org)
```


**Equations**

Support for math and equations.

```{math} e^{i\pi} + 1 = 0
---
label: euler
---
```

**Tables**

Support for tables.

```{list-table}
:header-rows: 1
:widths: 10 20 20

* - Token
  - Description
  - Example
* - FrontMatter
  - A YAML block at the start of the document enclosed by `---`
  - ```yaml
    ---
    key: value
    ---
    ```
```


---

**Footnotes**

A longer footnote definition.[^mylongdef]

[^mylongdef]: This is the _**footnote definition**_.

    That continues for all indented lines

    - even other block elements

    Plus any preceding unindented lines,
that are not separated by a blank line

This is not part of the footnote.