# Copyright (C) 2009-2010 Raul Jimenez
# Released under GNU LGPL 2.1
# See LICENSE.txt for more information

#from nose.tools import eq_, ok_
'''
import logging, logging_conf
logs_path = 'test_logs'
logs_level = logging.DEBUG
logging_conf.setup(logs_path, logs_level)
'''

import identifier
from identifier import Id, ID_SIZE_BITS, BITS_PER_BYTE
import node



TASK_INTERVAL = .01
TIMEOUT_DELAY = .4

CLIENT_ID = identifier.Id('\x41' * identifier.ID_SIZE_BYTES)
CLIENT_PORT = 6000
CLIENT_ADDR = ('127.0.0.1', CLIENT_PORT)
CLIENT_NODE = node.Node(CLIENT_ADDR, CLIENT_ID)
BT_PORT = 7777

SERVER_ID = identifier.Id('\x01' * identifier.ID_SIZE_BYTES)
SERVER_PORT = 6001
SERVER_ADDR = ('127.0.0.1', SERVER_PORT)
SERVER_NODE = node.Node(SERVER_ADDR, SERVER_ID)

SERVER2_ID = identifier.Id('\x43' * identifier.ID_SIZE_BYTES)
SERVER2_ADDR = ('128.0.0.2', 6002)
SERVER2_NODE = node.Node(SERVER2_ADDR, SERVER2_ID)

EXTERNAL_NODE_ADDR = ('128.0.0.1', 6881)
EXTERNAL_NODE = node.Node(EXTERNAL_NODE_ADDR)

NO_ADDR = ('128.0.0.1', 1)
DEAD_NODE = node.Node(NO_ADDR)

NODE_ID = identifier.Id('\x02' * identifier.ID_SIZE_BYTES)
TARGET_ID = NODE_ID
INFO_HASH = identifier.Id('\x60\xd5\xd8\x23\x28\xb4\x54\x75\x11\xfd\xea\xc9\xbf\x4d\x01\x12\xda\xa0\xce\x00')
INFO_HASH_ZERO = identifier.Id('\x00' * identifier.ID_SIZE_BYTES)
TID = 'a'
TID2 = 'b'
TOKEN = 'aa'

NUM_NODES = 8
NODE_IDS = [identifier.Id(chr(i) * identifier.ID_SIZE_BYTES) \
            for i in xrange(NUM_NODES)]
ADDRS = [('128.0.0.'+str(i), 7000 + i) for i in xrange(NUM_NODES)]
NODES = [node.Node(addr, node_id) \
             for addr, node_id in zip(ADDRS, NODE_IDS)]

# We don't have RNODES as constant because rnodes are modificable. In
# particular, it creates temporal depencencies.
#RNODES = [n.get_rnode() for n in NODES]
PEERS = ADDRS

NODE2_IDS = [identifier.Id('\x01'+chr(i) * (identifier.ID_SIZE_BYTES-1)) \
            for i in xrange(100, 100+NUM_NODES)]
ADDRS2 = [('128.0.0.'+str(i), 7000 + i) \
              for i in xrange(100, 100+NUM_NODES)]
NODES2 = [node.Node(addr, node_id) \
              for addr, node_id in zip(ADDRS2, NODE2_IDS)]
PEERS2 = ADDRS2

IPS = ['1.2.3.' + str(i) for i in xrange(NUM_NODES)]

#TODO2: make this faster
num_nodes_per_ld = 20
NODES_LD_IH = [[]] * BITS_PER_BYTE
for ld in xrange(BITS_PER_BYTE, ID_SIZE_BITS):
    NODES_LD_IH.append([])
    common_id = INFO_HASH_ZERO.generate_close_id(ld)
    #eq_(common_id.log_distance(INFO_HASH_ZERO), ld)
    for i in xrange(num_nodes_per_ld):
        this_id = Id(common_id.bin_id[:-1] + chr(i))
        #eq_(this_id.log_distance(INFO_HASH_ZERO), ld)
        NODES_LD_IH[ld].append(
            node.Node(('128.0.0.' + str(i), ld), this_id))
num_nodes_per_ld = 50
NODES_LD_CL = [[]] * BITS_PER_BYTE
for ld in xrange(BITS_PER_BYTE, ID_SIZE_BITS):
    NODES_LD_CL.append([])
    common_id = CLIENT_ID.generate_close_id(ld)
    #eq_(common_id.log_distance(INFO_HASH_ZERO), ld)
    for i in xrange(num_nodes_per_ld):
        this_id = Id(common_id.bin_id[:-1] + chr(i))
        #eq_(this_id.log_distance(INFO_HASH_ZERO), ld)
        NODES_LD_CL[ld].append(
            node.Node(('128.0.0.' + str(i), ld), this_id))

