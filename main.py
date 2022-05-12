import smtplib, ssl, getpass, csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail_sender = input(str("Masukkan akun gmail pengirim: ")) #variabel pengirim
password_sender = getpass.getpass(prompt="Masukkan password pengirim (tersembunyi): ") #variabel password pengirim
sent_subject = input(str("Masukkan subjek email: ")) #variabel subject
sent_body = input(str("Masukkan isi pesan email: ")) #variabel body


#functions - def
#1. func menampilkan receiver list .txt
def showList():
    try:
        file = open(r'C:\Users\ZAKI\Documents\AAA.Computing Projects\A.Zek-github-repositories-data\python-email-sender\receiver_list.txt', 'r')
        receiver = csv.reader(file)
        if file == '':
            print("\nData masih kosong")
        else:
            print("\n===Daftar Receiver Email===")
            print("\n")
            for data in receiver:
                print("nama = " + data[0])
                print("email = " + data[1])
                print("==================")
        file.close()
        print()
    except Exception as exception:
        print("Error: %s!\n" % exception)
        print()

#main-program / sending email part
try:
    file = open(r'C:\Users\ZAKI\Documents\AAA.Computing Projects\A.Zek-github-repositories-data\python-email-sender\receiver_list.txt', 'r') #membuka file receiver_list.txt
    receiver = csv.reader(file) #variabel receiver email
    for data in receiver: #untuk setiap data receiver dilakukan
        message = MIMEMultipart('alternative') #penggunaan MIMEMultipart sebagai template pesan
        message['Subject'] = sent_subject #menyertakan subjek email
        message['From'] = gmail_sender #menyertakan pengirim email
        message['To'] = data[1] #menyertakan penerima email

        bodyPart = sent_body #variabel penampung bodypart email

        message.attach(MIMEText(bodyPart, 'plain')) #menyertakan bodypart pesan email

        context = ssl.create_default_context() #membuat protokol pengiriman email dengan default
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server: #mengatur profil protokol server
            try: #dilakukan
                server.ehlo() #menetapkan localhost
                server.login(gmail_sender, password_sender) #menetapkan akun user pengirim
                server.sendmail(gmail_sender, data[1], msg=message.as_string()) #menetapkan pengirim, penerima, & isi pesan email
                server.close() #setelah selesai mengirim, server akan berhenti

                print('Email Kepada '+data[0]+' Berhasil Terkirim!') #menyampaikan pesan berhasil terkirim
            except Exception as exception: #exception handling - jika try di atas error
                print("Error: %s!\n\n" % exception) #menyertakan / memberitahukan alasan error try
    file.close() #data selesai
except Exception as exception: #exception handling - jika try di atas error
    print("Error: %s!\n\n" % exception) #menyertakan / memberitahukan alasan error try