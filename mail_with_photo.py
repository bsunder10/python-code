
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = ""
toaddr = ""
msg = MIMEMultipart() 

msg['From'] = fromaddr 

msg['To'] = toaddr 

msg['Subject'] = "Subject of the Mail"

body = "Body_of_the_mail"

msg.attach(MIMEText(body, 'plain')) 

filename = "impg.jpg"
attachment = open("/home/pi/Desktop/impg.jpg", "rb") 

p = MIMEBase('application', 'octet-stream') 

p.set_payload((attachment).read()) 

encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

msg.attach(p) 

s = smtplib.SMTP('smtp.gmail.com', 587) 

s.starttls() 

s.login(fromaddr, "<password>") 
text = msg.as_string() 

s.sendmail(fromaddr, toaddr, text) 

s.quit() 
print('done')
