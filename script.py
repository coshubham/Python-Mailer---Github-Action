import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_mail(workflow_name, repo_name, workflow_run_id):
    # Email details
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')

    # Print debug info
    print(f"SENDER: {sender_email}")
    print(f"RECEIVER: {receiver_email}")
    print(f"WORKFLOW_NAME: {workflow_name}")
    print(f"REPO_NAME: {repo_name}")
    print(f"RUN_ID: {workflow_run_id}")

    # Email message
    subject = f"Workflow {workflow_name} in {repo_name} has failed"
    body = (
        f"The workflow '{workflow_name}' in the repository '{repo_name}' has failed. "
        f"Please check the logs for more details.\n\nRun ID: {workflow_run_id}"
    )

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# ✅ Call the function (outside the function definition)
if __name__ == "__main__":
    send_mail(
        os.getenv('WORKFLOW_NAME'),
        os.getenv('REPO_NAME'),
        os.getenv('WORKFLOW_RUN_ID')
    )
