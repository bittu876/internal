import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
dataset = [["I liked the movie", "positive"],
           ["It’s a good movie. Nice story", "positive"],
           ["Hero’s acting is bad but heroine looks good.\
            Overall nice movie", "positive"],
            ["Nice songs. But sadly boring ending.", "negative"],
            ["sad movie, boring movie", "negative"]]
             
dataset = pd.DataFrame(dataset)
dataset.columns = ["Text", "Reviews"]

nltk.download('stopwords')

corpus = []

for i in range(0, 5):
    text = re.sub('[^a-zA-Z]', '', dataset['Text'][i])
    text = text.lower()
    text = text.split()
    ps = PorterStemmer()
    text = ''.join(text)
    corpus.append(text)
print("corpus")
print(corpus)
cv = CountVectorizer(max_features = 1500)

X = cv.fit_transform(corpus).toarray()
print("\n x Values \n")
print(X)
y = dataset.iloc[:, 1].values
print("\n y iloc values \n")
print(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
           X, y, test_size = 0.25, random_state =42)

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

classifier = GaussianNB();
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(" \n y_pred values \n")
print(y_pred)
cm = confusion_matrix(y_test, y_pred)
acc=accuracy_score(y_test,y_pred)
print("\n Accuracy \n")
print(acc)