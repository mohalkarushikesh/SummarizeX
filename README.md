# SummarizeX

SummarizeX is a web-based application for summarizing text using the Hugging Face Transformers library. Users can either upload a CSV file or enter text directly on the webpage to get the summarized text. The summarized text is displayed on the same webpage, and users can also download the summarized texts if a file is uploaded.

## Features

- Upload a CSV file or enter text directly on the webpage
- Summarize text using Hugging Face's pre-trained models
- Choose from multiple summarization models (BART, T5, Pegasus)
- Display summarized text on the same webpage
- Download summarized texts as a CSV file

## Requirements

- Python 3.6 or higher
- Flask
- pandas
- transformers
- PyTorch or TensorFlow

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/SummarizeX.git
   cd SummarizeX
   ```

2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000/`.

2. You can either upload a CSV file or enter text directly into the textarea.

   - **CSV File**: The CSV file should have a column named `text` containing the text to be summarized.
   - **Text Area**: Enter the text you want to summarize directly into the textarea.

3. Choose the summarization model from the dropdown menu.

4. Click the "Summarize" button.

5. The summarized text will be displayed on the same webpage within a container.

6. If you uploaded a CSV file, you can download the summarized texts as a CSV file by clicking the provided link.

## Example CSV File

```csv
id,text
1,The quick brown fox jumps over the lazy dog.
2,Artificial intelligence is transforming the world.
3,Natural Language Processing is a fascinating field.
```

## Example Input Text

```
Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural-language generation.

The history of NLP generally started in the 1950s, although work can be found from earlier periods. In 1950, Alan Turing published an article titled "Computing Machinery and Intelligence" which proposed what is now called the Turing test as a criterion of intelligence.

In the early days, many language-processing systems were based on complex sets of hand-written rules. Starting in the late 1980s, however, there was a revolution in natural language processing with the introduction of machine learning algorithms for language processing. This was due to both the steady increase in computational power and the gradual accumulation of a vast amount of textual data, which provided the necessary data for machine learning methods.

Early machine learning algorithms applied to NLP were decision trees, but statistical models, especially those based on statistical inference, provided better results. In the 2010s, representation learning and deep neural network-style machine learning methods became widespread in NLP. Popular techniques include word embeddings, like word2vec, and the Transformer model, introduced in a paper titled "Attention is All You Need", which led to the development of pre-trained language models such as BERT and GPT.

Modern NLP algorithms are based on machine learning, especially deep learning methods. Machine learning algorithms for NLP have demonstrated unprecedented efficacy for a variety of tasks, such as machine translation, sentiment analysis, and question-answering systems. Pre-trained models can be fine-tuned for specific applications, making NLP models increasingly versatile and effective.
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


![Image Description](https://github.com/user-attachments/assets/0959e3b7-5275-421c-acb8-65212cf44ea1)

