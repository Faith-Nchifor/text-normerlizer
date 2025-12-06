'''
Some utility functions to create and apply FSTs.
NB:  These methods were copied from the sample notebook demonstrating how FSTs work (https://colab.research.google.com/#scrollTo=I34ODvIYhJw9&fileId=https%3A//huggingface.co/datasets/DigitalUmuganda/Text_Normalization_Challenge_Unittests_Eng_Fra/blob/main/tutorial_FST_text_normalization.ipynb)
'''
import os
import pynini
from pynini.lib import pynutil, utf8

# create a directory to store far files
far_dir = 'data'
os.makedirs(far_dir,exist_ok=True)

far_path = os.path.join(far_dir,'fst.far')

# This function creates an FST that transduces a single input string to a single output string.

def I_O_FST(input_str: str, output_str: str):#, table: pynini.SymbolTable -> pynini.Fst:
    """Creates an FST mapping input_str to output_str."""

    # Ensure inputs are strings
    input_str = str(input_str)
    output_str = str(output_str)
    #Create two FSAs one for the input the other for the output alphabet
    input_accep = pynini.accep(input_str, token_type="utf8")
    output_accep = pynini.accep(output_str,  token_type="utf8")

    # Create the cross-product (input:output transducer), pynini.cross creates an FST from two FSAs
    fst = pynini.cross(input_accep, output_accep)

    return fst.optimize()


# function normalizes text
def apply_fst(text, fst):
    '''finds the best FST for input'''
    try:
        return(pynini.shortestpath(pynini.accep(text,token_type='utf8') @ fst).string("utf8"))

    except Exception as e:
        return(f"Error: {e}, for input:'{text}'")
    

