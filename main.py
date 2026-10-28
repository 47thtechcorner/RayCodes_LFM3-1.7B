import os
import json
import ollama

MODEL_NAME = "lfm3-1.7b"

def query_lfm3(system_prompt: str, user_prompt: str) -> str:
    """
    Directly invokes the registered LiquidAI/LFM3-1.7B model via Ollama.
    Assumes models/LFM3-1.7B-QAD-Q4_0.gguf is registered via 'ollama create lfm3-1.7b -f Modelfile'.
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages,
        options={
            "temperature": 0.1,
            "top_k": 50,
            "repeat_penalty": 1.1
        }
    )
    return response["message"]["content"]


def main():
    print("=" * 70)
    print("Liquid LFM3-1.7B: Production Edge Agent (Direct Ollama GGUF Execution)")
    print("=" * 70)
    
    os.makedirs("outputs", exist_ok=True)

    # Task 1: Privacy-First Browser Agent -> Interactive Action Flow HTML
    print("\n--- [Task 1] Running WebArena Browser Agent Sequencer ---")
    with open("inputs/web_store_page.html", "r", encoding="utf-8") as f:
        html_input = f.read()

    task1_system = """You are an autonomous WebArena browser controller.
Inspect the input web store DOM. Generate an interactive, self-contained HTML page representing the complete 4-step browser action sequence to search for the product and execute checkout.
Format with modern dark styling (#0b0f19), card containers, step numbers, target DOM selector tags, input values, and status pills. Output ONLY valid, raw HTML without markdown code blocks."""

    task1_user = f"Store Page DOM:\n{html_input}\n\nTask Goal: Search for the 2TB SSD, add to cart, and commit the checkout state."
    task1_html = query_lfm3(task1_system, task1_user)

    with open("outputs/task1_browser_agent_flow.html", "w", encoding="utf-8") as f:
        f.write(task1_html)
    print("-> Generated: outputs/task1_browser_agent_flow.html (Interactive Visual HTML)")

    # Task 2: 256K Legal & Policy Auditor -> Executive Contract Risk Matrix Markdown
    print("\n--- [Task 2] Running 256K Legal Compliance Auditor ---")
    with open("inputs/enterprise_cloud_msa.md", "r", encoding="utf-8") as f:
        legal_input = f.read()

    task2_system = """You are an expert contract compliance auditor.
Ingest the enterprise master services agreement. Audit the terms and output a structured Markdown report.
Include:
1. Executive summary quote with overall risk score.
2. Markdown table of Contract Risk Severity Matrix (Columns: Section & Clause, Severity Level [using red/yellow/green circle emojis], Risk Exposure Identified, Required Legal Remedy).
3. Diff block comparing the uncapped indemnity clause against a recommended mutual liability ceiling.
Output ONLY raw Markdown text."""

    task2_user = f"Contract Agreement Text:\n{legal_input}\n\nTask Goal: Identify uncapped liability exposure and provide counsel remediation."
    task2_md = query_lfm3(task2_system, task2_user)

    with open("outputs/task2_legal_audit_report.md", "w", encoding="utf-8") as f:
        f.write(task2_md)
    print("-> Generated: outputs/task2_legal_audit_report.md (Executive Risk Matrix Report)")

    # Task 3: Edge API Micro-Gateway -> Visual SVG Architecture Dispatch Graph
    print("\n--- [Task 3] Running Edge API Micro-Gateway Tool Calling ---")
    with open("inputs/customer_support_ticket.json", "r", encoding="utf-8") as f:
        ticket_input = f.read()

    task3_system = """You are an edge micro-gateway routing customer service events.
Parse the ticket and generate a standalone SVG architecture dispatch graph (viewBox="0 0 780 240") showing:
1. Inbound Ticket node with caller ID and parsed refund amount.
2. LFM3 Inference node with resolved intent and confidence score.
3. REST API Dispatch node with endpoint POST /v1/finance/refunds and execution status.
Use dark modern styling (#0c1017 base, #8b5cf6 accents, #10b981 success nodes). Output ONLY valid raw SVG xml starting with <svg> and ending with </svg>."""

    task3_user = f"Inbound Ticket Payload:\n{ticket_input}\n\nTask Goal: Parse refund request and construct verified visual REST tool dispatch."
    task3_svg = query_lfm3(task3_system, task3_user)

    with open("outputs/task3_api_gateway_dispatch.svg", "w", encoding="utf-8") as f:
        f.write(task3_svg)
    print("-> Generated: outputs/task3_api_gateway_dispatch.svg (Visual Dispatch Graph SVG)")

    print("\n" + "=" * 70)
    print("All 3 LFM3 visual agent deliverables generated in outputs/ via Ollama!")
    print("=" * 70)

if __name__ == "__main__":
    main()
