import re

def prettify(text):
    return text.replace(u'\u00a0', ' ').strip().strip(':').strip()

def parse_html_table(table):
    if table:
        table_list = []
        heading = table.find_all('th')
        for row in table.find_all('tr'):
            row_hash = {}
            for key, value in zip(heading, row.find_all('td')):
                row_hash[prettify(key.text)] = prettify(value.text)
            if row_hash:
                table_list.append(row_hash)
        return table_list
    else:
        return None

def parse_html_textarea(textarea):
    if textarea:
        records = re.split("\d+\)", prettify(textarea.text))
        return filter(None, map(lambda x: x.strip(), records))
    else:
        return None