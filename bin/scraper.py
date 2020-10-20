import requests
import re
from bs4 import BeautifulSoup
import data.db_session as db_session
from data.email import Email
from data.phone import Phone


response = requests.get('https://www.kitchenshop.ro/contactus')
soup = BeautifulSoup(response.text, 'html.parser')
soup = soup.get_text()

filename = 'test.csv'
f = open(filename, 'w')
headers = 'phone, email\n'
f.write(headers)


def main():

    run_session()
    insert_rows()
    f.close()


def run_session():
    db_session.run()


def parse_email():
    emails_list = set(re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", soup))
    return emails_list


def parse_phone():
    phone_list = set(re.findall(
        r"\d{4}.\d{3}.\d{3}", soup))
    return phone_list


def insert_rows():
    session = db_session.create_session()
    email_list = parse_email()
    phone_list = parse_phone()

    for one_phone in phone_list:
        p = Phone()
        p.phone_number = str(one_phone)
        session.add(p)
        f.write(str(one_phone) + ',' + '\n')
    for one_email in email_list:
        email = Email()
        email.email = str(one_email)
        session.add(email)
        f.write(str(one_email) + ',' + '\n')
    session.commit()


if __name__ == '__main__':
    main()
