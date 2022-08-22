# The Big IMDB quest

In the attached assignment my application scrapes given movie data (title, rating, number of ratings, number of Oscars) from IMDB and adjusts IMDB ratings based on two rules:
- Review Penalizer: based on the reviews, the ratings will be deducted according to the given rule
- Oscar Calculator: the ratings will be grown based on the number of won Oscars

## Base construction of my work

First, I scraped the required data from IMDB TOP250 movies site, but number of Oscars were not visible on this page. To get it, I made an another scraper, which collected the data from the TOP20 movies' own page. After the creation of the main dataframe, I made separate functions to adjust ratings based on reviews and Oscars, then in the final step I exported the results into a json file.

For the unit tests, I made 4 different files:
- two for the URL connection tests, one of them tests the main IMDB page, the other one tests one of the movies' own page
- one to check the correctness of the calculation of Review Penalizer
- one to check the correctness of the calculation of Oscar Calculator

## Steps to run

### 1. Install requirement packages in CMD

In first step, please open CMD and navigate to the folder, where to you check out/download the files, then run:
```
pip install -r requirements.txt
```
### 2. Run unit tests

Please run the below command in CMD, and if the final reply is 'OK', then the tests are successful:
```
python -m unittest discover -vvv
```

### 2. Run Scraper and Rating Adjustment applications

In CMD, please run functions.py application with the below command:
```
python functions.py
```
When the running is done, the application will export a json file to the folder, with TOP20_movies_data name.




