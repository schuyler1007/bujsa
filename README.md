# bujsa kyoudai matching algorithm

Check fall-2023 branch for updated algorithm: ```big_little_matching.cpp```, with ```matching``` being already compiled executable.

## Usage:

1. Open ```/src/match.py```
2. Edit .csv file path for bigs and littles, using formatting given by example files found in ```/misc```
3. Run ```/src/match.py```
4. Output should include the following:
   - Number of bigs and littles
   - Array format of bigs in littles (using curly brackets {})
   - Long list of big names, little names, and numbers next to them
   - Copy _**ONLY**_ the long list of names
6. Edit ```big_little_matching.cpp``` littles variable and bigs variable with respective arrays, and edit num_big and num_little with big/littles amounts
7. Compile ```big_little_matching.cpp``` 
8. Run the compiled file, i.e. ```./matching```
9. Paste output from python script
10. Matched list should output

## Known issues:

- As of now, unmatched littles are automatically assigned to the first listed big, and vice versa, but this does not effect other results

## Future plans:

- Checking for unmatched littles and sending a seperate list
- Automated pipeline from python script to C program
- Integration into web tool so no programming knowledge is necessary to use


