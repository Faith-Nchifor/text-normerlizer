import pynini
from sys import argv
from utils import apply_fst
from utils import normalize_text, far_path
from generate_en_fst import get_normilizer as get_en_normalizer
from generate_fre_fst import get_normilizer as get_fre_normalizer


if __name__ == '__main__':
    en = get_en_normalizer()

    fr = get_fre_normalizer()
    # en = pynini.accep('one')
    # fr  = pynini.accep('two')


    far = pynini.Far(far_path,'w')
   
    far.add('eng_fst', en)
    far.add('fre_fst', fr)
    far.close()



    # normalize_text('35 times')
    # print(apply_fst('198',number_normalizer_fst))