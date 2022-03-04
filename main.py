import pyautogui
import time
from functions.CSVFile import CSVFile
from functions.SendEmail import SendEmail

title_email = "Titulo do Email"
texto_do_email = """
Aqui envia o texto que deseja no email
"""

time_start_in_seconds = 5
time.sleep(time_start_in_seconds)
local_file_input = 'support/data_input/contacts_file.csv'
read_csv = CSVFile(local_file_input)
json = read_csv.read_csv_file()
count_json = len(json)
pos_mouse_x, pos_mouse_y = pyautogui.position()
count = 0
for i in json:
    print(f"Enviando email {count + 1} de {count_json}...")
    email = i['email'][0]
    send_email = SendEmail()
    send_email.click_button_send(pos_mouse_x, pos_mouse_y)
    send_email.send_email(email, title_email, texto_do_email)
    count += 1
    print(i)
    save_csv = CSVFile('support/data_output/emails_sent.csv')
    save_csv.save_csv_file(i)
print('Término de envio dos emails.')
