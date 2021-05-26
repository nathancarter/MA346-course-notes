#!/usr/bin/env python
# coding: utf-8

# # Abstraction
# 
# <a href="../../_slides/chapter-7-slides.html">See also the slides that summarize a portion of this content.</a>
# 

# ## Abstract vs. concrete
# 
# Abstract and concrete are at opposite ends of a spectrum; concrete refers to specific things, usually with more details in them, and abstract refers to general principles or ideas, usually unconnected to any specific example.  The following table may help clarify this.
# 
# |       | Concrete (or specific) | Abstract (or general) |
# |-------|----------------------|------------------------|
# | Example from science: | When we drop things, they fall to earth. | Gravitation obeys the principle $G_{\mu v}+\Lambda g_{\mu v}=\frac{8\pi G}{c^4}T_{\mu v}$ |
# | Example from business: | That startup failed because each partner tried to pull it in a different direction. | Organizations need everyone to pursue a single, clear vision. |
# | Example from ethics: | The Nazis' attacks on the Jews were a great evil. | Systematically disadvantaging any racial group is wrong. |
# 
# *Abstraction* is therefore the process of moving from the concrete toward the abstract, or from the specific to the general.  Therefore it's also called *generalization.*  Humans are pretty good at learning general principles from specific examples, so this is a natural thing for us to do.
# 
# It's very useful in all kinds of programming, including data-related work, so it's our focus in this chapter.

# ## Abstraction in mathematics
# 
# ### Example 1: Algebra class
# 
# My kids are teenagers and have recently taken algebra classes where they learned to "complete the square."  This procedure takes a quadratic equation like $16x^2-9x+5=0$ and manipulates it into a form that's easy to solve.
#  * Each homework problem was a *specific* example of this technique.
#  * If you apply the technique to the equation $ax^2+bx+c=0$, the result is the quadratic formula, $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$, a *general* solution to all quadratic equations.
# 
# Abstraction from the specific to the general tends to create more powerful tools, because they can be applied to any specific instance of the problem.  The quadratic formula is a powerful tool because it can solve any quadratic equation.

# ### Example 2: Excel formulas
# 
# If you took the grading policy out of the syllabus for this class, you could compute your grade in the course based on your scores on each assignment.  You could do this by hand with pencil and paper, or with a calculator.  Doing so would give you one specific course grade, for the specific assignment grades you started with.
# 
# Alternately, you could fire up a spreadsheet like Excel, and create cells for each assignment's score, then create formulas that would do the appropriate computation and give you the corresponding course grade.  This general solution works for any specific assignment grades you might type into the spreadsheet's input cells.
# 
# Again, the general version is more useful.

# ### Observations
# 
# Both of these mathematical examples involved replacing numbers with variables.  In Example 1, the coefficients in the specific example $16x^2-9x+5=0$ turned into $a$, $b$, and $c$ in $ax^2+bx+c=0$.  In Example 2, you didn't write formulas that had specific scores in them (as you would have if computing the scores by hand), but wrote formulas that contained Excel-style variables, which have names like A5 and B14, that come from the relevant cells.  In math (and in programming as well), abstraction typically involves *replacing specific constants with variables.*
# 
# Once we've rephrased our computation in terms of variables, we can do many different mathematical operations with it.
# 
#  1. We can think of our computation as a function.
#      * In Example 1, the quadratic formula can be seen as a function that takes as input the values $a,b,c$ and yields as output the two solutions of the equation.
#      * In Example 2, the Excel formulas can be seen as a function that take the assignment grades as input and yield the course grade as output.
#  2. We can ask what happens when one of the variables changes, a question that calculus focuses on.
#      * For instance, you could ask what happens to your computation as one of the variables gets larger and larger.  (In calculus, we wrote this as $\lim_{x\to\infty}$.)
#      * Or you could ask how quickly the result of the computation responds to changes in one input variable.  (In calculus, we wrote this as $\frac{d}{dx}$.)
#  3. We can make statements about the computation in terms of the input variables.
#      * In Example 1, we might say that "Every quadratic equation has two complex number solutions."
#      * In Example 2, we might say that "It's still possible for me to get an A- in this course if my final exam score is good enough."
# 
# The statement you just read about every quadratic equation is a *universal* statement, also called a "for all" statement.  You could rephrase it as:  For all inputs $a,b,c$, the outputs of the quadratic formula are two complex numbers.  The statement from Example 2 is an *existence* statement, also called a "for some" statement.  You could rephrase it as:  For some final exam scores, my final course grade is still a 4.0.  For all/for some statements are central to mathematics and we will see them show up a lot.  "For all" and "for some" are called *quantifiers* and are sometimes written $\forall$ (for all) and $\exists$ (for some, or "there exists").

# ## Abstraction in programming
# 
# ```{admonition} Big Picture - The value of abstraction in programming
# ---
# class: alert alert-primary
# ---
# This section covers the value of abstraction for every programmer.  It is a valuable viewpoint to have and skill to be able to employ.  See the rest of this section for details on how it works and how to use it.
# ```

# ### Example 3: Copying and pasting code
# 
# Best practices for coding include writing DRY code, where DRY stands for Don't Repeat Yourself.  If you find yourself writing the same code (or extremely similar code) more than once, especially if you're copying and pasting, this is a sure sign that you are not writing DRY code and should try to correct this style error.  The way to correct it is with abstraction, as shown below.  (The opposite of DRY code is WET code--Write Everything Twice.  Don't do that.)
# 
# In Spring and Fall 2020, my MA346 students analyzed COVID-19 case data from various states in the U.S.  They had DataFrames with case numbers, death numbers, and recovery numbers.  Let's imagine that they wanted to keep just the first 8 columns and give them clearly readable names.  The code might look like this.
# 
# ```python
# df_cases.drop( columns=df_cases.columns[8:], inplace=True )
# df_cases.columns = [ 'State', 'Country', 'Latitude', 'Longitude',
#                      'January', 'February', 'March', 'April' ]
# df_deaths.drop( columns=df_deaths.columns[8:], inplace=True )
# df_deaths.columns = [ 'State', 'Country', 'Latitude', 'Longitude',
#                       'January', 'February', 'March', 'April' ]
# df_recoveries.drop( columns=df_recoveries.columns[8:], inplace=True )
# df_recoveries.columns = [ 'State', 'Country', 'Latitude', 'Longitude',
#                           'January', 'February', 'March', 'April' ]
# ```
# 
# The typical way of creating code like what's shown above is to write just the code for `df_cases`, run it, verifiy that it works, and then copy and paste it twice and change the details to apply the same code to the other two DataFrames.  But this code can be made much cleaner through abstraction.
# 
# Rather than copy and paste the code and change key parts of it, replace those key parts with a *general* (that is, abstract) variable name, and then turn the code into a function.  Since this code drops the columns we don't care about, we could have made that the name of the function.
# 
# ```python
# def drop_unneeded_columns ( df ):
#     df.drop( columns=df.columns[8:], inplace=True )
#     df.columns = [ 'State', 'Country', 'Latitude', 'Longitude',
#                    'January', 'February', 'March', 'April' ]
# ```
# 
# Once this general version is complete, we can apply it to each specific case we need.
# 
# ```python
# drop_unneeded_columns( df_cases )
# drop_unneeded_columns( df_deaths )
# drop_unneeded_columns( df_recoveries )
# ```
# 
# There are several advantages to this new version.
# 
#  1. While it is still six lines of code, half of them are much shorter, so there's less to read and understand.
#  2. What the code is doing is more obvious, because we've given it a name; we're obviously dropping columns we don't need.
#  3. It wasn't immediately obvious in the first version of the code that we were repeating the same procedure three times.  Now it is.
#  4. If you later need to change which columns you keep or how you name them, you have to make that change in only one place (inside the function).  Before, you would have had to make the same change three times.
#  5. Also, if you tried to make a change to the code later, but accidentally forgot to change one of the three copies, you'd have broken your code and maybe not realized it.
#  6. You could share this same function to other notebooks or with other coders if needed.
# 
# So the moment you find yourself copying and pasting code, remember to stay DRY instead---create a function and call it multiple times, so that you get all these benefits.

# ### Alternatives
# 
# Another method of abstraction would have been a loop instead of a function.  Since the original code does the same thing three times, we could have rewritten it as follows instead.
# 
# ```python
# for df in [ df_cases, df_deaths, df_recoveries ]:
#     df.drop( columns=df.columns[8:], inplace=True )
#     df.columns = [ 'State', 'Country', 'Latitude', 'Longitude',
#                    'January', 'February', 'March', 'April' ]
# ```
# 
# This has all the same benefits as the previous method, except for \#6.
# 
# One could even combine the two methods together, as follows.
# 
# ```python
# def drop_unneeded_columns ( df ):
#     df.drop( columns=df.columns[8:], inplace=True )
#     df.columns = [ 'State', 'Country', 'Latitude', 'Longitude',
#                    'January', 'February', 'March', 'April' ]
# 
# for df in [ df_cases, df_deaths, df_recoveries ]:
#     drop_unneeded_columns( df )
# ```

# ### Example 4: Testing a computation
# 
# Let’s imagine that the same student as above, who has COVID-19 data, wants to investigate its connection to the polarized political climate in the U.S., since COVID-19 response has been very politicized. They want to ask whether there’s any correlation between the spread of the virus in a state and that state’s prevailing political leaning. So the student gets another dataset, this one listing the percentage of registered Republicans and Democrats in each U.S. state. They will want to look up each state in the COVID-19 dataset in this new dataset, to connect them. They try this:
# 
# So the student gets a second dataset, this one listing the percentage of registered Republicans and Democrats in each U.S. state.  They will want to look up each state in the COVID-19 dataset in this new dataset, to connect them.  They try this:

# In[1]:


# load political data
import pandas as pd
df_registration = pd.read_excel( '_static/political-registrations.xlsx',
                                 sheet_name=0 )

# make dictionaries for easy lookup:
percent_republican = dict( zip( df_registration['State'], df_registration['R%'] ) )
percent_democratic = dict( zip( df_registration['State'], df_registration['D%'] ) )

# see if it works on Alaska:
percent_republican['AK']


# Great, progress!  Let's just try one or two more random examples to be sure that wasn't a fluke.

# In[2]:


# see if it works on Alabama:
percent_republican['AL']


# Uh-oh.  Checking [the website where they got the data](http://centerforpolitics.org/crystalball/articles/registering-by-party-where-the-democrats-and-republicans-are-ahead/), the student finds that Alabama doesn't register voters by party, so Alabama isn't in the data.  They need some code that won't cause errors for any state input, so they update it:

# In[6]:


import numpy as np
percent_republican['AL'] if 'AL' in percent_republican else np.nan


# This technique looks like it will work for any input, because instead of giving an error it returns NaN.  Because NaN is the standard way to represent missing values, this makes sense.  Good, let's turn it into a function and test that function.

# In[7]:


def get_percent_republican ( state_code ):
    return percent_republican[state_code] if state_code in percent_republican else np.nan
def get_percent_democratic ( state_code ):
    return percent_democratic[state_code] if state_code in percent_democratic else np.nan

get_percent_republican( 'AK' ), get_percent_republican( 'AL' )


# In[8]:


get_percent_democratic( 'AK' ), get_percent_democratic( 'AL' )


# So Example 4 has shown us that abstracting a computation into a function can be done as part of an ordinary coding workflow:  Start easy, by doing the computation on just one input and get that working.  Once it does, test it on some other inputs.  Then create a function that works in general.
# 
# The benefits of this include all the benefits discussed after Example 3, plus this one:  The student wanted to run this computation for every row in a DataFrame.  That's easy to do now, with code like the following.
# 
# ```python
# df_cases['percent_republican'] = df_cases['Province/State'].apply( get_percent_republican )
# df_cases['percent_democratic'] = df_cases['Province/State'].apply( get_percent_democratic )
# ```

# ### Little abstractions (`lambda`)
# 
# When it would be handy to create a function, but the function is so small that it seems like giving it a name with `def` is overkill, you can use Python's `lambda` syntax to create the function.
# 
# (The name comes from the fact that some branches of computer science use notation like $\lambda x.3x+1$ to mean "the function that takes $x$ as input and gives $3x+1$ as output."  So they could write $f=\lambda x.3x+1$ instead of $f(x)=3x+1$.)
# 
# For example, let's say you have a dataset in which each row represents an hour of trading on an exchange, and the volume is classified using the codes 0, 1, 2, and 3, which stand (respectively) for low volume, medium volume, high volume, and unknown (missing data).  We'd like the dataset to be more readable, so we'd like to replace those numbers with the actual words low, medium, high, and unknown.  We could do it as follows.
# 
# ```python
# def explain_code ( code ):
#     words = [ 'low', 'medium', 'high', 'unknown' ]
#     return words[code]
# 
# df['volume'] = df['volume'].apply( explain_code )
# ```
# 
# But this requires several lines of code to do this simple task.  We could compress it into a one-liner as follows.
# 
# ```python
# df['volume'] = df['volume'].apply( lambda code: ['low','medium','high','unknown'][code] )
# ```
# 
# The limitation to Python's `lambda` syntax is that you can put inside only a single expression, which the function will return.  A function that needs to do several preparatory computations before returning an answer cannot be converted into `lambda` form.

# ## How to do abstraction
# 
# If you aren't sure how to take specific code and turn it into a general function, I suggest following the steps given here.  Once you've done this a few times, it will come naturally, without thinking through the steps.
# 
# Let's use the following example code to illustrate the steps.  It's useful in DataFrames imported from a file where dollar amounts were written in a form like $4,320,000.00, which pandas won't recognize as a number, because of the commas and the dollar sign.  This code converts such a column to numeric.  Since it's so useful, we may want to use it on multiple columns.
# 
# ```python
# df['Tuition'] = df['Tuition'].str.replace( "$", "" ) # remove dollar signs
# df['Tuition'] = df['Tuition'].str.replace( ",", "" ) # remove commas
# df['Tuition'] = df['Tuition'].astype( float )        # convert to float type
# ```
# 
# ### Step 1:  Decide which parts of the code are customizable.  That is, which parts of the code might change the next time you want to use it?
# 
# In this code, we certainly want to be able to specify a different column, so `'Tuition'` needs to be customizable.  Also, we've converted this column to type `float`, but perhaps some other column of money might better be represented as `int`, so we'll want the data type to be customizable also.
# 
# ### Step 2:  Move each of the customizable pieces of code out into a variable with a helpful name, declared before the code is run.
# 
# This is probably clearest if it's illustrated:
# 
# ```python
# column = 'Tuition'
# new_type = float
# df[column] = df[column].str.replace( "$", "" ) # remove dollar signs
# df[column] = df[column].str.replace( ",", "" ) # remove commas
# df[column] = df[column].astype( new_type )     # convert to new type
# ```
# 
# You can then re-run this code to be sure it still does what it's supposed to do.   (That is, check to be sure you haven't accidentally changed the code's meaning.)
# 
# ### Step 3:  Decide on a succinct description for what your code does, to use as the name of a new function.
# 
# In this case, we're converting a column of currency to a new type, but I don't want to call it `convert_currency` because that sound like we're using exchange rates between two currencies.  Let's call it `simplify_currency`.
# 
# ### Step 4:  Indent your original code and introduce a `def` line to define a new function with your chosen name.  Its inputs should be the names of the variables you created.
# 
# In our example:
# 
# ```python
# def simplify_currency ( column, new_type ):
#     df[column] = df[column].str.replace( "$", "" ) # remove dollar signs
#     df[column] = df[column].str.replace( ",", "" ) # remove commas
#     df[column] = df[column].astype( new_type )     # convert to new type
# ```
# 
# If you run it at this point, it doesn't actually do anything to your DataFrame, because the code shown above just defines a function.  So we need one more step.
# 
# ### Step 5:  Call your new function to accomplish what your original code used to accomplish.
# 
# ```python
# def simplify_currency ( column, new_type ):
#     df[column] = df[column].str.replace( "$", "" ) # remove dollar signs
#     df[column] = df[column].str.replace( ",", "" ) # remove commas
#     df[column] = df[column].astype( new_type )     # convert to new type
# 
# simplify_currency( 'Tuition', float )  # <--- Here we use our function.
# ```
# 
# This should have the same effect as the original code.  Except now you can re-use it on as many inputs as you like.
# 
# ```python
# simplify_currency( 'Fees', float )
# simplify_currency( 'Books', float )
# simplify_currency( 'Room and board', float )
# ```
# 
# Sorry, that's a depressing example.  Let's move on...
# 

# ## How do I know when to use abstraction?
# 
# Whenever you find yourself copying and pasting code with minor changes, this is a sure sign that you should write a function instead.  The reasons why are all the benefits listed at the end of [Example 3](#example-3-copying-and-pasting-code), above.
# 
# Also, if you have several lines of code in a row with only one thing changing, you can use abstraction to create a loop instead of a function.  We saw an example of this in the [Alternatives](#alternatives) section, above.  This is especially important if there's a numeric progression involved.
# 
# **Later, the skill of abstracting code will be a crucial part of our work on creating interactive dashboards.**  In class, we will practice using abstraction to improve code written in a redundant style.

# ```{admonition} Learning on Your Own - Writing Python modules
# ---
# class: alert alert-danger
# ---
# Once you've created a useful function, such as the `simplify_currency` function above, that you might want to reuse in many Python scripts or Jupyter notebooks, where should you store it?  Copying and pasting it across many notebooks creates the same problems that copying and pasting any code causes.  The best strategy is to create a Python module.
# ```
# 
# A tutorial on writing Python modules could answer the following questions.
# 
#  * How do I start creating a Python module?
#  * How do I move a function I've written into my new Python module?
#  * Where do I store a Python module I've created?
#  * How do I import my new module into scripts or notebooks I write?
#  * How do I use the functions in my module after I've imported it?
#  * Can I publish my module online in an official way?
# 
# ```{admonition} Learning on Your Own - Jupyter `%run` magic
# ---
# class: alert alert-danger
# ---
# In a Jupyter notebook, the `%run` command tells Jupyter to execute an entire other Jupyter notebook or Python script as if it had been inserted into a single cell in your current notebook.  (It's called a "magic" command because the `%` sign gives it a meaning beyond normal Python code.)  This command could be used to avoid creating Python modules in some cases.
# ```
# 
# A tutorial on the `%run` magic command would address these questions:
# 
#  * How exactly do I use the `%run` command to run one Jupyter notebook inside another?
#  * Why might I want to write a Jupyter notebook instead of a Python module?
#  * What are the pros and cons of doing this instead of writing a Python module?
# 

# ## What if abstraction seems tricky?
# 
# It's always good to be careful!  If writing Python functions is new to you, or you aren't sure that the functions you write are working correctly, it's good to stop and test them carefully before you rely on them.
# 
# If your function returns a value, you can run it on a few example inputs to be sure it works.  Let's say we had to write a Celsius-to-Fahrenheit converter, like this.

# In[9]:


def convert_C_to_F ( C ):
    return 9/5*C+32


# We could test to be sure that it works by plugging in some values for which we know the answer, and ensuring it gives the right output.

# In[10]:


convert_C_to_F( 0 ), convert_C_to_F( 100 )


# But then we still have to manually observe and verify that the numbers are correct.  Later, if something changes (perhaps we accidentally edited our original function), we could easily not notice, because we weren't re-checking these test outputs.
# 
# To solve that problem, Python provides the `assert` keyword.  It lets you, well, assert things that you think are true, and Python will check them.  If they are true, Python does nothing.  But if they aren't true, then Python throws an error message so that the problem will become visually obvious to you in your notebook.
# 
# So we could convert our tests up above into the `assert` format as follows.

# In[11]:


assert convert_C_to_F( 0 ) == 32
assert convert_C_to_F( 100 ) == 212


# Notice that there is no output.  That's a good thing.  Python is silent because there are no problems here.  If we had asserted something false, it would have given us an obvious error message, to increase the likelihood that we would notice and fix the problem.
# 
# Here's an assertion that's intentionally wrong, so you can see what the error messages look like.

# In[12]:


assert convert_C_to_F( 0 ) == 0        # this should give an error...


# But some functions don't return values.  The `drop_unneded_columns` function from earlier just modifies a DataFrame that we had already loaded.  In that case, since there is no output of the function for us to test, we could test its effectiveness by using `assert` on the DataFrame that was modified.  We might write statements like the following.
# 
# ```python
# assert len( df_cases.columns ) == 8
# assert df_cases.columns[4] == 'January'
# ```
# 
# Putting a few of these checks throughout your notebooks will ensure that if you change something important without realizing it, the next time you re-run your notebook, you'll immediately see the problem and can fix it.  This helps avoid compounding problems over time, and gives a sense of reassurance, when all the `assert`ions pass, that your code is still working smoothly.
