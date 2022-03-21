import re


text = "Ala ma kota, nazywa się Mruczek i jest bardzo wesołym zwierzakiem."
pattern = re.compile(r"[a-d]")
pattern2 = re.compile(r"[a-z]")
pattern3 = re.compile(r"[a-zA-Z]")

print(pattern.findall(text))
print(pattern2.findall(text))
print(pattern3.findall(text))