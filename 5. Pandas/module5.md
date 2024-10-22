# Pandas

## Contents

1. [DataFrames](#dataframes)

## DataFrames

`DataFrames` in `pandas` are _classes_ (i.e. additionally defined data types) that represent tables of data. They are made up of a collection `Series` which can represent rows or columns of a table.

```python
import pandas

myDf = pandas.DataFrame(
    {
        "ColumnA": [1, 2, 3],
        "ColumnB": [4, 5, 6]
    }
)
print(myDf)

>>>    ColumnA  ColumnB
>>> 0        1        4
>>> 1        2        5
>>> 2        3        6
```

We can import `DataFrames` from CSV files using the `read_csv` function.

```python
import pandas

df = pandas.read_csv("spotify-2023.csv")

print(df.head())

>>>                             track_name    artist(s)_name  artist_count  ...  instrumentalness_%  liveness_%  speechiness_%
>>> 0  Seven (feat. Latto) (Explicit Ver.)  Latto, Jung Kook             2  ...                   0           8              4
>>> 1                                 LALA       Myke Towers             1  ...                   0          10              4
>>> 2                              vampire    Olivia Rodrigo             1  ...                   0          31              6
>>> 3                         Cruel Summer      Taylor Swift             1  ...                   0          11             15
>>> 4                       WHERE SHE GOES         Bad Bunny             1  ...                  63          11              6
```

List the columns of the `DataFrame`.

```python
print(df.columns)

>>> Index(['track_name', 'artist(s)_name', 'artist_count', 'released_year',
>>>        'released_month', 'released_day', 'in_spotify_playlists',
>>>        'in_spotify_charts', 'streams', 'in_apple_playlists', 'in_apple_charts',
>>>        'in_deezer_playlists', 'in_deezer_charts', 'in_shazam_charts', 'bpm',
>>>        'key', 'mode', 'danceability_%', 'valence_%', 'energy_%',
>>>        'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%'],
>>>        dtype='object')
```

Get the streams `series`.

```python
streams = df["streams"]

print(streams.head())

>>> 0    141381703
>>> 1    133716286
>>> 2    140003974
>>> 3    800840817
>>> 4    303236322
```

Get the top 10 most streamed songs. Note how the dataset has an error.

```python
ranked_by_stream = df.sort_values("streams", ascending = False)
track_and_stream = ranked_by_stream[["track_name", "streams"]]
top10 = track_and_stream.head(10)
print(top10)

>>>                                 track_name                                            streams
>>> 574    Love Grows (Where My Rosemary Goes)  BPM110KeyAModeMajorDanceability53Valence75Ener...
>>> 33                               Anti-Hero                                          999748277
>>> 625                                 Arcade                                          991336132
>>> 253                          Glimpse of Us                                          988515741
>>> 455                         Seek & Destroy                                           98709329
>>> 98                      Summertime Sadness                                          983637508
>>> 891  Come Back Home - From "Purple Hearts"                                           97610446
>>> 427                      Where Are You Now                                          972509632
>>> 322                          I Love You So                                          972164968
>>> 130                              Queencard                                           96273746
```
