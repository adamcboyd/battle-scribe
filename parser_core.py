import re
import json

def parse_transcript(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    parsed_events = []
    for line in lines:
        line = line.strip()
        if not line:
            continue

        speaker_match = re.match(r"^(DM|Player):\s*(.*)", line)
        if speaker_match:
            role, content = speaker_match.groups()
            event = {
                "speaker": role,
                "text": content,
                "inferred_action": infer_action(content),
                "targets": infer_targets(content)
            }
            parsed_events.append(event)

    return parsed_events

def infer_action(text):
    text = text.lower()
    if "roll" in text:
        return "roll"
    elif "attack" in text or "swing" in text:
        return "attack"
    elif "damage" in text:
        return "damage"
    elif "cast" in text:
        return "cast spell"
    elif "misses" in text:
        return "miss"
    elif "hits" in text:
        return "hit"
    elif "dies" in text or "dead" in text:
        return "death"
    return "narration"

def infer_targets(text):
    targets = []
    goblin_match = re.findall(r"goblin|orc|troll|player|you", text, re.IGNORECASE)
    if goblin_match:
        targets.extend(goblin_match)
    return targets
