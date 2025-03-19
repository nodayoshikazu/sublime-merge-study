""" Prints Hello World """
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

class HelloWorld:
    """ Prints Hello World """

    def hello(self, name: str):
        """ Prints Hello World """
        logger.debug(f"Hello World! {name}")
        print("Hello!")


    def test(self):
        # Create an instance of HelloWorld and call the hello method
        h = HelloWorld()
        h.hello("Yoshikazu")
        h.hello("Chan")

    def hello_yoshi(self, name):
        hw = HelloWorld()
        print(f" Hello {name}")

    def hello_dude(self, name):
        hw = HelloWorld()
        print(f" Hey {name}!")


hw = HelloWorld()
hw.hello("John")
hw.test()
hw.hello_yoshi("noda")
hw.hello_dude("stupid")
