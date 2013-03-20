import sublime, sublime_plugin
from datetime import date


class InsertDate(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if prefix == 'isoD':
            val = date.today().isoformat()
        return [(prefix, prefix, val)] if val else []
