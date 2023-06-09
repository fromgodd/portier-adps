import asyncio
import aiohttp
import pyfiglet
import colored

async def check_port(session, host, port):
    try:
        url = f"http://{host}:{port}"
        async with session.get(url, timeout=3) as response:
            if response.status == 200:
                print(colored.stylize(f"Port {port} is open", colored.fg('green')))
    except (aiohttp.ClientConnectorError, asyncio.TimeoutError):
        print(colored.stylize(f"Port {port} is closed", colored.fg('red')))

async def main():
    host = input("Enter the target host: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    async with aiohttp.ClientSession() as session:
        tasks = []
        for port in range(start_port, end_port + 1):
            task = asyncio.create_task(check_port(session, host, port))
            tasks.append(task)

        await asyncio.gather(*tasks)

# Banner
banner = pyfiglet.Figlet().renderText("ADPS")
gradient_banner = colored.stylize(banner, colored.fg("red") + colored.bg("yellow"))
print(gradient_banner)

# Run the port scanner
print("Welcome to the Async Port Scanner!")
print("Please provide the following details:")
print()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
