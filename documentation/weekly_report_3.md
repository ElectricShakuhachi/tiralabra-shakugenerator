# Report - Week 3

**Total work hours = 6**

| sun | mon | tue | wed | thu | fri | sat | sun |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 0 | 1 | 3 | 2 |

## Activities

Set up unittest cases for trie class and generator class. Various
small bugfixes and additions to code in the two classes. Thoughwork
on how to procede with project, but clear focus on test cases this
week. Functionality to create and fill trie tree is central to the
project so testing it well is paramount.

Almost perfect code coverage at this point and also checked compliance
to style conventions by checking with pylint.

Code coverage reporting enabled and wrote some basic testing documentation.

## Project Progression

Fixed existing classes and worked on functionality to make sure properly responding to different input. Ready to code more features during next week - mostly concentrating on writing generated musical
part into a file and converting that to a playable midi. 

## Notes on Learning

I learned a lot about testing this week, re-strenghtening my knowledge
on what sort of input should be tested against and how to encapsulate parts of the code so that it doesn't provide entry point for non-defined input / behaviour by user. Also thought well about the possible amount of training data required and possibly generating tests to provide user with info on how much training data is adequate as well. That is in part a subjective matter, but a user might benefit from a subjective developer opinion being displayed when entering possibly inadequate amounts of data.

## Challenges / Issues

I wrote a couple of mistaken test prints inside code to see how it functions and it led me astray for a couple of hours trying to fix a problem that didn't exist. It taught me a valuable lesson on making sure testing methods are proper before acting on test results. Now testing is developed rather well in my opinion and it provides a good base to continuing with the project during next week. But it is important to keep developing testing semi-simultaneously with development. I tend to first develop a lot and then make test cases. This causes problems when bugs are discovered late. I have now learned about that and will keep writing tests too as I write classes and functions.

## What next

Developing functionality to save a list of generated midi integers and then another class to converting that to a playable midi file. And making sure testing is written pretty much together with class development.
