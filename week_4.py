def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()

        
        modified_content = content.upper()

        
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Content successfully written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
input_filename = 'input.txt'
output_filename = 'output.txt'
read_and_modify_file(input_filename, output_filename)
