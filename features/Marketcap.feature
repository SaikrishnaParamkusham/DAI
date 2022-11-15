Feature: MarketCap validation
  Scenario: Marketcap data validation
    Given an input data frame:
      | object | object |
      | Id | Marketcap |
      | 1  | 10000000  |
      | 2  | 10000010  |
      | 3  | 10000     |
      | 4  | 10        |
      | 5  | 1000      |
      | 6  | 23948     |
    When converted to a data frame using row as column names
    Then the filtered dataframes is:
      | object | object |
      |Id | Marketcap |
      | 1 | 10000000  |
      | 2 | 10000010  |