import utility


def parse_case_details(soup):
    case_details_table = soup.find_all("span", class_="case_details_table")
    if case_details_table:
        case_details = {}
        for row in case_details_table:
            all_text = row.find_all(text=True)
            for i in range(0, len(all_text), 2):
                case_details[utility.prettify(all_text[i])] = utility.prettify(all_text[i+1]) 
        return case_details
    else:
        return None

def parse_case_status(soup):
    case_status = soup.find(text="Case Status").parent.find_next_sibling("div").find_all("strong")
    if case_status:
        case_status = {}
        for i in range(0, len(case_status), 2):
            case_status[utility.prettify(case_status[i].text)] = utility.prettify(case_status[i+1].text)
        return case_status
    else:
        return None

def parse_petitoner_and_advocate(soup):
    petitoner_and_advocate = soup.find("span", class_="Petitioner_Advocate_table")
    return utility.parse_html_textarea(petitoner_and_advocate)

def parse_respondent_and_advocate(soup):
    respondent_and_advocate = soup.find("span", class_="Respondent_Advocate_table")
    return utility.parse_html_textarea(respondent_and_advocate)


def parse_acts_table(soup):
    acts_table = soup.find("table", id="act_table")
    return utility.parse_html_table(acts_table)


def parse_history_table(soup):
    history_table = soup.find("table", class_="history_table")
    return utility.parse_html_table(history_table)

def parse_orders_table(soup):
    table_list = []
    order_table = soup.find_all("table", class_="order_table")
    if order_table:
        heading = order_table[0].find_all("td")
        for table in order_table[1:]:
            cols = table.find_all("td")
            row_hash = {}
            for key, value in zip(heading, cols):
                row_hash[utility.prettify(key.text)] = utility.prettify(value.text)
            if row_hash:
                table_list.append(row_hash)
        return table_list
    else:
        return None
