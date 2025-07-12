import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, 'data')
MODEL_NAME = 'all-MiniLM-L6-v2'

INDEX_DIM = 384
TOP_K = 5
