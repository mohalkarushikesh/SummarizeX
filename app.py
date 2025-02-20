from flask import Flask, request, render_template
import pandas as pd
from transformers import pipeline
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        model_name = request.form['model']
        summarizer = pipeline('summarization', model=model_name)
        
        if 'file' in request.files and request.files['file'].filename != '':
            file = request.files['file']
            df = pd.read_csv(file)
            texts = df['text'].tolist()
            summaries = []
            for text in texts:
                summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
                summaries.append(summary[0]['summary_text'])
            df['summary'] = summaries
            output_file = os.path.join('static', 'summarized_texts.csv')
            df.to_csv(output_file, index=False)
            summary = "Summarization complete! Download the summarized texts from the link below."
        elif 'text' in request.form and request.form['text'] != '':
            text = request.form['text']
            summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
            summary = summary[0]['summary_text']

    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
