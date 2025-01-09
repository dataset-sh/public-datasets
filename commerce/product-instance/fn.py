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
@def_fn.with_instruction("Given a product category, name some instances of that category, "
                         "return them as the exact same format as the example I gave you.")
@def_fn.with_example(
    input='Baby Food',
    output=[
        "Pureed Carrots",
        "Mashed Bananas",
        "Squash Puree",
        "Applesauce",
        "Peach Puree",
        "Mixed Vegetable Puree",
        "Chicken and Rice Baby Food",
        "Oatmeal Cereal",
        "Pea Puree",
        "Sweet Potato Puree",
        "Pork and Apple Mash",
        "Rice Cereal"
    ]
)
def generate_product_instances(product_category):
  # any code you wrote here will be ignored.
  pass



if __name__ == "__main__":
    names = generate_product_instances('Vehicles & Parts/Vehicles/Watercraft/Yachts')
    print(names.value)
