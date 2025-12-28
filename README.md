# natural-language-to-sql-example

In this Example i will explore how to use LLMs to translate natural requests into SQL.
I will use a MCP server endpoint which takes natural language requests, transfers them into SQL using a LLM and then returns a result.

## what you need


**Data**

I will use Soccer player data from kaggle and load it into a DB, so download the csv file from https://www.kaggle.com/datasets/zoeme1/football-player-stats-and-ml-predictions

**a LLM**

I will use a open Ollama in my example with an open AI model. You might take a different selection, then adapt your tools, otherwise install ollama from https://ollama.com/  and download within ollama https://ollama.com/library/gpt-oss.

**UV and python**

I use python for my example. In order to manage my python project, i use uv

Install UV

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## more links

some more links to have a look into:

- https://medium.com/@tbrck/llm-powered-function-calling-get-started-a-simple-example-in-python-7bdbd4563c0d
- https://machinelearningmastery.com/10-python-one-liners-for-calling-llms-from-your-code/
- https://platform.openai.com/docs/api-reference/chat/create?lang=python
- https://modelcontextprotocol.io/docs/develop/build-server
- https://www.uber.com/en-DE/blog/query-gpt/

## to be deleted later, here is what i have done

```

# Create a new directory for our project
uv init nl-to-sql-mcp-example
cd ./nl-to-sql-mcp-example/

# Create virtual environment and activate it
uv venv
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]" httpx

# Create our server file
touch nl-to-sql-mcp-example.py

# added code
# ...

# start the mcp server
uv run nl-to-sql-mcp-example.py

npx @modelcontextprotocol/inspector
```






