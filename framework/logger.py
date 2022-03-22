import logging


class Logger:
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.INFO, filename=u'logger.log')

    @staticmethod
    def logging_info_data(sentence):
        logging.info(sentence)

    @staticmethod
    def clear_logger():
        f = open('logger.log', 'r+')
        f.truncate()
        f.close()
