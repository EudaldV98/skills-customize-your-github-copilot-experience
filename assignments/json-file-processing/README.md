# JSON File Processing

## 🎯 Objective

Learn how to read, process, and write JSON data in Python using file I/O. Students will build a program that loads structured data from a file, updates it, and saves changes back to disk.

## 📝 Tasks

### 🛠️ Read JSON data from a file

#### Description
Write a function that loads JSON data from a file and returns it as Python objects.

#### Requirements
Completed program should:

- Open and read a JSON file using Python file I/O
- Parse the JSON content using the `json` module
- Return the parsed data as Python dictionaries or lists
- Handle the case where the file does not exist with a clear error message

### 🛠️ Process and update data

#### Description
Write code to update the loaded data, such as adding a new record, updating a field, or filtering items.

#### Requirements
Completed program should:

- Modify the loaded JSON data in memory
- Add or update at least one item in the data set
- Use dictionary and list operations to transform the data
- Print a summary of the changes made

### 🛠️ Save updated data back to JSON

#### Description
Write a function that saves the updated Python data back to a JSON file.

#### Requirements
Completed program should:

- Write JSON data back to a file with proper formatting
- Preserve the data structure when saving
- Confirm successful save with a printed message
- Example usage:
  ```python
  save_data("data.json", updated_data)
  print("Data saved successfully")
  ```
