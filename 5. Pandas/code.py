import pandas

df = pandas.read_csv("spotify-2023.csv")

ranked_by_stream = df.sort_values("streams", ascending = False)
track_and_stream = ranked_by_stream[["track_name", "streams"]]
top10 = track_and_stream.head(10)
print(top10)

