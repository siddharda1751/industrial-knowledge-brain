import asyncio
from ingestion.watcher import start_watching
from ingestion.worker import worker
from services.service_manager import ServiceManager

FOLDER = "../KnowledgeBase"

async def main():
    services = ServiceManager()
    services.initialize()
    asyncio.create_task(worker(services))
    await start_watching(FOLDER)

if __name__ == "__main__":
    asyncio.run(main())