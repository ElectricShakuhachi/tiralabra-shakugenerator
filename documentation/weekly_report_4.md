# Report - Week 4

**Total work hours = 8**

| sun | mon | tue | wed | thu | fri | sat |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 2 | 0 | 0 | 0 | 0 | 0 | 6 |

## Activities / Project Progression

- created input converter class to use shaku-files as training material while retaining possibility to quite easily use other types of files by adding additional converters to convert them into integer arrays
- added some shaku -format training material, which are JSON data containing files generated from a separate project (ShakuNotator)
- changed folder structure to divide classes appropriately
- created interface classes enabling standalone iteractive cli usage and preparing for future non-interactive usage as plugin

## Notes on Learning

This weeks activities induced a lot of thought on dependency injection and class and function responsibility / decoupling etc. I have been aware of these principles for a long time, but practicing them is important as I still tend to start coding projects with terrible cohesion and tend to get quite far into it before realizing how bad they are and then start fixing them - which is arduous and quite messy work compared to having predicted intelligent class divisions and dependency management and the like from the start. Project by project I do notice myself catching onto these problems earlier, which feels great, obviously, even as it is still far from satisfactory from a professional standpoint. 

## Challenges / Issues

What is most educational is usually the challenging parts. As such, the above section on Learning somewhat covers one of my challenges, namely dealing with proper design by class divisions, responsibilities, decoupling and the like. I wasn't stuck on these principles, but it took some time and thought to get it to look better.

Specifically, I often have trouble separating UI from application logic. However, from the standpoint of this application, even as it is still important, I consider it a lower priority, because it does not and will not have a graphical user interface and the CLI is also not central to the project, because from end users standpoint it will be a plugin in a program that has its own GUI. Therefore separation from UI is not that much applicable here, because the Interface class in this application is not strictly speaking a user interface, even though it contains a Command Line Interface for testing purposes and in order to use the project as standalone for the purposes of the university course it is developed in. Nonetheless, it would make more sense to separate application logic from a class titled "Interface" - or at least name it otherwise if it in fact is not just an interface class.

Since the changes to the project I made this week were quite drastic, I'm still experiencing some trouble to get it to function, and tests are also not functioning properly due to changes in class structures and naming. 

## What next

Fixing the bugs that were introduced this week.
