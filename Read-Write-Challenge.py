def read_file(filename):
    """Read the content of the file."""
    with open(filename, 'r') as file:
        return file.readlines()


def write_file(filename, content):
    """Write the modified content to a new file."""
    with open(filename, 'w') as file:
        file.writelines(content)


def modify_content(content):
    """Modify the content (e.g., convert to uppercase)."""
    return [line.upper() for line in content]


def main():
    input_filename = input("Enter the filename to read: ")
    output_filename = "modified_" + input_filename

    try:
        # Read the original file
        original_content = read_file(input_filename)
        # Modify the content
        modified_content = modify_content(original_content)
        # Write the modified content to a new file
        write_file(output_filename, modified_content)

        print(f"Successfully written modified content to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
