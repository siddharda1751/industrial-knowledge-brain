from anyio import Path
from watchfiles import watch

from dispatcher import EventDispatcher

import uuid
from datetime import datetime

dispatcher = EventDispatcher()

def start_watching(folder_path):
    print(f"Watching folder: {folder_path}\n")

    for changes in watch(folder_path):
        for change, file in changes:
              event = {
                "event_id": str(uuid.uuid4()),
                "event_type": change.name.upper(),
                "source": "watcher",
                "resource_uri": str(Path(file).resolve()),
                "timestamp": datetime.now().isoformat(),
                "metadata": {}
            }
        dispatcher.dispatch(event)