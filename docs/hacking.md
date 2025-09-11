# Hacking Edition

Agent Zero includes a special Docker image based on Kali Linux with additional tools and modified prompts tailored for cybersecurity research.

## Quick Start

```bash
docker pull frdel/agent-zero-run:hacking
docker run -p 50001:80 frdel/agent-zero-run:hacking
```

Open `http://localhost:50001` in your browser after the container starts.

The hacking edition shares the same configuration files as the regular version. Mount a data directory if you want persistent storage:

```bash
docker run -p 50001:80 -v /path/to/a0-data:/a0 frdel/agent-zero-run:hacking
```

## Custom Prompts

The hacking image sets `AGENT_PROMPTS_SUBDIR=hacking`, enabling prompts from `prompts/hacking/` to override defaults. You can modify these files to suit your workflow.
