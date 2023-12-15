"""Application middleware."""

import reflex as rx


class CloseSidebarMiddleware(rx.Middleware):
    """Middleware to make sure the sidebar closes when the page changes."""

    def preprocess(self, app, state, event):
        """Preprocess the event.

        Args:
            app: The app to apply the middleware to.
            state: The client state.
            event: The event to preprocess.
        """
        if event.name == rx.event.get_hydrate_event(state):
            state.get_substate(["state","state","navbar_state"]).sidebar_open = False
            state.get_substate(["state","state","index_state"]).show_c2a = True
