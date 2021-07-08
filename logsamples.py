import logging

logging.basicConfig(level=logging.DEBUG, 
    filename="app.log", filemode="w", format='%(name)s - %(asctime)s - %(process)s - %(levelname)s - %(message)s',
    datefmt='%d-%m-%y %H:%M:%S')

logger = logging.getLogger("MyCustomLogger")

def foo():
    logger.debug("Entering...foo())")
    print("inside foo()")

    value = 100
    name = "Ajay"

    logger.debug("Exiting...foo())")
    logger.info("Exiting...foo())")
    logger.warning("Entering foo()...")
    logger.error("ERROR!: " + "value: " + str(value) + ". name: " + name)
    logger.critical("Exiting...foo())")


def bar():
    logger.debug("Entering...bar())")
    try:
        print("inside br()")
        raise Exception("Custom exception raised")
    except Exception as ex:
        logger.error("ERROR! ", exc_info=True)

    logger.debug("Exiting...bar())")

def foobar():
    logger.debug("Entering...foobar())")
    print("inside foobar()")
    logger.debug("Exiting...foobar())")

foo()
bar()
foobar()

bar()

foobar()

foo()
