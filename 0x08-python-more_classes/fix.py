import re
import sys

def fix_blank_lines(content):
    """Fix too many blank lines (E303)."""
    return re.sub(r'\n{3,}', '\n\n', content)

def fix_mixed_indentation(content):
    """Fix mixed spaces and tabs (E101, W191)."""
    return content.replace('\t', '    ')

def fix_blank_line_end(content):
    """Fix blank line at the end of the file (W391)."""
    return content.rstrip() + '\n'

def fix_long_lines(content, max_length=79):
    """Fix lines that are too long (E501)."""
    lines = content.splitlines()
    fixed_lines = []

    for line in lines:
        while len(line) > max_length:
            # Find the last space within the limit to split
            split_index = line.rfind(' ', 0, max_length)
            if split_index == -1:  # No space found, split at max_length
                split_index = max_length

            # Append the split line
            fixed_lines.append(line[:split_index])
            # Update line to the remainder
            line = line[split_index:].lstrip()  # Remove leading spaces for the next line
        
        fixed_lines.append(line)  # Append the remaining part of the line

    return '\n'.join(fixed_lines)

def fix_file(file_path):
    """Apply all fixes to the given file."""
    with open(file_path, 'r') as file:
        content = file.read()

    # Apply each fix
    content = fix_blank_lines(content)
    content = fix_mixed_indentation(content)
    content = fix_long_lines(content)  # Add long line fix
    content = fix_blank_line_end(content)

    # Write the fixed content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python fix.py <file.py>")
        sys.exit(1)

    file_path = sys.argv[1]  # Get the file name from command line arguments
    
    # Apply the fix to the given file
    try:
        fix_file(file_path)
        print(f"Fixed issues in {file_path}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please check the file name and try again.")
