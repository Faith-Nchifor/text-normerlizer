import pynini
import time
from utils import  far_path
from generate_en_fst import get_normilizer as get_en_normalizer
from generate_fre_fst import get_normilizer as get_fre_normalizer


if __name__ == '__main__':
    start  = time.time()
    en = get_en_normalizer()

    fr = get_fre_normalizer()
    
    end = time.time()

    print('compilation time:', end - start, 'seconds')


    far = pynini.Far(far_path,'w')
   
    far.add('eng_fst', en)
    far.add('fre_fst', fr)
    far.close()



    