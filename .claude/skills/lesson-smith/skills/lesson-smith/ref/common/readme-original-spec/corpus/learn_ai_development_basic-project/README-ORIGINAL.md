---
description: "An introduction to building real AI applications instead of chat demos. Calling an LLM API is the easy part. The engineering starts when you need output your code can actually trust, your own documents in front of the model, and something that can carry a task across more than one step. Almost every company is pushing AI into a product right now, and without that layer you stay stuck copying demos and guessing which piece just broke. This course builds it from scratch, in Python you can run and break on the spot. You finish able to stand up an AI application of your own on your own documents, read how the products in this space are actually put together, and know where to go deeper next."
github_about: "Intro to AI app development with LangChain and Strands Agents. From raw API calls to RAG and agents, every concept as runnable Python."
---

# learn_ai_development_basic-project

It's getting hard to find a software job that doesn't touch AI somewhere, and the model itself is almost never the hard part. The difficulty lives in everything wrapped around the call: getting a response back in a shape the rest of your code can depend on, putting your own documents where the model can see them, and letting it keep working when the job takes more than a single step. There's a name for that work, AI engineering, and it's all this course is about.

What you walk away with is a working skeleton. It talks to models from more than one vendor. It hands back structured output you can validate instead of a blob of text you parse by hand. It answers questions from files you supply. It calls tools to grind through jobs that take several steps. That's the basic tier, and the aim is narrow on purpose: stop copying demos you don't understand, start knowing which layer just broke and where to go look. Everything more advanced is built on exactly this.

LangChain and Strands Agents are the frameworks here, but neither one gets treated as a black box. Every mechanism gets written by hand against the raw SDK first, so you meet the problem before you meet the abstraction that solves it, and only then does the framework come in and delete the boilerplate. All of it is Python you can `uv run` the moment you read it. Run it, break it, fix it. Nothing here is a wall of concepts with nothing to execute.
