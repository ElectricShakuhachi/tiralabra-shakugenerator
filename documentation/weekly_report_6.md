# Report - Week 5

**Total work hours = 6**

| mon | tue | wed | thu | fri | sat | sun |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 0 | 1 | 5 |

## Activities

Debugging the remaining problems introduced in large progressions two weeks ago. I found out I had misinterpreted a specific parameter to contain a single list instead of multiple, causing failure in a specific method of another class, and that I had forgotten to convert the note pitch numbers to midi numbers before writing them to a midi file - causing pitches to be to low.
  After tracking and then fixing said problems, I added some documentation, fixed tests that had been broken by the update having changed class structure, and added some more tests. I also added a functionality to make sure that some additional musical rules are followed besides the Markov chain functionality - in order to avoid some overfitting etc. 

## Project Progression

Bugfixes, additional functionality for better music to be generated. Better tests, repo cleanliness and some added clarity in readability. Project is near end, with some additional functions to be added, as well as more training data so that the generated music would be better fitted for shakuhachi music. More documentation and tests will have to be done before the deadline of the entire project but it looks like everything like that is going to be done by the end of the course.


## Notes on Learning

Bugs were a bit hard to track due to not having docstrings on some classes and methods, and due to some ambiguous variable names (notably "data" as parameter in many cases) I learned about the importance of continuous documentation and thought toward future readability and such. 
 I also saw in practice what I had learned in theory about Markov strings - how some patterns could lead to an endless string of looped input if it was not manually protected against or if the training data wasn't sufficient. This possibility was logically apparent from the get go, but it was important to see it happen, so one would remember it better.

## Challenges / Issues

Bugfixes took quite a long time, leaving a bit little time for development of new features / documentation etc. other activities. Since I work full time along with studies and have small children, time cannot be added to the maximum allotted time that I have for the project - so it is paramount to develop and document well and with thought to avoid as much as possible having to spend a lot of time tracking a bug.

## What next

Adding training data and a couple of small extra functionalities, adding tests and checking formal rules and such, cleaning repo, documenting, etc. polishing project toward the finish.