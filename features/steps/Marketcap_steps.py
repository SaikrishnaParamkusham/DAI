from behave import *
from MarketcapModule import MarketCapEligibility
from steps import *
from behave_pandas import table_to_dataframe, dataframe_to_table

@given ("an input data frame")
def step_impl(context):
    context.MarketcapEligibility_table = context.table

@when('converted to a data frame using row as column names')
def step_impl(context):
    context.main_table = table_to_dataframe(context.MarketcapEligibility_table,
                                            column_levels = 0,index_levels=0)
    context.main_table.columns=context.main_table.iloc[0]
    context.main_table = context.main_table[1:]
    context.MarketcapEligibility_filter = MarketCapEligibility(context.main_table).filter_marketcap("Marketcap",2345612)

@then("the filtered dataframes is")
def step_impl(context):
    context.test_table = table_to_dataframe(context.table,column_levels=0, index_levels=0)
    context.test_table.columns = context.test_table.iloc[0]
    context.test_table = context.test_table[1:]
    assert context.MarketcapEligibility_filter[0].equals(context.test_table)

