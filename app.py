import beam

app = beam.App(
    name="hello-world",
    cpu=8,
    gpu="A10G",
    memory="32Gi",
    python_packages=[
        "langchain",
        "openai",
        "faiss-cpu",
        "unstructured",
        "tiktoken"
    ],
)

app.Trigger.RestAPI(
    inputs={"query": beam.Types.String()},
    outputs={"pred": beam.Types.String()},
    handler="run.py:handler",
)
