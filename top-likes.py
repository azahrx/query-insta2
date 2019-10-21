import pandas as pd
import pymongo
from instaloader import Instaloader, Profile

PROFILE = 'your_username'

L = Instaloader()

profile = Profile.from_username(L.context, PROFILE)

# Mengurutkan post berdasarkan banyaknya likes
posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes, reverse=True)

for i in posts_sorted_by_likes:
   print(i)
with open('toplikes.txt', 'w') as f:
    for i in posts_sorted_by_likes:
        print(i, file=f)

db.myCollection.insert(df.to_dict())
