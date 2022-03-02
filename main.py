import csv
import os
import pyautogui
import time
import logger

texto_do_email = """
Ciao buongiorno! Cari signori.

Mi chiamo Vanessa Carla Manfredini de Souza, sono italiana nata in Brasile, ma devo regolarizzare la mia cittadinanza italiana iure sanguinis, mia sorella, Sandra Mara Manfredini Santos, deve regolarizzare anche la sua cittadinanza iure sanguinis.

Andremo a vivere insieme in Italia e vorremmo sapere se sareste così gentili da farci sapere se possiamo utilizzare la stessa documentazione (Apostille dell'Aia) per regolarizzare la nostra cittadinanza iure sanguinis. So che i nostri documenti come l'atto di nascita sono individuali, vorrei sapere se possiamo usare gli stessi certificati del nostro (antenati), bisnonno, nonno e padre, visto che siamo della stessa famiglia?

Per programmare l'inizio del processo di cittadinanza è necessario avere la residenza iscritta con qualsiasi tipo di contratto di locazione, oppure averne uno specifico?

Mi scuso se ci sono errori di ortografia mentre sto imparando l'italiano.

Per favore, vorrei sapere qual è il tempo stimato di programmazione per avviare il processo di riconoscimento della cittadinanza jure sanguinis?

Ringrazio anticipatamente e porgo i miei più cordiali saluti,
Vanessa Manfredini
"""


class SendEmail:
    def __init__(self):
        self.local_file_input = f'{os.path.abspath(os.path.dirname(__file__))}/contacts_file.csv'
        print(self.local_file_input)
        self.title_email = 'Cittadinanza'
        self.body_email = texto_do_email
        self.position_mouse_x, self.position_mouse_y = self.position_mouse()
        self.n_rows = None
        self.id = None
        self.email = None
        self.provincia = None
        self.cidade = None
        self.pec = None

    def count_rows_csv(self):
        self.n_rows = len(open(self.local_file_input).readlines()) - 1

    def read_csv_and_send_email(self):
        with open(self.local_file_input) as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            cont = 1
            for self.id, self.cidade, self.provincia, self.email, self.pec in reader:
                print(f'Enviando email {cont} de {self.n_rows}')
                cont += 1
                if self.email == "":
                    return
                self.send_email()
                dictionary = dict(
                    {id: {"provincia": self.provincia, "cidade": self.cidade, "email": [self.email, self.pec]}}
                )
                logger.logging.info(dictionary)
                self.save_output_csv()
        print('Fim de envio dos e-mails.')

    def save_output_csv(self):
        with open('emails_sent.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([self.id, self.provincia, self.cidade, self.email, self.pec])

    def send_email(self):
        typo_time = 0.05
        pyautogui.click(self.position_mouse_x, self.position_mouse_y)
        pyautogui.write(self.email, typo_time)
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.write(self.title_email, typo_time)
        pyautogui.press('tab')
        pyautogui.typewrite(self.body_email)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'enter')
        time.sleep(1)

    @staticmethod
    def position_mouse():
        return pyautogui.position()


if __name__ == '__main__':
    time_start_in_seconds = 5
    time.sleep(time_start_in_seconds)
    send_email = SendEmail()
    send_email.count_rows_csv()
    send_email.read_csv_and_send_email()
