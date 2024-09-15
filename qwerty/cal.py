from  qwerty.calculations import Calculations
import asyncio

async def func():
  cal=Calculations(4,5)
  return await cal.add()


asyncio.run(func())