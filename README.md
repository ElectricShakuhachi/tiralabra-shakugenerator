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
poetry run invoke start --count=1
```

Replace 1 with lenght of music to be generated (number of measures)

When running without --count flag with integer, program will generate a default amount of 1 measure lenght of notes

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
