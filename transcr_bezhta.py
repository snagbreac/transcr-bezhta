import unicodedata

normalization_dict = {
    'я': 'йа',
    'a': 'а',
    'o': 'о',
    "e": "е",
    "y": "у",
    "u": "и",
    '': 'ᴴ',
    '': 'ᴴ',
    '': 'а\u0304',
    '': 'о\u0304',
    '': 'е\u0304',
    unicodedata.normalize('NFD', 'й'): 'й',
    '\u0304ь': 'ь\u0304',
}

confusables_I = "i𝛊𝖫۱𝓁ⵏ𝘭𝐥ꓡℐ𝙻ℹ𝜄𝗹𝓛ӏⅠ𐌠𝙡Ⲓ𝕃𝙇𞸀ıᎥ𝐢𝘐￨𝑖𝗟𝑳𖼨Ꙇ𐊊Ɩ𝒊𝞲ן𝚕ߊ𝕴і𝗜ͅ𝛪𝐼Ι𝘓ⅈ١𝗅ｉ𝗶ꭵ𝜤𝙸𝓲𐌉ⅼ𝕷ⅰＬ𝝞˛𐔦𝞘ℒɩ𝟷𝑰𝈪𐐛ǀ𑢲ᒪℓⳐ𖼖𝟭Ӏ𝖑𝘪𝝸𑢣𝚤𝚰𝔏Ꮮ𝚒𝙄𝒾׀𞺀ｌ𝔩Іɪꙇاﺎ𝜾𞣇Ɪ𝖨⏽𑣃𝖎𝟙∣𝕝𝐈𝔦ו⍳🯱ᛁﺍ𝕚𝙞𝐋𝐿𝒍ͺ𝓘𝑙ℑ𝟣ꓲⲓ𝕀𝗂|Ｉ𝓵Ⅼι"
for confusable in confusables_I:
    normalization_dict[confusable] = 'i'

digraphs_cyr2lat = {
    'пi': 'p’',
    'тi': 't’',
    'цi': 'c’',
    'чi': 'č’',
    'лi': 'ƛ',
    'лъ': 'ł',
    'кь': 'ƛ’',
    'кi': 'k’',
    'гъ': 'ʁ',
    'хъ': 'q',
    'къ': 'q’',
    'хi': 'ħ',
    'гi': 'ʕ',
    'гь': 'h',
    "аь": "ä",
    "оь": "ö",
    "уь": "ü",
}

consonants_cyr2lat = {
    'п': 'p',
    'б': 'b',
    'м': 'm',
    'в': 'w',
    'т': 't',
    'д': 'd',
    'с': 's',
    'з': 'z',
    'ц': 'c',
    'н': 'n',
    'ш': 'š',
    'ж': 'ž',
    'ч': 'č',
    'р': 'r',
    'й': 'j',
    'л': 'l',
    'к': 'k',
    'г': 'g',
    'х': 'χ',
    'ъ': 'ʔ',
}

vowels_cyr2lat = {
    "и": "i",
    "е": "e",
    "э": "e",
    "о": "o",
    "а": "a",
    "у": "u",
    "ᴴ": "\u0303",
    "\u0304": ":",
}

full_cyr2lat = digraphs_cyr2lat | consonants_cyr2lat | vowels_cyr2lat

def normalize_text(input_text:str) -> str:
    input_text = unicodedata.normalize('NFD', input_text).lower()
    for key in normalization_dict:
        input_text = input_text.replace(key, normalization_dict[key])
    return input_text

def cyr2lat_text(input_text:str) -> str:
    for key in full_cyr2lat:
        input_text = input_text.replace(key, full_cyr2lat[key])
    return input_text

def transcribe_text(input_text:str) -> str:
    text_normalized = normalize_text(input_text)
    text_post_cyr2lat = cyr2lat_text(text_normalized)
    return text_post_cyr2lat

def transcribe_text_from_file(path_to_input:str, path_to_output:str) -> None:
    with open(path_to_input, 'r', encoding='utf8') as fin:
        input_text = fin.read()
    output_text = transcribe_text(input_text)
    with open(path_to_output, 'w', encoding='utf8') as fout:
        fout.write(output_text)

if __name__ == '__main__':
    transcribe_text_from_file(
        path_to_input='input.txt',
        path_to_output='output.txt',
    )
