import asyncio
import unittest
import os

from toptica.lasersdk.async.client import Client, NetworkConnection


target = os.getenv("LASER")
@unittest.skipIf(not target, "LASER environment variable not defined")
class ClientTest(unittest.TestCase):
    def with_device(self, f):
        loop = asyncio.get_event_loop()
        async def run():
            async with Client(NetworkConnection(target, loop=loop)) as dev:
                return await f(dev)
        return loop.run_until_complete(run())

    def test_connect(self):
        async def run(dev):
            pass
        self.with_device(run)

    def test_get_label(self):
        async def run(dev):
            print(await dev.get("system-label", str))
        self.with_device(run)

    def test_get_status(self):
        async def run(dev):
            for k in ("power-supply:status-txt system-health-txt uptime-txt "
                    "fw-ver ssw-ver laser1:health-txt laser1:dl:cc:status-txt "
                    "laser1:dl:tc:status-txt " # laser1:dl:lock:state-txt "
                    "laser1:dl:pc:status-txt").split():
                print(k, await dev.get(k, str))
        self.with_device(run)

    def test_set_label(self):
        async def run(dev):
            old_label = await dev.get("system-label", str)
            new_label = "Laser SDK Client"
            await dev.set("system-label", new_label)
            new_label_readback = await dev.get("system-label", str)
            await dev.set("system-label", old_label)
            self.assertEqual(new_label_readback, new_label)
        self.with_device(run)
