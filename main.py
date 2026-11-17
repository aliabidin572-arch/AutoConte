
import gradio as gr

def autoconte_demo(topic):
    if not topic.strip():
        return "Masukkan topik sejarah terlebih dahulu."

    return f"""
AUTOCONTE - HISTORICAL CONTENT STUDIO

TOPIC:
{topic}

HOOK:
What really happened during {topic}?

SCRIPT:
Today, we explore the history of {topic}.

SCENE 1:
Historical introduction.

SCENE 2:
Main historical events.

SCENE 3:
Historical consequences.

FACT CHECK:
Historical facts must be verified.
"""

with gr.Blocks(title="AutoConte") as app:
    gr.Markdown("# AutoConte")
    gr.Markdown("AI Historical Shorts Content Studio")

    topic = gr.Textbox(
        label="Historical Topic",
        placeholder="Example: Battle of Narva 1944"
    )

    generate = gr.Button("Generate Content")
    output = gr.Textbox(label="Generated Content", lines=15)

    generate.click(
        autoconte_demo,
        inputs=topic,
        outputs=output
    )

app.launch(share=True)

