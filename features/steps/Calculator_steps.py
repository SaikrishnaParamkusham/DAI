from behave import *
from Calculation import Calculationclass
from steps import *

@given('values are {b}')
def step_impl(context, b):
    context.Calculationclass = Calculationclass()

@when('we add a and b')
def step_impl(context, b):
    context.Calculationclass_sum = context.Calculationclass.add_method(b)


@then('the result is {sum}')
def step_impl(context, sum):
    assert (context.Calculationclass_sum == sum)