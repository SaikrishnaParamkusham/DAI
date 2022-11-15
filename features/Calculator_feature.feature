Feature: Calculating two numbers

  Scenario Outline: Add a and b
    Given values are <b>
    When we add a and b
    Then the result is <sum>

    Examples: Add
    | b  | sum |
    | 7  | 12  |
    | 8  | 13  |
    | 9  | 14  |
    | 10 | 15  |
    | 11 | 16  |