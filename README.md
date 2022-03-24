# tiralabra-shakugenerator

[Specifications](https://github.com/ElectricShakuhachi/tiralabra-shakugenerator/blob/main/documentation/specifications.md)

[Week 1 Report](https://github.com/ElectricShakuhachi/tiralabra-shakugenerator/blob/main/documentation/weekly_report_1.md)
[Week 2 Report](https://github.com/ElectricShakuhachi/tiralabra-shakugenerator/blob/main/documentation/weekly_report_2.md)
[Week 3 Report](https://github.com/ElectricShakuhachi/tiralabra-shakugenerator/blob/main/documentation/weekly_report_3.md)
[Week 4 Report](https://github.com/ElectricShakuhachi/tiralabra-shakugenerator/blob/main/documentation/weekly_report_4.md)
[Week 5 Report](https://github.com/ElectricShakuhachi/tiralabra-shakugenerator/blob/main/documentation/weekly_report_5.md)
[Week 6 Report](https://github.com/ElectricShakuhachi/tiralabra-shakugenerator/blob/main/documentation/weekly_report_6.md)

## User Guide

Install dependencies with poetry:

```bash
poetry install
```

Use invoke rule to run program by command:

```bash
poetry run invoke start
```

[More detailed user guide](https://github.com/ElectricShakuhachi/tiralabra-shakugenerator/blob/main/documentation/user_guide.md)

## Testing

Run unit tests with:

```bash
poetry run invoke test
```

Generate a html coverage report by:

```bash
poetry run invoke coverage-report
```

Coverage report will be generate in html format to the folder "htmlcov" located under project root.

Run lint by:

```bash
poetry run invoke lint
```

[More detailed testing info](https://github.com/ElectricShakuhachi/tiralabra-shakugenerator/blob/main/documentation/testing.md)