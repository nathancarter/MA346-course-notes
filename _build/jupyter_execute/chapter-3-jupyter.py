# Jupyter

<a href="../../_slides/chapter-3-slides.html">See also the slides that summarize a portion of this content.</a>


## What's Jupyter?

The Jupyter project makes it possible to use code to experiment with and process data in your web browser.  It lets you do all of these things in one page (or browser tab):
 * write and run code
 * write explanations of code and data, including with mathematical formulas
 * view tables, plots, and other visualizations of data
 * interact with certain types of data visualizations

It's pronounced just like Jupiter, but has the funny spelling because it was originally built for Python, so they wanted to work a "py" in there somewhere.

You may prefer to use another tool to accomplish these tasks; your MA346 instructor won't force you to use Jupyter.  But you should still know about Jupyter for the following reasons:
 * Lots of people in data science and analytics use Jupyter notebooks, so you'll definitely encounter them and want to be familiar with how to read them, edit them, and run them.
 * It's becoming the *lingua franca* for how to share your data research online, so you may want to know how to publish Jupyter notebooks, something our course will cover.
 * It was a big enough deal to win one of the highest awards in the computer science profession, the [2017 ACM Software System Award](https://blog.jupyter.org/jupyter-receives-the-acm-software-system-award-d433b0dfe3a2).

In fact, these course notes were written in Jupyter.  That's why you'll see code inputs and outputs interspersed among them, because Jupyter lets you write documents with code built in, and it runs the code for you and shows you the output.  Here's an example:

import matplotlib.pyplot as plt
plt.plot( [5, -3, 10, 9, 1] )
plt.show()

Okay, sounds great, so where do we point our browser to start using this thing?  Well, you've got lots of options, so let's see what they are first.

## How does Jupyter work?

```{admonition} Big Picture - The structure of Jupyter
---
class: alert alert-primary
---
Jupyter is made of two pieces:
 1. The notebook interface, which shows you a document with code and visualizations in it, called "a Jupyter notebook."
 2. The engine behind the notebook, which runs your code, and is doing its work invisibly in the background; this engine is called the "kernel."

How you interact with each of these two pieces is important, and comes with some pitfalls to avoid.
```

### Jupyter in the cloud

The easiest way to start using Jupyter is to just point your browser at a website that offers you access to Jupyter in the cloud.  In such a situation, Jupyter's two pieces work like this:
 1. The notebook interface runs in your browser on your computer
 2. The kernel runs in the cloud on a server provided by someone else

Here are three examples of where you can use Jupyter notebooks in the cloud:
 1. Best choice: [Deepnote](https://deepnote.com/)<br/>[<img src='https://media-exp1.licdn.com/dms/image/C4E0BAQHeGGvBVLIhnQ/company-logo_200_200/0?e=2159024400&v=beta&t=DXm5dzcOA3HBAvB0BNQTnwrHdxt4QpshfMU0DtiyRK0' width=200 height=200/>](https://deepnote.com/)
    * They took the standard Jupyter interface and added more goodies
    * You can read and write files to/from your Google Drive
    * You can use multiple languages (though we'll stick to Python)
    * The amount of computing power they give you for free is pretty good
    * It's extremely easy to share your work with anyone
    * But you have access to Deepnote only because I signed our class up; they're a startup and they're not letting everyone in yet
 2. Next best choice: [Google Colab](https://colab.research.google.com/)<br/>[<img src='https://colab.research.google.com/img/colab_favicon_256px.png' width=200 height=200/>](https://colab.research.google.com/)
    * All the same positives as Deepnote except without as many interface goodies
    * Supports more languages than Deepnote does, but that's not relevant in MA346
 3. Third choice: [CoCalc](https://cocalc.com/)<br/>[<img src='https://upload.wikimedia.org/wikipedia/en/thumb/7/72/CoCalc_Logo.png/280px-CoCalc_Logo.png' width=241 height=200/>](https://cocalc.com/)
    * Many features that the previous two don't have, including a nice palette of common code snippets you can insert
    * But the notebook interface is nonstandard and different from Jupyter's in several ways
    * Perhaps the most limited in terms of how much computing you get for free, though this is not very important for MA346

Obviously, none of these is going to give you access to a supercomputer for free.  If you want to do any intense or lengthy computing in the cloud, you have to pay for them to let the kernel you're using run on big hardware.

### Jupyter on your machine

You can also choose to run Jupyter on your own machine.  In contrast to accessing Jupyter in the cloud, when you run it on your own machine, Jupyter's two pieces work like this:
 1. The notebook interface still runs in your browser on your computer
 2. The kernel now also runs on your computer, which has both advantages and disadvantages

Let's consider the major tradeoffs in each of these approaches.

| Why put Jupyter on my computer?    | Why choose the cloud instead?   |
|------------------------------------|---------------------------------|
| 1. Not limited by how much power a cloud company will give you for free. | 1. You don't have to install anything on your computer. |
| 2. Even if I don't have good wifi access, I can still use it. | 2. You can use it on a phone/tablet. |
| 3. May be easier to add specific Python packages you need for your work. | 3. Avoid accidentally leaving a kernel running invisibly. (See below.) |

If you want to go this route, there are several ways to install Jupyter on your machine.

**Easiest way:**  [Install Anaconda](anaconda-installation)
 * This is by far the easiest method, so start here.
 * Follow the link above for detailed instructions within these course notes; it is not necessary to also install VS Code, which the instructions make optional.
 * Once Anaconda is installed, you can launch it from the Windows Start menu or Mac Applications folder, then choose to launch either Jupyter Lab or the Jupyter Notebook.

Before we discuss the other methods of installing Jupyter, let's discuss the difference between Jupyter Lab and the Jupyter Noteboook.  Here's a summary:

| Jupyter Notebook   | Jupyter Lab              |
|--------------------|--------------------------|
| The original Jupyter project | Its newer successor |
| Uses multiple browser tabs   | Does everything in one tab |
| Supports many extensions     | Doesn't yet support all extensions |
| Has no console/terminal access | Has both console and terminal access |

Both technologies let you edit Jupyter notebooks.  (Yes, it's confusing that one app is called "the Jupyter Notebook" and the files are also called "Jupyter notebooks."  Sorry.)

```{admonition} Big Picture - How to shut down Jupyter
---
class: alert alert-primary
---
When you launch either the Jupyter Notebook or Jupyter Lab, you launch both the user interface (which you see in your browser) and the kernel (which you don't!).  **Just closing the browser tab DOES NOT CLOSE THE KERNEL.**  Doing this repeatedly (e.g., each day in class) will clog up your computer with many kernels running invisibly in the background.

Instead, do one of these things EVERY TIME you're done coding:
 * In Jupyter Notebook: File Menu > Close and Halt
 * In Jupyter Lab: File Menu > Shut down

These close the (invisible) kernel first, then let you close the user interface after that.
```

But that's a hassle!  Wouldn't it be easier if Jupyter were just an app I could run on my machine, like every other app?  In fact, because Jupyter is *not* an app, you can't even double-click Jupyter notebook files (which end with the `.ipynb` extension) and have them automatically open in Jupyter.  Another hassle!  How can we fix these things?

**Another option:**  Install [nteract](https://nteract.io/) (pronounced "interact")
 * This assumes you have a working Python installation.  The easiest way to do that is to install Anaconda, using the instructions up above.  That's why this one is listed second; it assumes you've done that first.
 * Then visit the website linked to above and follow the very easy process of installing the nteract app.
 * When you run nteract, it shows you a new, blank Jupyter notebook.  It has already launched the invisible kernel behind the scenes for you.  (No need to go to Anaconda Navigator first!)
 * You can also double-click notebooks to open them in nteract.  Easy, just like every other app on your machine.
 * When you quit nteract, it quits not only the user interface you see, but the invisible kernel as well.  Nothing to remember.

The only disadvantage here is that some Jupyter notebook extensions don't work in nteract.  But we won't be using many of those in MA346 anyway.

## Closing comments

There are many websites that make it easy to view Jupyter notebooks online.  This is very useful for sharing the results of your work when you're done.  Examples include [NbViewer](https://nbviewer.jupyter.org/) and [GitHub](https://github.com/), but there are others.  Notebooks are often shared in nerdy places on the Internet, with websites supporting viewing them with all their plots, tables, and math displayed nicely.  We will learn how to use GitHub in a future week.

There are various pros and cons to using Jupyter notebooks vs. plain old Python scripts, as you probably did in CS230.  There are also some hybrid technologies that exist to make notebooks more like scripts, or scripts more like notebooks (such as [Papermill](https://papermill.readthedocs.io/en/latest/), [VSCode notebook support](https://code.visualstudio.com/docs/python/jupyter-support), and others).  In this class, you can usually use whatever technology you prefer.  The instructor will use notebooks because they are good for communicating, and communicating is your instructor's job.

```{admonition} Learning on Your Own - Problems with Notebooks
---
class: alert alert-danger
---
Some folks [really don't like Jupyter notebooks](https://twitter.com/joelgrus/status/1033035196428378113?lang=en).  And they have good points!  Study what pitfalls notebooks have, based on the presentation at that link, and report on them to the class.
```

Such a report would include:
 * From the many problems the presentation lists, choose the 4-6 that are most relevant to MA346 students.
 * For each such problem:
    * Explain it carefully.
    * Show how a tool other than Jupyter doesn't have the same problem.
    * Suggest specific ways that MA346 students can avoid pitfalls surrounding that problem.
    
```{admonition} Learning on Your Own - Math in Notebooks
---
class: alert alert-danger
---
You can add mathematics to Jupyter notebooks and it looks very nice.  Here's an example of the quadratic formula:

$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$

This can be useful for explaining mathematical and statistical concepts in your work clearly, without resorting to ugly text attempts to look sort of like math.
```

Such a report would include:
 * An explanation of what a student would type into a Markdown cell to make some simple mathematics
 * A list of the 5-10 most common math notation or symbols the student will want to know how to create (particularly those relevant to statistics and/or data science)
 * Suggestions for where the student can go to learn more symbols or notation if they need it
