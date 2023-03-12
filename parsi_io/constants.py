import os
import logging


base_path = os.path.dirname(__file__)

resource_path = os.path.join(base_path, "resources")
if not os.path.exists(resource_path):
    logging.warning("resources directory does not exist! Most modules need resources in this directory.")

chunker_path = os.path.join(resource_path, "chunker.model")
if not os.path.exists(resource_path):
    logging.warning("chunker model does not exist!")

postagger_path = os.path.join(resource_path, "postagger.model")
if not os.path.exists(resource_path):
    logging.warning("postagger model does not exist!")