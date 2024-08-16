import os
from lxml import etree

def combine_svgs_to_xml(input_dir, output_file):
    # Create the root element for the combined XML
    root = etree.Element('combined_svgs')

    # Iterate over all SVG files in the directory
    for svg_filename in os.listdir(input_dir):
        if svg_filename.endswith('.svg'):
            svg_path = os.path.join(input_dir, svg_filename)

            # Read the SVG file content as bytes
            with open(svg_path, 'rb') as file:
                svg_content = file.read()
                svg_root = etree.fromstring(svg_content)

                # Append the SVG content to the combined XML root
                root.append(svg_root)

    # Write the combined XML to the output file
    tree = etree.ElementTree(root)
    tree.write(output_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')

    print(f"Combined SVG files from {input_dir} into {output_file}")

# Paths
input_directory = 'D:\sakana-ai\sakana-ai-2\kanjivg\kanji'
output_xml_file = 'D:\\sakana-ai\\sakana-ai-2\\kanjivg.xml'

# Combine SVG files
combine_svgs_to_xml(input_directory, output_xml_file)
