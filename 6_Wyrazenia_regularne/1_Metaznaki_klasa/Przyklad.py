import re


text = "Ala ma kota, nazywa się Mruczek i jest bardzo wesołym zwierzakiem."
pattern = re.compile(r'[abc]')
pattern1 = re.compile(r'[abc].')
pattern2 = re.compile(r'[abc.]')
pattern3 = re.compile(r'[^aoeiu]')

print(pattern.findall(text))
print(pattern1.findall(text))
print(pattern2.findall(text))
print(pattern3.findall(text))
