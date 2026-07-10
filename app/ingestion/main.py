import asyncio
from watcher import start_watching
from worker import worker

FOLDER = "../../KnowledgeBase"

async def main():
    asyncio.create_task(worker())
    await start_watching(FOLDER)

if __name__ == "__main__":
    asyncio.run(main())