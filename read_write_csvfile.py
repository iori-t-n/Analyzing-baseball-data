"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.
"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    
    This function assumes that the first row of the CSV file contains the field names. 
    """
    with open(filename, 'r', newline= '') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter= separator, quotechar= quote)
        fieldname = csvreader.fieldnames
    return fieldname

# Simple test
# print(read_csv_fieldnames("table3.csv", ",", "'"))

def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    list = []
    with open(filename, 'r', newline= '') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter= separator, quotechar= quote)
        for item in csvreader:
            list.append(item)
    return list

# Simple test
# print(read_csv_as_list_dict("table3.csv", ",", "'"))

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    nested_dict = {}
    with open(filename, 'r', newline= '') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter= separator, quotechar= quote)
        for row in csvreader:
            outer_key = row[keyfield]
            nested_dict[outer_key] = {key: value for key, value in row.items()}
    return nested_dict

# Simple test
# print(read_csv_as_nested_dict("table1.csv", "Field1", ",", "'"))


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=separator, quotechar=quote, quoting=csv.QUOTE_NONNUMERIC)
        csvwriter.writeheader()
        for row in table:
            csvwriter.writerow(row)

# Simple test
# table =  [{'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14}, {'a': 20, 'b': 21, 'c': 22, 'd': 23, 'e': 24}, {'a': 30, 'b': 31, 'c': 32, 'd': 33, 'e': 34}, {'a': 40, 'b': 41, 'c': 42, 'd': 43, 'e': 44}]
# fieldnames = ['a', 'b', 'c', 'd', 'e']
# print(write_csv_from_list_dict("output1.csv", table, fieldnames, ",", '"'))
