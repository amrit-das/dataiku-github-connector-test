# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
loan_data_scored = dataiku.Dataset("loan_data_scored")
loan_data_scored_df = loan_data_scored.get_dataframe()
## Adding some coments to replicate a change
## Adding some coments from Dataiku

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

post_scoring_analysis_df = loan_data_scored_df # For this sample code, simply copy input to output


# Write recipe outputs
post_scoring_analysis = dataiku.Dataset("post-scoring-analysis")
post_scoring_analysis.write_with_schema(post_scoring_analysis_df)
