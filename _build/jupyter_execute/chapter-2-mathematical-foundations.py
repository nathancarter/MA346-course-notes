# Mathematical Foundations

<a href="../../_slides/chapter-2-slides.html">See also the slides that summarize a portion of this content.</a>

```{admonition} Big Picture
---
class: alert alert-primary
---
The contents of this page are extremely foundational to the course.  We will be weaving these foundations through every lesson in the course after this one.
```

(Not yet complete.)

## Functions

**Definition:** A *function* is any method for taking a list of inputs and determining the corresponding output.

### Examples of functions

**Math:** We can write functions as in an algebra or calculus course, with notation like this:
 * $ f(x)=x^2-5 $
 * $ g(x,y,z)=\frac{x^2-y^2}{z} $

How is this a method for turning inputs into outputs?  Given an input like $x=2$, I can substitute it into $f(x)=x^2-5$ to get $2^2-5$ and perform arithmetic to get $-1$.  There are also computer programs into which you can type mathematical notation and ask it to apply the function for you.

**English:** We can write functions in plain English (or any other natural language, but we'll use English).  To do so, we write a *noun phrase,* and include blanks where the inputs belong:
 * the capitol of <u>&nbsp; &nbsp; &nbsp; &nbsp;</u>
 * the difference in ages between <u>&nbsp; &nbsp; &nbsp; &nbsp;</u> and <u>&nbsp; &nbsp; &nbsp; &nbsp;</u>

How is this a method for turning inputs into outputs?  Given an input like France, I can substitute it into "the capitol of <u>&nbsp; &nbsp; &nbsp; &nbsp;</u>" to get "the capitol of France" and use my knowledge to get Paris.  If it were a capitol I didn't know, I could use the Internet to find out.

**Python:** We can write functions in Python (or other programming languages, but this course focuses on Python), like this:

def square ( x ):
    return x**2

def is_a_long_word ( word ):
    return len(word) > 8

How is this a method for turning inputs into outputs?  I can ask Python to do it for me!

square(50)

is_a_long_word( 'Hello' )

**Tables:** Any two-column table can work as a function, if we follow a few conventions.  First, the left column will list the possible inputs to the function and second, the right column will list the corresponding outputs.  Third, each input must show up only once in the table, so there's no ambiguity about what its corresponding output is.  Here's an example, which converts Bentley email IDs to real names for a few members of the Mathematical Sciences Department:

| User ID | Name |
|---------|------|
| aaltidor | Alina Altidor |
| mbhaduri | Moinak Bhaduri |
| wbuckley | Winston Buckley |
| ncarter | Nathan Carter |
| lcherveny | Luke Cherveny |

(We could add more names, but it's just an example.)

How is this a method for turning inputs into outputs?  Using the fundamental operation of *lookup,* something that shows up in numerous places when working with data.  (We'll return to the concept of lookup at the end of this chapter.)  Given a User ID as input, we look for it in the first column of the table, and once it's found, the appropriate output is right next to it in the right column.

**Others:** Later in the course we will see other ways to represent functions, but the ones above are the most common.

### Which way is best?

The examples above show that you can express functions using math, English, Python, tables, and more.  Although none of these ways is always better than the others, we will typically give functions names and refer to them by those names.  This happens in English, math, and computer science.
 * In English:  We might call the table shown above a "name lookup table."
 * In Math:  Rather than writing out $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$ all the time, people just use the short name "the quadratic formula."
 * In Python:  The `def` keyword in Python is for giving names to functions so that you can use them later by just typing their name.

### Why care about functions?

The concept of a function was invented because it represents an important component of how humans think about the processing of information.  As you've seen above, functions show up in ordinary language, in mathematics, in tables of data, and code that processes data.  Even people who don't do data work use functions unknowingly all the time when they talk about information, as in:
 * I don't know all the state capitols.
 * You better learn your times tables.
 * What's Kayla's phone number?

Unsurprisingly, functions show up all over the place in data science.  In particular, when working with a pandas DataFrame, we use functions often to summarize columns (such as compute the max, min, or mean) or to compute new columns, as in this example:

```python
df['Per capita cost'] = df['Cost'] / df['Population']
```

## Writing functions in Python

In MA346, we'll almost always want the functions we use to be written in Python, so that we can run them on data.  Let's practice writing some functions in Python.

```{admonition} Exercise 1 - from mathematics
---
class: alert alert-secondary
---
Write a function `solve_quadratic` that takes as input three real numbers $a$, $b$, and $c$, and gives as output a list of all real number solutions to the equation $ax^2+bx+c=0$.  (It can return an empty list if there are no real number solutions.)

Example: `solve_quadratic(1,0,-4)` would yield `[-2,2]` because $1x^2+0x+(-4)=0$ is the same equation as $x^2=4$.
```

The above exercise requires only the basic arithmetic built into Python, but when we do more advanced mathematics and statistics, we will import tools like [numpy](https://numpy.org/) and [scipy](https://www.scipy.org/).

````{admonition} Exercise 2 - from English
---
class: alert alert-secondary
---
Write a function `last_closing_price` that takes as input a NYSE ticker symbol and gives as output the price of one share at the last closing time of the NYSE.  Hints:
 * The URL https://finance.yahoo.com/quote/GOOG gives data for Alphabet, Inc.  A similar URL works for any ticker symbol.
 * You can extract all tables from a web page as pandas DataFrames as follows:
```python
data_frames = pd.read_html( 'put the URL here' )
```
 * That page has only one table, so it will be `data_frames[0]`.

Example: `last_closing_price('GOOG')` yielded something like `1465.85` in mid-June 2020.
````

It is not always guaranteed that you can turn an idea expressed in English, like "look up the last closing price of a stock," into Python code.  For instance, no one knows how to write code that answers the question, "given a digital photo as input, return the year in which the photo was taken."  But coming up with creative ways to answer important questions in code is a very valuable skill we will work to develop.

````{admonition} Exercise 3 - from a table
---
class: alert alert-secondary
---
Write a function `country_capitol` that takes as input a string containing a country name and gives as output a string containing the name of the country's capitol.  Hints:
 * A list of countries and capitols appears here: https://www.boldtuesday.com/pages/alphabetical-list-of-all-countries-and-capitals-shown-on-list-of-countries-poster
 * To convert two columns of a pandas DataFrame into a Python `dict` for easy lookup, try the following.
```python
D = dict( zip( df['input column name'], df['output column name'] ) )
```

Example: `country_capitol('JORDAN')` would yield `'AMMAN'`.
````

Why do you think the `dict(zip())` trick given above works?  What exactly is it doing?

---
(I STOPPED WRITING HERE; BEGIN HERE NEXT TIME.)

---

## Terminology

 * Data types, including input and output types (almost the same thing as domain and range in mathematics)
 * Arity (unary, binary, ternary, nobody goes beyond that; most often people say "two-parameter function" instead)

## Relations

A relation is a function whose output is always true or false, i.e., its output type is bool.

Examples of relations:
 * Standard math equations/inequalities, like $x^2+y^2\ge z^2$ or $x\ge 0$
 * Any English declarative sentence with blanks, like "`__X__` is the capitol of `__Y__`" or "`__X__` is a fruit."
 * Any Python function that returns bool, like `def R(a,b): return a in b[1:]` or `def is_primary_color(c): return c in ['red','green','blue']`
 * Any set, and things are true if you find them in the set and false if you don't.  In particular:
   * A table whose rows are all the lists of inputs for which the relation is true.  For example, the capitol city relation above could be represented as a table of all country-capitol pairs.
   * *Every DataFrame is a relation.  Every SQL table is a relation.  SQL is an implementation of "relational algebra."*  (Mostly.  DataFrames can have duplicate rows, and SQL tables can if we ignore the index.  This is a difference between them and mathematical relations.)
 * Later in the class we'll see even other ways to represent functions.
 * The mathematical concept of a relation exists because it represents how humans think about a lot of things.  Highlight examples from everyday language that show that we talk and think this way all the time, even in non-technical domains (like "is older than" and many more).

Although these are all ways to express a relation, we typically *talk about* relations by using simple phrases, like "being a fruit" or "the less than relation for numbers" or "has more employees than."  Those phrases are almost always how we talk about relations, but they are not relations; just shorthand intuitive phrases for relations.

Relations are often used on datasets for *filtering*.  `df[relation on rows]` selects a subset of the df and returns it as a new df (or, rather, a view on the original).

## Relations and functions in data

Consider several real world datasets and ask, for each, which functions or relations show up in it.
 * Ask about input type/output type/totality/arity for each
 * Make sure you hit some situations where either you or they or both have no idea what the answer is because of lack of domain expertise.  Use this to highlight the importance of having a domain expert on your team.
 * Make sure you hit some functions that are invertible and some that aren't, for later reference.

## Connections between functions and relations

What are the similarities/differences between functions and relations?
 * On the one hand, a relation is a special kind of function; its outputs can't be just anything; they must be either true or false only.  (As in our definitions.)
 * On the other hand, a function is a special kind of relation: because we restrict it so that each $x$ relates to exactly one $y$, you can "apply" $f$ and get a single answer.
 * You can "apply" a relation like a function if you don't mind getting multiple outputs; you just can't write this inside a mathematical expression without it getting confusing, so we don't.

Let's get technical for a second:
 * A function is a relation in which *for each* input, *there is exactly one* output.
 * Point out the earlier example of an invertible function, and that it simply means swapping two columns in the data table that defines the function.
 * In other words, an invertible function is a relation that's also a function when you swap inputs and outputs; a function is invertible if *for each* output, *there is exactly one* input.

## An extremely common data operation: Lookup

Things to think about regarding the concept of "lookup":
 * Let's say we've got a Python list `L`.  How would you describe looking up `L[i]` in the list…is it like a function or a relation?  What are the input and output types?
 * Let's say we've got a Python dict `D`.  How would you describe looking up `D[key]` in the dict…is it like a function or a relation?  What are the input and output types?
 * Let's say we've got a pandas DataFrame `df`.  How would you describe looking up `df[df.X==Y].Z` in the DataFrame…how is it like a function, a relation, both, or neither?  What are the relevant inputs and outputs?

Conclusion: Sometimes "lookup" is a function and sometimes it's a relation.  In this last example, you can force it to be a function with `.iloc[0]` on the end.

Later in the course we will see that `df1.join(df2)` is highly related (sort of a vectorized lookup), and thus so are SQL joins, which are essentially the same