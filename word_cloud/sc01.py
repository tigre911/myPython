import json
import re
import jpype
import konlpy.tag
from konlpy.tag import Okt
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud

inputFileName = 'etnews.kr_facebook_2016-01-01_2018-08-01_4차 산업혁명'
data = json.loads(open(inputFileName+'.json', 'r', encoding='utf-8').read())

message=''
for item in data:
    if 'message' in item.keys():
        message = message + re.sub(r'[^\w]', ' ', item['message'])+''

print(message)
nlp = konlpy.tag.Okt()
nlp = Okt()
message_N = nlp.nouns(message)
print(message_N)

count = Counter(message_N)
print(count)

word_count= dict()

for tag, counts in count.most_common(80):
    if(len(str(tag)) > 1):
        word_count[tag] = counts

font_path = "C:/Windows/fonts/malgun.ttf"

wc = WordCloud(font_path=font_path,background_color='white', width=800, height=600)
cloud = wc.generate_from_frequencies(word_count)
plt.figure(figsize= (8,8))
plt.imshow(cloud)
plt.axis('off')
plt.show()