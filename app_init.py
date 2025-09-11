"""Simple entry point to launch the Agent Zero Web UI."""
from run_ui import run
from python.helpers import runtime, dotenv

if __name__ == "__main__":
    runtime.initialize()
    dotenv.load_dotenv()
    run()
