favorite_number = {
    'water':[1,6,7],
    'melon':[2,9,12],
    'papaya':[3,51,21],
    'banana':4,
    'fruit':5,
    'salad':[6,69,2,1,3],
}

for k,v in favorite_number.items():
    if isinstance(v, list):
        for i in v:
            print(f"{k}: {i}")
    else:
        print(f"{k}: {v}")