import json
import os
from datetime import datetime
from pathlib import Path

DEBUG = True #show debug messages in CLI
WEBSERVER_THREADS = 1

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
NOUNDERLINE = '\033[0m'

DATA_DIR = 'data'
TEST_DIR = 'test'
LOGGING_FILE = 'data_feeds.db'
DATEFORMAT = '%Y-%m-%d %H:%M:%S.%f %z'
DATA_EXT = '.csv'
LINE_START = '>'

FEED_NAME = 'feed_name'
DATA_POINT = 'data_point'
TIME_STAMP = 'time_stamp'

PROJECT_PATH = Path(os.path.dirname(os.path.realpath(__file__)))
DATA_PATH = PROJECT_PATH / DATA_DIR
TEST_PATH = PROJECT_PATH / TEST_DIR
LOGGING_PATH = DATA_PATH / LOGGING_FILE
LOGGING_FORMAT = ('%(asctime)s:%(thread)d - %(name)s - %(levelname)s - %(message)s')

def start_message(feed):
    return f'\n{HEADER}Starting {UNDERLINE}{feed.NAME}{NOUNDERLINE} {HEADER}data feed!{ENDC}'

def stop_message(feed):
    return f'\n{OKCYAN}Shutting down {UNDERLINE}{feed.NAME}{NOUNDERLINE} {OKCYAN}...{ENDC}'

def init_time_message(cls):
    return f'\nSiwa init time: {datetime.fromtimestamp(cls.init_time).strftime(DATEFORMAT)}'

get_color = lambda x: OKGREEN if x else FAIL
get_word = lambda x: '' if x else 'not '

def get_starttime_string(feed):
    if (hasattr(feed, 'START_TIME') and feed.START_TIME):
        #ensure START_TIME exists and is not None before trying to convert
        dt_from_timestamp = datetime.fromtimestamp(feed.START_TIME)
        human_readable_time_str = dt_from_timestamp.strftime(DATEFORMAT)
        return f'{human_readable_time_str}'
    else:
        #if START_TIME not initialized (i.e. because "start gauss" not issued yet)
        #(e.g. when calling `status` command before having ever started a feed)
        return f'[NEVER]'

def status_message(feed):
    x = feed.ACTIVE
    return f'{get_color(x)}{feed.NAME}{ENDC} with id {feed.ID} is {get_word(x)}active, with {feed.COUNT} data points served since {get_starttime_string(feed)}'

#################### WEB3 ####################

# POKT 
POKT_PORTAL_ID = 'a609ace3fe0c00927e127927'
POKT_ARBITRUM = 'arbitrum-one'
POKT_ETHEREUM = 'eth-mainnet'

# RPC Endpoints
ARBITRUM_GOERLI = 'https://goerli-rollup.arbitrum.io/rpc' 
ARBITRUM_MAINNET = f'https://{POKT_ARBITRUM}.gateway.pokt.network/v1/lb/{POKT_PORTAL_ID}'
ETHEREUM_MAINNET = f'https://{POKT_ETHEREUM}.gateway.pokt.network/v1/lb/{POKT_PORTAL_ID}'

# Addresses:
TRANSLUCENT_GAUSS_GOERLI_ARBITRUM = '0xB39AC20b8b0C840a863ceB58A29b597022d98Bf5'#'0x77f85f243dCd2A69F20c2A98F1ef993DC4492A51'

# ABIs below
TRANSLUCENT_FLUX_AGGREGATOR = '[{"inputs":[{"internalType":"address","name":"_link","type":"address"},{"internalType":"uint128","name":"_paymentAmount","type":"uint128"},{"internalType":"uint32","name":"_timeout","type":"uint32"},{"internalType":"address","name":"_validator","type":"address"},{"internalType":"int256","name":"_minSubmissionValue","type":"int256"},{"internalType":"int256","name":"_maxSubmissionValue","type":"int256"},{"internalType":"uint8","name":"_decimals","type":"uint8"},{"internalType":"string","name":"_description","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"int256","name":"current","type":"int256"},{"indexed":true,"internalType":"uint256","name":"roundId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"updatedAt","type":"uint256"}],"name":"AnswerUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"AvailableFundsUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"roundId","type":"uint256"},{"indexed":true,"internalType":"address","name":"startedBy","type":"address"},{"indexed":false,"internalType":"uint256","name":"startedAt","type":"uint256"}],"name":"NewRound","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"oracle","type":"address"},{"indexed":false,"internalType":"address","name":"admin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"OracleAdminUpdateRequested","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"oracle","type":"address"},{"indexed":true,"internalType":"address","name":"newAdmin","type":"address"}],"name":"OracleAdminUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"oracle","type":"address"},{"indexed":true,"internalType":"bool","name":"whitelisted","type":"bool"}],"name":"OraclePermissionsUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"OwnershipTransferRequested","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"requester","type":"address"},{"indexed":false,"internalType":"bool","name":"authorized","type":"bool"},{"indexed":false,"internalType":"uint32","name":"delay","type":"uint32"}],"name":"RequesterPermissionsSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint128","name":"paymentAmount","type":"uint128"},{"indexed":true,"internalType":"uint32","name":"minSubmissionCount","type":"uint32"},{"indexed":true,"internalType":"uint32","name":"maxSubmissionCount","type":"uint32"},{"indexed":false,"internalType":"uint32","name":"restartDelay","type":"uint32"},{"indexed":false,"internalType":"uint32","name":"timeout","type":"uint32"}],"name":"RoundDetailsUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"int256","name":"submission","type":"int256"},{"indexed":true,"internalType":"uint32","name":"round","type":"uint32"},{"indexed":true,"internalType":"address","name":"oracle","type":"address"}],"name":"SubmissionReceived","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previous","type":"address"},{"indexed":true,"internalType":"address","name":"current","type":"address"}],"name":"ValidatorUpdated","type":"event"},{"inputs":[{"internalType":"address","name":"_oracle","type":"address"}],"name":"acceptAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"acceptOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"allocatedFunds","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"availableFunds","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"_removed","type":"address[]"},{"internalType":"address[]","name":"_added","type":"address[]"},{"internalType":"address[]","name":"_addedAdmins","type":"address[]"},{"internalType":"uint32","name":"_minSubmissions","type":"uint32"},{"internalType":"uint32","name":"_maxSubmissions","type":"uint32"},{"internalType":"uint32","name":"_restartDelay","type":"uint32"}],"name":"changeOracles","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_oracle","type":"address"}],"name":"getAdmin","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_roundId","type":"uint256"}],"name":"getAnswer","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getOracles","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_roundId","type":"uint256"}],"name":"getTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestAnswer","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRound","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"linkToken","outputs":[{"internalType":"contract LinkTokenInterface","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxSubmissionCount","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxSubmissionValue","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minSubmissionCount","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minSubmissionValue","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"onTokenTransfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"oracleCount","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_oracle","type":"address"},{"internalType":"uint32","name":"_queriedRoundId","type":"uint32"}],"name":"oracleRoundState","outputs":[{"internalType":"bool","name":"_eligibleToSubmit","type":"bool"},{"internalType":"uint32","name":"_roundId","type":"uint32"},{"internalType":"int256","name":"_latestSubmission","type":"int256"},{"internalType":"uint64","name":"_startedAt","type":"uint64"},{"internalType":"uint64","name":"_timeout","type":"uint64"},{"internalType":"uint128","name":"_availableFunds","type":"uint128"},{"internalType":"uint8","name":"_oracleCount","type":"uint8"},{"internalType":"uint128","name":"_paymentAmount","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"paymentAmount","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"requestNewRound","outputs":[{"internalType":"uint80","name":"","type":"uint80"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"restartDelay","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_requester","type":"address"},{"internalType":"bool","name":"_authorized","type":"bool"},{"internalType":"uint32","name":"_delay","type":"uint32"}],"name":"setRequesterPermissions","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newValidator","type":"address"}],"name":"setValidator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_roundId","type":"uint256"},{"internalType":"int256","name":"_submission","type":"int256"}],"name":"submit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"timeout","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_oracle","type":"address"},{"internalType":"address","name":"_newAdmin","type":"address"}],"name":"transferAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"updateAvailableFunds","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint128","name":"_paymentAmount","type":"uint128"},{"internalType":"uint32","name":"_minSubmissions","type":"uint32"},{"internalType":"uint32","name":"_maxSubmissions","type":"uint32"},{"internalType":"uint32","name":"_restartDelay","type":"uint32"},{"internalType":"uint32","name":"_timeout","type":"uint32"}],"name":"updateFutureRounds","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"validator","outputs":[{"internalType":"contract AggregatorValidatorInterface","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawFunds","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_oracle","type":"address"},{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawPayment","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_oracle","type":"address"}],"name":"withdrawablePayment","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'