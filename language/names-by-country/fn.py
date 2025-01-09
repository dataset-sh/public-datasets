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

my_gpt_opts = GptApiOptions(temperature=1.0, n=50)


@def_fn.openai(client=openai_client, opts=my_gpt_opts)
@def_fn.with_instruction("Given the name of a country/region and gender, generate a typical but not so common person's name")
@def_fn.with_example(
    input={
        'country': 'United States',
        'gender': 'Female'
    },
    output='Evelina Harper'
)
@def_fn.with_default_args('Print Hello World')
def generate_names(country, gender):
  # any code you wrote here will be ignored.
  pass


if __name__ == "__main__":
    names = generate_names(country='', gender='')