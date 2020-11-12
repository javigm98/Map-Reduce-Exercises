# Map-Reduce-Exercises
Python Map and Reduce functions to solve problems applying well-known map-reduce patterns.

For each exercise it is included the mapper and reducer scripts, the input file used to test it (in the folder Input Files) and an example of output file (in the folder Output Files).

The exercises included are:
### Excercise 1: Distributed Grep
Given a word, the program sould output the lines of the 'input.txt' document that contains it.
- Map Function: [`P1_mapper.py`](P1_mapper.py)
- Reducer Function: [`P1_reducer.py`](P1_reducer.py)
- Input File: [`input.txt`](Input%20Files/input.txt)
- Output File: [`output1.txt`](Output%20Files/output1.txt)
- Test Command: `./P1_mapper.py the < input.txt | sort | ./P1_reducer.py > output1.txt`

### Excercise 2: URL frequency
Find the frecuency of each URL ina  sample Apache log file.
- Map Function: [`P2_mapper.py`](P2_mapper.py)
- Reducer Function: [`P2_reducer.py`](P2_reducer.py)
- Input File: [`access_log`](Input%20Files/access_log)
- Output File: [`output2.txt`](Output%20Files/output2.txt)
- Test Command: `./P2_mapper.py < access_log | sort | ./P2_reducer.py > output2.txt`

### Excercise 3: Stock Summary
Write a MapReduce job to calculate the average daily stock price at close of Alphabet Inc. (GOOG)
per year since 2009. The fields in the .csv file are: Date, Open, High, Low,	Close, Adj Close, Volume
- Map Function: [`P3_mapper.py`](P3_mapper.py)
- Reducer Function: [`P3_reducer.py`](P3_reducer.py)
- Input File: [`GOOGLE.csv`](Input%20Files/GOOGLE.csv)
- Output File: [`output3.txt`](Output%20Files/output3.txt)
- Test Command: `./P3_mapper.py < GOOGLE.csv | sort | ./P2_reducer.py > output3.txt`

### Excercise 4: Movie Rating
Write a two phases map-reduce job to show a range of average ratings and the movies that belong to it: 
Range 1: 1 or lower
Range 2: 2 or lower (but higher than 1)
Range 3: 3 or lower (but higher than 2)
Range 4: 4 or lower (but higher than 3)
Range 5: 5 or lower (but higher than 4)

The map-reduce is performed in two phases: a first one which outputs the movies id and ist average ratings and a second ones that produces the final output.
In the input file the film id corresponds to the first column and the rating is the third one.
- Map Function: [`P4a_mapper.py`](P4a_mapper.py), [`P4b_mapper.py`](P4b_mapper.py)
- Reducer Function: [`P4a_reducer.py`](P4a_reducer.py), [`P4b_reducer.py`](P4b_reducer.py)
- Input File: [`ratings.csv`](Input%20Files/ratings.csv)
- Output File: [`output4.txt`](Output%20Files/output4.txt)
- Test Command: `./P4a_mapper.py < ratings.csv | sort -n| ./P4a_reducer.py | ./P4b_mapper.py | sort | ./P4b_reducer.py > output4.txt`

### Excercise 5: Meteorite Landing
Write a MapReduce job to calculate the average mass per meteorite class. You have to clean de data. The columns needed are the thir one (meteroite class) and the fourth (meteorite mass).
- Map Function: [`P5_mapper.py`](P5_mapper.py)
- Reducer Function: [`P5_reducer.py`](P5_reducer.py)
- Input File: [`Meteorite_Landings.csv`](Input%20Files/Meteorite_Landings.csv)
- Output File: [`output5.txt`](Output%20Files/output5.txt)
- Test Command: `./P5_mapper.py < Meteorite_Landings.csv | sort | ./P5_reducer.py > output5.txt`


