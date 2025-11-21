import os
import sys

def find_and_replace(root_dir, old_text, new_text):
    """
    Recursively searches and replaces a string in all files within a directory.
    """
    
    print(f"Starting search and replace in the current directory: {os.path.abspath(root_dir)}\n")
    count = 0

    # os.walk generates the file names in a directory tree
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude the .git directory and the script's folder from directory traversal
        if '.git' in dirnames:
            dirnames.remove('.git')

        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            
            # Skip the script file itself
            if filepath == os.path.abspath(__file__):
                continue
            
            # Attempt to read the file as text using UTF-8 encoding
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Check if the old text exists in the file content
                if old_text in content:
                    new_content = content.replace(old_text, new_text)
                    
                    # Write the modified content back to the file
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    
                    print(f"✅ SUCCESS: Replaced '{old_text}' in: {filepath}")
                    count += 1
                # else: pass # No need to print for every file that doesn't match
            
            except UnicodeDecodeError:
                # Skips files that are likely binary (images, fonts, compressed files, etc.)
                print(f"🚫 SKIPPED: Binary or non-UTF-8 file skipped: {filepath}")
            except Exception as e:
                # Catch all other potential file errors
                print(f"❌ ERROR: Could not process {filepath}. Reason: {e}")

    print(f"\n--- Replacement Complete! ---")
    print(f"Successfully performed replacement in {count} files.")


if __name__ == "__main__":
    
    # Set the root directory to the current working directory automatically
    root_directory = os.getcwd() 
    
    # --- User Input Section ---
    print("This script will find and replace text in all files and subfolders of the current location.")
    
    # Use the example names provided in your request as defaults
    default_old = "abd3d.design"
    default_new = "https://abd-3d.github.io"
    
    # Get the strings for replacement
    old_string = input(f"Enter the text to be replaced (default: {default_old}): ").strip()
    new_string = input(f"Enter the new replacement text (default: {default_new}): ").strip()

    # Use defaults if the user hits Enter without typing
    if not old_string:
        old_string = default_old
    if not new_string:
        new_string = default_new
        
    # Safety Check
    if not old_string or not new_string:
        print("\nReplacement strings cannot be empty. Please restart the script.")
        sys.exit()

    print(f"\n*** ACTION SUMMARY ***")
    print(f"Target Directory: {root_directory}")
    print(f"Replacing: '{old_string}'")
    print(f"With:      '{new_string}'")
    print("************************\n")
    
    # Confirmation before proceeding
    confirmation = input("Type 'YES' to proceed with the changes: ").strip()
    
    if confirmation == "YES":
        find_and_replace(root_directory, old_string, new_string)
    else:
        print("Operation cancelled by user.")