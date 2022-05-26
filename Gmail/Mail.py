from  email  import  message
from  http  import  server
from  Gmail.Google  import  Create_Service
from  email.mime.text  import  MIMEText
from  email.mime.multipart  import  MIMEMultipart
import  base64

  

CLIENT_SECRET_FILE  =  "./Gmail/token/client_secret.json"
API_NAME  =  'gmail'
API_VERSION  =  'v1'
SCOPES  = ['https://mail.google.com/']


def send_email(message_content: str, send_to: str, subject: str ):
    service  =  Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    mineMessage  =  MIMEMultipart()

    # gui den 
    mineMessage['to'] =  send_to # địa chỉ nhận
    # tieu de 
    mineMessage['subject'] =  subject # subject

    # ghep thanh mot buc thu hoan chinh
    mineMessage.attach(MIMEText(message_content, 'plain')) 

    raw_string  =  base64.urlsafe_b64encode(mineMessage.as_bytes()).decode()

    message  =  service.users().messages().send(userId='me', body={'raw': raw_string}).execute()

    return message


# if __name__ == "__main__":
#     print(send_email("xin chao buoi toi", "tuananh1421999@gmail.com", "chao buoi toi"))