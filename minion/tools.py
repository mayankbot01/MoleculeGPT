import os
import subprocess
import requests
from bs4 import BeautifulSoup
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

class FileReadTool(BaseTool):
    def get_schema(self):
        return {
            "type": "function",
            "function": {
                "name": "read_file",
                "description": "Read content from a file.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Path to the file."}
                    },
                    "required": ["path"]
                }
            }
        }
    
    def execute(self, path: str):
        try:
            with open(path, "r") as f:
                return {"content": f.read()}
        except Exception as e:
            return {"error": str(e)}

class WebBrowseTool(BaseTool):
    def get_schema(self):
        return {
            "type": "function",
            "function": {
                "name": "browse_web",
                "description": "Browse a website and extract text content.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "url": {"type": "string", "description": "The URL to browse."}
                    },
                    "required": ["url"]
                }
            }
        }
    
    def execute(self, url: str):
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            for script in soup(["script", "style"]):
                script.decompose()
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = "
".join(chunk for chunk in chunks if chunk)
            return {"content": text[:5000]}
        except Exception as e:
            return {"error": str(e)}

TOOL_MAP = {
    "execute_shell": ShellTool(),
    "write_file": FileWriteTool(),
    "read_file": FileReadTool(),
    "browse_web": WebBrowseTool()
}
