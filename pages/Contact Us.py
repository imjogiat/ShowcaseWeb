import streamlit as stlt
import wbpg_email

stlt.title("Contact Us")

with stlt.form(key= "email_form"):
    email_address = stlt.text_input("Your email address: ")
    raw_email_msg = stlt.text_area("Your message: ")
    submit = stlt.form_submit_button("Submit")

    email_msg = f"""\
Subject: Web Portfolio email from {email_address}
From: {email_address}
{raw_email_msg}
    """

    if submit:
        wbpg_email.send_email(email_msg)