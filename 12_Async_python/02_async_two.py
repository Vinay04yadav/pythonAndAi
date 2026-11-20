import asyncio

async def brew(name):
    print(f"Brewing {name} chai...")
    await asyncio.sleep(3)
    print(f"{name} chai is ready!")

async def brew_coffee():
    print(f"Brewing coffee...")
    await asyncio.sleep(2) # if instead of this we use time.sleep() then we notice that each tea is getting brewed one by one, making program slow but using async, await, asyncio... things are being done faster.
    print(f"Coffee is ready!")


# Another way to call co-routines.
async def main():
    #asyncio.gather() is used to run multiple coroutines concurrently and collect their results together.
    await asyncio.gather(
        brew("Masala"),
        brew("Ginger"),
        brew("Elaichi"),
        brew_coffee()
    )

# run the co-routine main() -> it has all the others running in it
asyncio.run(main())