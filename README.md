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

[Detailed user guide](https://github.com/ElectricShakuhachi/tiralabra-shakugenerator/blob/main/documentation/user_guide.md)

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

[Details on tests](https://github.com/ElectricShakuhachi/tiralabra-shakugenerator/blob/main/documentation/testing.md)

## The future of the application

This application has been developed as part of a university course in the University of Helsinki. In the scope of the course, the interactive usage of the application via terminal was developed, but the application is planned to be used as a plugin for the ShakuNotator (shakuhachi sheet music notation application), also developed as university coursework, but also under continuous development after the course - for personal use.
  The purpose of this application (beyond coursework) is to aid musical composition for shakuhachi. As such, non-interactive usage of the program is to be developed, so as to add it as a plugin to the ShakuNotator, which will handle user interactions with the functionality of this program. The planned use is to generate one or a few measures at a time, and manually review and edit them to be more musically pleasing. Such usage will potentially improve the musical productivity of the user, providing them with melodies corresponding to the shakuhachi style of music, with some added randomness for creative sound. Markov tree musical creation is by far not able to create professional sounding, enjoyable music, but this is why this application is meant to be manually reviewed and edited by the composer, and the application is meant to be used iteratively to generate short parts of the composed music. Future versions will also include features which will verify the output against pre-existing parts of the composition when generating multi-part music, to comply with some regular harmonics of shakuhachi music. What is left to the user is - ideally - the core part of the musical work - concentrating on tweaking the music so as to allow them to reach their desired musical expression.
