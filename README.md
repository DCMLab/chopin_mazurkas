![Version](https://img.shields.io/github/v/release/DCMLab/chopin_mazurkas?display_name=tag)
[![DOI](https://zenodo.org/badge/383397003.svg)](https://doi.org/10.5281/zenodo.7473566)
![GitHub repo size](https://img.shields.io/github/repo-size/DCMLab/chopin_mazurkas)
![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-9cf)


This is a README file for a data repository originating from the [DCML corpus initiative](https://github.com/DCMLab/dcml_corpora)
and serves as welcome page for both 

* the GitHub repo [https://github.com/DCMLab/chopin_mazurkas](https://github.com/DCMLab/chopin_mazurkas) and the corresponding
* documentation page [https://dcmlab.github.io/chopin_mazurkas](https://dcmlab.github.io/chopin_mazurkas)

For information on how to obtain and use the dataset, please refer to [this documentation page](https://dcmlab.github.io/chopin_mazurkas/introduction).

# Frédéric Chopin – Mazurkas (A corpus of annotated scores)


## Getting the data

* download repository as a [ZIP file](https://github.com/DCMLab/chopin_mazurkas/archive/main.zip)
* download a [Frictionless Datapackage](https://specs.frictionlessdata.io/data-package/) that includes concatenations
  of the TSV files in the four folders (`measures`, `notes`, `chords`, and `harmonies`) and a JSON descriptor:
  * [chopin_mazurkas.zip](https://github.com/DCMLab/chopin_mazurkas/releases/latest/download/chopin_mazurkas.zip)
  * [chopin_mazurkas.datapackage.json](https://github.com/DCMLab/chopin_mazurkas/releases/latest/download/chopin_mazurkas.datapackage.json)
* clone the repo: `git clone https://github.com/DCMLab/chopin_mazurkas.git` 


## Data Formats

Each piece in this corpus is represented by five files with identical name prefixes, each in its own folder. 
For example, the Mazurka G major (Brown Index 16, no. 1) has the following files:

* `MS3/BI16-1.mscx`: Uncompressed MuseScore 3.6.2 file including the music and annotation labels.
* `notes/BI16-1.notes.tsv`: A table of all note heads contained in the score and their relevant features (not each of them represents an onset, some are tied together)
* `measures/BI16-1.measures.tsv`: A table with relevant information about the measures in the score.
* `chords/BI16-1.chords.tsv`: A table containing layer-wise unique onset positions with the musical markup (such as dynamics, articulation, lyrics, figured bass, etc.).
* `harmonies/BI16-1.harmonies.tsv`: A table of the included harmony labels (including cadences and phrases) with their positions in the score.

Each TSV file comes with its own JSON descriptor that describes the meanings and datatypes of the columns ("fields") it contains,
follows the [Frictionless specification](https://specs.frictionlessdata.io/tabular-data-resource/),
and can be used to validate and correctly load the described file. 

### Opening Scores

After navigating to your local copy, you can open the scores in the folder `MS3` with the free and open source score
editor [MuseScore](https://musescore.org). Please note that the scores have been edited, annotated and tested with
[MuseScore 3.6.2](https://github.com/musescore/MuseScore/releases/tag/v3.6.2). 
MuseScore 4 has since been released which renders them correctly but cannot store them back in the same format.

### Opening TSV files in a spreadsheet

Tab-separated value (TSV) files are like Comma-separated value (CSV) files and can be opened with most modern text
editors. However, for correctly displaying the columns, you might want to use a spreadsheet or an addon for your
favourite text editor. When you use a spreadsheet such as Excel, it might annoy you by interpreting fractions as
dates. This can be circumvented by using `Data --> From Text/CSV` or the free alternative
[LibreOffice Calc](https://www.libreoffice.org/download/download/). Other than that, TSV data can be loaded with
every modern programming language.

### Loading TSV files in Python

Since the TSV files contain null values, lists, fractions, and numbers that are to be treated as strings, you may want
to use this code to load any TSV files related to this repository (provided you're doing it in Python). After a quick
`pip install -U ms3` (requires Python 3.10 or later) you'll be able to load any TSV like this:

```python
import ms3

labels = ms3.load_tsv("harmonies/BI16-1.harmonies.tsv")
notes = ms3.load_tsv("notes/BI16-1.notes.tsv")
```


## Version history

See the [GitHub releases](https://github.com/DCMLab/chopin_mazurkas/releases).

## Questions, Suggestions, Corrections, Bug Reports

Please [create an issue](https://github.com/DCMLab/chopin_mazurkas/issues) and/or feel free to fork and submit pull requests.

## Cite as

> Hentschel, J., Rammos, Y., Neuwirth, M., Moss, F. C., & Rohrmeier, M. (2024). An annotated corpus of tonal piano music from the long 19th century. Empirical Musicology Review, 18(1), 84–95. https://doi.org/10.18061/emr.v18i1.8903

## License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)).

![cc-by-nc-sa-image](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)

## File naming convention

The file names listed in the [Overview](#overview) below refer to the Brown Index (BI) and opus numbers whereever 
possible. File names ending on `-#` translate to `no. #`.


## Overview
|  file_name  |measures|labels|standard|                             annotators                             |    reviewers    |
|-------------|-------:|-----:|--------|--------------------------------------------------------------------|-----------------|
|BI105-2op30-2|      64|   116|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI105-3op30-3|      95|   159|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH (1-72), AN, DK|
|BI105-4op30-4|     139|   228|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI115-1op33-1|      48|    90|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI115-2op33-2|     135|   202|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI115-3op33-3|      48|   119|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI115-4op33-4|     224|   374|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI122op41-2  |      68|   143|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI126-1op41-4|      74|   151|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI126-3op41-1|     139|   233|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI126-4op41-3|      78|   120|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI134        |     224|   312|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI140        |     247|   213|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI145-1op50-1|     104|   216|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI145-2op50-2|     103|   152|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI145-3op50-3|     192|   309|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI153-1op56-1|     204|   444|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI153-2op56-2|      84|   156|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI153-3op56-3|     220|   481|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|AN, DK           |
|BI157-1op59-1|     130|   257|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|AN, DK           |
|BI157-2op59-2|     111|   209|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|AN, DK           |
|BI157-3op59-3|     154|   358|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|AN, DK           |
|BI16-1       |      32|    51|2.2.0   |Wendelin Bitzan                                                     |JH, AN           |
|BI16-2       |      32|    47|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.3.0)                       |AN, TS           |
|BI162-1op63-1|     102|   169|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|AN, DK           |
|BI162-2op63-2|      56|    80|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|AN, DK           |
|BI162-3op63-3|      76|   123|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|AN, DK           |
|BI163op67-4  |      80|   117|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|AN, DK           |
|BI167op67-2  |      56|    78|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|AN, DK           |
|BI168op68-4  |      40|    80|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|AN, DK           |
|BI18op68-2   |      64|   125|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI34op68-3   |      60|   109|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI38op68-1   |      72|   139|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI60-1op06-1 |      72|   204|2.3.0   |Wendelin Bitzan (2.1.1), AJW (2.3.0), Davor Krkljus (2.3.0)         |AN, AJW, JH, DK  |
|BI60-2op06-2 |      72|   104|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI60-3op06-3 |      90|   145|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI60-4op06-4 |      24|    67|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI61-1op07-1 |      64|   104|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI61-2op07-2 |      56|   114|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI61-3op07-3 |     105|   205|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI61-4op07-4 |      44|   104|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI61-5op07-5 |      20|    38|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI71         |      68|   122|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.3.0)                       |AN, TS           |
|BI73         |      32|    44|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.3.0)                       |AN, TS           |
|BI77-1op17-1 |      60|   112|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI77-2op17-2 |      68|   171|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI77-3op17-3 |      81|   214|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI77-4op17-4 |     132|   226|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI85         |      57|    91|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.3.0)                       |AN, TS           |
|BI89-1op24-1 |      64|   124|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI89-2op24-2 |     120|   226|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI89-3op24-3 |      43|    65|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI89-4op24-4 |     146|   294|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH (1-34), AN, DK|
|BI93-1op67-1 |      60|    94|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI93-2op67-3 |      56|    97|2.3.0   |Wendelin Bitzan (1.0.0), Adrian Nagel (2.2.0), Davor Krkljus (2.3.0)|JH, AN, DK       |
|BI105-1op30-1|      53|     0|        |                                                                    |                 |


*Overview table automatically updated using [ms3](https://ms3.readthedocs.io/).*
