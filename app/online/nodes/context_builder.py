from app.online.models import OnlineState


class ContextBuilderNode:

    def __call__(
        self,
        state: OnlineState
    ) -> OnlineState:

        return state