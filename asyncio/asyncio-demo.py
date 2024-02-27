import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    print("Main program started")

    # Create tasks
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    # Wait for tasks to complete
    await t1
    await t2

    print("Main program completed")

# Run the event loop
asyncio.run(main())
