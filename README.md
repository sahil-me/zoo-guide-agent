# 🤖 Zoo Guide Agent 🐻🐘🦁🐧

https://github.com/user-attachments/assets/14855b8e-f39b-497c-90bc-f3ac24d85031

> 🎥 Watch **Zoo Guide Agent** in action! 🐾

> [!CAUTION]
> The Cloud Run deployment is currently unavailable because the Google Cloud project has exhausted its available credits. The project was previously deployed and tested successfully on Google Cloud Run.

---

## Table of Contents

- [Introduction](#introduction)
- [Architecture Diagram](#architecture-diagram)
- [Project Structure](#project-structure)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Application Workflow](#application-workflow)
- [Screenshots](#screenshots)
- [Generative AI Capabilities & Integration](#generative-ai-capabilities--integration)
- [AI-Assisted Development](#ai-assisted-development)
- [Google Skills Challenge Lab Reference](#google-skills-challenge-lab-reference)
- [Future Enhancements](#future-enhancements)
- [Resources](#resources)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Introduction

**Zoo Guide Agent** is a tool-aware AI agent application developed as part of hands-on Google Cloud and generative AI learning experiences. It pairs a conversational zoo guide agent (`zoo_guide_agent`) with a Model Context Protocol (MCP) server component (`mcp-on-cloudrun`), powered by **Google Agent Development Kit (ADK)** and **Gemini models**, with containerized deployment on **Google Cloud Run**.

The project explores how to build interactive AI assistants capable of invoking external MCP tools and cloud services to answer zoo-related and general discovery queries (such as locating animals like penguins or exploring exhibit details) with structured, reliable responses.

The repository organizes the agent implementation, MCP server/client modules, containerization configuration, and dependency specifications into a clean, reproducible workspace ready for local testing and serverless cloud deployment.

The project demonstrates practical concepts in agent orchestration, Model Context Protocol (MCP) tool integration, prompt design, Python dependency management with `uv` and `pip`, and containerized Cloud Run deployment.

This repository documents my implementation and learning with Google Cloud Generative AI, ADK, MCP servers, and Cloud Run workflows, including project structure, supporting modules, and learning resources.

---

## Architecture Diagram

The following diagram illustrates the architecture of **Zoo Guide Agent**, connecting the agent workflow with MCP tools and Google Cloud services:

```mermaid
flowchart TD
    U["User / Client Prompt"] -->|" Query "| A["Zoo Guide Agent (ADK)<br/>tour_guide_workflow"]

    A --> G["Model<br/>Gemini"]
    A --> M["MCP Client / Tool Call"]
    A --> BT["Built-in Tools<br/>(Wikipedia / Google Search)"]

    subgraph MCPSvc ["mcp-on-cloudrun (Google Cloud Run)"]
        M -->|" Streamable-HTTP /mcp "| S["FastMCP Server<br/>(server.py)"]
        S --> T["Zoo Animal Tools<br/>(fetch_animals_by_species, etc.)"]
    end

    BT -->|" Tool results "| A
    T -->|" Tool results "| A
    G <-->|" Reasoning & synthesis "| A
    A -->|" Final response "| U

    classDef user fill:#e8f0fe,stroke:#4285f4,color:#202124
    classDef app fill:#e6f4ea,stroke:#34a853,color:#202124
    classDef gcp fill:#fef7e0,stroke:#f9ab00,color:#202124
    classDef tool fill:#fce8e6,stroke:#ea4335,color:#202124
    classDef agent fill:#fef9e7,stroke:#f9ab00,color:#202124

    class U user
    class S,CR app
    class G,MCPSvc gcp
    class A agent
    class M,T,BT tool
```

> [!NOTE]
> This diagram provides a high-level overview of the agent reasoning loop, MCP tool execution, and Google Cloud Run hosting architecture.

### Architecture Overview

1. **User / Client Prompt**
   - Sends natural language zoo guide questions and prompts (such as locating animals or exhibit details) to the agent workflow.

2. **Zoo Guide Agent (`tour_guide_workflow`)**
   - Orchestrates multi-step reasoning, sub-agent routing (`greeter`, `comprehensive_researcher`, `response_formatter`), and tool selection using `agent.py` and Gemini models.

3. **MCP Server & Tool Integration (`mcp-on-cloudrun`)**
   - Exposes zoo animal tools via Model Context Protocol (`server.py` and `local_mcp_call.py`) alongside built-in tools (`wikipedia`, `google_search`) for local testing and remote execution.

4. **Google Cloud Run & Gemini**
   - Hosts containerized services (`Dockerfile`) on Google Cloud Run (`europe-west4`) while Gemini provides model reasoning and response synthesis from tool outputs.
  
---

## Project Structure

The repository organizes the workspace directory, MCP server module, ADK agent package, and project governance files into a clean layout.

```text
zoo-guide-agent/                                   # Repository root directory
├── zoo_guide_agent/                               # Workspace project folder
│   ├── mcp-on-cloudrun/                           # MCP server, local client script, and container setup
│   │   ├── Dockerfile                             # Container build configuration for Cloud Run
│   │   ├── local_mcp_call.py                      # Local test/invocation client for MCP tool calls
│   │   ├── pyproject.toml                         # Project metadata and `uv` / Python dependencies
│   │   ├── server.py                              # FastMCP server implementation and zoo animal tools
│   │   └── uv.lock                                # Locked dependency versions for reproducible builds
│   │
│   ├── zoo_guide_agent/                           # Core Zoo Guide ADK Agent package
│   │   ├── __init__.py                            # Package initialization module
│   │   ├── agent.py                               # Multi-agent workflow, instructions, and tool wiring
│   │   └── requirements.txt                       # Pip dependency list for the ADK agent environment
│   │
│   └── README-cloudshell.txt                      # Default Google Cloud Shell environment reference file
│
├── .gitignore                                     # Excludes secrets, caches, virtual envs, and OS files
├── CODE_OF_CONDUCT.md                             # Community conduct guidelines
├── CONTRIBUTING.md                                # Contribution workflows and guidelines
├── LICENSE                                        # Open-source license terms (Apache-2.0)
├── README.md                                      # Project documentation
└── SECURITY.md                                    # Security vulnerability reporting policy
```

> [!NOTE]
> This tree mirrors the exact repository structure on GitHub. Refer to `zoo_guide_agent/mcp-on-cloudrun/` and `zoo_guide_agent/zoo_guide_agent/` for component implementations.

### Key Components

- **`zoo_guide_agent/mcp-on-cloudrun/`** — Contains the FastMCP server (`server.py`), local MCP test script (`local_mcp_call.py`), `Dockerfile`, `pyproject.toml`, and `uv.lock`.
- **`zoo_guide_agent/zoo_guide_agent/`** — Contains the ADK sequential agent workflow (`agent.py`), package initializer (`__init__.py`), and `requirements.txt`.
- **`README-cloudshell.txt`** — Default Cloud Shell workspace readme included from the lab environment.
- **`.gitignore`** — Excludes `.env` files, credentials, virtual environments (`.venv/`), and Python caches (`__pycache__/`) from version control.
- **`CONTRIBUTING.md, CODE_OF_CONDUCT.md, and SECURITY.md`** — Outline contribution standards, community conduct, and security-reporting guidelines.

---

## Features

- **Conversational Zoo Guide Agent:** Answers zoo and animal discovery queries with structured, helpful context.
- **Model Context Protocol (MCP) Integration:** Connects agent workflows with MCP tools via `server.py` and `local_mcp_call.py`.
- **Local & Cloud Run Execution Support:** Supports testing locally while packaging cleanly for Google Cloud Run with Docker.
- **Reproducible Dependency Management:** Includes `pyproject.toml`, `uv.lock`, and `requirements.txt` for consistent environment setup.
- **Clean Secret & Cache Hygiene:** Configured with `.gitignore` to prevent accidental commits of `.env` files, credentials, or build/cache artifacts.
- **Modular Agent & Tool Separation:** Keeps `zoo_guide_agent` and `mcp-on-cloudrun` cleanly separated for easier maintenance and extension.

> [!NOTE]
> Actual runtime behavior depends on valid Google Cloud credentials, enabled APIs, allowed models, and proper environment configuration.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language for agent logic and MCP server/client code |
| **Google Agent Development Kit (ADK)** | Agent orchestration and tool-calling framework |
| **Model Context Protocol (MCP)** | Standardized tool interface between agents and external capabilities |
| **Gemini Models & Vertex AI** | Core LLM reasoning, instruction following, and response generation |
| **Google Cloud Run** | Serverless container hosting platform for cloud deployment |
| **`uv` & `pip`** | Python package and lockfile/environment dependency management |
| **Docker** | Containerization of application and MCP server components |
| **Git & GitHub** | Version control and source code hosting |

> [!NOTE]
> The table describes the technologies and patterns reflected in the project implementation.

---

## Application Workflow

**Zoo Guide Agent** is structured around clear environment setup, MCP tool orchestration, sequential agent execution, and response synthesis

### 1️⃣ Environment & Dependency Setup

- Configure required environment variables (such as Google Cloud project ID, region, or model settings) in a local `.env` file while keeping `.env` out of version control.
- Install dependencies using `uv sync` (in `zoo_guide_agent/mcp-on-cloudrun/`) or `pip install -r zoo_guide_agent/zoo_guide_agent/requirements.txt`.

### 2️⃣ MCP Server & Local Testing

- Run or verify MCP tool execution using `zoo_guide_agent/mcp-on-cloudrun/server.py` and `zoo_guide_agent/mcp-on-cloudrun/local_mcp_call.py`.
- Confirm tool schemas, responses, and error handling work as expected.

### 3️⃣ Agent Query & Tool Routing

- Send a prompt to the agent (for example, `"Where can I find penguins?"`) via `adk web` or Antigravity CLI.
- The sequential agent workflow (`tour_guide_workflow` with `greeter`, `comprehensive_researcher`, and `response_formatter`) and Gemini model evaluate the request and invoke MCP zoo tools (`fetch_animals_by_species`, `fetch_animal_details`) along with built-in tools (`wikipedia`, `google_search`) when needed.

### 4️⃣ Containerization & Cloud Run Deployment

- Build the container image using `zoo_guide_agent/mcp-on-cloudrun/Dockerfile`.
- Deploy services to Google Cloud Run (such as `coding-zoo-mcp-server` and `coding-zoo-tour-guide` in `europe-west4`) with required environment configuration and IAM permissions.

### 5️⃣ Response Synthesis

- Tool outputs are returned to the agent and Gemini model, then synthesized into a structured, conversational response for the user.

--- 

## Screenshots

This section showcases **Zoo Guide Agent** in action, including CLI/agent interactions, MCP server/client runs, and Google Cloud / Cloud Run views.

### Agent Development Kit (ADK) Web UI

<img width="1366" height="768" alt="Agent Development Kit (ADK)" src="https://github.com/user-attachments/assets/ce4b810b-bf22-430f-a7c1-cd5af52df049" />
<img width="1366" height="768" alt="Agent Development Kit (ADK) Web UI" src="https://github.com/user-attachments/assets/14c86f7e-05cd-44d4-abdd-b2937cd974db" />

### Google Cloud Console Dashboard

<img width="1366" height="768" alt="Google Cloud Console Dashboard" src="https://github.com/user-attachments/assets/9b30b17b-eb6d-4e50-b8d2-bca24a6d5497" />

### Cloud Shell Terminal

<img width="1366" height="768" alt="ADK Agent and MCP Tool Execution Logs" src="https://github.com/user-attachments/assets/4d053070-f89e-4f11-911b-9780137de475" />
<img width="1366" height="768" alt="Cloud Run Deployment in Progress" src="https://github.com/user-attachments/assets/b15a81d6-4734-4724-a433-83bd64c53f56" />
<img width="1366" height="768" alt="Cloud Run Deployment Complete and Service URL" src="https://github.com/user-attachments/assets/21ae24a5-fa8e-4812-a0aa-bb95d4a28813" />
<img width="1366" height="768" alt="Python Dependency Installation - 1" src="https://github.com/user-attachments/assets/2706042a-f4cf-45f0-9c47-bb5dd980ac51" />
<img width="1366" height="768" alt="Python Dependency Installation - 2" src="https://github.com/user-attachments/assets/763ee8ac-d587-4373-91ec-b26524829a88" />
<img width="1366" height="768" alt="Python Dependency Installation - 3" src="https://github.com/user-attachments/assets/07176118-a31f-4503-a3f2-41c884118da7" />
<img width="1366" height="768" alt="Local ADK Web Server Startup" src="https://github.com/user-attachments/assets/16e1f656-a9cc-44e6-b556-1888fda4936b" />
<img width="1366" height="768" alt="Local ADK Web Server shut down" src="https://github.com/user-attachments/assets/d7a47e7e-4f34-4524-84c5-4c6d4e8702df" />

### ADK Agent Workflow Graph

<img width="551" height="215" alt="ADK Sequential Agent Workflow Graph - Response Formatter Active" src="https://github.com/user-attachments/assets/10e99b81-a9bb-4985-a1ff-87b0872396a7" />
<img width="555" height="214" alt="ADK Sequential Agent Workflow Graph - Comprehensive Researcher Active" src="https://github.com/user-attachments/assets/3cf72861-73c2-41eb-805e-b9e854f5d927" />

### FastMCP 2.0 Server

<img width="1366" height="768" alt="FastMCP 2.0 Zoo Animal Data MCP Server Running on HTTP" src="https://github.com/user-attachments/assets/db4e78af-476f-4aaa-b7d4-5d147d171573" />
<img width="1366" height="768" alt="FastMCP Server Handling CallToolRequest and ListToolsRequest" src="https://github.com/user-attachments/assets/d95fe84e-be2a-4612-9edd-9e1f1d6d9214" />

### Antigravity CLI & MCP Tool Execution

<img width="1366" height="768" alt="Antigravity CLI Active MCP Servers and Zoo Remote Tools" src="https://github.com/user-attachments/assets/e38e723a-84fb-4c51-9733-3067ec590e1e" />
<img width="1366" height="767" alt="Antigravity CLI Querying Penguins via Zoo Remote MCP Tool" src="https://github.com/user-attachments/assets/1a3035fa-696f-471a-afd5-a749673c7acf" />
<img width="1366" height="768" alt="Antigravity CLI Slash Command and Lion Zoo Information Output" src="https://github.com/user-attachments/assets/cf4644cf-70b9-407d-9d16-fc824e60e728" />

### Project Source Code

<img width="1366" height="768" alt="Project Source Code - zoo_guide_agent/agent.py" src="https://github.com/user-attachments/assets/bcb8b66b-ec3a-478f-b74a-20f0f05c869c" />
<img width="1366" height="768" alt="Project Source Code - mcp-on-cloudrun/server.py" src="https://github.com/user-attachments/assets/694c13b6-db1b-48d4-958e-538ea516dbce" />

### ADK Web UI — Agent Conversations, Traces & Events

#### Bears Query

<img width="1366" height="768" alt="Bears Query - 1" src="https://github.com/user-attachments/assets/61ba1fa7-f730-4a19-9dcc-aec02c02b954" />
<img width="1366" height="768" alt="Bears Query - 2" src="https://github.com/user-attachments/assets/0341cce7-8a08-470a-9ae9-61f7e2f11e9e" />
<img width="1366" height="768" alt="Bears Query - 3" src="https://github.com/user-attachments/assets/397a2919-7715-48aa-9dba-62256385a102" />
<img width="1366" height="768" alt="Bears Query - 4" src="https://github.com/user-attachments/assets/6320e5da-dd99-4213-8a81-2ff06ce439c6" />
<img width="1366" height="768" alt="Bears Query - 5" src="https://github.com/user-attachments/assets/15125814-ccaf-4f74-844f-317aebc72525" />
<img width="1366" height="768" alt="Bears Query - 6" src="https://github.com/user-attachments/assets/8fa9d888-a34d-4ce4-b1ad-07e91005a885" />
<img width="1366" height="768" alt="Bears Query - 7" src="https://github.com/user-attachments/assets/c6dba5bc-7da6-49ad-9ad1-90b5ceb65b17" />

#### Elephants Query

<img width="1366" height="766" alt="Elephants Query - 1" src="https://github.com/user-attachments/assets/82880618-ad67-45a2-b0f3-ecb062d32d94" />
<img width="1366" height="768" alt="Elephants Query - 2" src="https://github.com/user-attachments/assets/233f7375-a5cc-4450-8531-8fdbdef2bc04" />
<img width="1366" height="768" alt="Elephants Query - 3" src="https://github.com/user-attachments/assets/5ccdd9fc-15ef-41fd-9988-42d7905d3c3c" />
<img width="1366" height="767" alt="Elephants Query - 4" src="https://github.com/user-attachments/assets/cd242b48-d738-4a7f-a00f-a101ed63725c" />
<img width="686" height="462" alt="Elephants Query - 5" src="https://github.com/user-attachments/assets/df6f9bb1-6897-485c-b72f-77a97a72f517" />
<img width="682" height="606" alt="Elephants Query - 6" src="https://github.com/user-attachments/assets/05fc536f-8369-4b75-8829-eba146352ab2" />

#### Tigers Query

<img width="1366" height="768" alt="Tigers Query - 1" src="https://github.com/user-attachments/assets/68048055-6d33-4e0b-a4b8-48e95b2afad7" />
<img width="1366" height="768" alt="Tigers Query - 2" src="https://github.com/user-attachments/assets/9cc4eaea-6486-4b43-ac7b-67c4edccd743" />
<img width="1366" height="768" alt="Tigers Query - 3" src="https://github.com/user-attachments/assets/13887ccf-0372-4c0c-9873-d848caeeb7ac" />
<img width="1366" height="768" alt="Tigers Query - 4" src="https://github.com/user-attachments/assets/27d2c50a-ae66-48fb-8fde-2c7df4086518" />

### Google Cloud Run Service & Logs

<img width="1366" height="768" alt="Cloud Run Overview - active services" src="https://github.com/user-attachments/assets/6d5d161b-4b69-45f9-b740-e75ecb18169c" />
<img width="1366" height="768" alt="Cloud Run Services" src="https://github.com/user-attachments/assets/cb78f7f2-7cd4-4898-98fd-b7b42b66a8a7" />
<img width="1366" height="768" alt="Observability Metrics - 1" src="https://github.com/user-attachments/assets/d434c9b5-43f1-45d7-a8f3-2c583bcc418c" />
<img width="1366" height="768" alt="Observability Metrics - 2" src="https://github.com/user-attachments/assets/b518a5ae-db73-4f0d-9cc4-cdeda279d75b" />
<img width="1366" height="768" alt="Observability Metrics - 3" src="https://github.com/user-attachments/assets/61a03e5a-8acf-47a6-8663-1f7ec3e6920a" />
<img width="1366" height="768" alt="Observability Metrics - 4" src="https://github.com/user-attachments/assets/5990cf2d-5a61-41cc-8f48-8f61f141cc03" />
<img width="1366" height="768" alt="Service Logs" src="https://github.com/user-attachments/assets/103bb553-8831-41b6-9f65-4dd6b3f7bd82" />
<img width="1366" height="768" alt="Logs Explorer" src="https://github.com/user-attachments/assets/95a99268-2404-4c03-afc6-cd06fdb26ea0" />

---

## Generative AI Capabilities & Integration

### ADK Agent Orchestration

- Coordinates multi-step prompt evaluation, instruction following, and tool invocation within `zoo_guide_agent`.

### Model Context Protocol (MCP) Tools

- Exposes structured tools via `mcp-on-cloudrun` so the agent can interact with external capabilities cleanly.

### Gemini Model Reasoning

- Uses Gemini models to interpret user intent, synthesize tool results, and generate accurate, conversational responses.

---

## AI-Assisted Development

AI tools can support the development and exploration of modern generative AI applications by helping explain unfamiliar code, investigate implementation issues, understand agent architectures, and improve technical documentation.

During the development and learning process for **Zoo Guide Agent**, AI assistance was used to support activities such as:

- Exploring Google ADK agent structure, prompts, and MCP tool-calling workflows.
- Troubleshooting environment, model selection, and Cloud Run deployment details.
- Structuring repository documentation, `.gitignore rules`, and contribution guides.

AI-generated suggestions and code should be reviewed critically, verified against the actual implementation, and tested before being adopted.

---

## Google Skills Challenge Lab Reference

This project was developed alongside hands-on Google Cloud learning lab modules.

### Challenge Lab

**Build a Smart Cloud Application with Vibe Coding and MCP**

[Open the Google Skills lab](https://www.skills.google/paths/1282/course_templates/1459/labs/647519)

### Learning Context

The repository serves as a personal source-code project associated with this learning experience.

It provides a place to explore and document:
- Building AI agents with Google ADK and Gemini models.
- Integrating Model Context Protocol (MCP) tools (`mcp-on-cloudrun`).
- Managing Python dependencies with `uv` and `requirements.txt`.
- Containerizing and deploying agent/MCP services on Google Cloud Run.

For official learning objectives, instructions, and environment setup requirements, refer to the Google Skills lab link provided above.

---

## Future Enhancements

The following ideas could be considered for future versions of **Zoo Guide Agent**:

- **Rich Zoo Data & Exhibit Search:** Expand MCP tools with structured zoo map, animal habitat, feeding schedule, and exhibit lookup capabilities.
- **Automated Unit & Integration Tests:** Add `pytest` suites covering agent routing, MCP tool responses, and error edge cases.
- **Enhanced Observability & Logging:** Add structured logging and tracing across `zoo_guide_agent` and `mcp-on-cloudrun`.
- **Interactive Client Interface:** Build a dedicated web or mobile chat client on top of the Cloud Run backend.

> [!IMPORTANT]
> These are potential improvements, not claims that the features are already fully implemented.

---

## Resources

[![Model Context Protocol](https://img.shields.io/badge/MCP-Documentation-0F172A?logo=anthropic&logoColor=white)](https://modelcontextprotocol.io/)
[![Google ADK](https://img.shields.io/badge/Google%20ADK-Documentation-4285F4?logo=google)](https://adk.dev/)
[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Documentation-4285F4?logo=googlecloud)](https://cloud.google.com/docs)
[![Cloud Run](https://img.shields.io/badge/Cloud%20Run-Documentation-4285F4?logo=googlecloudrun)](https://cloud.google.com/run/docs)
[![Vertex AI](https://img.shields.io/badge/Vertex%20AI-Documentation-4285F4?logo=google)](https://cloud.google.com/vertex-ai/docs)
[![Gemini](https://img.shields.io/badge/Gemini-Documentation-8E75B2?logo=google)](https://ai.google.dev/gemini-api/docs)
[![uv](https://img.shields.io/badge/uv-Documentation-DE5FE9?logo=python&logoColor=white)](https://docs.astral.sh/uv/)
[![Docker](https://img.shields.io/badge/Docker-Documentation-2496ED?logo=docker&logoColor=white)](https://docs.docker.com/)
[![Python](https://img.shields.io/badge/Python-Documentation-3776AB?logo=python)](https://docs.python.org/3/)
[![Git](https://img.shields.io/badge/Git-Documentation-F05032?logo=git&logoColor=white)](https://git-scm.com/doc)
[![GitHub](https://img.shields.io/badge/GitHub-Documentation-181717?logo=github)](https://docs.github.com/)

---

## Disclaimer

**Zoo Guide Agent** is a learning and demonstration project associated with Google Cloud training.

The project utilizes third-party technologies and services, including Google Cloud Run, Vertex AI, Gemini, Model Context Protocol (MCP), and Python packages. The availability, functionality, pricing, and policies of external cloud services are subject to their respective providers' terms.

Access to Google Skills lab environments and temporary GCP projects expires after completion or quota exhaustion. A completed lab does not imply permanent public availability of the deployed backend service.

This repository is intended for educational and demonstration purposes. Do not commit API keys, access tokens, service-account credentials, `.env` files, or private configuration files to source control.

---

## Contributing

Contributions are welcome! If you would like to improve **Zoo Guide Agent**, fix a bug, add tests, or improve the documentation, please review the following guidelines:

- [Contributing Guide](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)

Please ensure that contributions are focused, documented, and tested where appropriate. Never include secrets or private configuration in issues, commits, or Pull Requests.

---

## License

This project is licensed under the **Apache License 2.0**.

See the [LICENSE](./LICENSE) file for details.

---

## Author

[**Sahil Sharma**](https://github.com/sahil-me)

Thank you for exploring **Zoo Guide Agent**! If you find the project useful, consider giving the repository a ⭐ to show your support.

