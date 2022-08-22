# The Big IMDB quest

In the attached assignment my application scrapes given movie data (title, rating, number of ratings, number of Oscars) from IMDB and adjusts IMDB ratings based on two rules:
- Review Penalizer: based on the reviews, the ratings will be deducted according to the given rule
- Oscar Calculator: the ratings will be grown based on the number of won Oscars

## Base construction of my work

First, I scrape the required data from IMDB TOP250 movies site, but number of Oscars are not visible on this page. To get it, I made an another scraper, which collects the data from the TOP20 movies' own page. After the created of main dataframe, I made a separate function to adjust ratings based on reviews and Oscars, then in the final step I export the results into a json file.

In the unit tests, I made 4 different files:
- two for the URL connection tests, one of them tests the main IMDB page, the other one tests one of the movies' own page
- one for to check the correctness of the calculation of Review Penalizer
- one for to check the correctness of the calculation of Oscar Calculator

## Steps to run

### 1. Install requirement packages in CMD

In first step, please open CMD and navigate to the folder, where you check out/download the files, then run:
```
pip install -r requirements.txt
```
### 2. Run unit tests

Please run the below command in CMD, and if the reply is 'OK', then the test is successful:
```
python -m unittest discover -vvv
```

### 2. Run Scraper and Rating Adjust applications

In CMD, please start to run functions.py application with the below command:
```
python functions.py

```
When the running is done, the application exports a json file to the folder, on TOP20_movies_data name.




