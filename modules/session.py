#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import report
from conf import utils

rpt = report.htmltags()

def analysis(http_objs):
    requests = http_objs["total_requests"]
    response_headers = http_objs["response_headers"]
    request_URLs = http_objs["request_URL"]
    
    headers = {"Set-Cookie":"Cookie write",
    "Set-Cookie2":"Cookie write"}
    
    set_cookie_rows = []

    sessions_id_rows = []
    sessions_id = []
    
    sessions_pattern = utils.parser_xml("conf/statements/session_patterns.xml", "item", "")

    for i in xrange(0, requests):
        protocol = request_URLs[i]["protocol"]
        url = request_URLs[i]["url"]
        path = request_URLs[i]["path"]
        params = request_URLs[i]["params"]
        query = request_URLs[i]["query"]

        full_path = protocol + "://" + url + path
                
        for header in response_headers[i].iterkeys():
            if header in headers.iterkeys():            
                set_cookie_rows.append("<td>" + rpt.href(full_path) + "</td><td>" + str(response_headers[i][header]) + "</td>")
                        
        for item in sessions_pattern:
            if item in query:
                set_cookie_rows.append("<td>" + rpt.href(full_path) + "</td><td>" + query + "</td>")

    collums = {"Cookies":["Path", "Set-Cookie"], "SessionIDUrl":["Path", "Query"]}
    rows = {"Cookies":set_cookie_rows, "SessionIDUrl":sessions_id_rows}
    
    tip = "Tip: <a href='https://www.owasp.org/index.php/Session_Management_Cheat_Sheet' target='_blank'>Session Management Cheat Sheet</a> and <a href='https://www.owasp.org/index.php/Testing_for_Session_Management' target='_blank'>Testing for Session Management</a>"

    rpt.make_table("session", tip, collums, rows)


