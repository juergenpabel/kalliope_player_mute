#!/usr/bin/python3

import logging
import time
from threading import Thread
from kalliope import Utils 

logging.basicConfig()
logger = logging.getLogger("kalliope")


class Mute(Thread):
    def __init__(self, **kwargs):
        super(Mute, self).__init__()
        logger.debug("[player:mute] __init__()")

    def run(self):
        logger.debug("[player:mute] run()")
        while True:
            time.sleep(1)

    def pause(self):
        logger.debug("[player:mute] pause()")

    def unpause(self):
        logger.debug("[player:mute] unpause()")

