import asyncio

class Calculations:
  
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
  async def add(self):
    await asyncio.sleep(1) 
    return self.x+self.y
  
  async def sub(self):
    await asyncio.sleep(1) 
    return self.x - self.y
  
  async def mul(self):
    await asyncio.sleep(1) 
    return self.x * self.y
  
  async def div(self):
    await asyncio.sleep(1) 
    return self.x/self.y