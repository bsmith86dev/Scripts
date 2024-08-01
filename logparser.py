def parse_log_file(file_path):
    # Lists to store lines with "failed" and "warnings"
    failed_lines = []
    warning_lines = []

    # Open the file and read it line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Check if the line contains "failed"
            if "failed" in line:
                failed_lines.append(line.strip())

            # Check if the line contains "warnings"
            if "warnings" in line:
                warning_lines.append(line.strip())

    # Print the results
    print("Lines containing 'failed':")
    for failed_line in failed_lines:
        print(failed_line)

    print("\nLines containing 'warnings':")
    for warning_line in warning_lines:
        print(warning_line)


# Example usage: Replace 'your_log_file.txt' with your actual log file path
parse_log_file('your_log_file.txt')
