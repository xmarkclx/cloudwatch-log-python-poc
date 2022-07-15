#!/usr/bin/env python
import os
import watchtower
import logging
from dotenv import load_dotenv

load_dotenv()

logGroup = os.environ.get('LOGGROUP')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(watchtower.CloudWatchLogHandler(
    'LOGGROUPINAWS' if logGroup is None else logGroup))

logger.info("Hi again!")
logger.info(dict(foo="bar", details={}))
