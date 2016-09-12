from behave import *

use_step_matcher("re")


@then("I want to print it")
def step_impl(context):
    print('')
    print(context.base_url)
    print('')
