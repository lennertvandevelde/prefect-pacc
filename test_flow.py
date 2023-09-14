from prefect import flow, get_run_logger


@flow()
def main_flow():
    logger = get_run_logger()
    logger.info("Hello MainFlow!")
    sub_flow()


@flow()
def sub_flow():
    logger = get_run_logger()
    logger.info("Hello SubFlow!")