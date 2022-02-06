# tiralabra-shakugenerator

[Specifications](https://github.com/ElectricShakuhachi/tiralabra-shakugenerator/blob/main/documentation/specifications.md)

[Week 1 Report](https://github.com/ElectricShakuhachi/tiralabra-shakugenerator/blob/main/documentation/weekly_report_1.md)


[Week 2 Report](https://github.com/ElectricShakuhachi/tiralabra-shakugenerator/blob/main/documentation/weekly_report_2.md)


[Week 3 Report](https://github.com/ElectricShakuhachi/tiralabra-shakugenerator/blob/main/documentation/weekly_report_3.md)

## User Guide

Install dependencies with poetry:

```bash
poetry install
```

Application utilizes a list of integers in csv file, located at root directory and namec "training_data.csv"

Training data can be changed by manually editing the list of midi numbers in the file. 

Currently (end of week 3) the training data is too short - during project week 4 a longer, more adequate training data will be added to the same file.

use invoke rule to run program by command:

```bash
poetry run invoke start --count=30
```

replace 30 with lenght of music to be generated (number of notes)

When running without --count flag with integer, program will generate a default amount of 30 notes

Currently (week 3) program only generates same-lenght notes but rhytm variance will be added later. Currently the notes are only generated into a csv temporary file called output.csv. On every run this file will be replaced unless moved or renamed. Later running program will generate a midi file instead.

## Testing

More detailed testing documentation will be created.
Basics of testing:

run tests with:

```bash
poetry run invoke test
```

Generate a html coverage report by:

```bash
poetry run invoke coverage-report
```

Coverage report will be generate in html format to the folder "htmlcov" located under project root.

NOTE: Accurate coverage is provided only by the invoke commands coverage and coverage-report, not in console when running invoke test,
which appears to show lower coverage than actual.

Run lint by:

```bash
poetry run invoke lint
```
