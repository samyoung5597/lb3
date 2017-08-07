import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import os
import sys
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



DATABASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': '%s\db' % BASE_DIR
}

LOG_LIVEL = logging.DEBUG

LOG_TYPES = {
    'access': 'access.log',
    'login_in': 'login_in.log'
}
TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},

}

