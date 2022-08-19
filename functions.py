from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np

def Scraper():
    url = 'https://www.imdb.com/chart/top/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    movies = soup.select('td.titleColumn')

    # as of the number of Oscars visible just on the movie's own page, then I created a loop to scrape the first 20 movies
    movie_id=[b.attrs.get('href') for b in soup.select('td.posterColumn a')]
    oscar_df=pd.DataFrame(columns=[0])

    for m in movie_id[:20]:
        url_id = 'https://www.imdb.com'+ m
        r2 = requests.get(url_id)
        soup2 = BeautifulSoup(r2.content, 'html5lib')
        movie_nr=[b for b in soup2.find('a', attrs={'class': 'ipc-metadata-list-item__label ipc-metadata-list-item__label--link', 
                                                    'href' : re.compile('awards')})]
        oscar_df.loc[len(oscar_df)]=movie_nr

    oscar_df=oscar_df[0].str.split(' ',5,expand=True)
    for c in oscar_df:
        if str(oscar_df[c].dtype) in ('object', 'string_', 'unicode_'):
            oscar_df[c].fillna(value='', inplace=True)

    oscar_df[1]=np.where((oscar_df[1]=="for") | (oscar_df[1]==""),0,oscar_df[1])
    oscar_nr=oscar_df[1].to_dict()


    # split ratings and number of ratings from text field
    rating=[b.attrs.get('title') for b in soup.select('td.ratingColumn strong')]

    rating_df=pd.DataFrame(rating)
    rating_df=rating_df[0].str.split(' ',5,expand=True)
    rating_nr=rating_df[3].str.replace(',','').astype(int).to_dict()

    # it will be the final df
    movie_list=pd.DataFrame(columns=['title','ratings','nr_of_ratings', 'nr_of_oscars'])

    for index in range(0, len(movies[:20])):
        movie_string = movies[index].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        if index>9:
            movie_title = movie[len(str())+3:-7] 
        else:
            movie_title = movie[len(str())+2:-7]
        data = [movie_title, rating[index][:3], rating_nr[index], oscar_nr[index]]

        movie_list.loc[len(movie_list)]=data

    movie_list=movie_list.sort_index(ascending=False).reset_index(drop=True)
    return movie_list


def RatingAdjustment():
    movie_list=Scraper()
    movie_list['adj_ratings']=movie_list['ratings'].copy()
    movie_list['adj_ratings']=movie_list['adj_ratings'].astype(float)
    movie_list['nr_of_oscars']=movie_list['nr_of_oscars'].astype(float)
    
    # Review Penalizer
    def ReviewPenalizer():
        movie_list['adj_ratings']=movie_list['adj_ratings']-((((max(movie_list['nr_of_ratings'])-movie_list['nr_of_ratings'])/100000).apply(np.floor))*0.1)
        return movie_list

    # Oscar Calculator
    def OscarCalculator():
        movie_list=ReviewPenalizer()
        movie_list.loc[(movie_list['nr_of_oscars'].between(1,2)), 'adj_ratings'] = movie_list['adj_ratings']+0.3
        movie_list.loc[(movie_list['nr_of_oscars'].between(3,5)), 'adj_ratings'] = movie_list['adj_ratings']+0.5
        movie_list.loc[(movie_list['nr_of_oscars'].between(6,10)), 'adj_ratings'] = movie_list['adj_ratings']+1
        movie_list.loc[(movie_list['nr_of_oscars']>10), 'adj_ratings'] = movie_list['adj_ratings']+1.5
        return movie_list
    return OscarCalculator().to_json('TOP20_movies_data.json', orient='records', force_ascii=False)

if __name__ == '__main__':
    print("IMDB Scraper and Rating Adjustment functions started running...")
    RatingAdjustment()
    print("TOP20_movies_data.json have been saved in the folder")

