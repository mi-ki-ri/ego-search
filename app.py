from googlesearch import search

with open("mikiri_ja.txt", mode="w") as f:
  f.write("")
with open("mikiri_en.txt", mode="w") as f:
  f.write("")

with open("mikiri_ja.txt", mode="a") as f:

  for url in search('"見切り発車P"', lang="ja", tld="co.jp"):
      print(url)
      f.write(url)
      f.write("\n")

with open("mikiri_en.txt", mode="a") as f:

  for url in search('"Mikirihassha P"', lang="en", tld="com"):
      print(url)
      f.write(url)
      f.write("\n")