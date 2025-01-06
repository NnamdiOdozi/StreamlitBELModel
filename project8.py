import pandas as pd
import copy  # Import the copy module for deep copying

class CashFlowModel:
    def __init__(self):
        self.data = {}  # Holds the current state of the data
        self.original_data = {}  # Holds the original unmodified data

    def add_entry(self, year, interest_rate, cash_flow):
        self.data[year] = {"interest_rate": interest_rate, "cash_flow": cash_flow}

    def load_data_from_excel(self, filename):
        df = pd.read_excel(filename)
        for index, row in df.iterrows():
            year = row[df.columns[0]]
            interest_rate = row[df.columns[1]]
            cash_flow = row[df.columns[2]]
            self.add_entry(year, interest_rate, cash_flow)
        # Save a deep copy of the original data
        self.original_data = copy.deepcopy(self.data)

    def reset_data(self):
         # Reset the current data to the original unmodified state using a deep copy
        self.data = copy.deepcopy(self.original_data)
        
    def calculate_present_value(self):
        present_value = 0
        for year, entry in self.data.items():
            interest_rate = entry["interest_rate"]
            cash_flow = entry["cash_flow"]
            present_value += cash_flow / ((1 + interest_rate) ** year)
        return present_value

    
    def sensitivity_test(self, interest_rate_factor, cash_flow_factor):
       

        # Apply sensitivity adjustments
        for entry in self.data.values():
            entry["interest_rate"] *= interest_rate_factor
            entry["cash_flow"] *= cash_flow_factor

        # Calculate the present value after applying sensitivity adjustments
        present_value = self.calculate_present_value()
         # Reset data to its original state 
        self.reset_data()
        return present_value

    


