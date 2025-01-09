## FileCreator Class

The `file_creator` class is a utility tool designed to simplify the process of creating multiple files with different extensions in a specified directory.

### Features
- Creates multiple files with specified extensions in one operation
- Automatically creates the target directory if it doesn't exist
- Validates input parameters to ensure correct file creation
- Supports various file extensions (txt, py, md, etc.)

### Usage Example

```python

# Initialize the file creator
fc = file_creator()

#Define your parameters
folder = "test_files"
files = ["document1", "script1", "readme"]
extensions = ["txt", "py", "md"]

# Create files

result = fc.create_files(folder, files, extensions)
print(result) # Output: "Created 3 files in folder 'test_files'"
```


### Parameters
- `folder`: Target directory path where files will be created
- `files`: List of file names without extensions
- `files`: List of extensions for each file (must match the length of files list)

### Error Handling
- Validates that the number of files matches the number of extensions
- Checks for None values in required parameters
- Creates the target directory if it doesn't exist
