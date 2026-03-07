import unicodedata

normalization_dict = {
    '': 'ᴴ',
    '': 'ᴴ',
    '': 'а\u0304',
    '': 'о\u0304',
    '': 'е\u0304',
    unicodedata.normalize('NFD', 'й'): 'й',
    '\u0304ь': 'ь\u0304',
    'a': 'а',
    'o': 'о',
    "e": "е",
    "y": "у"
}

confusables_I = "i𝛊𝖫۱𝓁ⵏ𝘭𝐥ꓡℐ𝙻ℹ𝜄𝗹𝓛ӏⅠ𐌠𝙡Ⲓ𝕃𝙇𞸀ıᎥ𝐢𝘐￨𝑖𝗟𝑳𖼨Ꙇ𐊊Ɩ𝒊𝞲ן𝚕ߊ𝕴і𝗜ͅ𝛪𝐼Ι𝘓ⅈ١𝗅ｉ𝗶ꭵ𝜤𝙸𝓲𐌉ⅼ𝕷ⅰＬ𝝞˛𐔦𝞘ℒɩ𝟷𝑰𝈪𐐛ǀ𑢲ᒪℓⳐ𖼖𝟭Ӏ𝖑𝘪𝝸𑢣𝚤𝚰𝔏Ꮮ𝚒𝙄𝒾׀𞺀ｌ𝔩Іɪꙇاﺎ𝜾𞣇Ɪ𝖨⏽𑣃𝖎𝟙∣𝕝𝐈𝔦ו⍳🯱ᛁﺍ𝕚𝙞𝐋𝐿𝒍ͺ𝓘𝑙ℑ𝟣ꓲⲓ𝕀𝗂|Ｉ𝓵Ⅼι"
for confusable in confusables_I:
    normalization_dict[confusable] = 'i'

dygraphs_cyr2lat = {
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

with open('input.txt', 'r', encoding='utf8') as fin:
    test_string = fin.read()
test_string = unicodedata.normalize('NFD', test_string)
test_string = test_string.lower()
for key in normalization_dict:
    test_string = test_string.replace(key, normalization_dict[key])

for key in dygraphs_cyr2lat:
    test_string = test_string.replace(key, dygraphs_cyr2lat[key])
for key in consonants_cyr2lat:
    test_string = test_string.replace(key, consonants_cyr2lat[key])
for key in vowels_cyr2lat:
    test_string = test_string.replace(key, vowels_cyr2lat[key])

with open('output.txt', 'w', encoding='utf8') as fout:
    fout.write(test_string)
