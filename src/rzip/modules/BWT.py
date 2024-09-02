class BWT:
    def __init__(self, text):
        self.text = text

    def transform(self):
        # Generate the table of cyclically shifted strings
        table = [self.text[i:] + self.text[:i] for i in range(len(self.text))]
        # Sort the table lexicographically
        table_sorted = sorted(table)
        # Extract the last column of the sorted table
        last_column = [row[-1] for row in table_sorted]
        # Find the index of the original string in the sorted table
        original_index = table_sorted.index(self.text)
        return ''.join(last_column), original_index

    def inverse_transform(self, bwt, original_index):
        n = len(bwt)
        # Initialize the table with empty strings
        table = [''] * n
        for _ in range(n):
            # Prepend the BWT to each string in the table
            table = sorted([bwt[i] + table[i] for i in range(n)])
        # Retrieve the row that corresponds to the original string index
        original_row = table[original_index]
        return original_row
