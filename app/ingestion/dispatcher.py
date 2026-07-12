import json
from .queue__manager import job_queue

class EventDispatcher:
    async def dispatch(self, event):

        print("\n========== EVENT ==========")
        print(json.dumps(event, indent=4))
        print("===========================\n")

        await job_queue.put(event)

        print("Queued Successfully ... \n")