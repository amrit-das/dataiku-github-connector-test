# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
loan_data = dataiku.Dataset("loan_data")
loan_data_df = loan_data.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

code_recipe_output_df = loan_data_df # For this sample code, simply copy input to output


# Write recipe outputs
code_recipe_output = dataiku.Dataset("code-recipe-output")
code_recipe_output.write_with_schema(code_recipe_output_df)
