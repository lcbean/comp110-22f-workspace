"""Dictionary related utility functions."""

__author__ = "730557892"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a CSV of data into a list of rows as a dictionary."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(rows: list[dict[str, str]], column_name: str) -> list[str]:
    """Produce a list of values in a selected column."""
    result: list[str] = []
    i: int = 0
    for row in rows:
        result.append(rows[i][column_name])
        i += 1
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a list of rows into a dictionary of columns."""
    column_dictionary: dict[str, list[str]] = {}
    for row in row_table: 
        for column_name in row:
            column_dictionary[column_name] = column_values(row_table, column_name)
    return column_dictionary


def head(column_table: dict[str, list[str]], number: int) -> dict[str, list[str]]:
    """Produce a table with only the first few rows of data for each column of a given table."""
    first_few: dict[str, list[str]] = {}
    for column in column_table: 
        first_values: list[str] = []
        i: int = 0
        for item in column_table[column]:
            if i < number:
                first_values.append(item)
            i += 1
        first_few[column] = first_values
    return first_few   


def select(columns: dict[str, list[str]], selected: list[str]) -> dict[str, list[str]]:
    """Returns only the selected columns in a table of columns."""
    only_selected: dict[str, list[str]] = {}
    for column in selected:
        only_selected[column] = columns[column]
    return only_selected


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column based tables."""
    combined: dict[str, list[str]] = {}
    for column in table_1:
        combined[column] = table_1[column]
    for column in table_2:
        if column in combined:
            combined[column] += table_2[column]
        else:
            combined[column] = table_2[column]
    return combined


def count(a_list: list[str]) -> dict[str, int]:
    """Produces a dictionary that counts how many of each item is in the list."""
    tally: dict[str, int] = {}
    for item in a_list:
        if item in tally:
            tally[item] += 1
        else:
            tally[item] = 1
    return tally

    