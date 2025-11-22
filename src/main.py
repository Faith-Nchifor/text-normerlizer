from sys import argv
from utils import apply_fst
from normalize_en  import get_normilizer as normalize_en


if __name__ == '__main__':
    number_normalizer_fst =  normalize_en()
    print(apply_fst('198',number_normalizer_fst))