# Detailed Course Schedule

This include all topics covered and all assignments given and when they are due.

## Week 1 - 9/3/2020 - Introduction and mathematical foundations

### Slides for today

 * <a href='../../_slides/chapter-1-slides.html'>Chapter 1: Introduction to data science</a>
 * <a href='../../_slides/chapter-2-slides.html'>Chapter 2: Mathematical foundations</a>

### Due before next class

 * **DataCamp**
    * Optional, basic review:
       * [Introduction to Python](https://www.datacamp.com/courses/intro-to-python-for-data-science)
       * [Python Data Science Toolbox, Part 1](https://www.datacamp.com/courses/python-data-science-toolbox-part-1)
    * Required (though it may still be review):
       * [Intermediate Python](https://www.datacamp.com/courses/intermediate-python-for-data-science), chapters 1-4
       * [pandas Foundations](https://www.datacamp.com/courses/pandas-foundations), just chapter 1
       * [Manipulating DataFrames with pandas](https://www.datacamp.com/courses/manipulating-dataframes-with-pandas), just chapter 1
    * [See here for a cheat sheet](big-cheat-sheet.html#before-week-2-review-of-cs230) of all the content of the above DataCamp lessons.
 * **Reading**
    * Each week, you are expected to read the appropriate chapters from the course notes *before* class.  Since this is the first day for the course, I did not expect you to have read Chapters 1-2 in advance.  But that means that you must now read them together with Chapters 3-4 before next week.
    * [Chapter 1: Introduction to data science](chapter-1-intro-to-data-science) (adds details to today's class content)
    * [Chapter 2: Mathematical foundations](chapter-2-mathematical-foundations) (adds details to today's class content)
    * [Chapter 3: Computational notebooks (Jupyter)](chapter-3-jupyter) (prepares for next week)
    * [Chapter 4: Python review focusing on pandas and mathematical foundations](chapter-4-review-of-python-and-pandas) (prepares for next week)
 * **Other**
    * If you don't already have a Python environment installed on your computer, [see these instructions for installing one](anaconda-installation).  As part of that process, ensure that you can open both Jupyter Lab and VS Code.
    * Optional: There are many LOYO opportunities from this week's course notes (chapters 1 and 2).  See the syllabus for a definition of LOYO and consider forming a team and siezing one of the opportunities.

---

## Week 2 - 9/10/2020 - Jupyter and a review of Python and pandas

### Slides for today

 * <a href='../../_slides/chapter-3-slides.html'>Chapter 3: Computational notebooks (Jupyter)</a>

(There are no slides for Chapter 4, because it was just a review of CS230.)

### Due before next class

 * **DataCamp**
    * [Manipulating DataFrames with pandas](https://www.datacamp.com/courses/manipulating-dataframes-with-pandas), chapters 2-4
    * [See here for a cheat sheet](big-cheat-sheet.html#before-week-3) of all the content of the above DataCamp lessons.
 * **Reading**
    * [Chapter 5: Before and after, in mathematics and communication](chapter-5-before-and-after)
    * [Chapter 6: Pandas single-table verbs](chapter-6-single-table-verbs)


---

## Week 3 - 9/17/2020 - Before and after, single-table verbs

### Slides for today

 * <a href='../../_slides/chapter-5-slides.html'>Chapter 5: Before and after, in mathematics and communication</a>
 * <a href='../../_slides/chapter-6-slides.html'>Chapter 6: Pandas single-table verbs</a>

### Due before next class

 * **Communication exercise**
    * Download <a href='../../_static/homework-exercise-on-code-communication.ipynb'>this Jupyter notebook</a>.
    * Download <a href='../../_static/practice-project-dataset-1.csv'>this CSV file</a> into the same folder.
    * The first half of the notebook has plenty of comments and explanations, but the second half does not.  Use the principles discussed in class today (and covered in [Chapter 5 of the course notes](chapter-5-before-and-after)) to comment/document/explain the second half of that file.
    * Upload your work to a new Deepnote project.  (Don't forget the data file!)
    * Email the URL for that project to your instructor.
 * **DataCamp**
    * [pandas Foundations](https://www.datacamp.com/courses/pandas-foundations), just chapter 2
    * [See here for a cheat sheet](big-cheat-sheet.html#before-week-4-review-of-visualization-in-cs230) of all the content of the above DataCamp lessons.
 * **Reading**
    * [Chapter 7: Abstraction in mathematics and computing](chapter-7-abstraction)
    * [Chapter 8: Version control and GitHub](chapter-8-version-control)


---

## Week 4 - 9/24/2020 - Abstraction and version control

### Slides for today

 * <a href='../../_slides/chapter-7-slides.html'>Chapter 7: Abstraction in mathematics and computing</a>
 * <a href='../../_slides/chapter-8-slides.html'>Chapter 8: Version control and GitHub</a>

### Due before next class

 * **Version control exercise**
    * This assignment is described in the final slide for Chapter 8, linked to above.
 * **DataCamp**
    * [Intermediate Python](https://www.datacamp.com/courses/intermediate-python-for-data-science), chapter 5
    * [Statistical Thinking in Python, Part 1](https://www.datacamp.com/courses/statistical-thinking-in-python-part-1), all chapters
    * [Introduction to Data Visualization with Python](https://www.datacamp.com/courses/introduction-to-data-visualization-in-python), chapters 1 and 3 only
    * [See here for a cheat sheet](big-cheat-sheet.html#before-week-5) of all the content of the above DataCamp lessons.
 * **Reading**
    * [Chapter 9: Math and stats in Python](chapter-9-math-and-stats)
    * [Chapter 10: New visualization tools](chapter-10-visualization)


---

## Week 5 - 10/1/2020 - Math and stats in Python, plus Visualization

### Slides for today

 * <a href='../../_slides/chapter-9-slides.html'>Chapter 9: Math and stats in Python</a>
 * <a href='../../_slides/chapter-10-slides.html'>Chapter 10: New visualization tools</a>

### Due before next class

 * **Data preparation exercise**
    * Look at the 2016 election data [on this page of NPR's website](https://www.npr.org/2016/11/08/500927768/2016-presidential-election-results-for-each-state).
    * Extract the table from that page into a CSV file (for example, by copying and pasting into Excel, then touching it up as needed).
    * Write a Jupyter notebook that imports the CSV file.
    * Ensure that you remove all rows that are not for entire states (which you can do in Excel or Jupyter, whichever you prefer).
    * Publish the notebook and the dataset together to a Deepnote or Colab project.
    * Share the project URL with your instructor by email.
    * We will use this dataset in class next week.
 * **DataCamp**
    * [Merging DataFrames with pandas](https://learn.datacamp.com/courses/merging-dataframes-with-pandas), chapters 1-3
       * **NOTE:** We will not cover this content in class next week.  We will cover it the subsequent week instead.  But I'm assigning you to do it this week because then you won't have any homework next week, when the project is due, and you'll be able to focus on that instead.
    * [See here for a cheat sheet](big-cheat-sheet.html#before-week-6) of all the content of the above DataCamp lessons.
 * **Reading**
    * [Chapter 11: Processing the rows of a `DataFrame`](chapter-11-processing-rows)
 * **Other**
    * Optional: There are several LOYO opportunities from this week's course notes (chapters 9 and 10).  Consider forming a team and siezing one of the opportunities.

---

## Week 6 - 10/8/2020 - Processing the Rows of a `DataFrame`

### Slides for today

 * <a href='../../_slides/chapter-11-slides.html'>Chapter 11: Processing the rows of a `DataFrame`</a>

### Due before next class

 * **No DataCamp this week, so that you can focus on the project.**
 * **Reading**
    * [Chapter 12: Concatenation and Merging](chapter-12-concat-and-merge)
 * **Other**
    * Optional: There are a few LOYO opportunities from this week's course notes (chapter 11).  Consider forming a team and siezing one of the opportunities.

---

## Week 7 - 10/15/2020 - Concatenation and Merging

### Slides for today

 * <a href='../../_slides/chapter-12-slides.html'>Chapter 12: Concatenation and Merging</a>

### Due before next class

It's a light week, because you just did Project 1 and deserve a little time to rest.

 * **DataCamp**
    * [Streamlined Data Ingestion with pandas](https://learn.datacamp.com/courses/streamlined-data-ingestion-with-pandas)
    * [See here for a cheat sheet](big-cheat-sheet.html#before-week-8) of all the content of the above DataCamp lessons.
 * **Reading**
    * [Chapter 13: Miscellaneous Munging Methods (ETL)](chapter-13-etl)


---

## Week 8 - 10/22/2020 - Miscellaneous Munging Methods (ETL)

### Slides for today

 * <a href='../../_slides/chapter-13-slides.html'>Chapter 13: Miscellaneous Munging Methods (ETL)</a>

### Due before next class

 * **DataCamp** (last one for the whole semester!)
    * [Introduction to SQL for Data Science](https://learn.datacamp.com/courses/introduction-to-sql)
       * **NOTE:** Bentley's CS350 course goes into this content in far greater detail.  You can see this lesson as a small preview or taste of that course.
    * [See here for a cheat sheet](big-cheat-sheet.html#before-week-9) of all the content of the above DataCamp lessons.
 * **Reading**
    * [Chapter 14: Dashboards](chapter-14-dashboards)
 * **Other**
    * Install [Streamlit](https://www.streamlit.io/) (`pip install streamlit`).  Take a screenshot to prove you did so.
    * [Create a Heroku account](https://signup.heroku.com/).  Then [install the Heroku command-line tools](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).  Ensure that after doing so, you can get to a terminal and run `heroku login` successfully.  Take a screenshot to prove you did so.
    * Email both screenshots in one email to your instructor.
 * **Project Planning**
    * Optional: If you want to get ahead on the final project in a way that's rather easy and fun, start hunting for datasets that cover a topic you're interested in and might want to analyze.  Try to find a dataset that's pretty comprehensive, so that there are plenty of options for ways to analyze, visualize, and manipulate it.


---

## Week 9 - 10/29/2020 - Dashboards

### Slides for today

 * <a href='../../_slides/chapter-14-slides.html'>Chapter 14: Dashboards</a>

### Due before next class

 * **Reading**
    * [Chapter 15: Relations as graphs and network analysis](chapter-15-networks)

(Perhaps more assignments are coming; this section is still incomplete.)


---

## Week 10 - 11/5/2020 - Relations, graphs, and networks

### Slides for today

 * <a href='../../_slides/chapter-15-slides.html'>Chapter 15: Relations as graphs and network analysis</a>

### Due before next class

 * **Reading**
    * [Chapter 16: Relations as matrices](chapter-16-matrices)

(Perhaps more assignments are coming; this section is still incomplete.)


---

## Week 11 - 11/12/2020 - Relations as matrices

### Slides for today

 * <a href='../../_slides/chapter-16-slides.html'>Chapter 15: Relations as matrices</a>

### Due before next class

 * **Reading**
    * [Chapter 17: Introduction to machine learning](chapter-17-machine-learning)

(Perhaps more assignments are coming; this section is still incomplete.)


---

## Week 12 - 11/19/2020 - Introduction to machine learning

### Slides for today

 * <a href='../../_slides/chapter-17-slides.html'>Chapter 17: Introduction to machine learning</a>

### Due before next class

 * None yet

(Perhaps more assignments are coming; this section is still incomplete.)


---

## Week 13 - 11/26/2020 - Thanksgiving break, no class

No assignments over break, but it would be wise to continue to make progress on the Final Project.


---

## Week 14 - 12/3/2020 - Final Exam Review and Final Project Workshop

 * **Final Exam**
    * Based on the review we do in class today, study for the Final Exam.
 * **Final Project**
    * Come to class today ready to use half of class to work on your final project in class, and ask questions of the instructor if/when you get stuck on anything.