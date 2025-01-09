import sys
import os
import click
from openai import OpenAI
from mkb import def_fn


mkb_openai_api_key = os.environ.get('MKB_OPENAI_API_KEY', None)

if mkb_openai_api_key is None:
    open_ai_key_file = os.path.expanduser('~/.openai.key')
    if os.path.exists(open_ai_key_file):
        with open(open_ai_key_file) as f:
            mkb_openai_api_key = f.read().strip()

if mkb_openai_api_key is None or mkb_openai_api_key == '':
    click.secho('Please set MKB_OPENAI_API_KEY environment variable or ~/.openai.key file.', fg='red')
    sys.exit(1)

from mkb.impl.openai import GptApiOptions
openai_client = OpenAI(api_key=mkb_openai_api_key)

my_gpt_opts = GptApiOptions(temperature=0.5)


@def_fn.openai(client=openai_client, opts=my_gpt_opts)
@def_fn.with_instruction("Given a dataset paper's title and abstract, "
                         "generate list of tags the dataset relevant tags such as its application,source data, usage, problem solved, language, and ,etc.")
@def_fn.with_example(
            input={
                'title': 'Building Large-Scale English and Korean Datasets for Aspect-Level Sentiment Analysis in Automotive Domain',
                'abstract': 'We release large-scale datasets of users’ comments in two languages, English and Korean, for aspect-level sentiment analysis in automotive domain. The datasets consist of 58,000+ commentaspect pairs, which are the largest compared to existing datasets. In addition, this work covers new language (i.e., Korean) along with English for aspect-level sentiment analysis. We build the datasets from automotive domain to enable users (e.g., marketers in automotive companies) to analyze the voice of customers on automobiles. We also provide baseline performances for future work by evaluating recent models on the released datasets.'
            },
            output=[
                'english',
                'korean',
                'automotive',
                'aspect sentiment',
            ]
)
@def_fn.with_example(
            input={
                'title': 'Neural CRF Model for Sentence Alignment in Text Simplification',
                'abstract': 'The success of a text simplification system heavily depends on the quality and quantity of complex-simple sentence pairs in the training corpus, which are extracted by aligning sentences between parallel articles. To evaluate and improve sentence alignment quality, we create two manually annotated sentence-aligned datasets from two commonly used text simplification corpora, Newsela and Wikipedia. We propose a novel neural CRF alignment model which not only leverages the sequential nature of sentences in parallel documents but also utilizes a neural sentence pair model to capture semantic similarity. Experiments demonstrate that our proposed approach outperforms all the previous work on monolingual sentence alignment task by more than 5 points in F1. We apply our CRF aligner to construct two new text simplification datasets, Newsela-Auto and Wiki-Auto, which are much larger and of better quality compared to the existing datasets. A Transformer-based seq2seq model trained on our datasets establishes a new state-of-the-art for text simplification in both automatic and human evaluation.'
            },
            output=[
                'text simplification',
                'sentence alignment',
                'wikipedia',
                'newsela'
            ]
)
def tag_dataset_paper(title, abstract):
  # any code you wrote here will be ignored.
  pass



if __name__ == "__main__":
    names = tag_dataset_paper(
        title='Offensive Language Detection on Video Live Streaming Chat',
        abstract='This paper presents a prototype of a chat room that detects offensive expressions in a video live streaming chat in real time. Focusing on Twitch, one of the most popular live streaming platforms, we created a dataset for the task of detecting offensive expressions. We collected 2,000 chat posts across four popular game titles with genre diversity (e.g., competitive, violent, peaceful). To make use of the similarity in offensive expressions among different social media platforms, we adopted state-of-the-art models trained on offensive expressions from Twitter for our Twitch data (i.e., transfer learning). We investigated two similarity measurements to predict the transferability, textual similarity, and game-genre similarity. Our results show that the transfer of features from social media to live streaming is effective. However, the two measurements show less correlation in the transferability prediction.',
    )
    print(names.value)
