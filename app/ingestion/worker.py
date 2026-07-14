from .queue__manager import job_queue
from ingestion.pipelines.create import CreatePipeline
from ingestion.pipelines.delete import DeletePipeline

async def worker(services):
    print("Worker Started ... \n")
    create_pipeline = CreatePipeline(services)
    delete_pipeline = DeletePipeline(services)

    while True:
        event = await job_queue.get()

        print("=" * 40)
        print("Worker Received Event")
        print(event)
        print("=" * 40)

        await route_event(event,create_pipeline, delete_pipeline)
        job_queue.task_done()

async def route_event(event,create_pipeline, delete_pipeline):
    event_type = event["event_type"]

    if event_type == "ADDED":
        print("Launching ADD pipeline ... \n")
        await create_pipeline.run(event)
    elif event_type == "MODIFIED":
        print("Launching MODIFY pipeline ... \n")
    elif event_type == "DELETED":
        print("Launching DELETE pipeline ... \n")
        await delete_pipeline.delete_file(event["resource_uri"])
    else:
        print(f"Unknown event type: {event_type}. No action taken.")
    