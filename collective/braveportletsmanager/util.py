"""Some utility functions"""
import logging
import sys


LOGGER = logging.getLogger('collective.braveportletsmanager')
def logException(msg, context=None, logger=LOGGER):
    """Logs error into log file and if possible into zope error log"""
    logger.exception(msg)
    if context is not None:
        error_log = getattr(context, 'error_log', None)
        if error_log is not None:
            error_log.raising(sys.exc_info())
