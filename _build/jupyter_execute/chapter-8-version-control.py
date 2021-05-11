#!/usr/bin/env python
# coding: utf-8

# # Version Control
# 
# <a href="../../_slides/chapter-8-slides.html">See also the slides that summarize a portion of this content.</a>
# 

# ## What is version control and why should I care?
# 
# ```{admonition} Big Picture - Why people use tools like git
# ---
# class: alert alert-primary
# ---
# The most common version control system is called `git`.  It helps you with:
#  * keeping old snapshots of your work in case you need to undo a mistake
#  * collaborating with others on your team by sharing a project
#  * publishing your project online, for sharing or as a backup
# ```
# 
# It's called "version control" software because of the first of those bullet points.  The other two are also important, but aren't the main purpose of `git`.  Let's dive a little deeper into each of those three points and learn some terminology.

# ## Details and terminology
# 
# ### Repositories
# 
# When you start a new project, you should make a folder to contain just the stuff for that project.  By default, a folder on your computer is *not* tracked by `git`.  If you want `git` to start tracking a folder and keeping snapshots, to enable the features listed above, you have to turn the folder into what is called a **`git` repository**, or for short, a **repo.**  (You might also hear "source code repository" or "source repo" or similar terms.)
# 
# Once you do so, `git` is ready to track the changes in that folder.  But it need some direction from you.  Let's see why.
# 
# ### Tracking changes
# 
# As you work on the project, inevitably you have ups and downs.  Maybe it goes like this:
#  1. You start by downloading a dataset from the instructor and starting a new blank Python script or Jupyter notebook in your repo folder.  Everything's fine so far.  😀
#  2. You try to load the dataset but keep getting errors.  You don't manage to solve it before you have to go to dinner.  😡
#  3. A friend at dinner reminded you about setting the text encoding, and that fixed the problem.  You get the dataset loading before bed.  Yes!  😀
#  4. The next day before MA346 you get the data cleaned without a problem.  😀
#  5. During class, the instructor asks your team to make progress on a hypothesis test, but you run out of time in class before you can figure out all the details.  The last few lines of code still give errors.  😡
# 
# And so on.  You could make the story up yourself.
# 
# If you were keeping snapshots of your work for the project, you typically wouldn't want to have any broken ones.  That is, you might want to have stored your work in steps 1, 3, and 4, because if you ever had to undo some mistake you made later, you'd want to go back to a situation where you know everything was working fine. 😀  &nbsp; Nobody wants to rewind to a broken repository; that's not helpful. 😡
# 
# So you wouldn't want your version control system to automatically make snapshots for you; it would probably save a snapshot after 1, 2, 3, 4, and 5, some broken and some not.  Therefore `git` doesn't do this.  If you want to save a snapshot, you have to tell `git` to do so; this is called **committing** your changes.  (Or sometimes you'll hear people call it **making a commit.**)  When you do so, you attach a brief note (one phrase or half a sentence) describing it, called a **commit message.**
# 
# If you did so after each of steps 1, 3, and 4, above, you might have a list of commit messages that look like this:
#  * Downloaded dataset and started new Python script
#  * Wrote code to load data
#  * Added code to clean data
# 
# Later, if you wanted to go back to some old snapshot, `git` can show you this list of commit messages so you know exactly which one you'd like to rewind to.  (At this point, I'll stop calling them "snapshots" and start using the official term, "commits.")
# 
# In fact, these course notes are stored in a `git` repository, and you can [see its list of commits online, here](https://github.com/nathancarter/MA346-course-notes/commits/master).
# 
# ### Sharing online
# 
# When you want to back your work up on another computer (in case yours gets broken, or if you want to publish it for others to see) there are websites that specialize in `git`.  The most popular is [GitHub](https://github.com/), acquired by Microsoft in 2018.  In these notes, we'll teach you how to use GitHub and assume that's where you're publishing your work.
# 
# The `git` term for a site on which you back up or publish a repository is called a **remote.**  This is in contrast to the repo folder on your computer, which is called your **local** copy.
# 
# There are three important terms to know regarding dealing with remotes in `git`; I'll phrase each of them in terms of using GitHub, but the same terms apply to any remote:
#  * For repositories you created:
#     * Sending my most recent commits to GitHub is called **pushing** my changes (that is, my commits).
#  * For repositories someone else created:
#     * Getting a copy of a repository is called **cloning** the repository.  It's not the same as downloading.  A download contains just the latest version; a clone contains all past snapshots, too.
#     * If the original author updates the repository with new content and I want to update my clone, that's called **pulling** the changes (opposite of push, obviously).
# 
# Although technically it's possible to pull and push to the same repository, we'll come to that later.  Let's start simple.
# 
# So how do we do all the things just described?  The next section gives the specifics.

# ## How to use `git` and GitHub
# 
# ```{warning}
# When you're reading this chapter to prepare for Week 4's class, you do not need to follow all these instructions.  We will do them together in class.  Feel free to just skim this section for now, and begin reading again in [the next section](#what-if-i-want-to-collaborate).
# ```
# 
# ### Get a GitHub account
# 
# [Do so on this page of the GitHub website.](https://github.com/join)  Easy!
# 
# ```{warning}
# Please choose a GitHub username that lets me know who you are.  Grading will be a confusing challenge if everyone has names like `DarkKitten75XD`.
# ```
# 
# Just be sure to remember the username and password, because you'll need them in the next step.
# 
# ### Download the GitHub app
# 
# If you ever hear horror stories of people dealing with `git`, there are two main reasons for this.  First, they may have had a repo get screwed up because multiple people were trying to edit it in conflicting ways.  We will avoid such problems by focusing first on using `git` by yourself before we consider how to use it on a team project.  Second, they may have been using `git`'s command-line interface, meaning they interact with it through typing commands, rather than using an app.  We will avoid this hassle by getting the GitHub app.
# 
# [Download and install the GitHub app from here.](https://desktop.github.com/)
# 
# When you set the app up, it will ask for the username and password of your GitHub account, so it can connect to the GitHub site.
# 
# ### Create a repository
# 
# Let's create a repository for you to use when submitting Project 1 later in a little over two weeks.
#  * If you haven't already done so, create a folder on your computer for storing your work on Project 1.
#     * You don't have to put anything in the repository at all---the folder can stay empty for now.
#  * Using the GitHub app, turn that folder into a repository.
#     * From the File menu, choose "Add local repository..." and pick the folder you just created.
# 
# ### Publish the repository
# 
# It's okay that your repository is still empty; you can add files later.
# 
#  * In the center of the GitHub app window there should be a button called "Publish repository."
#  * If not, go to the Repository menu and choose "Push."
# 
# ```{warning}
# Ensure that you check the box to **keep the code private.**  This is so that when you actually begin work on Project 1, you are not tempting anyone else to violate Bentley's academic integrity policy by looking at your work.
# ```
# 
# ### View it online
# 
# From the GitHub app, click the Repository menu, and "View on GitHub."  Easy!  You've successfully found where the repository lives online.
# 
# Because you marked the repository private, anyone other than you who visits that page won't be allowed to see the repository.  You can see it only because you've already logged in to GitHub with your username and password.
# 
# Later you'll share this repository with your instructor so that he can visit it to grade your Project 1, once it's complete.
# 
# ### Make a commit
# 
# In order to commit some changes to our new Project 1 repo, we have to actually do something in that folder, so there *are* some changes to commit.  Let's do some simple setup.
# 
#  * The Project 1 assignment on Blackboard lists three datasets you should download for use in the project.  If you haven't already downloaded them, do so now.  Once you've downloaded them, move them into the folder for your new repo.
#  * Return to the GitHub app and you should notice the three new files listed in the left column, showing you what's new in the repo since it was created.
#  * On the bottom left of the page, type an appropriate commit message, such as "Adding data files," and click "Commit to master."
#     * You can have multiple different flavors of a project all in one repo.  They're called **branches** and the main one is called the **master branch** by default.
#     * In an effort to remove any potential reference to slavery, however indirect, [GitHub is in the process of changing the term "master" to "main,"](https://www.zdnet.com/article/github-to-replace-master-with-alternative-term-to-avoid-slavery-references/) but that process is not yet complete as of this writing.
#     * In the meantime, think of the term "master" as just a reference to the primary copy of your work.
#     * You probably won't need to create any other branches in any repo in MA346.
# 
# You should see your changes disappear from the left column.  This doesn't mean that they've been removed!  It just means that the snapshot has been saved, so those changes aren't "new" any more.  They've been committed (saved) to the repo's history.
# 
# ### Publish your commit
# 
# Push your changes to the repo with the Push button in the center of the app, then reload the webpage that views the repo online.  You should see your new data files in the web interface.  That's how easy it is to publish your work to GitHub!
# 
# ### Repeat as needed
# 
# Whenever you make changes to your work and want to save a snapshot, feel free to repeat the "commit" instructions you see above.  The best practice is to do this as often as possible, but to try to never commit a project that's got errors or broken code.  So try to make small, successful changes and commit after each one.
# 
# ```{warning}
# The GitHub app and `git` in general can see *only changes that you have saved to disk!*  So if you've edited a Python script but *have not saved,* then `git`/GitHub will not be able to see those changes.  The GitHub app looks only at the files on your hard drive.  It does not spy on what you're doing in Jupyter or VS Code or any other app you have open.
# 
# **The takeaway:**  Be sure to save your files to disk before you try to commit.
# ```
# 
# Whenever you want to publish your most recent commits to the GitHub site, repeat the "publish" instructions you see above.

# ## What if I want to collaborate?
# 
# Collaborating with `git` is a very specific type of collaboration.
# 
# On the one hand, it's much less snappy and convenient than Google-docs-style collaboration, which happens instantaneously.  You can see one another's cursors moving about the document and making edits in real time, live.  (You can do this on Deepnote and CoCalc, too, in Jupyter notebooks.)
# 
# On the other hand, that's actually a good thing.  If you and someone else are editing code at the same time, one of you might make changes to a variable name at the top of the file that breaks code you're writing using that variable at the bottom of the file.  With `git`, you have to take intentional steps to combine two people's work, and this helps you make sure that the changes are consistent and don't lead to broken code.
# 
# Here's how you do it.
# 
# ### How to let someone view your private repository
# 
# You will want to do this with your Project 1 repository in two different ways.
#  * Recall that you're permitted to have a collaborator on Project 1 in MA346 if you want one.  If so, you would add them as a collaborator using the steps below.
#  * Every team will share their Project 1 repository with the instructor, so that I can grade it later.
# 
# The steps for sharing a private repository with selected individuals are very straightforward:
#  * Visit your repository on GitHub.
#  * Click Settings (rightmost tab near the top of the page), then Manage access (near the top left), and Invite teams or people (bottom center).
#  * You'll need the GitHub username of your intended collaborator.  My username on GitHub is (unsurprisingly) `nathancarter`.
# 
# To share a public repository, you can just email the link.  Also, people doing a web search or viewing your GitHub profile can see all your public repositories (but not your private ones, of course).
# 
# ### How to have two contributors in a repository
# 
# Let's say Teammate A creates the repository and shares it with Teammate B, using the procedure described above.  Then Teammate B needs to get their own local copy, like so:
#  * Visit the repository on the GitHub website.
#  * Click the green Code button, and on the menu that appears, choose Open with GitHub Desktop.
#  * This will launch the GitHub app and ask Teammate B to choose where on their computer they'd like to store a clone of the repository.
#     * When you choose a folder, the repository will be placed as a new *folder* inside the one you choose.
#     * For example, if you pick `My Documents\MA346\`, then the repository will be cloned into `My Documents\MA346\the-repo-name\`, with all the files inside that inner folder.
# 
# Then Teammate A can go off and do some work on the project and *Teammate B can do work at the same time.*  They should coordinate, however, so that they don't do conflicting work.  We'll come back to this in detail later.
# 
# Let's say Teammate A accomplishes some stuff and wants to commit it and share it with Teammate B.  They can do this:
#  * Do a commit just as they ordinarily would.  (See instructions up above.)
#  * Push that commit to GitHub just as before.  (See instructions up above.)
#  * Tell Teammate B they have pushed, so that Teammate B knows there's new work they'll want to get.
# 
# Then Teammate B uses the GitHub app to **pull** the latest changes from the repo.  This will download Teammate A's work and automatically merge it in with Teammate B's latest copy of things.
# 
# But wait...that sounds like it could go horribly wrong!  What if Teammates A and B were editing the same file?  Yes, it is important to coordinate, like so:
# 
# **Good ways to collaborate:**
#  * Teammate A can work on data cleaning in one Python script while Teammate B works on data analysis in a Jupyter notebook (a totally different file).
#  * Teammate A works on data analysis code (in a Python file) while Teammate B starts writing a report (in a Word doc).
#  * Teammate A edits code at the top of a file while Teammate B edits different code at the bottom of the same file.
# 
# If you follow one of these workflows, then you will not run into any headaches.  But it is possible to create headaches in two different ways.
# 
# The first headache comes if you both edit the same part of the same file.  Then when Teammate B tries to pull the changes from the repository, `git` will tell them there's a conflict and they need to resolve it.  Resolving the conflict can be done, but it's a huge pain, and would probably require a trip to office hours for help.  Try to avoid it.  (Not that I don't want to see you in office hours---I do!  But I'd love to save you the headache of the problem in the first place.)
# 
# The second headache comes if Teammate B doesn't check to be sure that Teammate A's changes integrate smoothly.  Here's an example of how this might happen:
#  1. Becky edits the last few cells of a Jupyter notebook, sees that they work well, and commits the changes to her local repo.
#  2. She now wants to pass these edits to Carlo, so she uses the GitHub app to push.  The app tells her she can't push yet, because Carlo pushed some changes that Becky needs to download first.  This is great, because it's ensuring that the team makes sure that their work combines sensibly before publishing it online---nice!
#  3. So Becky clicks the Pull button in the app.  Because the team was careful not to edit the same code, it works smoothly and brings Carlo's changes down to Becky's local repo on her laptop.  Great!
#  4. At this point comes the danger:  Becky can push her latest changes to the web, *but she hasn't yet checked to be sure they still work.*  She knows they worked *before* she pulled Carlo's work in.  But what if Carlo changed something that makes Becky's code no longer run?
# 
# It's always important, before pushing your code to the GitHub site, to check once more that it still runs correctly.  If it doesn't, fix the problems and commit the fixes first, before you push to the web.

# ## Complications we're skipping
# 
# Everything you need to know for using `git` in MA346 is described up above.  But there is much more to `git` than this simple chapter has covered.  In particular:
#  * We will not need to introduce the concept of "branches," which are very important for software development teams.  Branches are less important in data science than they are in software development, so we won't cover them.
#  * The instructions above help you avoid the concept of a "merge conflict" (when two people edit the same part of the same file).  Learning how to resolve merge conflicts is an important part of `git` usage, but the instructions above should help you avoid the problem in the first place.
#  * There are many ways to use `git` on the command line, without the GitHub app user interface.  We will not cover those in our course.
# 
# If you're a CIS major or minor and want to dive into the details we're not covering, [DataCamp has a git course](https://learn.datacamp.com/courses/introduction-to-git) that covers many low-level details.  Feel free to take that course if you like while you have free DataCamp access in MA346, but we won't use all those details in our work.
# 
# ```{admonition} Learning on Your Own - VS Code's git features
# ---
# class: alert alert-danger
# ---
# If you use VS Code for your Python coding, you may find it convenient to use VS Code's git features, rather than having to switch back and forth to the GitHub app.  Feel free to investigate those features on your own, and if you do so, prepare a tutorial video for the class covering:
#  * how to do each of the activities covered in these notes using VS Code's `git` support rather than the GitHub app
#  * the advantages and disadvatages to each of those two options
# ```
# 
