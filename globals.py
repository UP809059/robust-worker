import socket

# Port numbers are arbitary (outside of avoiding reserved ports) but must be the same for every node on the network

# Can't use proper socket.SO_BROADCAST port as this requires root
BROADCAST_OUT_PORT = 56433
# BROADCAST_IN_PORT = 56434

COLLEAGUE_LISTEN_PORT = 56435
COLLEAGUE_TALK_PORT = 56436
MASTER_DIRECT_PORT = 56437
FROM_MASTER_PORT = 56438

BROADCAST_ASK_FOR_COLLEAGUE = "COLL_REQ"

COLLEAGUE_ADVERT_RESPONSE = "AVALIABLE_TO_COLLEAGUE"
COLLEAGUE_ADVERT_CONFIRMATION = "COLL_ADVERT_CONFIRM_REQ"
COLLEAGUE_REQUEST_PROGRESS = "COLL_GIVE_PROG"

LOCALHOST_NAME = socket.gethostname()

MASTER_ADDR = "master"

SLAVE_REQ_WORK = "MASTER_GIVE_WORK"

# WORK_BLOCK_SIZE = 1000000
WORK_BLOCK_SIZE = 10000
# WORK_BLOCK_SIZE = 100

SYNC_THRESHOLD = 2

COLLEAGUE_PROGRESS_PREFIX = "COLL_PROG:"


BLOCKS_TO_CALCULATE = 250