import json
import collections
def analyze_log(filepath: str) -> dict:
    jsonl=[]
    with open(filepath,"r",encoding="utf-8") as f:
        for i in f:
            jsonl.append(json.loads(i))
    result={
        "total"=len(jsonl),
    }
    return result