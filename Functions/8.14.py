def car(manufacturer, model, **stuffs):
    stuffs['manufacturer'] = manufacturer
    stuffs['model'] = model
    return stuffs

print(car('subaru', 'outback', color='blue', tow_package=True))
print(car('subaru', 'outback', color='blue', tow_package=True, year=2018))
print(car('subaru', 'outback', color='blue', tow_package=True, year=2018, price=20000))
