'''
Create FSTs for numbers from 0 - 1000 in French
'''

import pynini
from utils import I_O_FST, far_dir, apply_fst

units_map = {
    "0": "zéro", "1": "un", "2": "deux", "3": "trois", "4": "quatre",
    "5": "cinq", "6": "six", "7": "sept", "8": "huit", "9": "neuf"
}


teens_map = {
    "10": "dix", "11": "onze", "12": "douze", "13": "treize",
    "14": "quatorze", "15": "quinze", "16": "seize",
    "17": "dix-sept", "18": "dix-huit", "19": "dix-neuf"
}

tens_digit_map = {
    "2": "vingt",
    "3": "trente",
    "4": "quarante",
    "5": "cinquante",
    "6": "soixante",
    "7": "soixante-dix",
    "8": "quatre-vingt",
    "9": "quatre-vingt-dix"
}

hundreds = {
    "100": "cent",
    "200": "deux cents",
    "300": "trois cents",
    "400": "quatre cents",
    "500": "cinq cents",
    "600": "six cents",
    "700": "sept cents",
    "800": "huit cents",
    "900": "neuf cents"
}

import os
import pynini
from utils import I_O_FST, far_dir

units_map = {
    "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
    "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"
}


teens_map = {
    "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen",
    "14": "fourteen", "15": "fifteen", "16": "sixteen",
    "17": "seventeen", "18": "eighteen", "19": "nineteen"
}

tens_digit_map = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}

hundreds = {
    "100": "one hundred",
    "200": "two hundred",
    "300": "three hundred",
    "400": "four hundred",
    "500": "five hundred",
    "600": "six hundred",
    "700": "seven hundred",
    "800": "eight hundred",
    "900": "nine hundred"
}

# FST to insert a space: outputs " "
fst_insert_space = I_O_FST("", " ") # <eps> -> " "

# FST to insert an 'and'
fst_insert_and = I_O_FST("", "and") 

# FSTs for 0-9: list
fst_units_list = [I_O_FST(x, y) for x, y in units_map.items()]


# FSTs for 0 to 9
def generate_unit_FSTs():
    

    fst_units = pynini.union(*fst_units_list).optimize()
    return fst_units

# FSTs for Teens (10-19) - These are irregular
def generate_teen_FSTs():


    fst_teens_list = [I_O_FST(x, y) for x, y in teens_map.items()]
    fst_teens = pynini.union(*fst_teens_list).optimize()
    return pynini.union(*fst_teens_list).optimize()


def generate_fst_tens_digits():
    fst_tens_digit_list = [I_O_FST(digit, text) for digit, text in tens_digit_map.items()]
    fst_tens_digits = pynini.union(*fst_tens_digit_list).optimize()
    return pynini.union(*fst_tens_digit_list).optimize()

# FST to handle the "0" in "20", "30", "40" (consumes "0", outputs nothing)
def generate_tens_FSTs():

    
    fst_eat_zero = I_O_FST("0", "") # "0" -> <eps>
    fst_exact_tens = (fst_tens_digits + fst_eat_zero).optimize()
    return fst_exact_tens

#  FSTs for 21-29
def generate_compund_tens_FSTs():


    compound_units_map = {k: v for k, v in units_map.items() if k != "0"}
    fst_compound_units_digit_list = [I_O_FST(num, text) for num, text in compound_units_map.items()]
    fst_compound_units_digits = pynini.union(*fst_compound_units_digit_list).optimize()

    fst_compound_tens = (fst_tens_digits + fst_insert_space + fst_compound_units_digits).optimize()
    return fst_compound_tens

#  form new FSTs for 100-900 from the units map by adding 'hundreds'
def generate_hundred_units_FSTS():

    hundred_units_map = {k: v for k, v in hundreds.items() }
    fst_h_units_digit_list = [I_O_FST(num, text) for num, text in hundred_units_map.items()]
    fst_h_units_digits = pynini.union(*fst_h_units_digit_list).optimize()
    return fst_h_units_digits

def generate_hundreds():
    single_hundreds = {k[0]: v for k, v in hundreds.items() }
    single_hundreds_list = [I_O_FST(num, text) for num, text in single_hundreds.items()]
    fst_hundreds = pynini.union(*single_hundreds_list).optimize()
    return fst_hundreds

#  another fst for hundred +  compound variables:121-199, 221-299, ... 921-999
def generate_hundreds_compound_FSTs():
    fst_hundreds = generate_hundreds()
    return (fst_hundreds + fst_insert_space + fst_insert_and + fst_insert_space + fst_compound_tens).optimize()



# FSTs for 101 - 109, 201-209,...,901-909
def generate_fst_hundred_units():
    _hundreds = {k[:-1]: v for k, v in hundreds.items() }
    _hundreds_list = [I_O_FST(num, text) for num, text in _hundreds.items()]
    fst_hundreds = pynini.union(*_hundreds_list).optimize()
    fst_units_minus_zero = pynini.union(*fst_units_list[1:]).optimize()
    fst_hundred_units = (fst_hundreds + fst_insert_space +  fst_insert_and + fst_insert_space + fst_units_minus_zero ).optimize()
    return fst_hundred_units


fst_units = generate_unit_FSTs()
fst_teens = generate_teen_FSTs()
fst_tens_digits = generate_fst_tens_digits()
fst_exact_tens = generate_tens_FSTs()

fst_hundreds = generate_hundreds()
fst_compound_tens = generate_compund_tens_FSTs()

# 100,200,...,900
fst_hundred_units = generate_fst_hundred_units()

# FSTs for 121-199, 221-299, ... 921-999
fst_hundreds_compound = (fst_hundreds + fst_insert_space + fst_insert_and + fst_insert_space + fst_compound_tens).optimize()

# FSTs for teens in hundreds
fst_hundred_teens = (fst_hundreds + fst_insert_space +  fst_insert_and + fst_insert_space + fst_teens ).optimize()

# for 120, 130, 140, 150
fst_hundred_tens = (fst_hundreds + fst_insert_space +  fst_insert_and + fst_insert_space + fst_exact_tens ).optimize()

# for 100,200,...,900
fst_hundreds_ = generate_hundred_units_FSTS()

# combine all FSTS 



def get_normilizer():
   
    fst = pynini.union(
    fst_units,           # Handles "0"-"9"
    fst_teens,           # Handles "10"-"19"
   fst_exact_tens,      # Handles "20", "30", "40"
    fst_compound_tens,   # Handles "21-29", "31-39"
    fst_hundred_units,
    fst_hundred_teens,
    fst_hundred_tens,
    fst_hundreds_compound,
    fst_hundreds_
    
    ).optimize()
    text = '290'
    result = apply_fst(text, fst=fst)
    print(result)

    # # save to far file
    # far_path = os.path.join(far_dir,'en_fst.far')
    # far = pynini.Far(far_path,'w')
    # far.add('en_fst', fst)

    # print('done')

if __name__ == "__main__":
    get_normilizer()






