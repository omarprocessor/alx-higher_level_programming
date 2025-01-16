#!/bin/bash
# Send a request to the URL passed as an argument
# -o /dev/null: Discards the body of the response
# -s: Silent mode, to suppress progress and error messages
# -w "%{http_code}": Outputs only the HTTP status code of the response
curl -o /dev/null -s -w "%{http_code}" "$1"

