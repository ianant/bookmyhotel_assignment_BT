import logging
logging.basicConfig(filename='Logs\\info.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(message)s')

logger=logging.getLogger("BookMyHotel")