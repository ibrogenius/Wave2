elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

elements['hydrogen']['is noble gas'] = False
elements['helium']['is noble gas'] = True

print(elements['hydrogen']['is noble gas'])
print(elements['helium']['is noble gas'])