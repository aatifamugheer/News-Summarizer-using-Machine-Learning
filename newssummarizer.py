import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():
    
    url = url_text.get("1.0", tk.END).strip()


    article = Article(url)
    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    authors.config(state='normal')
    publish_date.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    

    title.delete("1.0", tk.END)
    title.insert("1.0", article.title)

    authors.delete("1.0", tk.END)
    authors.insert("1.0", ", ".join(article.authors))

    publish_date.delete("1.0", tk.END)
    publish_date.insert("1.0", article.publish_date)

    summary.delete("1.0", tk.END)
    summary.insert("1.0", article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete("1.0", tk.END)
    sentiment.insert("1.0", f'Polarity: {analysis.polarity}, Sentiment: {"Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"}')

    title.config(state='disabled')
    authors.config(state='disabled')
    publish_date.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')
root = tk.Tk()
root.title("News Summarizer")
root.geometry("600x800")


tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=2, width=100)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text="Authors")
alabel.pack()

authors = tk.Text(root, height=2, width=100)
authors.config(state='disabled', bg='#dddddd')
authors.pack()

plabel = tk.Label(root, text="Publish Date")
plabel.pack()

publish_date = tk.Text(root, height=2, width=100)
publish_date.config(state='disabled', bg='#dddddd')
publish_date.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=100)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=2, width=100)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

url_text = tk.Text(root, height=2, width=100)
url_text.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()

