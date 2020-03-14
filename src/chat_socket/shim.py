import json
import time
import asyncio

from .message_a_user import lambda_handler
from .local_sockets import local_sockets


def queue_message(message):
    # simulate async on server
    time.sleep(0.1)
    mock_event = {
        'Records': [{
            'Sns': {
                'Message': message
            }
        }]
    }
    lambda_handler(mock_event, None,
                   send_message_to_socket=send_message_to_socket)


def send_message_to_socket(connection_id, data):
    print(f'send_message_to_socket {connection_id}')
    socket = local_sockets[connection_id]
    asyncio.create_task(socket.send(data.decode()))
