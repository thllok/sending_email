import pandas as pd
from datetime import date, datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def database_connect():
    url = URL.create(
        'mysql+pymysql',
        username='hide',
        password='hide',
        host='hide',
        port=00000,
        database='hidde')
    engine = create_engine(url)
    with engine.begin() as con:
        df_holiday = pd.read_sql_table('xxxx', con)
        df_country = pd.read_sql_table('xxxx', con)
    return df_holiday, df_country

def generate_holiday_table(df_holiday, df_country):
    #hide
    return signal_hk,signal_tw,table

def read_email_body(file_path,table,sign):
    with open(file_path, 'r') as file:
        body_content = file.read()
    body_content = body_content.replace("{{TABLE_CONTENT}}", table.to_html(index = False))
    body_content = body_content.replace("{{USER_SIGNATURE}}", sign)

    return body_content
def load_email_config(file_path):
    with open(file_path) as file:
        config = json.load(file)
    return config

def email_sending():
    gmail_info = "gmail.json"
    a_email_body_file = "team_a_email_body.html"
    b_email_body_file = "team_b_email_body.html"
    df_holiday, df_country = database_connect()
    signal_hk, signal_tw, table = generate_holiday_table(df_holiday, df_country)

    # content = open(gmail_info)
    config = load_email_config(gmail_info)
    sender = config["username"]
    password = config["password"]
    sign = config["signature"]
    receiver_TeamA = config["receiver_team_A"]
    receiver_TeamB = config["receiver_team_B"]
    CC_TeamA = config["CC_TeamA"]
    CC_TeamB = config["CC_TeamB"]
    subject = config["subject"]

    a_body = read_email_body(a_email_body_file,table,sign)
    b_body = read_email_body(b_email_body_file,table,sign)
    # Replace specific placeholders in the email body with dynamic content

    print(f"signal_hk:{signal_hk}\nsignal_tw:{signal_tw}")
    if signal_hk == 1 or signal_tw == 1:
        send_email(sender, password, receiver_TeamA, CC_TeamA, subject, a_body)
        send_email(sender, password, receiver_TeamB, CC_TeamB, subject, b_body)



def send_email(sender, password, receiver, cc, subject, body):
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = ", ".join(receiver)
    message["CC"] = ", ".join(cc)
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    text=message.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()


if __name__ == "__main__":

    email_sending()
