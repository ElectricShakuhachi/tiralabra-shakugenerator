# Shakugenerator User Guide

## How to install:

Install dependencies with poetry:

```bash
poetry install
```

Use invoke rule to run program by command:

```bash
poetry run invoke start
```

## How to use:

At the start, the user will be prompted with two questions in the terminal:

First:

```
Choose type of output
(1 = wav, 2 = csv, 3 = midi 0 = quit) :
```

To choose the type of output, type a single digit as adviced.

Then:

```How many measures should be generated? (0 to quit)```

Type any positive integer, corresponding to the lenght of the generated music. The lenght is measured in musical measures. The lenght of a single measure and the tempo of the music can be configured in the .env -file as adviced below in section "How to configure"

After the user has correctly answered (and not inputted 0 for quit) for the above questions, output is produced in the requested format. The terminal will also display a list of the note pitches and lenghts that were produced. 

If the user chose csv as the required output format, a csv file will be written, where each note representation consists of a pitch integer and lenght integer separated by a regular comma, and the note representations are separated by a semicolon.

If the user chose midi or wav format, the corresponding file is created, from which the music can be played. (Most computers can play wav files, but for midi playback additional applications might need to be installed / configured)

## How to configure



