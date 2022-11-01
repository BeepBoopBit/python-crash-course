favorite_places = {
    'water':['philippines', 'korea'],
    'melon':['japan', 'korea'],
    'papaya':['philippines', 'japan', 'korea'],
    'fruit': "watermelon"
}

for k,v in favorite_places.items():
    if isinstance(v, list):
        for i in v:
            print(f"{k}: {i}")
    else:
        print(f"{k}: {v}")