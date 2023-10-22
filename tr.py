from googletrans import Translator
import os

def hindi_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='hi', dest='en')
    return translation.text

def convert_filename(input_filename):
    # Extract the file extension
    root, ext = os.path.splitext(input_filename)

    # Extract the file name without extension
    file_name = os.path.basename(root)

    # Translate the Hindi text to English
    english_name = hindi_to_english(file_name)

    # Combine the English name with the original extension
    output_filename = f"{english_name}{ext}"

    return output_filename

if __name__ == "__main__":
    # Replace this with your Hindi file name
    hindi_filename = "आएगा आएगा आएगा लीले चढ़ सांवरा आएगा Kanhaiya Mittal ji - Agra Latest kirtan 2022- 4K UHD"

    # Convert the Hindi file name to English-like text
    english_filename = convert_filename(hindi_filename)

    print("Original Hindi File Name:", hindi_filename)
    print("Converted English-like File Name:", english_filename)
