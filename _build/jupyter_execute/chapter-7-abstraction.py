# Abstraction

<a href="../../_slides/chapter-7-slides.html">See also the slides that summarize a portion of this content.</a>


```{warning}
These notes are not yet written.  I'll come back and do that later.
```

* In mathematics
  * Binders: limits, summations, products, integrals, quantification, etc.
    * Note that we will be using quantification to discuss lots of stuff throughout the course, so don't be shy with it!  I'm not suggesting we necessarily introduce $\forall,\exists$, but you can introduce "each" and "all" and various synonyms.
    * Simply introduce these as small scopes.  They introduce a variable we use for just a short time.  That's their job.
    * But they connect to functions in that $f(x)=x^2$ is shorthand for $f=\lambda x.x^2$, and thus all binders are really operations on functions that serve as the body.  Maybe don't mention this here; you're coming to lambda in Python below…revisit then.
  * Learning from examples to general principles, which humans are good at, but computers aren't.
  * "Given numbers x, y, and z, we define..."
* In computing (:framed_picture: is being able to answer lots of questions about this, as well as being able to do it)
  * Lambda expressions
  * What should make a coder realize it's time to apply this skill?
    * Multi-line blocks of code repeated many times with different parameters that should use functions.
    * A single-line block of code repeated many times but in a clear numeric progression, which should use a loop.
    * For realistic examples of these, peruse the code submitted to MA346 Project 2 Spring 2020.
  * You can teach it as steps, perhaps starting with a smaller step such as "move all the changeable values out into parameters at the outset."
  * Are there IDEs that can help?  (Could be a team essay/video/presentation.)
* Practice doing this with LOTS of code examples, creating functions, loops, etc. (and Streamlit scripts later)
  * Once they've practiced it on small examples, have them do it on the same homework they turned in last week, in which the same analysis code was repeated twice for two different subsamples.  Merge these into function definitions and calls instead.  This will also require updating the comments!
* LOYO (since we now know how to write DRY code):
  * Making your own Python modules (see your old MA705/346 content on this) :bulb: