import instaloader
import pandas as pd

L = instaloader.Instaloader()

L.login('USER', 'PASSWORD')

USER = 'your_target'
PROFILE = USER

profile = instaloader.Profile.from_username(L.context, PROFILE)

# Menghitung jumlah likes
likes = set()
print('Jumlah like dalam profil {}.'.format(profile.username))
for post in profile.get_posts():
    print(post)
    likes = likes | set(post.get_likes())

print('Jumlah followers dalam profil {}.'.format(profile.username))
followers = set(profile.get_followers())

# Hasil ghost followers dari like terendah
ghosts = followers - likes
print('Ambil ghost followers.')
with open('ghostfol.txt', 'w') as f:
    for ghost in ghosts:
        print(ghost.username, file=f)

db.myCollection.insert(df.to_dict())
