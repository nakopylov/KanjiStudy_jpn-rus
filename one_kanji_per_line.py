def convert_to_one_kanji_per_line(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            kanji_lines = input_file.readlines()

            # Flatten the list of lines and remove leading/trailing whitespaces
            kanji_list = [kanji.strip() for line in kanji_lines for kanji in line]

        # Filter out blank lines
        kanji_list = [kanji for kanji in kanji_list if kanji]

        # Add a space after each kanji and join with newline
        kanji_with_space = '\n'.join([f"{kanji} " for kanji in kanji_list])

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Write one kanji per line followed by a space to the output file
            output_file.write(kanji_with_space)

        print(f"Conversion successful. Output saved to {output_file_path}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_file_path = 'input.txt'  # Replace with the path to your input file
output_file_path = 'output.txt'  # Replace with the desired output file path

convert_to_one_kanji_per_line(input_file_path, output_file_path)
