#!/usr/bin/env python2
# coding:utf-8

import smtplib
import email.mime.text


def sendMail(HtmlString):
    HOST = "smtp.139.com"
    SUBJECT = "The IP address has been changed"
    TO = "121671486@139.com"
    FROM = "13718799673@139.com"
    # Remask = "The IP address has been changed"

    msg = email.mime.text.MIMEText("""
        <html>
                <head>
                        <meta charset="utf-8" />
                </head>
                <body>
                        <em><h1>ip:%s</h1></em>
                </body>
        </html>
        """ % (HtmlString), "html", "utf-8")

    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['TO'] = TO

    try:
        # 465
        server = smtplib.SMTP_SSL(HOST, '465')
        server.ehlo(HOST)
        # 25 不推荐
        # server = smtplib.SMTP()
        # server.connect(HOST,'25')
        # server.starttls()
        server.login("13718799673@139.com", "dfewfewfwefwefew")
        server.sendmail(FROM, TO, msg.as_string())
        server.quit()
        print ("Send mail suc")
    except:
        print ("Send mail Error")


if __name__ == '__main__':
    sendMail("dd")
