from moonraker.plugins import Plugin
import logging

class Palette(Plugin):

    def __init__(self, manager):
        super().__init__(manager)
        self.manager.register_upload_hook(self.preprocess_file)
    def register(self):
        self.manager.register_action("palette", self.palette)

    def preprocess_file(self, file):
        # Do some preprocessing on the file here.
        # For example, you could convert the file to a different format.
        return file

    def palette(self, args):
        print("Palette plugin activated")
        logger = logging.getLogger(__name__)
        logger.info("I am bad at this.")