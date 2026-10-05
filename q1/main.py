import json
from collections import Counter
def analyze_log(filepath: str) -> dict:
    jsonl=[]
    try:
        with open(filepath,"r",encoding="utf-8") as f:
            for i in f:
                try:
                    jsonl.append(json.loads(i))
                except(json.JSONDecodeError):
                    pass
    except(FileNotFoundError):
        pass
    by_level=Counter(x.get("level") for x in jsonl)
    by_user=Counter(x.get("user") for x in jsonl)
    error=[x for x in jsonl if x["level"]=="ERROR"]
    result={
        "total":len(jsonl),
        "by_level":dict(by_level),
        "by_user":dict(by_user),
        "last_error":error[-1].get("message") if error else None
    }
    return result
print(analyze_log("error.jsonl"))