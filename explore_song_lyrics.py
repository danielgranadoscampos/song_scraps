# Explore song lyrics

#pandas
import pandas as pd

#chart url
url = 'http://kworb.net/spotify/country/cr_weekly.html'
df = pd.read_html(url)

dfs = df[0]
dfs

#lyrics genius
import lyricsgenius as lg

# Here you need to insert your token from de client in your genius app
genius = lg.Genius("your token")

# Changing name of columns
dfs[['singer', 'song_name']] = dfs['Artist and Title'].str.rsplit(' - ',n=1, expand=True)

# initialize a list to store the lyrics
lyrics_list = []

# iterate over the rows of the dataframe
for i, row in dfs.iterrows():
    # get the artist and song name from the row
    artist = row['singer']
    song_name = row['song_name']
    
    # search for the song lyrics
    song = genius.search_song(song_name, artist)
    if song is not None:
        # append the lyrics to the list if the song was found
        lyrics_list.append(song.lyrics)
    else:
        # append None if the song was not found
        lyrics_list.append(None)


# Here we make text readable (no "/" and no "/n" )
lyrics_list = [s.replace("\n", "") for s in lyrics_list]

my_list = [s.replace("\n", " ").replace("\\", " ") if s is not None else s for s in lyrics_list]

import re

my_list = [s for s in my_list if isinstance(s, str)]

my_list = [re.sub(r'\[.*?\]', '', s) for s in my_list]

# Join full text
text = " ".join(my_list)


# Explore lyrics in a world cloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt


sw = {'-','a','ante', 'bajo', 'cada', 'con','cómo', 'como', 'cuando', 'de', 'del', 'desde', 'e','eh', 'el', 'en', 'entre', 'es', 'eso', 'este', 'está', 'la', 'las', 
              'le', 'les', 'lo', 'los','más', 'mi', 'mi', 'me', 'muy', 'ni', 'no', 'o', 'oh', 'para', 'pero', 'por', 'que', 'qué', 'se', 'sé', 'si', 'sin', 'sobre', 'su', 
              'sus','ti', 'te', 'tu', 'tú','uh','un', 'una', 'uno', 'y', 'ya', 'yo'}


wordcloud = WordCloud(stopwords=sw).generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()