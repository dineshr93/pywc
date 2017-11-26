from wordcloud import WordCloud
# Read the whole text.
text = open('pdf.txt').read()
# Generate a word cloud image
wordcloud = WordCloud().generate(text)
# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud.recolor(random_state=2017))
plt.title('Most Frequent Words')
plt.axis('off')
plt.show()
#----output----