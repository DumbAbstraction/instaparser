import json
import datetime
import operator
import sys

argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

filename = str(argv[0])
targetYear = str(argv[1])
maxList = int(argv[2])

json_data = None
entries = []


class InstaEntry:
	def __init__(self, _url, _likes, _timestamp):
		self.url = _url
		self.likes = _likes
		self.timestamp = _timestamp


with open(filename, "r") as f:
    json_data = json.load(f)

print("Found " + str(len(json_data)) + " total entries.<br>")

for data in json_data:
	rawTimestamp = int(data["taken_at_timestamp"])
	ts = datetime.datetime.fromtimestamp(rawTimestamp).strftime('%Y-%m-%d %H:%M:%S')
	if (ts.startswith(targetYear)):
		url = data["display_url"]
		likes = data["edge_media_preview_like"]["count"]
		ie = InstaEntry(url, likes, ts)
		entries.append(ie)

print("Found " + str(len(entries)) + " from " + targetYear + ".<br>")
entries.sort(key=operator.attrgetter("likes"))

def formatPhoto(index):
	print("<img src=\"" + entries[index].url + "\">")
	print("<i> -> <b>" + str(entries[index].likes) + "</b> likes</i><br>")
	print("<br>")

print("<br>")
print("<h3>" + str(maxList) + " Most Likes:</h3>")
for i in range(0, maxList):
	formatPhoto(len(entries)-i-1)

print("<br>")

print("<h3>" + str(maxList) + " Least Likes:</h3>")
for i in range(0, maxList):
	formatPhoto(maxList-i)



