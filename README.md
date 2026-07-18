**This is a simple coding agent harness built from scratch in Python using the [OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents).** 

I built it mainly as a learning experiment to understand what coding agents really are under the hood. It works perfectly fine for simpler tasks, but it *cannot* be trusted for production-level tasks, so use at your own risk!

The harness includes all the basic things you'd expect a coding agent to have, such as:
- A few basic functions/tools (for reading files, executing them, etc.)
- An Agentic™ feedback loop
- A system prompt

**Want to run it?** Doing so is very simple; just...
1. Install [uv](https://docs.astral.sh/uv/) if you don't have it already
2. Run `uv sync` in the root of the project directory
3. Rename `.env.example` to `.env`
4. Add your OpenRouter API key to `.env`
5. Run the agent using `uv run main.py "[your prompt here]"`

Note: the `calculator` directory is a sample working directory. Feel free to modify the corresponding variable in `config.py` as needed.