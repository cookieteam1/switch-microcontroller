import smtplib
import credentials as cr

def sendMail():
    try:
        smtpObj = smtplib.SMTP(host=cr.smtpserv,port=cr.smtpport)
        smtpObj.starttls()
        smtpObj.login(user=cr.email,password=cr.pw)
        smtpObj.sendmail(from_addr=cr.email, to_addrs=cr.receiver, msg=cr.message) 
        smtpObj.close()        
        print("Successfully sent email")
    except :
        print("Error: unable to send email")

if __name__=='__main__':
    sendMail()