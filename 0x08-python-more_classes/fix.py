import re

def fix_blank_lines(content):
    """Fix too many blank lines (E303)."""
    # Remove any sequence of more than 2 consecutive blank lines
    return re.sub(r'\n{3,}', '\n\n', content)

def fix_mixed_indentation(content):
    """Fix mixed spaces and tabs (E101, W191)."""
    # Replace tabs with 4 spaces
    return content.replace('\t', '    ')

def fix_blank_line_end(content):
    """Fix blank line at the end of the file (W391)."""
    # Remove blank lines at the end of the file
    return content.rstrip() + '\n'

def fix_file(file_path):
    """Apply all fixes to the given file."""
    with open(file_path, 'r') as file:
        content = file.read()

    # Apply each fix
    content = fix_blank_lines(content)
    content = fix_mixed_indentation(content)
    content = fix_blank_line_end(content)

    # Write the fixed content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    file_path = "4-rectangle.py"  # Replace with the correct file path
    fix_file(file_path)
    print(f"Fixed issues in {file_path}")

