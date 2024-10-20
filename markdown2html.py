#!/usr/bin/python3
"""
Python script that converts a Markdown file to HTML.
Parses headings, unordered list, and ordered list syntax.
"""

import sys
import os
import re


def parse_heading(line):
    """
    Parse Markdown heading syntax and generate HTML tag.
    """
    match = re.match(r'^(#+)\s(.*)$', line)
    if match:
        level = len(match.group(1))
        content = match.group(2)
        return f'<h{level}>{content}</h{level}>\n'
    return line


def parse_unordered_list(line):
    """
    Parse Markdown unordered list syntax and generate HTML tag.
    """
    match = re.match(r'^-\s(.*)$', line)
    if match:
        item = match.group(1)
        return f'<li>{item}</li>\n'
    return line


def parse_ordered_list(line):
    """
    Parse Markdown ordered list syntax and generate HTML tag.
    """
    match = re.match(r'^\*\s(.*)$', line)
    if match:
        item = match.group(1)
        return f'<li>{item}</li>\n'
    return line


if __name__ == '__main__':
    # Check if correct number of arguments provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>",
              file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read Markdown content and parse headings
    # unordered lists, and ordered lists
    with open(markdown_file, 'r') as md_file:
        md_content = md_file.readlines()

    html_content = []
    for line in md_content:
        html_line = parse_heading(line)
        html_line = parse_unordered_list(html_line)
        html_line = parse_ordered_list(html_line)
        html_content.append(html_line)

    # Write HTML content to output file
    with open(html_file, 'w') as html_output:
        html_output.writelines(html_content)
