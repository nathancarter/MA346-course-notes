#!/usr/bin/env python
# coding: utf-8

# # Processing the Rows of a DataFrame
# 
# <a href="../../_slides/chapter-11-slides.html">See also the slides that summarize a portion of this content.</a>

# ## Goal
# 
# Back in the early days of programming, when I was a kid, we wrote code with stone tools.
# 
# ![Image of cave man chiseling](_images/cave-man-public-domain.jpg)
# 
# And when we wanted to work with all the elements of an array, we had no choice but to write a loop.

# In[47]:


shipments_received = [ 6, 9, 3, 4, 0, 0, 10, 4, 7, 6, 6, 0, 0, 13 ]

total = 0
for num_received in shipments_received:
    total += num_received

total


# Most introductory programming courses teach loops, and for good reason; they are very useful and versatile!  But there are a few reasons we'll try to avoid loops in data work whenever we can.
# 
# First, we want to promote **readability** of our code.  Loops are always at least two lines of code in Python; the one above is three because it has to initialize the `total` variable to zero.  Many alternatives to loops can be done in just one line of code, which is more readable.
# 
# The more important reason is **speed.**  Loops in Python are not very efficient, and this can be a serious problem.  In the final project for MA346 in Spring 2020, many students came to my office hours with a loop that had been running for hours, and they didn't know if or when it would finish.  There are *many* ways to speed loops up, sometimes by just altering the loop, but usually by replacing the loop with something else entirely.
# 
# **In fact, that's the purpose of this chapter:  *What can I do to improve a slow loop?***
# 
# The title of the chapter mentions DataFrames specifically, because in data work we're almost always processing a DataFrame row-by-row.  But many of the techniques we'll cover apply to many different kinds of loops, with or without DataFrames.
# 
# An added benefit is that improving (or replacing) loops with something faster often means writing shorter or clearer code as well, achieving improvements in readability at the same time.

# ## The `apply()` function
# 
# The most common use of a loop is when we need to do the same thing to each element of a sequence of values.  Let's see an example.
# 
# ### Baseball example
# 
# In an earlier homework assignment, I provided a cleaned dataset of baseball players' salaries.  Let's take a look at the original version of the dataset when I downloaded it [from the web](https://data.world/natereed/baseball-salaries), before it was cleaned.

# In[48]:


import pandas as pd
df = pd.read_csv( '_static/baseball-salaries.csv' )
df.head()


# The "years" column looks particularly annoying.  Why does it say "1 (1991)" instead of just 1991?  Let's take a look at some other rows...

# In[49]:


df.iloc[14440:14445,:]


# Aha, some entries in the "years" column represent multiple years.  We might naturally want to split that column up into three columns: number of years, first year, and last year.  Creating each of the three new columns would be an exercise all on its own, so we will choose just one example, the task of extracting the first year from the text.  If we wrote a loop, it might go something like this.
# 
# ### Using a loop

# In[50]:


first_years = [ ]
for text in df['years']:
    if text[1] == ' ': # one-digit number of years
        first_years.append( int( text[3:7] ) )
    else: # two-digit number of years
        first_years.append( int( text[4:8] ) )
df['first_year'] = first_years
        
df.iloc[[0,14441],:] # quick spot check of our work


# The final column of the table immediately above shows that our loop seems to do the job.
# 
# But pandas' `apply()` function was made for the task of taking the same action on every entry in a Series or DataFrame.  You write `df['column'].apply(f)` to apply the function `f` to every entry in the chosen column.  For example, we could simplify our work above as follows.  The differences are noted in the comments.
# 
# ### Using `apply()`

# In[51]:


# No need to start with an empty list.
def get_first_year ( text ):     # Function name helps explain the code.
    if text[1] == ' ':
        return int( text[3:7] )  # Clearer and shorter than append().
    else:
        return int( text[4:8] )  # Clearer and shorter than append().
df['first_year'] = df['years'].apply( get_first_year )

df.iloc[[0,14441],:] # same check as before


# If we're honest, the code didn't get *that* much simpler.  But `apply()` is especially nice if the function we want to write is a function that already exists.  Here's a silly example, but it illustrates the point.

# In[52]:


df['name_length'] = df['name'].apply( len )
df.head()


# Using `apply()` will run a little faster than writing your own loop, but unless the DataFrame is really huge, you probably won't notice the difference, so speed is not a significant concern here.  But switching to the `apply()` form sets us up nicely for a later speed improvement [we'll discuss further below](#parallel-apply).
# 
# Although it's less often useful, you can use `df.apply(f)` to run `f` on each column of the DataFrame, or `df.apply(f,axis=1)` to run `f` on each row of the DataFrame.
# 
# There is a very similar pandas function called `map()`.  It behaves very similarly to `apply()`, with a few subtle differences.  This is unfortunate because in computer programming more broadly, the concepts of "map" and "apply" are often used synonymously/interchangeably.  So to have them behave almost the same (but slightly differently!) in pandas is unfortunate.  Oh well.  Here are the differences:
# 
# | Feature | `apply()` | `map()` |
# |---------|-----------|---------|
# | You can use it on DataFrames, as in `df.apply(f)` | Yes | No  |
# | You can provide extra `args` or `kwargs`          | Yes | No  |
# | You can use a dictionary instead of `f`           | No  | Yes |
# | You can ask it to skip NaNs                       | No  | Yes |
# 
# ```{admonition} Big Picture - Informally, map is the same as apply
# ---
# class: alert alert-primary
# ---
# In most programming contexts, including data work, if someone speaks of "mapping" or "applying" a function, they mean the same thing:  Automatically running the function on each element of a list or series.
#  * The function for this is often called `map()` or `apply()`, as in pandas, but not always.
#  * In mathematics, it's called using a function "elementwise," meaning on each element of a structure separately.
#  * In the popular language Julia, it's called "broadcasting" a function over an array or table.
# ```
# 
# The function that you give to `apply()` can't be just any function.  Its input type needs to match the data type of the individual elements in the Series or DataFrame you're applying it to.  Its output type will determine what kind of output you get.  For example, the `get_first_year()` function defined above takes strings as input and gives integers as output.  So using `apply(get_first_year)` will need to be done on a Series containing strings, and will produce a Series containing integers.
# 
# If you have a function that takes multiple inputs, you might want to bind some of the arguments so that it becomes a unary function and can be used in `apply()`.  Or you can use the `args` or `kwargs` feature of `apply()`, but we won't cover that in these course notes.  You can see a small example in [the pandas documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html).  We will, however, take a look at the possibility of using a dictionary with `map()`, because it is extremely useful.  We will consider a simple example application, but do a more sophisticated one in class.

# ### Using `map()`
# 
# Let's assume that the analysis we wanted to do cared only about whether the baseball player had an infield position (IF), outfield position (OF), was a pitcher (P), or a designated hitter (DH), and we didn't care about any other details of the position (such as first base vs. second base, or starting pitcher vs. relief pitcher).  We'd therefore like to simplify the "pos" column and convert all infield positions to IF, and so on.  First, let's see what all the positions are.

# In[53]:


df['pos'].unique()


# We could convert them with a big `if` statement, like you see here, but this is tedious and repetitive code.

# In[54]:


def simpler_position ( pos ):   # BAD STYLE.  See better version below.
    if pos == 'P':  return 'P'
    if pos == 'SP': return 'P'
    if pos == 'RP': return 'P'
    if pos == 'C':  return 'IF'
    if pos == '1B': return 'IF'
    if pos == '2B': return 'IF'
    if pos == '3B': return 'IF'
    if pos == 'SS': return 'IF'
    if pos == 'OF': return 'OF'
    if pos == 'LF': return 'OF'
    if pos == 'CF': return 'OF'
    if pos == 'RF': return 'OF'
    if pos == 'DH': return 'DH'

df['simple_pos'] = df['pos'].apply( simpler_position )
df.head()


# All the repetitive code is just establishing a simple relationship among some very short strings.  We could store that same relationship in a dictionary with many fewer lines of code.  Note that we must use `map()`, because `apply()` doesn't accept dictionaries.

# In[55]:


df['simple_pos'] = df['pos'].map( {
    'P':  'P',    'SP': 'P',    'RP': 'P',    'C':  'IF',
    '1B': 'IF',   '2B': 'IF',   '3B': 'IF',   'SS': 'IF',
    'OF': 'OF',   'LF': 'OF',   'CF': 'OF',   'RF': 'OF',   'DH': 'DH'
} )
df.head()


# In class, we will do a more complex example of applying a dictionary using `map()`.  Before class, you may want to glance back at Exercise 3 from [the Chapter 2 notes](chapter-2-mathematical-foundations), which shows you how to take two columns of a DataFrame representing a mathematical function and convert them into a dictionary for use in situations just like this one.  And be sure to complete the homework about the NPR dataset before class as well, because we will use that in our example!
# 
# Also, just to add to the confusion of too many pandas functions, there's another one called `replace` that can be used to apply a dictionary to one or more columns in a DataFrame.  So the code above that's written `df['pos'].map( { ... } )` could have been written `df['pos'].replace( { ... } )`.  I mention this option because it's a little more readable than "map," since "replace" is a more common English word.
# 
# ### Parallel `apply()`
# 
# I mentioned earlier that converting a loop into an `apply()` or `map()` call doesn't gain us much speed.  But it is also the first step in a process that can give a more significant speed improvement.  There's a Python package called [swifter](https://github.com/jmcarpenter2/swifter) that you can install using the instructions on that page.  Once it's installed, you can convert any code like `df['column'].apply(f)` easily into a faster version by replacing it with `df['column'].swifter.apply(f)`.  That's all!
# 
# Under the hood, swifter is trying a variety of speedup mechanisms (many of which we discuss in this chapter) and deciding which of them works best for your situation.  The most common one for large dataset is probably parallel processing.  This means that if your computer has more than one processor core (which most modern laptops do), then it can process more than one entry of the data at once, each on a separate core.
# 
# Without swifter, you could accomplish the same thing with code like the following.  (In fact, if you have trouble installing swifter, you can use this code instead.)

# In[56]:


# Use Python's built-in multiprocessing module to find your number of cores.
import multiprocessing as mp
n_cores = mp.cpu_count()

# Create a "pool" of functions that can work at the same time and run them.
pool = mp.Pool( n_cores )
df['simple_pos'] = pool.map( simpler_position, df['pos'], n_cores )

# Clean up afterwards.
pool.close()
pool.join()

# See result.
df.head()


# ## Map-Reduce
# 
# ```{admonition} Big Picture - Important phrases: map-reduce and split-apply-combine
# ---
# class: alert alert-primary
# ---
# Both *map-reduce* and *split-apply-combine* are data manipulation buzzwords that you'll want to be familiar with, for
#  * thinking about your own data manipulation work,
#  * discussing that work with coworkers, and
#  * knowing what people are saying in, e.g., interviews.
# 
# This section covers map-reduce and the next section covers split-apply-combine.
# ```
# 
# A map-reduce process is one that takes any list, *maps* a specific function across all entries of the list, then *reduces* those outputs down to a single, smaller result.  Consider the following picture, which shows a very simple map-reduce operation that takes a DataFrame about numbers of students and teachers over time and computes the highest student/teacher ratio across all semesters.
# 
# ![Illustration of Python code for mapping a DataFrame to student/teacher ratio, then computing the maximum](_images/map-reduce.png)
# 
# Let's actually do the above computation on some small sample (fictional) data:

# In[57]:


# setup - example tiny dataset (fake data)
sociology_department = pd.DataFrame( {
    'Year'       : [  2016,   2016,  2017,   2017,  2018,   2018,  2019,   2019,  2020,   2020 ],
    'Semester'   : [ 'Spr', 'Fall', 'Spr', 'Fall', 'Spr', 'Fall', 'Spr', 'Fall', 'Spr', 'Fall' ],
    '# Students' : [   177,    186,   167,    263,   180,    193,   189,    281,   201,    210 ],
    '# Teachers' : [     2,      2,     3,      4,     3,      2,     3,      4,     2,      2 ]
} )
sociology_department


# In[58]:


# map-reduce work, one line:
( sociology_department['# Students'] / sociology_department['# Teachers'] ).max()


# As mentioned earlier, "map" is a synonym for "apply," so the first step of the process applies the same operation to all rows of the DataFrame; in this case, that operation extracts two values from each row and computes the ratio of the two.  The "reduce" operation in this case is a simple `max()` operation, but it could be more complex in other examples.
# 
# If we wanted to actually use the pandas `apply` function, we could restructure the above code to use it, but it wouldn't be as clean.  Just to show that it can be done, I write it here, but the shorter version above is preferred.

# In[59]:


student_teacher_ratio = lambda row: row['# Students'] / row['# Teachers']
sociology_department.apply( student_teacher_ratio, axis=1 ).max()


# So a map-reduce operation involves two functions, the first performing a `map()` operation (as discussed earlier), and the second doing something new.  The function used for the reducing step must be something that takes an entire list or series as input and produces a single value as output.  The `max()` operation was used in the example above, but other operations are common, such as `min()`, `sum()`, `len()`, `mean()`, `median()`, and more.
# 
# Here are two other examples of map-reduce operations.  Notice that the map operation in the second one is extremely simple (just looking up a column) but it still fits the map-reduce pattern.
# 
# ```python
# # Average property size of a home in acres
# df_homes['lot size sq ft'].apply( sq_ft_to_acres ).mean()
# 
# # Largest property size of a home in square feet
# df_homes['lot size sq ft'].max()
# ```
# 
# ### Argmin and argmax
# 
# A very common function that shows up in statistics is called `argmin` (and its companion `argmax`).  These are also implemented in pandas and are very useful in map-reduce situations.  In the example above, let's say we didn't want to know the maximum student/teacher ratio, but we wanted to know in which semester that maximum ratio happened.  We can replace `max` in the above code with `argmax` to ask that question.

# In[60]:


( sociology_department['# Students'] / sociology_department['# Teachers'] ).argmax()


# The `argmax` function is short for "the argument that yields the maximum," or in other words, what value would I need to supply as *input* to the map function to get the maximum output?  In this case, the map function takes each row and computes its student/teacher ratio, so we're asking pandas, "When you found the maximum ratio, which row was the input?"  The answer was row 9, and we can see that it's the correct row as follows.

# In[61]:


sociology_department.iloc[9]


# While the pandas documentation for `argmin` and `argmax` suggest that they return multiple values in the case of ties, this doesn't seem to be true.  They seem to return the first index only.  You can therefore always rely on the result of `argmin`/`argmax` being a single value, never a list or series.  If you want the indices of all max/min entries, you will need to compute it another way.

# ### Map-reduce example: sample standard deviation
# 
# The formula for the standard deviation of a sample of data should be familiar you to from GB213.
# 
# $$ s=\sqrt{\frac{\sum_{i=1}^n (x_i-\bar x)^2}{n-1}} $$
# 
# Let's assume we've already computed the mean value $\bar x$.  Then computing the standard deviation is actually a map-reduce operation.  The map function takes each $x_i$ as input and computes $(x_i-\bar x)^2$ as output.  The reduce operation then does a sum, divides by $n-1$, and takes a square root.  We could code it like so:

# In[62]:


import numpy as np

example_data = df['first_year']
x_bar = example_data.mean()

def map_func ( x ):
    return ( x - x_bar ) ** 2
def reduce_func ( data ):
    return np.sqrt( data.sum() / ( len(data) - 1 ) )

reduce_func( example_data.map( map_func ) )


# Of course, we didn't have to code that.  There's already an existing standard deviation function built into pandas, and it gives almost exactly the same answer.  (I suspect theirs does something more careful with tiny issues of accuracy than my simple example does.)

# In[63]:


example_data.std()


# But it is still important to notice that the pattern in computing a sample standard deviation is a map-reduce pattern, because we cannot always rely on pandas to do computations for us.  For instance, if the data we were dealing with were many gigabytes spread over a database, we couldn't load it all into a pandas DataFrame in memory and then call `data.std()` to get our answer.
# 
# There are specialized tools in the industry for applying the map-reduce paradigm to databases (even if the database is enormous and spread over many different servers).  One famous example is [Apache Spark](https://spark.apache.org/), but there are many.
# 
# Many more examples of map-reduce from math and statistics could have been shown instead of the one above.  Any time a list of values collapses to give a single result, map-reduce is behind it.  This happens for summations, approximations of integrals (e.g., trapezoidal rule), expected values, matrix multiplication, computing probabilities from trees of possible outcomes, any weighted averages (chemical concentrations, portfolio values, etc.), and many more.

# ## Split-Apply-Combine
# 
# Data scientist and R developer Hadley Wickham seems to coin lots of important phrases.  Recall from [the Chapter 5 notes](chapter-5-before-and-after) that he introduced the phrase "tidy data."  He also introduced the phrase "split, apply, combine," in [this paper](https://www.jstatsoft.org/article/view/v040i01).
# 
# It is another extremely common operation done on DataFrames, and it is closely related to map-reduce, as we will see below.
# 
# Let's say you were concerned about pay equity, and wanted to compute the median salary across your organization, by gender, to get a sense of whether there were any important discrepancies.  The computation would look something like the following.  (We assume that the gender column contains either M for male, F for female, or a missing value for those who do not wish to classify.)
# 
# ![Illustration of Python code for grouping a DataFrame by gender, then mapping to salary, then computing the median within groups](_images/split-apply-combine.png)
# 
# As you can see from the picture, the first phase (called "split") breaks the data into groups by the categorical variable we care about---in this case, gender.  After that, each smaller DataFrame undergoes a map-reduce process, and the results of each small map-reduce get aggregated into a result, indexed by the original categorical variable.
# 
# Note that the output type of the split operation (which, in pandas, is a `df.groupby()` call) is *NOT* a DataFrame, but rather a collection of DataFrames.  It is essential to follow a `df.groupby()` call with the apply and combine steps of the process, so that the result is a familiar and usable type of object again---a pandas DataFrame.
# 
# The easiest type of split-apply-combine is shown in the picture above and can be done with a single line of code.  We'll compute minimum number of students by year with the DataFrame from our map-reduce example.

# In[64]:


sociology_department.groupby('Year')['# Students'].min()


# Split-apply-combine is actually a specific type of pivot table.  Thus split-apply-combine operations can be done on data in Excel as well, using its pivot table features.  We can even use `df.pivot_table()` to mimic the above procedure, as follows.  (Because we don't need data separated into separate columns, we don't provide a columns variable.)

# In[65]:


sociology_department.pivot_table( index=['Year'], columns=[], values='# Students', aggfunc='min' )


# ## More on math in Python
# 
# ### Arithmetic in formulas
# 
# Recall that pandas is built on NumPy, and in [Chapter 9 of the notes](chapter-9-math-and-stats) we talked about NumPy's support for vectorization.  If we have a Series `height` containing heights in inches and we need instead to have it in centimeters, we don't need to do `height.apply()` and give it a conversion function, because we can just do `height * 2.54`.  NumPy automatically *vectorizes* this operation, spreading the "times 2.54" over each entry in the `height` array.
# 
# This is quite natural, because we have mathematical notation that does the same thing (in math, not Python).  If you've taken a class involving vectors, you know that vector addition $\vec x+\vec y$ means to do exactly what NumPy does---add the corresponding entries in each vector.  Similarly, scalar multiplication $s\vec x$ means to multiply $s$ by each entry in the vector $\vec x$, just like `height * 2.54` does in Python.  So NumPy is not inventing something strange here; it's normal mathematical stuff.
# 
# NumPy supports vectorizing all the basic mathematical operations.  For example, if we have created a linear model $\hat y=\beta_0+\beta_1 x$ with parameters stored in Python variables `β0` and `β1`, we can apply it to an entire series of inputs `xs` at once with the following code, because NumPy knows how to spread both `+` and `*` across arrays.
# 
# ```python
# y_hat = β0 + β1 * xs
# ```
# 
# In fact, if we had actual `ys` that went with the `xs`, we could then compute a list of residuals all at once with `y_hat - ys`, or even compute the RMSE (root mean squared error) with code like this.
# 
# ```python
# np.sqrt( np.sum( ( y_hat - ys ) ** 2 ) / len( ys ) )
# ```
# 
# The subtraction with `-` and the squaring with `** 2` would all be spread across arrays of inputs correctly, because NumPy comes with code to support doing so.  This is very similar to the computation of RSSE that we discussed in Chapter 9.
# 
# ### Conditionals with `np.where()`
# 
# This removes a lot of the need for both loops and `apply()`/`map()` calls, but not all.  One of the first things that makes us think we might need a loop is when a conditional computation needs to be done.  For instance, let's say we were given a dataset like the following (made up) example.

# In[66]:


patients = pd.DataFrame( {
    'id' : [ 100615, 51, 100616, 83, 100607, 100618, 19, 65 ],
    'height' : [ 72, 158, 75, 173, 68, 67, 163, 178 ],
    'dose' : [ 2, 0, 2.5, 2, 0, 2, 2.5, 0 ]
} )
patients


# Let's imagine that we then found out that it was the result of merging data from two different studies, one done in the U.S. and one done in France.  The data with IDs that begin with 100 are from the U.S. study, where heights were measured in inches.  The data with two-digit IDs are from the French study, where heights were measured in cm.  We need to standardize the units.
# 
# We can't simply convert to cm with `patients['height'] * 2.54` because that would apply the conversion to all data rather than just the measurements in inches.  We need some conditional logic, perhaps using an `if` statement, to be selective.  Our first inclination might be a loop.

# In[67]:


# Before changing the contents, I'm going to make a backup,
# so that later I can show you a second method.
backup = patients.copy()

# solving the problem with a loop:
for index,row in patients.iterrows():
    if row['id'] > 100000:  # US data
        patients.loc[index,'height'] *= 2.54
patients


# Note that `row['height'] *= 2.54` actually wouldn't alter the DataFrame, so we're forced to use `patients.loc[]` instead.
# 
# But if you were trying to follow the advice in this chapter of the notes, you might switch to an `apply()` function instead.  The trouble is, it's a bit annoying to do, because we need the `if` to operate on the "id" column and the conversion to operate on the "height" column, so which one do we call `apply()` on?  We can call `apply()` on the whole DataFrame, but the loop is actually simpler in that case!
# 
# The solution here is to use NumPy's `np.where()` function.  It lets you select just which rows should get which type of computation, like so:

# In[68]:


# Let's get back the original data...
patients = backup.copy()

# solution with np.where():
patients['height'] = np.where( patients['id'] > 100000, patients['height'] * 2.54, patients['height'] )
patients


# The `np.where()` function works just like `=IF()` does in Excel, taking three inputs: a conditional, an "if" result, and an "else" result.  But the difference is that `np.where()` is vectorized, effectively doing an Excel `=IF()` on each entry in the Series separately.  You can read an `np.where()` function just like a sentence:
# 
# Where patient id is over 100000, do patient height times 2.54, otherwise just keep the original height.
# 
# In summary, thanks to `np.where()`, even many conditional computations don't require a loop or an apply; they can be done with NumPy vectorization as well.
# 
# ### Speeding up mathematics
# 
# There are also some very impressive tools for speeding up mathematical operations in NumPy a *LOT.*  I will not cover them here, but will list several below as opportunities for Learning On Your Own.  But I'll give a preview of one of the solutions, Cython.  Note that these speedup tools are relevant only if you have a very large dataset over which you need to do complex mathematical computations, so that you notice pandas behaving slowly, and thus you need a speed boost.
# 
# Let's say I have the following function that computes $n!$, the product of all positive integers up to $n$.  (This is not the best way to write this function, but it's just an example.)

# In[69]:


def factorial ( n ):
    result = 1
    for i in range( 1, n+1 ):
        result *= i
    return result

factorial( 5 )


# I can ask Jupyter to compile this into C code for me, so that it runs faster, as follows.
# 
# First, use one cell of the notebook to load the Cython extension.
# 
# ```python
# %load_ext cython
# ```
# 
# Then, ask Cython to convert your Python code into C.  This requires giving it some hints (highlighted in the comments below) about the data types of the variables.  In this simple case, they're all integers.
# 
# ```python
# %%cython -a
# def factorial ( int n ):   # n is an integer
#     cdef int result, i     # so are result and i
#     result = 1
#     for i in range( 1, n+1 ):
#         result *= i
#     return result
# ```
# 
# If you run the above code in Jupyter, it will show you an interactive display of the code it created and how much speedup you can expect.  The function still generates the same outputs as before, but typically much faster.  How much faster?  Check out the tutorial linked to below for more information.
# 
# ```{admonition} Learning on Your Own - CuPy (fastest option)
# ---
# class: alert alert-danger
# ---
# Doing certain types of computations can be sped up significantly by using graphics cards (originally designed for gaming rather than data science) instead of the computer's CPU (which does all the non-graphics computations).  See [this blog post](https://towardsdatascience.com/make-your-python-functions-10x-faster-142ab40b31a7) for information on CuPy, a Python library for harnessing your GPU to do fast arithmetic.
# 
# CuPy requires you to first describe to it the computation you'll want to do quickly, and it will compile it into GPU-friendly code that you can then use.  This is an extra level of annoyance for the programmer, but often produces the fastest results.
# ```
# 
# ```{admonition} Learning on Your Own - NumExpr (easiest option)
# ---
# class: alert alert-danger
# ---
# If you've already got some code that does the arithmetic operation you want on NumPy arrays (or pandas Series, which are also NumPy arrays), then it's pretty easy to convert that code to use NumExpr.  It doesn't give as big a speedup as CuPy, but it's easier to set up.  [See this blog post](https://towardsdatascience.com/speed-up-your-numpy-and-pandas-with-numexpr-package-25bd1ab0836b) for details, and note the connection to `pd.eval()`.
# ```
# 
# ```{admonition} Learning on Your Own - Cython (most flexible)
# ---
# class: alert alert-danger
# ---
# The previous two options work only for speeding up arithmetic.  To speed up any operation (including string manipulation, working with dictionaries, sets, or any Python class), you'll need Cython.  This is a tool for converting Python code into C code automatically, without your having to learn to program in C.  C code almost always runs significantly faster than Python code, but C is much less easy to use, especially for data work.  See [this tutorial](https://ipython-books.github.io/55-accelerating-python-code-with-cython/) on using Cython in Jupyter, plus the example below.
# ```
# 

# ## So do we *always* avoid loops?
# 
# No, there are some times when you might still want to use loops.
# 
# ### When to opt for a loop
# 
# The two most prominent times to choose loops are these.
# 
#  1. If the code you're running is a search for one thing, and you want to stop once it's found, a loop might be best.  Take the home mortgage database of 15 million records, for example.  Let's say you were looking for an example of a Hispanic male in Nevada applying for a mortgage for a rental property.  If you ask pandas to filter the dataset, it will examine all 15M rows and give you *all* the ones fitting these criteria.  But you just needed one.  Maybe you'd find it in the first 50,000 rows and not need to search the other 14.95 million!  A loop definitely has the potential to be faster in such a case.
#  
#  2. Sometimes the computation you're doing involves comparing one row to adjacent rows.  For example, you might want to find those days when the price of a stock was significantly more or less than it was on the two adjacent days (one before and one after).  Although it's possible to do this without a loop, the code is a harder to write and to read, as you can see in the example below.  With a loop, it's not as fast, but it's clearer.  So if speed isn't an issue, use the loop.
# 
# Let's see how we might write the code for the stock example just given, but instead of stock data, we'll use the (made up) student and teacher data from earlier.

# In[70]:


# get just the column I care about:
num_students = sociology_department['# Students']

results = [ ]
# For each semester execpt the first and last...
for index in sociology_department.index[1:-1]:
    # If it's bigger than the previous and the next...
    if num_students.loc[index] > num_students.loc[index-1] and        num_students.loc[index] > num_students.loc[index+1]:
        results.append( index )  # Save it for later

# Show me just the semesters I saved.
sociology_department.loc[results,:]


# Compare that to the same results computed using vectorization in NumPy rather than a loop.  If the data were large, this implementation would be faster, but it's definitely not as clear to read.

# In[71]:


# Get all but first and last, for searching.
to_search = sociology_department.iloc[1:-1]

# Compute arrays of previous/next quarters, for comparison.
previous_num_stu = sociology_department.iloc[:-2]
next_num_stu = sociology_department.iloc[2:]

# Adjust indices so they match the to_search Series.
previous_num_stu.index = previous_num_stu.index + 1
next_num_stu.index = next_num_stu.index - 1

# Do the computation using NumPy vectorized comparisons.
to_search[( to_search['# Students'] > previous_num_stu['# Students'] )         & ( to_search['# Students'] > next_num_stu['# Students'] )]


# Any time when speed isn't an issue, and you think the clearest way to write the code is a loop, then go right ahead and write clear code!  Loops aren't always bad.
# 
# ### Factoring computations out of the loop
# 
# Sometimes what's making a loop slow is a repeated computation that doesn't need to happen inside the loop.  How can we tell whether a computation needs to be in a loop or not?
# 
# The *loop variable* is the variable that immediately follows the `for` statement in a loop.  In the loop example above, that's the `index` variable.  Usually any computation inside the loop that doesn't use the `index` variable can be moved outside the loop, so that we run it just once, before the loop, and save time.
# 
# For example, in the final project some students did for MA346 in Spring 2020, some teams had a loop that processed a large database of baseball players, and tried to look their names up in a different database.  It went something like this:
# 
# ```python
# for name in baseball_df['player name']:
#     if name in other_df["Player's Name"]:
#         # then do stuff here
# ```
# 
# Because the two DataFrames were very large, this loop took literally hours to run on students' laptops, and made it impossible for them to improve their code in time to finish the project.  The first thing I suggested was to change the code as follows.
# 
# ```python
# for name in baseball_df['player name']:
#     if name in other_df["Player's Name"].unique():
#         # then do stuff here
# ```
# 
# The `.unique()` function computes a smaller list from `other_df['name']`, in which each name shows up only once.  This meant a smaller search to do, and sped up the loop, but even so, it wasn't fast enough.  It still took about 30 minutes, which made it hard for students to iteratively improve their code.
# 
# But notice that the loop variable, `name`, doesn't appear anywhere in the computation of `other_df["Player's Name"].unique()`.  So we're asking Python to compute that list of unique names over and over, each time through the loop.  Let's bring that outside the loop so we have to do it only once.
# 
# ```python
# unique_name_list = other_df["Player's Name"].unique()
# for name in baseball_df['player name']:
#     if name in unique_name_list:
#         # then do stuff here
# ```
# 
# This loop ran much faster, and most students were able to use it to do the work of their final project.
# 
# Note that this advice, factoring out a computation that does not depend on the loop variable, is sort of the opposite of abstraction.  In abstraction, you make the list of all the variables that your computation *does* depend on, and move those up to the top, as input parameters.  Here we're taking a look at which variables our computation *doesn't* depend on, so that we can move the computation itself up to the top, so it is done outside the loop.
# 
# ### Knowing how long you'll have to wait
# 
# It can be very frustrating to run a code cell and see no output for a long time, while the computer seems to be doing nothing.  We start to wonder whether it will take 15 seconds to process the data, and we should just have a little patience, or 15 minutes and we should go get a coffee, or 15 hours and we should give up and rewrite the code.  Which is it?  How can we tell except just waiting?
# 
# There are two easy ways to get some feedback as your loop is progressing.  The easiest one is to install the `tqdm` module, whose purpose is to help you see a progress bar for a long-running loop.  After following [tqdm's installation instructions](https://github.com/tqdm/tqdm#installation) (using `pip` or `conda`), just import the module, then take the Series or list over which you're looping and wrap it in `tqdm(...)`, as in the example below.
# 
# ```python
# from tqdm.notebook import tqdm
# 
# results = [ ]
# for index in tqdm( sociology_department.index[1:-1] ):  # <---- Notice tqdm here.
#     if num_students.loc[index] > num_students.loc[index-1] and \
#        num_students.loc[index] > num_students.loc[index+1]:
#         results.append( index )  # Save it for later
# sociology_department.loc[results,:]
# ```

# While the computation is running, a progress bar shows up in the notebook, filling as the computation progresses.  It looks like the following example.
# 
# ![A screenshot of a tqdm progress bar](_images/tqdm-progress-bar.png)
# 
# The numbers indicate that over 300 of the 1000 steps in that large loop are complete, and they have taken 12 seconds (written 00:12) and there are about 27 seconds left (00:27).  The loop completes about 25.02 iterations per second.  With a progress bar like this, even for a computation that might run for hours, you can tell very quickly how long you will have to wait, and whether it's worth it to wait or if you need to speed up your loop instead.

# ## When the bottleneck is the dataset
# 
# Sometimes, you can't get around the fact that you just have to process a lot of data, and that can be slow.  Unless you're working for a company that will provide you with some powerful computing resources in the cloud on which to run your Jupyter notebook, so that it runs faster than it does on your laptop (or the free Colab/Deepnote machines), you'll just have to run the slow code.  But there are still some ways to make this better.
# 
# **Don't run it more than you have to.**  Often, the slow code is something that happens early in your work, such as cleaning a huge dataset or searching through it for just the rows you need for your analysis.  Once you've written code that does this, save the result to a file with `pd.to_csv()` or `pd.to_pickle()` and don't run that code again.
# 
# Don't fall into the trap of thinking that all your code needs to be in one Python script or one Jupyter notebook.  If that slow code that cleaned your data never needs to be run again, then once you've run it and saved the output, save the script/notebook, close it, and start a new script or notebook to contain your data analysis code.  Then when you re-run your analysis, you don't have to sit around and wait for the data cleaning to happen all over again!
# 
# This advice is especially important if the slow part of your work requires fetching data from the Internet.  Network downloads are the slowest and least predictable part of your work.  Once it's been done correctly, don't run it again.
# 
# **Do your work on a small dataset.**  If the dataset you have to analyze is still large enough that your analysis code itself runs slowly as well, try the following.  Near the top of your file, replace the actual data with a small sample of it, perhaps using code like this.

# In[72]:


patients = patients.sample( 3 )
patients


# Now the entire rest of my script or noteboook will operate on only this tiny DataFrame.  (Obviously, you'd want to choose a number larger than three in your code!  I'm doing a tiny example here.  You might reduce 100,000 rows to just 1,000, for example.)
# 
# Then as you create your data analysis code, which inevitably involves running it many times, you won't have to wait for it to process all 100,000 rows of the data.  It can work on just 1,000 and run 100x faster.  When your analysis code works and you're ready to write your report, delete the code that creates a small sample of the data and re-run your notebook from the start, now opearting on the whole dataset.  It will be slower, but you have to sit through that only once.
# 
# *Danger!*  Don't forget to delete that cell when your code is polished and you want to do the real, final analysis!  I suggest adding a note in giant text at the end of your notebook saying something like, "Don't forget, before you turn this in, USE THE WHOLE DATASET!"  Then you'll remember to do that key step before you complete the project.
# 
# **If the dataset is truly huge,** so large that it can't be stored in your computer's memory all at once, then trying to load it will either generate out-of-memory errors or it will slow the process down enormously while the computer tries to use its hard drive as temporary extra memory storage.  In such cases, don't forget the tip at the end of [this DataCamp chapter](big-cheat-sheet.html#chapter-1-using-iterators-in-pythonland) about the `chunksize` parameter.  It lets you process large files in smaller chunks.
