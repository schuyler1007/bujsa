# bujsa kyoudai matching algorithm

Check spring-2025 branch for updated algorithm, and translated into python: ```big_little_matching.cpp```, with ```matching``` being already compiled executable.

## Web Deployment Version:

Directly upload big and little preference csvs, returning a table of matches from the algorithm. No programming knowledge required, simply save preference forms from google sheets to csv. 

[Link](https://kyoudai-algo-site.vercel.app)

## File Formatting

When uploading the csv, this is incredibly important. Your files MUST look like they do in the examples below. 

[Bigs Preferences Example](https://docs.google.com/spreadsheets/d/1GZn0-PW8SyR_jK4R9T40YpH98LRMZmgFVmsZfHau_VA/edit?gid=0#gid=0) [Littles Preferences Example](https://docs.google.com/spreadsheets/d/11uSyPQk54nS1KL4QzCcnpCK55ClWsT06MEypuzKm2cI/edit?gid=0#gid=0)


## Usage (depreceated, use web delployed version):

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


