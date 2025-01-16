#!/bin/bash
# Script that sends a GET request with a custom header variable and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
