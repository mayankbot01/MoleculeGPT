# MoleculeGPT - Minion System Replica

MoleculeGPT is a high-performance replica of Stripe's Minion system, designed for developer productivity and automated task execution. It leverages advanced LLMs to act as an autonomous agent capable of browsing the web, editing code, and executing terminal commands.

## Features

- **Autonomous Agent**: Powered by state-of-the-art LLMs with a reasoning loop.
- **Tool Integration**: Built-in support for web browsing, shell execution, and file system operations.
- **Project Context Awareness**: Automatically indexes and understands your codebase.
- **Safe Execution**: Sandboxed environment for running untrusted code.

## Project Structure

- `minion/`: Core logic for the agent and tool definitions.
- `api/`: Backend API for communication between the agent and UI.
- `web/`: Frontend dashboard for monitoring and interacting with Minions.
- `main.py`: Main entry point for the CLI.

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up your API keys in `.env`.
3. Run the Minion:
   ```bash
   python main.py
   ```

## License

This project is licensed under the MIT License.
