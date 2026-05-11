"""
MCP File System Integration Layer

This module implements the Model Context Protocol (MCP) design pattern 
for secure local file system orchestration, storage, and history retrieval.
"""

import json
import os


class MCPResearchStorage:
    def __init__(self, storage_path="data/research_history.json"):
        self.file_path = storage_path
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def save_research(self, topic, report):
        """
        Saves research reports to the local MCP-managed filesystem.
        """
        history = self.load_history()
        
        from datetime import datetime
        history.append({
            "topic": topic,
            "report": report,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        # Keep only the last 20 researches
        history = history[-20:]

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4)

    def load_history(self):
        """
        Retrieves historical reports from the MCP-managed storage layer.
        """
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except:
                return []
