import socket
import ssl
import datetime


def getSSL(hostname):
    print(f"{hostname}")

    # https://www.w3schools.com/python/python_datetime.asp
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
    context = ssl.create_default_context()

    # to wrap a socket.
    conn = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname=hostname,)
    conn.settimeout(3.0)
    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()

    Exp_ON=datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
    Days_Remaining= Exp_ON - datetime.datetime.utcnow()

    print(f"Expires ON:- {Exp_ON} \n Remaining:- {Days_Remaining}")
    print("----------------------------------")

domains = ['google.com', 'yahoo.com', "twitter.com"]

for domain in domains:
    getSSL(domain)

print("Complete")