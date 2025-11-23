# Finite State Transducer for numbers 0-1000

Repo Contains:

- The source Code located in `/src`
- The FAR file found in the `data` directory
- The report

To get Started,

- clone this repo. Navigate to the directory
- create a virtual environment with conda: `conda create --name env`
- activate environment: `conda activate env`
- install pynini: `conda install conda-forge::pynini`

- To generate the number FST, run `python src/main.py`
- To use the generated FSTs, run `python src/normalize.py`s
