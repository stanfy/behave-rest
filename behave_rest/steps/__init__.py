from __future__ import unicode_literals

from behave import *
import nose
import requests
from nose.tools import assert_equal
import jpath
import json

use_step_matcher("parse")


@step('I set base URL to "{base_url}"')
def set_base_url(context, base_url):
    if base_url.startswith("context"):
        context.base_url = getattr(context, base_url[8:])
    else:
        context.base_url = base_url.encode('ascii')


@step('I add path "{path}" to base URL')
def add_path_to_url(context, path):
    context.base_url += "/" + path


@step('I do not want to verify SSL certs')
def do_not_verify_ssl_certs(context):
    context.verify_ssl = False


@step('I want to verify SSL certs')
def verify_ssl_certs(context):
    context.verify_ssl = True


@step('I set "{header_name}" header to "{header_value}"')
def set_header(context, header_name, header_value):
    if header_value.startswith("context"):
        context.headers[header_name.encode('ascii')] = getattr(context, header_value[8:]).encode('ascii')
    else:
        context.headers[header_name.encode('ascii')] = header_value.encode('ascii')


@step('I set Authorization header to "{header_value}"')
def set_auth_header(context, header_value):
    # This will set standard "Authorization" to provided value adding "Bearer " word
    header_name = "Authorization"
    if header_value.startswith("context"):
        header_value = "Bearer " + getattr(context, header_value[8:])
        context.headers[header_name.encode('ascii')] = header_value.encode('ascii')
    else:
        header_value = "Bearer " + header_value
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


@step('I want to reuse parameter "{parameter_name}" at path "{json_path}"')
def store_parameter_with_path(context, parameter_name, json_path):
    data = context.r.json()
    parameter_value = jpath.get(json_path, data)

    print('')
    print(parameter_value)
    print('')

    setattr(context, parameter_name, parameter_value)

    print('')
    print(getattr(context, parameter_name))
    print('')


@step('I want to reuse "{header_name}" header')
def store_header(context, header_name):
    data = context.r.headers

    return setattr(context, header_name, data[header_name])


@step('I make a {request_verb} request to "{url_path_segment}"')
def get_request(context, request_verb, url_path_segment):
    if not hasattr(context, 'verify_ssl'):
        context.verify_ssl = True

    url = context.base_url + '/' + url_path_segment

    context.r = getattr(requests, request_verb.lower())(url, headers=context.headers, verify=context.verify_ssl)

    log_full(context.r)

    return context.r


@given('I make an untrusted {request_verb} request to "{url_path_segment}"')
def untrusted_request(context, request_verb, url_path_segment):
    url = context.base_url + '/' + url_path_segment

    context.r = getattr(requests, request_verb.lower())(url, headers=context.headers, verify=False)

    log_full(context.r)

    return context.r


@step('I make a {request_verb} request to "{url_path_segment}" with parameters')
def request_with_parameters(context, request_verb, url_path_segment):
    if not hasattr(context, 'verify_ssl'):
        context.verify_ssl = True

    url = context.base_url + '/' + url_path_segment

    params = {}

    for row in context.table:
        for x in context.table.headings:
            params[x] = row[x]
            if row[x].startswith("context"):
                params[x] = eval(row[x])

    context.r = getattr(requests, request_verb.lower())(url, params, headers=context.headers, verify=context.verify_ssl)

    log_full(context.r)

    return context.r


@step('I make an untrusted {request_verb} request to "{url_path_segment}" with parameters')
def request_with_parameters(context, request_verb, url_path_segment):
    url = context.base_url + '/' + url_path_segment

    params = {}

    for row in context.table:
        for x in context.table.headings:
            params[x] = row[x]
            if row[x].startswith("context"):
                params[x] = eval(row[x])

    context.r = getattr(requests, request_verb.lower())(url, params, headers=context.headers, verify=False)

    log_full(context.r)

    return context.r


@step('the response status code should equal {expected_http_status_code}')
def status_code_validation(context, expected_http_status_code):
    nose.tools.assert_equal(context.r.status_code, int(expected_http_status_code))


@step('the response status code should not equal {invalid_http_status_code}')
def status_code_validation(context, invalid_http_status_code):
    nose.tools.assert_not_equal(context.r.status_code, int(invalid_http_status_code))


@step('the response status code should be among {expected_http_status_codes}')
def status_code_array_validation(context, expected_http_status_codes):
    expected_codes_list = [int(x) for x in expected_http_status_codes.split(',')]
    nose.tools.assert_in(context.r.status_code, expected_codes_list)


@step('the response status message should equal "{expected_http_status_message}"')
def status_message_validation(context, expected_http_status_message):
    nose.tools.assert_equal(context.r.reason, str(expected_http_status_message))


@step('the response parameter "{parameter_name}" should equal {expected_parameter_value}')
def parameter_validation(context, parameter_name, expected_parameter_value):
    data = context.r.json()

    if expected_parameter_value.startswith("context"):
        expected_parameter_value = getattr(context, expected_parameter_value[8:])
        nose.tools.assert_equal(data[parameter_name], expected_parameter_value)
    else:
        converted_value = json.loads(expected_parameter_value)
        nose.tools.assert_equal(data[parameter_name], converted_value)


@step('JSON at path "{json_path}" should equal {expected_json_value}')
def json_object_validation(context, json_path, expected_json_value):
    data = context.r.json()
    actual_json_value = jpath.get(json_path, data)

    if expected_json_value.startswith("context"):
        expected_json_value = getattr(context, expected_json_value[8:])
        nose.tools.assert_equal(actual_json_value, expected_json_value)

    else:
        converted_value = json.loads(expected_json_value)
        nose.tools.assert_equal(actual_json_value, converted_value)


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

