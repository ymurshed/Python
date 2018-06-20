import asyncio


async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888,
                                                   loop=loop)

    print('Send: %r' % message)
    writer.write(message.encode())

    data = await reader.read(100)
    print('Received: %r' % data.decode())

    print('Close the socket')
    writer.close()

async def stop_after(loop, stop_after_time):
    await asyncio.sleep(stop_after_time)
    loop.stop()


loop = asyncio.get_event_loop()
loop.create_task(tcp_echo_client('I am thor!', loop))
loop.create_task(tcp_echo_client('I am captain america!', loop))
loop.create_task(tcp_echo_client('I am iron man!', loop))

loop.run_forever()
#loop.create_task(stop_after(loop, 65))
loop.close()
