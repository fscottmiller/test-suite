from behave import *

@given('the ticker symbol "{sym}", the start date "{start}" and the end date "{end}"')
def stepA(context, sym, start, end):
	context.params = [sym,start,end]

### Web ###

@given('we are on google.com')
def step(context):
	
@when('we search for github')
def step(context):

@then('we will see github in the search results')
def step(context):

#### API ###

@given('we need api data')
def step(context):
	# https://jsonplaceholder.typicode.com/users

@when('we query the api')
def step(context):

@then('we will receive a valid response')
def step(context):

