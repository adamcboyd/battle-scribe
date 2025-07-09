import json
import os
import pandas as pd
import streamlit as st

# Load the parsed JSON data
output_file_path = "output/parsed_output.json"
if os.path.exists(output_file_path):
    with open(output_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    st.error("Parsed output file not found.")
    st.stop()

# Convert JSON data to a DataFrame
df = pd.DataFrame(data)

# Define color and emoji mappings for inferred actions
action_styles = {
    "roll": ("🎲", "#D1E8FF"),
    "damage": ("💥", "#FFE4B5"),
    "attack": ("⚔️", "#FFD1DC"),
    "death": ("💀", "#FFCCCC"),
    "narration": ("🗣️", "#F0F0F0"),
    "default": ("📜", "#FFFFFF"),
}

# Render each log entry with color and emoji
st.title("📝 Battle Scribe Log Viewer")
st.markdown("Visual output of parsed D&D-style combat logs")

for entry in df.itertuples():
    action = getattr(entry, "inferred_action", "default")
    emoji, bg_color = action_styles.get(action, action_styles["default"])
    speaker = getattr(entry, "speaker", "Unknown")
    text = getattr(entry, "text", "")
    
    st.markdown(
        f"""
        <div style="background-color: {bg_color}; padding: 10px; border-radius: 5px; margin-bottom: 5px;">
            <strong>{emoji} {speaker}:</strong> {text}
        </div>
        """,
        unsafe_allow_html=True
    )
