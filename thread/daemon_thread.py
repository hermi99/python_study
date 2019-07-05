import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

if __name__ == '__main__':
    logging.debug('Starting')
    logging.debug('Exiting')