from  qwerty.calculations import Evaluate
import asyncio

async def func():
  cal=Evaluate()
  return await cal.find().add()


asyncio.run(func())