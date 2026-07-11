from app.online.models import OnlineState


class LLMNode:

    def __call__(
        self,
        state: OnlineState
    ) -> OnlineState:

        return state