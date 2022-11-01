pet01 = {
    'kind': 'dog',
    'owner': 'john',
    'details':{
        'age':12,
        'name':'fido'
    }
}
pet02 = {
    'kind': 'cat',
    'owner': 'water',
    'details':{
        'age':12,
        'name':'melon'
    }
}
pet03 = {
    'kind': 'dog',
    'owner': 'banana'
}

pets = [pet01, pet02, pet03]

for pet in pets:
    for k,v in pet.items():
        if isinstance(v, dict):
            print(f"{k}:")
            for k1,v1 in v.items():
                print(f"{k1}: {v1}")
        else:
            print(f"{k}: {v}")