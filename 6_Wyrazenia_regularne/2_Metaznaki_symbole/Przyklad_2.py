import re

text = "+48 123 456 789 oraz +48 987 654 321"
pattern = re.compile(r'^\+\d\d \d\d\d \d\d\d \d\d\d') #Początek linii
print(pattern.findall(text))

pattern2 = re.compile(r'\+\d\d \d\d\d \d\d\d \d\d\d$') #Koniec linii
print(pattern2.findall(text))

text_2 = "Witaj! Miło Cię poznać.""Cześć! Co słychać?""Hej! Co słychać?"
pattern3 = re.compile(r'Witaj|Cześć') #| - lub
print(pattern3.findall(text_2,))
