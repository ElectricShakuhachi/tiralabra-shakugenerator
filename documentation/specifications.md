# Specification Document

## Requested Misc Information

- Degree programme: Bachelor's in Computer Science
- Programming language: Python
- Additional possible review languages: C
- Human Language Used: English, reviews for projects in Finnish possible
- Sources: To be determined

## Topic of Project: Musical Accompaniment generator for ShakuNotator

In the course "Ohjelmistotekniikka", I coded the application [ShakuNotator](https://github.com/ElectricShakuhachi/ot-harjoitustyo),
which proved to be a large effort, still under development for personal use after the course. The application is sheet music notation software for Japanese *shakuhachi* -bamboo flute.
As the project for this course, I am developing a tool that can later be integrated to the aforementioned project. It is a Markov chain music generation tool that gets one measure of musical notes in one or multiple parts as input and generates viable accompaniment for them.

In addition, the tool shall be able to be configured so that the music it generates follows scalable parameters as probability indicators for various musical properties. For example, a parameter, a float value between 0-1 could indicate the probability of each note in the produced sequence going up or down. 0 would represent a configuration in which each note would be lower than the previous one, and 1 a configuration the opposite. Any value between that would be a respective probability weight. Other possible scalable parameters could be rhythm bias between slow and fast, prominence of so called meri-notes, dissonance-consonance, etc. Regarding these parameters, the data structures and possible additional algorithms will be determined during the course. It is notable that some of these scales may have contradictions to one another so some form of hierarchical structure will have to be created.

The learning data utilized by the Markov chain implementation will consist of .shaku -files generated with ShakuNotator. However the handling of these files is independent from the earlier project, so that in effect the only link to said project is the .shaku -file structure itself. These files are JSON format files containing the different parts of the music, each containing a set of note data. Additionally .shaku -files contain metadata on the composition such as composer name. The configuration of this project could also include a possibility to exert a bias toward compositions matching certain metadata.

The input data is a set of parts containing each a maximum of 16 notes - each in rhytm configuration that does not exceed one musical measure. The application will generate an accompaniment part matching the input data based on the applications learning data. 

The final use of the application is meant to be an integration into the ShakuNotator -project, however for the purposes of evaluation of this course, functionality is created so as to avoid the need of installation of the separate project. There will be a configuration file, where the input data for the application can be written into, and the application will generate two midi files on each run, one producing only the input data into sound, and another one with the generated accompaniment. A folder with example input data files is provided so reviewers will not have to write input files themselves for manual review - unless they wish to do so.

## Additional functionality that might be developed:

- Inputting an unfinished measure of accompaniment data and having the application finish it instead of generating a completely new accompaniment part