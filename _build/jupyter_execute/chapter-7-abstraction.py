# Abstraction

<a href="../../_slides/chapter-7-slides.html">See also the slides that summarize a portion of this content.</a>


## Abstract vs. concrete

Abstract/concrete are opposite ends of a spectrum:

|       | Concrete (or specific) | Abstract (or general) |
|-------|----------------------|------------------------|
| Example from science: | When we drop things, they fall to earth. | $G_{\mu v}+\Lambda g_{\mu v}=\frac{8\pi G}{c^4}T_{\mu v}$ (Einstein's field equation) |
| Example from business: | That startup failed because each partner tried to pull it in a different direction. | Organizations need a clearly stated vision. |
| Example from ethics: | The Nazis' attacks on the Jews were a great evil. | Systematically disadvantaging any racial group is wrong. |

*Abstraction* is therefore the process of moving from the concrete toward the abstract, or from the specific to the general.  Therefore it's also called *generalization.*  Humans are pretty good at learning general principles from specific examples, so this is a natural thing for us to do.

It's very useful in all kinds of programming, including data-related work, so it's our focus in this chapter.

## Abstraction in mathematics

### Example 1: Algebra class

My kids are teenagers and have recently taken algebra classes where they learned to "complete the square."  This procedure takes a quadratic equation like $16x^2-9x+5=0$ and manipulates it into a form that's easy to solve.
 * Each homework problem was a *specific* example of this technique.
 * If you apply the technique to the equation $ax^s+bx+c=0$, the result is the quadratic formula, $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$, a *general* solution to all quadratic equations.

Abstraction from the specific to the general tends to create more powerful tools, because they can be applied to any specific instance of the problem.

### Example 2: Excel formulas

If you took the grading policy out of the syllabus for this class, you could compute your grade in the course based on your scores on each assignment.  You could do this by hand with pencil and paper, or with a calculator.  Doing so would give you one specific course grade, for the specific assignment grades you started with.

Alternately, you could fire up a spreadsheet like Excel, and create cells for each assignment's score, then create formulas that would do the appropriate computation and give you the corresponding course grade.  This general solution works for any specific assignment grades you might type into the spreadsheet's input cells.

Again, the general version is more useful.

### Observations

Both of these mathematical examples involved replacing numbers with variables.  In Example 1, the coefficients in the specific example $16x^2-9x+5=0$ turned into $a$, $b$, and $c$ in $ax^2+bx+c=0$.  In Example 2, you didn't write formulas that had specific scores in them (as you would have if computing the scores by hand), but wrote formulas that contained Excel-style variables, which have names like A5 and B14, that come from the relevant cells.  In math (and in programming as well), abstraction typically involves *replacing specific constants with variables.*

Once we've rephrased our computation in terms of variables, we can do many different mathematical operations with it.
 1. We can think of our computation as a function.
     * In Example 1, the quadratic formula can be seen as a function that takes as input the values $a,b,c$ and yields as output the two solutions of the equation.
     * In Example 2, the Excel formulas can be seen as a function that take the assignment grades as input and yield the course grade as output.
 2. We can ask what happens when one of the variables changes, a question that calculus focuses on.
     * For instance, you could ask what happens to your computation as one of the variables gets larger and larger.  (In calculus, we wrote this as $\lim_{x\to\infty}$.)
     * Or you could ask how the result of the computation responds to changes in one input variable.  (In calculus, we wrote this as $\frac{d}{dx}$.)
 3. We can make statements about the computation in terms of the input variables.
     * In Example 1, we might say that "Every quadratic equation has two complex number solutions."
     * In Example 2, we might say that "It's still possible for me to get a 4.0 in this course if my final exam score is good enough."

The statement above from Example 1 is a *universal* statement, also called a "for all" statement.  You could rephrase it as:  For all inputs $a,b,c$, the outputs of the quadratic formula are two complex numbers.  The statement from Example 2 is an *existence* statement, also called a "for some" statement.  You could rephrase it as:  For some final exam scores, my final course grade is still a 4.0.  For all/for some statements are central to mathematics and we will see them show up a lot.  "For all" and "for some" are called *quantifiers* and are sometimes written $\forall$ (for all) and $\exists$ (for some, or "there exists").

## Abstraction in programming

```{admonition} Big Picture
---
class: alert alert-primary
---
This section covers the value of abstraction for every programmer.  It is a valuable viewpoint to have and skill to be able to employ.  See the rest of this section for details on how it works and how to use it.
```

### Example 3: Copying and pasting code

Best practices for coding include writing DRY code, where DRY stands for Don't Repeat Yourself.  If you find yourself writing the same code (or extremely similar code) more than once, especially if you're copying and pasting, this is a sure sign that you are not writing DRY code and should try to correct this style error.  The way to correct it is with abstraction, as shown below.  (The opposite of DRY code is WET code--Write Everything Twice.  Don't do that.)

Here is an example of some code a student once wrote for me in a past data science course.  They had three pandas DataFrames of data about COVID-19, one containing numbers of cases, one containing numbers of deaths, and one containing numbers of recoveries.  They wanted to change the column names in each DataFrame.

```python
df_cases = df_cases.add_suffix( '_cases' )
df_cases.columns = ['Province/State','Country/Region','Lat','Long'] + list(df_cases.columns[4:])
df_deaths = df_deaths.add_suffix( '_deaths' )
df_deaths.columns = ['Province/State','Country/Region','Lat','Long'] + list(df_deaths.columns[4:])
df_recoveries = df_recoveries.add_suffix( '_recoveries' )
df_recoveries.columns = ['Province/State','Country/Region','Lat','Long'] + list(df_recoveries.columns[4:])
```

I suspect the student wrote the first two lines, ran them, verified that they worked, and then copied and pasted them twice and changed the variable names to apply the same code to the other two DataFrames.  But this code can be made much cleaner through abstraction.  Rather than copy and paste the code, then change key parts of it, replace those key parts with a *general* (that is, abstract) variable name, and then turn the code into a function.  Since this code renames columns, the student could have made that the name of the function.

```python
def rename_columns ( df ):
    df = df.add_suffix( '_cases' )
    df.columns = ['Province/State','Country/Region','Lat','Long'] + list(df.columns[4:])
```

Once this general version is complete, you can apply it to each specific case you need.

```python
rename_columns( df_cases )
rename_columns( df_deaths )
rename_columns( df_recoveries )
```

There are several advantages to this new version.
 1. While it is still six lines of code, half of them are much shorter, so there's less to read and understand.
 2. What the code is doing is more obvious, because we've given it a name; we're obviously renaming columns.
 3. It wasn't immediately obvious in the first version of the code that we were repeating the same procedure three times.  Now it is.
 4. If you later need to change how you rename columns, you have to make that change in only one place (inside the function).  Before, you would have had to make the same change three times.
 5. Also, if you tried to make a change to the code later, but accidentally missed changing one of the three, you'd have broken code and not realize it.
 6. You could share this same function to other notebooks or with other coders if needed.

So the moment you find yourself copying and pasting code, remember to stay DRY instead--create a function and call it multiple times, so that you get all these benefits.

### Alternatives

Another method of abstraction would have been a loop instead of a function.  Since the original code does the same thing three times, we could have rewritten it as follows instead.

```python
for df in [ df_cases, df_deaths, df_recoveries ]:
    df = df.add_suffix( '_cases' )
    df.columns = ['Province/State','Country/Region','Lat','Long'] + list(df.columns[4:])
```

This has all the same benefits as the previous method, except for \#6.

One could even combine the two methods together, as follows.

```python
def rename_columns ( df ):
    df = df.add_suffix( '_cases' )
    df.columns = ['Province/State','Country/Region','Lat','Long'] + list(df.columns[4:])

for df in [ df_cases, df_deaths, df_recoveries ]:
    rename_columns( df )
```

### Example 4: Testing a computation

Let's imagine that the same student as above, who has COVID-19 data, wants to investigate its connection to the polarized political climate in the U.S., since COVID-19 response has become very politicized.  They want to ask whether there's any correlation between the spread of the virus in a state and that state's prevailing political leaning.  So the student gets another dataset, this one listing the percentage of registered Republicans and Democrats in each U.S. state.  They will want to look up each state in the COVID-19 dataset in this new dataset, to connect them.  They try this:

# load political data
import pandas as pd
df_pol_reg = pd.read_excel( '_static/political-registrations.xlsx',
                            sheet_name=0 )

# make dictionaries for easy lookup:
state_rep_pct = dict( zip( df_pol_reg['State'], df_pol_reg['R%'] ) )
state_dem_pct = dict( zip( df_pol_reg['State'], df_pol_reg['D%'] ) )

# see if it works on Alaska:
state_rep_pct['AK']

Great, progress!  Let's just try one or two more random examples to be sure that wasn't a fluke.

# see if it works on Alabama:
state_rep_pct['AL']

Uh-oh.  Checking [the website where they got the data](http://centerforpolitics.org/crystalball/articles/registering-by-party-where-the-democrats-and-republicans-are-ahead/), the student finds that Alabama doesn't register voters by party, so Alabama isn't in the data.  They need some code that won't cause errors for any state input, so they update it:

import numpy as np
state_rep_pct['AL'] if 'AL' in state_rep_pct else np.nan

Great, this looks like it will work for any input.  Let's turn it into a function and test that function.

def get_rep_pct ( state_code ):
    return state_rep_pct[state_code] if state_code in state_rep_pct else np.nan
def get_dem_pct ( state_code ):
    return state_dem_pct[state_code] if state_code in state_dem_pct else np.nan
get_rep_pct( 'AK' ), get_rep_pct( 'AL' ), get_dem_pct( 'AK' ), get_dem_pct( 'AL' )

So Example 4 has shown us that abstracting a computation into a function can be done as part of an ordinary coding workflow:  Start easy, by doing the computation on just one input and get that working.  Once it does, test it on some other inputs.  Then create a function that works in general.

The benefits of this include all the benefits discussed after Example 3, plus this one:  The student wanted to run this computation for every row in a DataFrame.  That's easy to do now, with code like the following.

```python
df_cases['state_rep_pct'] = df_cases['Province/State'].apply( get_rep_pct )
df_cases['state_dem_pct'] = df_cases['Province/State'].apply( get_dem_pct )
```

### Little abstractions (`lambda`)

When it would be handy to create a function, but the function is so small that it seems like giving it a name with `def` is overkill, you can use Python's `lambda` syntax to create the function.

(The name comes from the fact that some branches of computer science use notation like $\lambda x.3x+1$ to mean "the function that takes $x$ as input and gives $3x+1$ as output."  So they could write $f=\lambda x.3x+1$ instead of $f(x)=3x+1$.)

For example, let's say you have a dataset in which each row represents an hour of trading on an exchange, and the volume is classified using the codes 0, 1, 2, and 3, which stand (respectively) for low volume, medium volume, high volume, and unknown (missing data).  We'd like the dataset to be more readable, so we'd like to replace those numbers with the actual words low, medium, high, and unknown.  We could do it as follows.

```python
def explain_code ( code ):
    words = [ 'low', 'medium', 'high', 'unknown' ]
    return words[code]

df['volume'] = df['volume'].apply( explain_code )
```

But this requires several lines of code to do this simple task.  We could compress it into a one-liner as follows.

```python
df['volume'] = df['volume'].apply( lambda code: ['low','medium','high','unknown'][code] )
```

The limitation to Python's `lambda` syntax is that you can put inside only a single expression, which the function will return.  A function that needs to do several preparatory computations before returning an answer cannot be converted into `lambda` form.

## How to do abstraction

If you aren't sure how to take specific code and turn it into a general function, I suggest following the steps given here.  Once you've done this a few times, it will come naturally, without thinking through the steps.

Let's use with the following example code to illustrate the steps.  It's useful in DataFrames imported from a file where dollar amounts were written in a form like $4,320,000.00, which pandas won't recognize as a number, because of the commas and the dollar sign.  This code converts such a column to numeric.  Since it's so useful, we may want to use it on multiple columns.

```python
df['Tuition'] = df['Tuition'].str.replace( "$", "" ) # remove dollar signs
df['Tuition'] = df['Tuition'].str.replace( ",", "" ) # remove commas
df['Tuition'] = df['Tuition'].astype( float )        # convert to float type
```

### Step 1:  Decide which parts of the code are customizable.  That is, which parts of the code might change the next time you want to use it?

In this code, we certainly want to be able to specify a different column, so `'Tuition'` needs to be customizable.  Also, we've converted this column to type `float`, but perhaps some other column of money might better be represented as `int`, so we'll let the type be customizable also.

### Step 2:  Move each of the customizable pieces of code out into a variable with a helpful name, declared before the code is run.

This is probably clearest if it's illustrated:

```python
column = 'Tuition'
new_type = float
df[column] = df[column].str.replace( "$", "" ) # remove dollar signs
df[column] = df[column].str.replace( ",", "" ) # remove commas
df[column] = df[column].astype( new_type )
```

You can then re-run this code to be sure it still does what it's supposed to do.

### Step 3:  Decide on a succinct description for what your code does, to use as the name of a new function.

In this case, we're converting a column of currency to a new type, but I don't want to call it "convert currency" because that sound like we're using exchange rates between two currencies.  Let's call it "simplify currency."

### Step 4:  Indent your original code and introduce a `def` line to define a new function with your chosen name.  Its inputs should be the names of the variables you created.

In our example:

```python
def simplify_currency ( column, new_type ):
    df[column] = df[column].str.replace( "$", "" ) # remove dollar signs
    df[column] = df[column].str.replace( ",", "" ) # remove commas
    df[column] = df[column].astype( new_type )
```

If you run it at this point, it doesn't actually do anything to your DataFrame, because this just defines a function.  So we need one more step.

### Step 5:  Call your new function to accomplish what your original code used to accomplish.

```python
def simplify_currency ( column, new_type ):
    df[column] = df[column].str.replace( "$", "" ) # remove dollar signs
    df[column] = df[column].str.replace( ",", "" ) # remove commas
    df[column] = df[column].astype( new_type )

simplify_currency( 'Tuition', float )
```

This should have the same effect as the original code.  Except now you can re-use it on as many inputs as you like.

```python
simplify_currency( 'Fees', float )
simplify_currency( 'Books', float )
simplify_currency( 'Room and board', float )
```

Sorry, that's a depressing example.  Let's move on...


## How do I know when to use abstraction?

Whenever you find yourself copying and pasting code with minor changes, this is a sure sign that you should write a function instead.  The reasons why are essentially the six benefits listed at the end of [Example 3](#example-3-copying-and-pasting-code), above.

Also, if you have several lines of code in a row with only one thing changing, you can use abstraction to create a loop instead of a function.  We saw an example of this in the [Alternatives](#alternatives) section, above.  This is especially important if there's a numeric progression involved.

In class, we will practice using abstract to improve code written in a redundant style.

**Later, the skill of abstracting code will be a crucial part of our work on creating interactive dashboards.**

```{admonition} Learning on Your Own - Code refactoring
---
class: alert alert-danger
---
Some IDEs an help automate the process of abstraction.  This is part of a larger set of features that such apps often call "refactoring" or "code refactoring."  Consider researching features in VS Code, PyCharm, or Eclipse that support code refactoring in Python and creating a report or video showing the class how to use those features to accomplish the content of this chapter.
```

```{admonition} Learning on Your Own - Writing Python modules
---
class: alert alert-danger
---
Once you've created a useful function, such as the `simplify_currency` function above, that you might want to reuse in many Python scripts or Jupyter notebooks, where should you store it?  Copying and pasting it across many notebooks creates the same problems that copying and pasting any code causes.  The best strategy is to create a Python module.
```

A tutorial on writing Python modules could answer the following questions.
 * How do I start creating a Python module?
 * How do I move a function I've written into my new Python module?
 * Where do I store a Python module I've created?
 * How do I import my new module into scripts or notebooks I write?
 * How do I use the functions in my module after I've imported it?
 * Can I publish my module online in an official way?
