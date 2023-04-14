# Create_README

This tiny repo. contains a script to automatically create the `README.md` file with a template.

## Explanations

Put the python script `output-structure-for-readme.py` in a folder `.../.../folder_name`. When executing it, it will automatically creates `README.md` OR appends to `README.md` (if it already exists) with the following structure. 

```
# <NAME OF FOLDER>

This folder contains TODO

## Structure

### Folders
- <folder_0> : TODO
- <folder_1> : TODO
...

### Files
- <file_0> : TODO
- <file_1> : TODO
...

```

## How to use it ?

Put the `output-structure-for-readme.py` script in a folder and execute it.

## TODO

I'm thinking about using GPT-like solutions to automatically add a small description attached to each folders and files (i.e. replace the TODO with AI-generated text)

## Example

If you execute `output-structure-for-readme.py` in this repo you append the follwoing raw data to this file:

# Create_README

This folder contains TODO

## Structure

### Folders
- `empty_folder_0` : TODO

- `.git` : TODO

### Files
- `empty_file_0` : TODO

- `README.md` : TODO

