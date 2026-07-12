from .queue__manager import job_queue

async def worker():
    print("Worker Started ... \n")

    while True:
        event = await job_queue.get()

        print("=" * 40)
        print("Worker Received Event")
        print(event)
        print("=" * 40)

        route_event(event)
        job_queue.task_done()

def route_event(event):
    event_type = event["event_type"]

    if event_type == "ADDED":
        print("Launching ADD pipeline ... \n")
    elif event_type == "MODIFIED":
        print("Launching MODIFY pipeline ... \n")
    elif event_type == "DELETED":
        print("Launching DELETE pipeline ... \n")
    else:
        print(f"Unknown event type: {event_type}. No action taken.")
    