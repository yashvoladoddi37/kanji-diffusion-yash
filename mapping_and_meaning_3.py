import re
import xml.etree.ElementTree as ET
import os

svg_dir = 'D:\\sakana-ai\\sakana-ai-2\\kanji-svg-path'
png_dir = 'D:\\sakana-ai\\sakana-ai-2\\kanji-png-path'
jpg_dir = 'D:\\sakana-ai\\sakana-ai-2\\kanji-jpg-path'

#Mapping the kanji filename to the kanji literal using kanjivg.xml

kvg_element_pattern = re.compile(r'kvg:element="([^"]+)"')
lit2name = {}
is_above_kanji = False

with open('kanjivg.xml', 'r', encoding='utf-8') as kanjivg:
    for line in kanjivg:
        if '<g ' in line:
            is_above_kanji = True
        if is_above_kanji:
            kanji_id = re.search(r'id="([^"]+)"', line)
            lit = kvg_element_pattern.search(line)
            if lit:
                lit2name[lit.group(1)] = kanji_id.group(1).replace('kvg:', '')
                is_above_kanji = False   

#Mapping the kanji filename to the English kanji meaning using kanjidic2.xml and write them in your json file

root = ET.parse('kanjidic2.xml').getroot()

metadata_file_path = os.path.join('D:\sakana-ai\sakana-ai-2', 'kanji_metadata.json')

with open(metadata_file_path, 'w') as metadata:
    for character in root.findall("character"):
        lit = character.find("literal").text
        meanings = []
        for meaning in character.findall(".//reading_meaning/rmgroup/meaning"):
            # Only English meanings, remove for all languages
            if 'r_type' not in meaning.attrib and 'm_lang' not in meaning.attrib:
                meanings.append(meaning.text)
        concat_meanings = ", ".join(meanings)
        if lit in lit2name:
            metadata.write(f'{{"file_name": "{lit2name[lit]}.jpg", "text": "a Kanji meaning {concat_meanings}"}}\n')
                
