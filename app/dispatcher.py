import json
from dataclasses import asdict

class EventDispatcher:
    def dispatch(self, event):

        print("\n========== EVENT ==========")
        print(json.dumps(event, indent=4))
        print("===========================\n")