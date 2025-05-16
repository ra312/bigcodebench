from datasets import load_dataset

# full dataset
ds = load_dataset("bigcode/bigcodebench", split="v0.1.4")

# dataset streaming (will only download the data as needed)
ds = load_dataset("bigcode/bigcodebench", split="v0.1.4")

ds = ds.rename_columns({
    "complete_prompt": "complete",
    "instruct_prompt": "instruct",
    "canonical_solution": "solution",
})

ds.to_json("test.jsonl", orient="records", lines=True)
