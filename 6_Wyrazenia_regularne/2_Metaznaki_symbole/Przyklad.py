import re

text = "Kontaktowy numer telefonu: +48 123 456 789 (dostępny od 8:00 do 16:00)"
pattern = re.compile(r'\+\d\d \d\d\d \d\d\d \d\d\d')
print(pattern.findall(text))

text_2 = "Ala ma kota, nazywa się Mruczek i jest bardzo wesołym zwierzakiem. Mruczek ma 5 lat."
pattern2 = re.compile(r'\d') #tylko cyfry
pattern3 = re.compile(r'\D') #wszystko oprócz cyfr
pattern4 = re.compile(r'\s') #tylko znaki białe
pattern5 = re.compile(r'\w') #litery i cyfry
print(pattern2.findall(text_2))
print(pattern3.findall(text_2))
print(pattern4.findall(text_2))
print(pattern5.findall(text_2))
