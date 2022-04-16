import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Daten lesen
data = pd.read_csv("Spam data.csv")

# Data Understanding
# print(data.values)
print(data.head())

# Summary Stats
print(data.describe())
Category_distr = pd.DataFrame(data["Category"].value_counts())

# Verteilung Category
print(Category_distr["Category"] / len(data.index))

# NAs
print(pd.isnull(data).sum())

# Anzahl Wörter pro Message
spam = data[data["Category"] == "spam"]
true = data[data["Category"] == "ham"]
Word_count_spam = [len(message.split()) for message in spam["Message"]]
Word_count_true = [len(message.split()) for message in true["Message"]]
Word_count = pd.DataFrame({'value': [round(st.mean(Word_count_spam), 2),
                                        round(st.mean(Word_count_true), 2)],
                           'Category': ["spam", "true"]})

print(round(st.mean(Word_count_true), 2), round(st.mean(Word_count_spam), 2))

# Bar chart
Word_count.plot.bar(x = 'Category', y = 'value', rot = 0, title = "Anzahl Wörter pro Message")
plt.show()

# Wordcloud ohne stopwords
sw = set(STOPWORDS)
wc_spam = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=sw).generate(str(spam["Message"].values))
wc_true= WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=sw).generate(str(true["Message"].values))

plt.imshow(wc_true, interpolation="bilinear")
plt.axis("off")
plt.title("Wordcloud true")
plt.savefig("Wordcloud_true.png")
plt.show()

plt.imshow(wc_spam, interpolation="bilinear")
plt.axis("off")
plt.title("Wordcloud spam")
plt.savefig("Wordcloud_spam.png")
plt.show()


# save plots
