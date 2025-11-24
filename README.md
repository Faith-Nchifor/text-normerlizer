# Finite State Transducer for numbers 0-1000 

Normalizes numbers from 0- 1000 in either English or French

**This repo Contains:**

- The source Code located in `/src`
- The FAR file found in the `data` directory
- The report explaining my findings and methods

## Structure of Repo

- `data/   ` contains the FAR archive of normalized numbers from 0-1000 for both French and English
- `scr/` Is the source code of the repo
- - `generate_en_fst.py` and `generate_fre_fst.py` are used to generate FSTs for English and French 
- - `utils.py` are utility functions that help the program run
- - `normalize.py` calls the FSTs to normalize input sentences
- `requirements.txt` lists the packages required for this project to run
- `fst_report.pdf` explains my methodology and findings

### To get Started,

- clone this repo. Navigate to the parent directory
- create a virtual environment with conda: `conda create --name env`
- activate environment: `conda activate env`
- install pynini: `conda install conda-forge::pynini`

### To normalize input text to either French or English
- To use the generated FSTs, run `python src/normalize.py --text "what is 41 times 970?" --lang "eng"` 
- The options for `--lang` are `eng` for English and `fre` for French.
- You replace the `--text` argument with your prefered text. If you do not provide either `text` or `lang`, the default `text` and `lang` variables would be used. 


### To compile a new FST file
(This is already found in /data/fst.far)

- run `python src/main.py`

