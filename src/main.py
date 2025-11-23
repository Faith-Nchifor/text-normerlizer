from sys import argv
from utils import apply_fst
from normalize_en  import get_normilizer as normalize_en
from utils import normalize_text


if __name__ == '__main__':
    number_normalizer_fst =  normalize_en()
    normalize_text('35 times')
    # print(apply_fst('198',number_normalizer_fst))