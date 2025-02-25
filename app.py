from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
from transformers import pipeline
import os

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/chat', methods=['GET', 'POST'])
def index():
    summary = ""
    user_input_text = ""  # Variable to store user input text
    if request.method == 'POST':
        try:
            model_name = request.form['model']
            summarizer = pipeline('summarization', model=model_name)
        except KeyError:
            return "Model not selected. Please choose a model and try again."

        max_tokens = 1024

        if 'file' in request.files and request.files['file'].filename != '':
            file = request.files['file']
            df = pd.read_csv(file)
            texts = df['text'].tolist()
            summaries = []
            for text in texts:
                if len(text.split()) > max_tokens:
                    return render_template('index.html', summary="Input text exceeds the maximum token limit of 1024 tokens. Please provide a shorter text.", user_input_text="")
                summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
                summaries.append(summary[0]['summary_text'])
            df['summary'] = summaries
            output_file = os.path.join('static', 'summarized_texts.csv')
            df.to_csv(output_file, index=False)
            summary = "Summarization complete! Download the summarized texts from the link below."
        elif 'text' in request.form and request.form['text'] != '':
            text = request.form['text']
            user_input_text = text  # Store user input text
            if len(text.split()) > max_tokens:
                return render_template('index.html', summary="Input text exceeds the maximum token limit of 1024 tokens. Please provide a shorter text.", user_input_text=user_input_text)
            summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
            summary = summary[0]['summary_text']

    return render_template('index.html', summary=summary, user_input_text=user_input_text)

if __name__ == '__main__':
    app.run(debug=True)
