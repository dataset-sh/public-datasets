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

my_gpt_opts = GptApiOptions(temperature=1.0)


@def_fn.openai(client=openai_client, opts=my_gpt_opts)
@def_fn.with_instruction("Given a product category, naming style example, and a connotation, suggest a list of new branding names for me."
                         "return them as the exact same format as the example I gave you.")
@def_fn.with_example(
    input={
        'category': 'Animals & Pet Supplies',
        'connotation': '',
        'style_name': '',
        'style_example': '',
    },
    output=[
        "Pawfect Love",
        "SnuggleTails",
        "HeartPaws",
        "FurEver Friends",
        "Paws & Hugs",
        "Furry Bonds",
        "Loyal Paws",
        "CuddlePaws",
        "WarmWhiskers",
    ]
)
def generate_brand(product_category, connotation):
  # any code you wrote here will be ignored.
  pass

def style_and_example(name, examples):
    return {
        'style_name': name,
        'style_example': examples
    }




class BuiltInStyles:
    Descriptive     = style_and_example('Descriptive')
    Evocative       = style_and_example('Evocative')
    Invented        = style_and_example('Invented')
    Abstract        = style_and_example('Abstract')
    Metaphorical    = style_and_example('Metaphorical')
    Phonetic        = style_and_example('Descriptive')
    Exotic          = style_and_example('Exotic')
    Alphanumeric    = style_and_example('Alphanumeric')

if __name__ == "__main__":
    names = generate_product_connotation(
        product_category='Electronics/Video',
        connotation='',

    )
    print(names.value)
