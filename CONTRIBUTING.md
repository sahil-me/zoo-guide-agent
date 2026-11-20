<!---
Copyright 2026 Sahíl Sharma. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Contribute to Zoo Guide Agent

Everyone is welcome to contribute, and we value every contribution. Code contributions are not the only way to support the project. Improving agent reasoning workflows, MCP tool integrations, prompt instructions, Cloud Run deployment configurations, error handling, performance, architecture, security, testing, or documentation are all valuable ways to contribute to **Zoo Guide Agent**.

This project was developed as part of hands-on exploration into building tool-aware AI agents with Google Agent Development Kit (ADK), Model Context Protocol (MCP) servers (`mcp-on-cloudrun`), Gemini models, and serverless deployment on Google Cloud Run. Contributions that improve agent accuracy, tool reliability, maintainability, and practical cloud-native AI agent patterns are especially welcome.

If you find this project helpful, consider sharing it with others, referencing it in your blogs or projects, discussing it on social platforms, or simply giving the repository a ⭐️ to support the project and the community.

**However you choose to contribute, please be mindful and respect our [Code of Conduct](https://github.com/sahil-me/zoo-guide-agent/blob/main/CODE_OF_CONDUCT.md).**

## Ways to contribute

There are several ways you can contribute to **Zoo Guide Agent**.

- **ADK Agent Workflows & Prompts:** Enhance agent instructions, reasoning steps, routing logic, and multi-turn zoo guide responses.
- **MCP Tool-Calling Integration:** Add, test, or refine MCP tools and endpoints exposed via `mcp-on-cloudrun` (`server.py` and `local_mcp_call.py`).
- **Gemini Model Configuration:** Improve model selection, thinking/reasoning settings, structured outputs, and response reliability.
- **Cloud Run & Containerization:** Optimize `Dockerfile` builds, environment configuration, startup times, and Google Cloud Run deployment workflows.
- **Python & Dependency Management:** Maintain clean Python typing, async/sync execution, error handling, and `pyproject.toml` / `uv.lock` / `requirements.txt` consistency.
- **Performance Optimization:** Reduce tool-call latency, optimize container image size, and streamline local/remote MCP communication.
- **Security & Credential Handling:** Help ensure safe handling of API keys, Google Cloud credentials, `.env` isolation, and least-privilege access.
- **Testing:** Add or improve unit tests, MCP client/server tests, and end-to-end agent integration tests.
- **Documentation:** Improve the `README`, setup instructions, architecture diagrams, MCP/ADK walkthroughs, and contribution guides.

> All contributions are valuable to the project and its learning community. 🥰

## Submitting a bug-related issue or feature request

Feel free to open an issue when you encounter a bug or have an idea for improving **Zoo Guide Agent**. Include relevant error logs, reproduction steps, Python/`uv` versions, Google Cloud / ADK environment details, or MCP/Cloud Run configuration context when appropriate.

Please check the existing issues before creating a new one. This helps avoid duplicate reports and makes it easier to track existing problems.

### Did you find a bug?

**Zoo Guide Agent** becomes more reliable through community feedback, issue reporting, testing, and meaningful contributions.

Before reporting an issue, please make sure the bug has not already been reported under the repository's **Issues** section.

When submitting a bug report, please include the following information:
- Your operating system and development environment (e.g., Windows, macOS, Linux, Cloud Shell).
- Python version (`python --version`) and `uv` version (`uv --version`, if used).
- Execution target (local CLI/script, local MCP server, or deployed Google Cloud Run service).
- Steps to reproduce the issue.
- A short description of the expected behavior and what actually happened.
- Relevant error messages, stack traces, or Cloud Run / terminal logs.
- The affected component, such as `zoo_guide_agent` (`agent.py`), `mcp-on-cloudrun` (`server.py`, `local_mcp_call.py`), `Dockerfile`, or dependency files.
- Screenshots or terminal outputs, if applicable.
- Any other information that may help reproduce or understand the issue.

Please do not include **API keys**, **passwords**, **authentication tokens**, **service-account credentials**, `.env` **files**, **GCP project IDs/URLs with sensitive context**, or other **sensitive information** in an issue.

### Do you want a new feature?

If there is a new feature you'd like to see in **Zoo Guide Agent**, please open an issue and describe:

1. **Motivation**

   Explain the problem, limitation, or use case that the feature would address.

2. **Feature Description**

   Describe the proposed feature and how you would expect it to work from a user or caller perspective.

3. **ADK, MCP & AI Integration**

   If the feature affects AI or tool capabilities, explain how it should influence agent instructions, MCP tool schemas/handlers, model selection, or response formatting.

4. **Service & Project Architecture**

   If the feature affects `zoo_guide_agent`, `mcp-on-cloudrun`, or Cloud Run deployment, describe the expected changes to modules, endpoints, or configuration files.

5. **Implementation Details**

   If you have an implementation idea, architecture suggestion, or code snippet, feel free to include it.

6. **Additional References**

   If the feature is inspired by an external project, paper, design, or technical reference, please include the relevant link.

A clear and well-written feature request makes it easier to evaluate and discuss the proposal.

## Do you want to improve MCP tools and Cloud Run services?

The `mcp-on-cloudrun` component powers tool access and cloud hosting for the agent workflows.

You can contribute by:

- Adding new domain tools or refining existing MCP tool definitions and parameters.
- Improving input validation, error handling, and connection resilience in `server.py` and `local_mcp_call.py`.
- Optimizing container builds in `Dockerfile` and dependency resolution in `pyproject.toml`, `uv.lock`, and `requirements.txt`.
- Improving local-to-remote parity between local MCP testing and Cloud Run deployments.

When modifying MCP tools or prompts, ensure that outputs remain clean, accurate, and aligned with expected schemas and response formats.

## Do you want to improve ADK agent and reasoning logic?

Agents drive the conversational intelligence and tool orchestration of the application.

You can contribute by:

- Refining system instructions and examples for better tool selection and grounding.
- Improving error recovery when MCP tools or model calls fail or time out.
- Enhancing multi-turn context handling and response clarity for zoo guide queries.
- Ensuring clean separation between agent logic and external tool/service integrations.

## Do you want to improve testing and reliability?

Testing ensures the agent and MCP tools remain stable and easy to maintain.

You can contribute by:

- Adding unit tests for agent logic, tool handlers, and utility functions.
- Adding integration tests for local MCP calls (`local_mcp_call.py`) and server endpoints (`server.py`).
- Testing error handling when external services, credentials, or models are unavailable.
- Improving test coverage and reproducible setup instructions.

## Do you want to improve documentation?

We're always looking for improvements that make **Zoo Guide Agent** clearer and easier to understand.

You can contribute by:

- Fixing typos or grammatical errors.
- Improving the `README` and local/Cloud Run setup guides.
- Documenting the project architecture, folder structure (`mcp-on-cloudrun` and `zoo_guide_agent`), and MCP tool flow.
- Adding examples of running queries, testing MCP tools locally, and deploying to Cloud Run.

Documentation contributions are especially appreciated when they help new contributors understand the project, set up their environment, and get started safely.

## Fixing outstanding issues

If you notice an existing issue and have a fix in mind, feel free to **[start contributing](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)** and open a Pull Request.

### Making code changes

<details>
<summary><strong>Step-by-step contribution workflow</strong></summary>

#### 1. Fork the repository

Go to the [Zoo Guide Agent repository](https://github.com/sahil-me/zoo-guide-agent) on GitHub and click the **Fork** button.

#### 2. Clone your forked repository

Replace `<username>` with your GitHub username.

```bash
git clone https://github.com/<username>/zoo-guide-agent.git
```

Navigate into the project directory:

```bash
cd zoo-guide-agent
```

#### 3. Create a new branch

Create a separate branch for your feature or bug fix.

```bash
git checkout -b feature/your-feature-name
```

For a bug fix, you can use a name such as:

```bash
git checkout -b fix/issue-description
```

#### 4. Ensure Python and `uv` (or virtual environment) are installed

Verify your Python installation:

```bash
python --version
```

If using `uv`, verify it is installed:

```bash
uv --version
```

#### 5. Install dependencies

Sync or install dependencies for the workspace or target component (`mcp-on-cloudrun` / `zoo_guide_agent`):

```bash
uv sync
```

Or using `pip` with a virtual environment:

```bash
python -m venv .venv

# On Windows (PowerShell): .venv\Scripts\Activate.ps1

# On macOS/Linux: source .venv/bin/activate

pip install -r zoo_guide_agent/requirements.txt
```

#### 6. Configure environment variables

If running agents, MCP tools, or Google Cloud / Vertex AI / Gemini workflows, configure your local `.env` file or environment variables according to the project's instructions (keeping `.env` untracked).

> Never commit API keys, tokens, `.env` files, service account JSON files, or secrets to the repository.

#### 7. Run the project locally

Run or test the MCP server, local client script, or agent workflow to verify everything works before making changes:

```bash
python mcp-on-cloudrun/local_mcp_call.py
```

#### 8. Make your changes

- Develop the feature or fix the issue.
- Follow the existing project structure, Python naming conventions, and clean code practices.
- Keep changes focused and maintainable.
- Avoid unrelated modifications.
- Test your changes thoroughly across relevant components.

#### 9. Run tests

Run your test suite or verification scripts to ensure no regressions were introduced:

```bash
pytest
```

Verify that the agent and MCP tools behave as intended and handle errors gracefully.

#### 10. Commit your changes

From the repository root, review the files you have changed and stage only the intended changes.

```bash
git status
git add <file-or-directory>
git commit -m "Describe your change"
```

Avoid committing `.env` files, virtual environments (`.venv/`), `__pycache__/`, build artifacts, or unrelated modifications.

#### 11. Push to your fork

```bash
git push origin feature/your-feature-name
```

Replace the branch name if you used a different one.

#### 12. Create a Pull Request

Open your fork on GitHub and create a Pull Request targeting the original Zoo Guide Agent repository.

In your Pull Request description:
- Explain what you changed.
- Reference any related issue.
- Describe agent reasoning, MCP tool, or Cloud Run configuration updates.
- Include logs, test outputs, or screenshots when appropriate.

#### 13. Address feedback

If maintainers leave comments or request changes, address the feedback and push the required updates to your branch.

Thank you for taking the time to review and improve the project!

</details>

## Contribution Guidelines

To keep the project maintainable and welcoming:
- Keep Pull Requests focused on a single feature, fix, or improvement.
- Avoid unnecessary changes to unrelated files.
- Follow existing Python style guidelines and project conventions.
- Test changes locally before submitting a Pull Request.
- Keep API keys, credentials, `.env` files, and sensitive configuration out of the repository.
- Provide clear commit messages and Pull Request descriptions.
- Be respectful and constructive when reviewing or discussing contributions.

## I want to become a maintainer of the project. How do I get there?

**Zoo Guide Agent** is a learning and demonstration project focused on building tool-enabled AI agents with Google ADK, MCP servers, Gemini models, and Google Cloud Run.

Contributors interested in improving agent workflows, MCP integrations, cloud deployment configurations, testing, documentation, and architecture are welcome.

If you are interested in contributing at a deeper level, consistently submitting meaningful improvements, reviewing Pull Requests, improving documentation, or helping maintain the project, feel free to get involved and collaborate.

Thank you for contributing to **Zoo Guide Agent**! 🦁🐧🐻
