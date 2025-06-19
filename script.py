import smtplib   # for sending emails
from email.mime.text import MIMEText # for creating email text
from email.mime.multipart import MIMEMultipart  # for creating multipart emails
import os  # for accessing environment variables
def send_mail(workflow_name, repo_name, workflow_run_id):
       #Email details
       sender_email = os.getenv('SENDER_EMAIL')
       sender_password = os.getenv('SENDER_PASSWORD')
       receiver_email = os.getenv('RECEIVER_EMAIL')

       #Email message
       subject = f"Workflow {workflow_name} in {repo_name} has failed"
       body = f"The workflow {workflow_name} in the repository {repo_name} has failed. Please check the logs for more details.\nMore Details: \nRun_ID: {workflow_run_id}"
       msg = MIMEMultipart()

       msg['From'] = sender_email
       msg['To'] = receiver_email  
       msg['Subject'] = subject
       msg.attach(MIMEText(body, 'plain'))
       try:
           # Connect to the SMTP server
               server = smtplib.SMTP('smtp.gmail.com', 587) 
               server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
               server.login(sender_email, sender_password)  # Login to the email account
               text = msg.as_string()  # Convert the message to a string format
               server.sendmail(sender_email, receiver_email, text)  # Send the email
               server.quit()  # Close the connection to the SMTP server
               print("Email sent successfully!")
       except Exception as e:
           print(f"Failed to send email: {e}")  # Print error if email sending fails
       send_mail(os.getenv('WORKFLOW_NAME'), os.getenv('REPO_NAME'), os.getenv('WORKFLOW_RUN_ID'))  # Call the function with environment variables