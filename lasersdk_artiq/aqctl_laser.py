#!/usr/bin/env python3

import argparse
import logging
import sys
import asyncio

from toptica.lasersdk.async.client import Client, NetworkConnection

from artiq.protocols.pc_rpc import Server
from artiq.tools import (verbosity_args, simple_network_args, init_logger,
                         bind_address_from_args)


logger = logging.getLogger(__name__)


class RPCClient(Client):
    param_types = {
            "bool": bool,
            "str": str,
            "int": int,
            "float": float,
            "bytes": bytes
    }
    async def get(self, param_name, *param_types):
        """Client.get() with parameter types as strings."""
        return await super().get(param_name,
                *(self.param_types[typ] for typ in param_types))

    async def ping(self):
        await self.get("system-label", "str")
        return True


def get_argparser():
    parser = argparse.ArgumentParser(
        description="""Laser SDK client controller.
        Use this controller for a TOPTICA DLC Pro.

        This exposes a low-level client (i.e. without knowledge of the
        parameter tree structure and types) as an ARTIQ device controller.
        Note: The param_type arguments to the get() method need to be passed as
        strings, not as types.""")
    parser.add_argument(
        "-d", "--device", default=None,
        help="Device host name or IP address.")
    simple_network_args(parser, 3272)
    verbosity_args(parser)
    return parser


def main():
    args = get_argparser().parse_args()
    init_logger(args)

    if args.device is None:
        print("You need to supply a -d/--device "
              "argument. Use --help for more information.")
        sys.exit(1)

    async def run():
        async with RPCClient(NetworkConnection(args.device, loop=loop)) as dev:
            server = Server({"laser": dev}, None, True)
            await server.start(bind_address_from_args(args), args.port)
            try:
                await server.wait_terminate()
            finally:
                await server.stop()

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run())
    finally:
        loop.close()


if __name__ == "__main__":
    main()
