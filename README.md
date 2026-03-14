# Cyrillic-to-Latin Converter for Bezhta

## Basic usage

- Clone the repository (or just download `transcr_bezhta.py` and skip this):
```bash
$ git clone -q https://github.com/snagbreac/transcr-bezhta.git
$ cd transcr-bezhta
```
- Create `input.txt` (should contain the text for transcription) in the same folder as `transcr_bezhta.py`:
```bash
$ echo "Аьдам-инсаллис бишшун йукъо бечелъи гей аьдаьмли мегьцас миц." >> input.txt
```
- Run `transcr_bezhta.py`:
```bash
$ python transcr_bezhta.py
```
- The results will be in `output.txt`:
```bash
$ cat output.txt
ädam-insallis biššun juq’o bečełi gej ädämli mehcas mic.
```