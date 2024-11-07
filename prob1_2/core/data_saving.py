## run this in python manage.py shell 

# import pandas as pd
# from core.models import Song

# df = pd.read_csv('core/output.csv')

# songs = [
#     Song(
#         index = row['index'],
#         id = row['id'],
#         title = row['title'],
#         danceability = row['danceability'],
#         energy = row['energy'],
#         key = row['key'],
#         loudness = row['loudness'],
#         mode = row['mode'],
#         acousticness = row['acousticness'],
#         instrumentalness = row['instrumentalness'],
#         liveness = row['liveness'],
#         valence = row['valence'],
#         tempo = row['tempo'],
#         duration_ms = row['duration_ms'],
#         time_signature = row['time_signature'],
#         num_bars = row['num_bars'],
#         num_sections = row['num_sections'],
#         num_segments = row['num_segments'],
#         Class = row['class']
#     )
#      for _, row in df.iterrows()
# ]

# Song.objects.bulk_create(songs)