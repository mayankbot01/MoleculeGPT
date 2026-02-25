import os
import subprocess
from typing import Dict, Any

class BaseTool:
    def get_schema(self) -> Dict[str, Any]:
        raise NotImplementedError
    
    def execute(self, **kwargs) -> Any:
        raise NotImplementedError

class ShellTool(BaseTool):
    def get_schema(self):
        return {
            "type": "function",
            "function": {
                "name": "execute_shell",
                "description": "Execute a shell command in the terminal.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "command": {"type": "string", "description": "The command to run."}
                    },
                    "required": ["command"]
                }
            }
        }
    
    def execute(self, command: str):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
            return {"stdout": result.stdout, "stderr": result.stderr, "exit_code": result.returncode}
        except Exception as e:
            return {"error": str(e)}

class FileWriteTool(BaseTool):
    def get_schema(self):
        return {
            "type": "function",
            "function": {
                "name": "write_file",
                "description": "Write content to a file.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Path to the file."},
                        "content": {"type": "string", "description": "Content to write."}
                    },
                    "required": ["path", "content"]
                }
            }
        }
    
    def execute(self, path: str, content: str):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                f.write(content)
            return {"status": "success", "path": path}
        except Exception as e:
            return {"error": str(e)}

TOOL_MAP = {
    "execute_shell": ShellTool(),
    "write_file": FileWriteTool()
}
