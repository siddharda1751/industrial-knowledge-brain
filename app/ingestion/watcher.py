from pathlib import Path
from watchfiles import awatch

from .dispatcher import EventDispatcher

import uuid
from datetime import datetime

dispatcher = EventDispatcher()

async def start_watching(folder_path):
    print(f"Watching folder: {folder_path}\n")

    async for changes in awatch(folder_path):
        for change, file in changes:
              event = {
                "event_id": str(uuid.uuid4()),
                "event_type": change.name.upper(),
                "source": "watcher",
                "resource_uri":str(Path(file).resolve()),
                "timestamp": datetime.now().isoformat(),
                "metadata": {}
            }
        await dispatcher.dispatch(event)