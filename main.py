import smtplib, ssl, getpass

gmail_sender = input(str("Masukkan akun gmail pengirim: "))
password_sender = getpass.getpass(prompt="Masukkan password pengirim (tersembunyi): ")


context = ssl.create_default_context() #membuat protokol pengiriman email dengan default
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server: #mengatur profil protokol server
    server.ehlo() #menetapkan localhost
    server.login(gmail_sender, password_sender) #menetapkan email & pass user/sender
    with open(r'C:\Users\ZAKI\Documents\AAA.Computing Projects\A.Zek-github-repositories-data\python-email-sender\receiver_list.txt', 'r') as file: #membaca file rceiver
        gmail_receiver = file.read().replace('\n', ',') #mengatur variabel sebagai receiver

        sent_from = gmail_sender #variabel sender
        sent_to = gmail_receiver #variabel receiver
        sent_subject = input(str("Masukkan subjek email: ")) #variabel subject
        sent_body = input(str("Masukkan isi pesan email: ")) #variabel body

        #deklarasi body email
        message = """\
        from: %s
        to: %s
        subject: %s

        %s
        """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

        try:
            server.sendmail(
                sent_from, sent_to, message
            )
            server.close()

            print('Email sent!')
        except Exception as exception:
            print("Error: %s!\n\n" % exception)