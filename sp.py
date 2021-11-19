import requests
from bs4 import BeautifulSoup

with open("results.txt", mode="w") as f:
  f.write("no,url,title\n")


lines = []
with open("all.txt") as f:
  lines = f.readlines()

for i, line in enumerate( lines ):
  try:
    get = requests.get(line, timeout=10)
    if not get:
      continue
  except:
    continue

  soup = BeautifulSoup(get.text,features="html.parser")
  title_text = ""
  title_tag = soup.select_one("title")
  if title_tag:
    title_text = title_tag.text.replace("\n", "").replace(",", "")
  lineWithoutBrake = line.replace("\n","")

  with open("results.txt", mode="a") as f:

    f.write(f"{i},{lineWithoutBrake},{title_text}\n")