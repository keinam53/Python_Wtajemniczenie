import re

text = "Ala ma kota, nazywa się Mruczek i jest bardzo wesołym zwierzakiem. Mruczek ma 5 lat."
pattern = re.compile(r".") #. - wszystkie znaki
print(pattern.findall(text))

text_2 = "00-123"
pattern_2 = re.compile(r"\d\d.\d\d\d")
print(pattern.findall(text_2))
