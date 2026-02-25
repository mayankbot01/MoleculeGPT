import os
import json
from typing import List, Dict, Any
from openai import OpenAI
from .tools import TOOL_MAP

class MinionAgent:
    def __init__(self, model: str = "gpt-4-turbo", system_prompt: str = None):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.history = []
        self.system_prompt = system_prompt or "You are a Minion, an autonomous AI agent designed for developer productivity."
        self.tools = [tool.get_schema() for tool in TOOL_MAP.values()]

    def run(self, task: str):
        self.history.append({"role": "system", "content": self.system_prompt})
        self.history.append({"role": "user", "content": task})

        while True:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.history,
                tools=self.tools,
                tool_choice="auto"
            )

            message = response.choices[0].message
            self.history.append(message)

            if not message.tool_calls:
                return message.content

            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)
                
                print(f"Executing tool: {tool_name} with args: {tool_args}")
                tool = TOOL_MAP.get(tool_name)
                if tool:
                    result = tool.execute(**tool_args)
                else:
                    result = f"Error: Tool {tool_name} not found."

                self.history.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_name,
                    "content": str(result)
                })
