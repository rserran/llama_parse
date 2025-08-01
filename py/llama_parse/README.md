# LlamaParse

[![PyPI - Downloads](https://img.shields.io/pypi/dm/llama-parse)](https://pypi.org/project/llama-parse/)
[![GitHub contributors](https://img.shields.io/github/contributors/run-llama/llama_parse)](https://github.com/run-llama/llama_parse/graphs/contributors)
[![Discord](https://img.shields.io/discord/1059199217496772688)](https://discord.gg/dGcwcsnxhU)

LlamaParse is a **GenAI-native document parser** that can parse complex document data for any downstream LLM use case (RAG, agents).

It is really good at the following:

- ✅ **Broad file type support**: Parsing a variety of unstructured file types (.pdf, .pptx, .docx, .xlsx, .html) with text, tables, visual elements, weird layouts, and more.
- ✅ **Table recognition**: Parsing embedded tables accurately into text and semi-structured representations.
- ✅ **Multimodal parsing and chunking**: Extracting visual elements (images/diagrams) into structured formats and return image chunks using the latest multimodal models.
- ✅ **Custom parsing**: Input custom prompt instructions to customize the output the way you want it.

LlamaParse directly integrates with [LlamaIndex](https://github.com/run-llama/llama_index).

The free plan is up to 1000 pages a day. Paid plan is free 7k pages per week + 0.3c per additional page by default. There is a sandbox available to test the API [**https://cloud.llamaindex.ai/parse ↗**](https://cloud.llamaindex.ai/parse).

Read below for some quickstart information, or see the [full documentation](https://docs.cloud.llamaindex.ai/).

If you're a company interested in enterprise RAG solutions, and/or high volume/on-prem usage of LlamaParse, come [talk to us](https://www.llamaindex.ai/contact).

## Getting Started

First, login and get an api-key from [**https://cloud.llamaindex.ai/api-key ↗**](https://cloud.llamaindex.ai/api-key).

Then, make sure you have the latest LlamaIndex version installed.

**NOTE:** If you are upgrading from v0.9.X, we recommend following our [migration guide](https://pretty-sodium-5e0.notion.site/v0-10-0-Migration-Guide-6ede431dcb8841b09ea171e7f133bd77), as well as uninstalling your previous version first.

```
pip uninstall llama-index  # run this if upgrading from v0.9.x or older
pip install -U llama-index --upgrade --no-cache-dir --force-reinstall
```

Lastly, install the package:

`pip install llama-parse`

Now you can parse your first PDF file using the command line interface. Use the command `llama-parse [file_paths]`. See the help text with `llama-parse --help`.

```bash
export LLAMA_CLOUD_API_KEY='llx-...'

# output as text
llama-parse my_file.pdf --result-type text --output-file output.txt

# output as markdown
llama-parse my_file.pdf --result-type markdown --output-file output.md

# output as raw json
llama-parse my_file.pdf --output-raw-json --output-file output.json
```

You can also create simple scripts:

```python
import nest_asyncio

nest_asyncio.apply()

from llama_parse import LlamaParse

parser = LlamaParse(
    api_key="llx-...",  # can also be set in your env as LLAMA_CLOUD_API_KEY
    result_type="markdown",  # "markdown" and "text" are available
    num_workers=4,  # if multiple files passed, split in `num_workers` API calls
    verbose=True,
    language="en",  # Optionally you can define a language, default=en
)

# sync
documents = parser.load_data("./my_file.pdf")

# sync batch
documents = parser.load_data(["./my_file1.pdf", "./my_file2.pdf"])

# async
documents = await parser.aload_data("./my_file.pdf")

# async batch
documents = await parser.aload_data(["./my_file1.pdf", "./my_file2.pdf"])
```

## Using with file object

You can parse a file object directly:

```python
import nest_asyncio

nest_asyncio.apply()

from llama_parse import LlamaParse

parser = LlamaParse(
    api_key="llx-...",  # can also be set in your env as LLAMA_CLOUD_API_KEY
    result_type="markdown",  # "markdown" and "text" are available
    num_workers=4,  # if multiple files passed, split in `num_workers` API calls
    verbose=True,
    language="en",  # Optionally you can define a language, default=en
)

file_name = "my_file1.pdf"
extra_info = {"file_name": file_name}

with open(f"./{file_name}", "rb") as f:
    # must provide extra_info with file_name key with passing file object
    documents = parser.load_data(f, extra_info=extra_info)

# you can also pass file bytes directly
with open(f"./{file_name}", "rb") as f:
    file_bytes = f.read()
    # must provide extra_info with file_name key with passing file bytes
    documents = parser.load_data(file_bytes, extra_info=extra_info)
```

## Using with `SimpleDirectoryReader`

You can also integrate the parser as the default PDF loader in `SimpleDirectoryReader`:

```python
import nest_asyncio

nest_asyncio.apply()

from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader

parser = LlamaParse(
    api_key="llx-...",  # can also be set in your env as LLAMA_CLOUD_API_KEY
    result_type="markdown",  # "markdown" and "text" are available
    verbose=True,
)

file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(
    "./data", file_extractor=file_extractor
).load_data()
```

Full documentation for `SimpleDirectoryReader` can be found on the [LlamaIndex Documentation](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader.html).

## Examples

Several end-to-end indexing examples can be found in the examples folder

- [Getting Started](/docs/examples-py/parse/demo_basic.ipynb)
- [Advanced RAG Example](/docs/examples-py/parse/demo_advanced.ipynb)
- [Raw API Usage](/docs/examples-py/parse/demo_api.ipynb)

## Documentation

[https://docs.cloud.llamaindex.ai/](https://docs.cloud.llamaindex.ai/)

## Terms of Service

See the [Terms of Service Here](./TOS.pdf).

## Get in Touch (LlamaCloud)

LlamaParse is part of LlamaCloud, our e2e enterprise RAG platform that provides out-of-the-box, production-ready connectors, indexing, and retrieval over your complex data sources. We offer SaaS and VPC options.

LlamaCloud is currently available via waitlist (join by [creating an account](https://cloud.llamaindex.ai/)). If you're interested in state-of-the-art quality and in centralizing your RAG efforts, come [get in touch with us](https://www.llamaindex.ai/contact).
