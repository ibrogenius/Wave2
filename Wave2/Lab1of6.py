verse = '''If you can keep your head when all about you
Are losing theirs and blaming it on you, 
If you can trust yourself when all men are doubt you,
But make allowance for their doubting too; 
If you can wait and not be tired by waiting,
Or being lied about, don't deal in lies,
Or being hated, don't give way to hating,
And yet don't look too good, nor talk too wise'''

print(verse, '\n')
verse_list = verse.split()
print(verse_list, '\n')
verse_set = set(verse_list)
print(verse_set, '\n')
num_unique = len(verse_set)
print(num_unique, '\n')