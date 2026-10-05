import json
from collections import Counter
def analyze_log(filepath: str) -> dict:
    jsonl=[]
    with open(filepath,"r",encoding="utf-8") as f:
        for i in f:
            jsonl.append(json.loads(i))
    by_level=Counter(x.get("level") for x in jsonl)
    by_user=Counter(x.get("user") for x in jsonl)
    error=[x for x in jsonl if x["level"]=="ERROR"]
    result={
        "total":len(jsonl),
        "by_level":by_level,
        "by_user":by_user,
        "last_error":error[-1]["message"]
    }
    return result