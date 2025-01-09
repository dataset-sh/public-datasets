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

my_gpt_opts = GptApiOptions(temperature=1.0, model='gpt-4o')


@def_fn.openai(client=openai_client, opts=my_gpt_opts)
@def_fn.with_instruction("Given a paper's title and abstract, tell me if the paper is introducing or extending a new dataset. (Yes/No)")
@def_fn.with_example(
            input={
                'title': 'Polish evaluation dataset for compositional distributional semantics models',
                'abstract': 'The paper presents a procedure of building an evaluation dataset. for the validation of compositional distributional semantics models estimated for languages other than English. The procedure generally builds on steps designed to assemble the SICK corpus, which contains pairs of English sentences annotated for semantic relatedness and entailment, because we aim at building a comparable dataset. However, the implementation of particular building steps significantly differs from the original SICK design assumptions, which is caused by both lack of necessary extraneous resources for an investigated language and the need for language-specific transformation rules. The designed procedure is verified on Polish, a fusional language with a relatively free word order, and contributes to building a Polish evaluation dataset. The resource consists of 10K sentence pairs which are human-annotated for semantic relatedness and entailment. The dataset may be used for the evaluation of compositional distributional semantics models of Polish.'
            },
            output='No'
)
@def_fn.with_example(
            input={
                'title': 'French CrowS-Pairs: Extending a challenge dataset for measuring social bias in masked language models to a language other than English',
                'abstract': 'Warning: This paper contains explicit statements of offensive stereotypes which may be upsetting. Much work on biases in natural language processing has addressed biases linked to the social and cultural experience of English speaking individuals in the United States. We seek to widen the scope of bias studies by creating material to measure social bias in language models (LMs) against specific demographic groups in France. We build on the US-centered CrowS-pairs dataset to create a multilingual stereotypes dataset that allows for comparability across languages while also characterizing biases that are specific to each country and language. We introduce 1,679 sentence pairs in French that cover stereotypes in ten types of bias like gender and age. 1,467 sentence pairs are translated from CrowS-pairs and 212 are newly crowdsourced. The sentence pairs contrast stereotypes concerning underadvantaged groups with the same sentence concerning advantaged groups. We find that four widely used language models (three French, one multilingual) favor sentences that express stereotypes in most bias categories. We report on the translation process from English into French, which led to a characterization of stereotypes in CrowS-pairs including the identification of US-centric cultural traits. We offer guidelines to further extend the dataset to other languages and cultural environments.'
            },
            output='Yes'
)
def paper_has_dataset(title, abstract):
  # any code you wrote here will be ignored.
  pass



if __name__ == "__main__":
    names = paper_has_dataset(
        title='CEPOC: The Cambridge Exams Publishing Open Cloze dataset',
        abstract='Open cloze tests are a standard type of exercise where examinees must complete a text by filling in the gaps without any given options to choose from. This paper presents the Cambridge Exams Publishing Open Cloze (CEPOC) dataset, a collection of open cloze tests from world-renowned English language proficiency examinations. The tests in CEPOC have been expertly designed and validated using standard principles in language research and assessment. They are prepared for language learners at different proficiency levels and hence classified into different CEFR levels (A2, B1, B2, C1, C2). This resource can be a valuable testbed for various NLP tasks. We perform a complete set of experiments on three tasks: gap filling, gap prediction, and CEFR text classification. We implement transformer-based systems based on pre-trained language models to model each task and use our dataset as a test set, providing promising benchmark results.',
    )
    print(names.value)
