"""
Nomadcoder Python Study 1st
For Loop code challenge by jh0152park
created at 2024.03.17
"""

import requests

BASE_URL = "https://nomad-movies.nomadcoders.workers.dev/movies/"
movie_ids = [
    238,
    680,
    550,
    185,
    641,
    515042,
    152532,
    120467,
    872585,
    906126,
    840430,
]

for id in movie_ids:
    data = requests.get(f"{BASE_URL}{id}").json()
    print(
        f"Title: {data['title']}\nScore: {data['vote_average']}\nOverview: {data['overview']}\n\n"
    )
