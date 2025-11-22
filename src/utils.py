import pynini

# Cell 3: Helper function to create input:output FSTs
# This function creates an FST that transduces a single input string to a single output string.

def I_O_FST(input_str: str, output_str: str):#, table: pynini.SymbolTable) -> pynini.Fst:
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


def apply_fst(text, fst):
    '''finds the best FST for input'''
    try:
        return(pynini.shortestpath(pynini.accep(text,token_type='utf8') @ fst).string("utf8"))

    except Exception as e:
        return(f"Error: {e}, for input:'{text}'")