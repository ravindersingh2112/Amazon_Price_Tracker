import requests
from bs4 import BeautifulSoup as bs
import smtplib
import ssl
from email.message import EmailMessage

URL = 'https://www.amazon.in/dp/B0BR4176V7/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-6&pf_rd_r=R90JFKGZ8QDAGYD71T0V&pf_rd_t=101&pf_rd_p=2be1aa47-7185-4845-bbd5-73a113feebfb&pf_rd_i=81107433031'
header = {'User-Agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254'}


def extract_price():
    page = requests.get(URL, headers= header)
    soup = bs(page.content, 'html.parser')
    price = float(soup.find('span', class_='a-price-whole').text.split()[0].replace(',',""))
    return price

def notify():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "s3o3n3u3@gmail.com"
    receiver_email = "singhravinder02112@gmail.com"
    password = 'fptthunixuwwreyi'
    p = extract_price()
    subject = 'BUY NOW!'
    message = f"""
    Price has Dropped to {p}! Buy your product now!
    Link: {URL}
              """
    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = receiver_email
    em['Subject'] = subject
    em.set_content(message)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, em.as_string())
        print("Message Sent")

my_price = 17000
if extract_price() <= my_price:
    notify()