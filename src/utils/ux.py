from langchain.messages import AIMessage, ToolMessage
from enum import StrEnum
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

class MessageTypes(StrEnum):
    AI_MESSAGE = "ai_message"
    TOOL_MESSAGE = "tool_message"
    SYSTEM_MESSAGE = "system_message"

MESSAGE_STYLES = {
    MessageTypes.AI_MESSAGE: {
        "title": "🤖 Agent Messages",
        "style": "bold cyan",
        "border": "cyan",
    },
    MessageTypes.TOOL_MESSAGE: {
        "title": "🛠 Tool Message",
        "style": "bold yellow",
        "border": "yellow",
    },
    MessageTypes.SYSTEM_MESSAGE: {
        "title": "⚙️ System Message",
        "style": "bold magenta",
        "border": "magenta",
    },
}

def extract_tool_message(messages: list[AIMessage | ToolMessage]) -> ToolMessage | None:
    for message in reversed(messages):
        if isinstance(message, ToolMessage):
            return message.content
    return None

def extract_ai_message(messages: list[AIMessage | ToolMessage]) -> str | None:
    for message in reversed(messages):
        if isinstance(message, AIMessage):
            return message.content
    return None

def it_prints_if_not_none(header: str, value: any):
    if value is not None:
        print(f"{header}:\n{value}\n")

def printify(
    message: str,
    message_type: MessageTypes,
    *,
    expand: bool = True
):
    style_config = MESSAGE_STYLES.get(message_type)

    # Fallback safety
    if not style_config:
        console.print(message)
        return

    text = Text(message, style=style_config["style"])

    panel = Panel(
        text,
        title=style_config["title"],
        border_style=style_config["border"],
        expand=expand,
    )

    console.print(panel)
