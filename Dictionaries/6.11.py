cities = {
    'water':{
        'country':'philippines',
        'population': 1000000
    },
    'melon':{
        'country':'japan',
        'population': 2000000
    },
    'papaya':{
        'country':'korea',
        'population': 3000000
    },
}

for k,v in cities.items():
    print(f"{k}:")
    for i in v:
        print(f"{k}: {i}")