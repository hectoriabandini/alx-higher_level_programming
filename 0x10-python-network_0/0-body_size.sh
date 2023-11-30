#!/bin/bash

# Check if URL is provided as argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send request and display size of response body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
