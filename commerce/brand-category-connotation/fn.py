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
@def_fn.with_instruction("Given a product category, produce a list os possible connotation that a brand can be associated with, "
                         "return them as the exact same format as the example I gave you.")
@def_fn.with_example(
    input='Vehicles & Parts/Vehicles/Watercraft/Yachts',
    output=[
        "Luxury & Prestige",
        "Freedom & Adventure",
        "Innovation & Technology",
        "Connection to Nature",
        "Tradition & Heritage",
        "Adventure & Sport",
    ]
)
def generate_product_connotation(product_category):
  # any code you wrote here will be ignored.
  pass



if __name__ == "__main__":
    names = generate_product_connotation('Electronics/Video')
    print(names.value)
