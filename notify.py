import smtplib
import credentials as cr

def sendMail():
    try:
        smtpObj = smtplib.SMTP(host=cr.smtpserv,port=cr.smtpport)
        smtpObj.starttls()
        smtpObj.login(user=cr.email,password=cr.pw)
        smtpObj.sendmail(from_addr=cr.email, to_addrs=cr.receiver, msg=cr.message) 
        smtpObj.quit()        
        print("Successfully sent email")
    except smtplib.SMTPAuthenticationError:
        print("Error: The server didn\'t accept the username/password combination")
    except smtplib.SMTPHeloError:
        print("Error: Server didn\'t reply to HELO")
    except smtplib.SMTPNotSupportedError:
        print("Error: The AUTH command is not supported by the server")
    except smtplib.SMTPException:
        print("Error: No suitable authentication method was found")
    except :
        print("Error: unable to send email")

if __name__=='__main__':
    sendMail()