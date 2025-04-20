# cleanup_text.py

def clean_text(input_file, output_file):
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into paragraphs based on double newlines
    paragraphs = text.split('\n\n')

    # Process each paragraph to remove all line breaks within it
    cleaned_paragraphs = []
    for paragraph in paragraphs:
        # Replace all single newlines with a space
        cleaned_paragraph = paragraph.replace('\n', ' ')
        # Strip leading/trailing whitespace and collapse multiple spaces into one
        cleaned_paragraph = ' '.join(cleaned_paragraph.split())
        cleaned_paragraphs.append(cleaned_paragraph)

    # Join the cleaned paragraphs with double newlines
    cleaned_text = '\n\n'.join(cleaned_paragraphs)

    # Write the cleaned text to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

    print(f"Text cleaned and saved to {output_file}")

# Example usage
input_file = '/Users/jeb/wordpile/03 Workbench/StarCorps/rangen/textdb-master.txt'
output_file = 'textdb-master-cleaned.txt'  # Replace with your desired output file name
clean_text(input_file, output_file)