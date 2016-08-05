from __future__ import unicode_literals
from behave import *
import nose
import requests
from nose.tools import assert_equal

use_step_matcher("parse")


@step('I set base URL to "{base_url}"')
def set_base_url(context, base_url):
    if base_url.startswith("context"):
        context.base_url = getattr(context, base_url[8:])
    else:
        context.base_url = base_url.encode('ascii')


@step('I set "{header_name}" header to "{header_value}"')
def store_header(context, header_name, header_value):
    if header_value.startswith("context"):
        context.headers[header_name.encode('ascii')] = getattr(context, header_value[8:])
    else:
        context.headers[header_name.encode('ascii')] = header_value.encode('ascii')


@step('I clear "{header_name}" header')
def remove_header(context, header_name):
    context.headers.pop(header_name, None)


@step('I clear all headers')
def remove_all_headers(context):
    context.headers.clear()


@step('I want to reuse "{parameter_name}" parameter')
def store_parameter(context, parameter_name):
    data = context.r.json()

    return setattr(context, parameter_name, data[parameter_name])


@step('I make a {request_verb} request to "{url_path_segment}"')
def get_request(context, request_verb, url_path_segment):
    url = context.base_url + '/' + url_path_segment

    context.r = getattr(requests, request_verb.lower())(url, headers=context.headers)

    log_full(context.r)

    return context.r


@step('I make a {request_verb} request to "{url_path_segment}" with parameters')
def request_with_parameters(context, request_verb, url_path_segment):
    url = context.base_url + '/' + url_path_segment

    params = {}

    for row in context.table:
        for x in context.table.headings:
            params[x] = row[x]
            if row[x].startswith("context"):
                params[x] = eval(row[x])

    context.r = getattr(requests, request_verb.lower())(url, params, headers=context.headers)

    log_full(context.r)

    return context.r


@step('the response status code should equal {expected_http_status_code}')
def status_code_validation(context, expected_http_status_code):
    nose.tools.assert_equal(context.r.status_code, int(expected_http_status_code))


@step('the response status code should be among {expected_http_status_codes}')
def status_code_array_validation(context, expected_http_status_codes):
    expected_codes_list = [int(x) for x in expected_http_status_codes.split(',')]
    nose.tools.assert_in(context.r.status_code, expected_codes_list)


@step('the response status message should equal "{expected_http_status_message}"')
def status_message_validation(context, expected_http_status_message):
    nose.tools.assert_equal(context.r.reason, str(expected_http_status_message))


@step('the response parameter "{parameter_name}" should equal "{expected_parameter_value}"')
def parameter_validation(context, parameter_name, expected_parameter_value):
    data = context.r.json()

    nose.tools.assert_equal(data[parameter_name], str(expected_parameter_value))


@step('the response header "{header_name}" should equal "{expected_header_value}"')
def parameter_validation(context, header_name, expected_header_value):
    nose.tools.assert_equal(context.r.headers[header_name], str(expected_header_value))


@step('the response structure should equal "{expected_response_structure}"')
def response_structure_validation(context, expected_response_structure):
    data = context.r.json()
    try:
        response_valid = getattr(context.json_responses, expected_response_structure)

        assert response_valid.check(data)
    except NameError:
        print("")
        print("File with responses not found")
        print("")


def log_full(r):
    req = r.request
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """

    print("")
    print("")

    print('{}\n{}\n{}\n\n{}'.format(
        '-----------REQUEST-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

    print("")

    print('{}\n{}\n{}\n\n{}'.format(
        '-----------RESPONSE-----------',
        str(r.status_code) + ' ' + r.reason,
        '\n'.join('{}: {}'.format(k, v) for k, v in r.headers.items()),
        r.text,
    ))
    print("")

    print('Operation took ' + str(round(r.elapsed.total_seconds(), 3)) + 's')

    print("")
    print("")
    print("")
    print("")
