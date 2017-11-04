import feedparser

d = feedparser.parse('http://www.iium.edu.my/rss/announcement_rss')

for entry in d.entries:
	print (entry.published, entry.title)

