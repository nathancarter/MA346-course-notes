# Review of Python and pandas

<a href="../../_slides/chapter-4-slides.html">See also the slides that summarize a portion of this content.</a>

<font color='red'>THIS PAGE IS NOT COMPLETELY WRITTEN.  What is below is in outline/draft form.</font>


1. Python review that focuses on remembering pandas
  * (Don't forget to ask yourself: How can I connect this back to functions and relations?)
  * Where to get these exercises:
    * Start with the dataset I've downloaded for you and the notebook/script that loads it, a sample of approximately 0.1% of all mortgage applications in the US in 2018, filtered to include only those that are a conventional loan for home purchase of a principal residence, etc., etc.  (That is, I've done all the filtering that was required in MA346 S20 Project1.)
    * Drop all columns except these: `interest_rate`, `property_value`, `state_code`, `tract_minority_population_percent`, `derived_race`, `derived_sex`, `applicant_age`
    * Use info/head to understand the contents of the table.
    * Convert columns to numeric or categorical, as needed.
    * Show that you remember how to select just those rows that are, say, for women, or for Asians, or for people over age 75.
    * Somehow get them to bump into the error of writing to a view on a dataframe, so that you can cover the essential view/copy distinction, which should be a big-picture item. :framed_picture:
  * Have them write up solutions in Colab and then Slack/Teams chat the link to the #general channel.
  * Keep Slack/Teams open in the podium browser and click the links as they come in to discuss the solutions together.
  * What to do with this work:
    * Keep it because we will build on it in the future.
    * If we didn't finish all this, take a team as volunteers to do it and share it with everyone afterwards.
    * They are NOT yet required to comment their code!  See below.  (You haven't yet modeled it.)
    * Connect as much of this as possible to Excel, because they'll bump into Excel very often in their careers, and often that's the best tool for a job rather than R/Python.  Show which things are easier in Excel and which are not.
2. What if you don't remember this stuff?
  * Where to find docs and how to read them
  * How to do a good help search
  * How to distinguish good advice from crap advice
    * Maybe even an assignment that asks them to find some incorrect coding advice (blog, docs, etc.) and say how they discerned that it was bad?  This might be too hard.
3. Python review that focuses on mathematical exercises to really strengthen their coding fluency and mathematical understanding
   * Where to get these exercises:
     * Create some that will make them think about functions and relations.
     * Create some that will make them remember the foundations of pandas.
     * Consider poaching from any of the $>400$ exercises in A Primer on Scientific Programming, listed on pages xxiii-xxxi.
   * Have them write up solutions in Colab and then Slack chat the link to the #general channel.
   * Keep Slack open in the podium browser and click the links as they come in to discuss the solutions together.
4. Functional-style code (lots of nesting) vs. imperative-style code (lots of lines)
   * Explanatory power of naming variables well
   * Ability to split it over multiple cells, with more documentation between
   * More understandable for those new to coding, because each thing to understand is smaller