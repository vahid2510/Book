
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

import nbformat
from nbclient import NotebookClient
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule

console = Console()


def execute_notebook(nb_path: Path, timeout: int = 180, kernel_name: Optional[str] = None) -> int:
    if not nb_path.exists():
        console.print(f"[red]Notebook not found:[/red] {nb_path}")
        return 2

    console.print(Panel.fit(f"Running notebook:\n[bold]{nb_path}[/bold]", border_style="green"))

    nb = nbformat.read(nb_path, as_version=4)
    client = NotebookClient(
        nb,
        timeout=timeout,
        kernel_name=kernel_name or "python3",
        allow_errors=True,
        record_timing=False
    )
    client.execute()

    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        out_list = cell.get("outputs", [])
        if not out_list:
            continue
        console.print(Rule(title=f"cell {i}"))
        for out in out_list:
            otype = out.get("output_type")
            if otype == "stream":
                text = out.get("text", "")
                if text:
                    console.print(Panel(text, title="stdout", border_style="cyan"))
            elif otype in {"display_data", "execute_result"}:
                data = out.get("data", {})
                text = data.get("text/plain") or data.get("text") or ""
                if text:
                    console.print(Panel(text, title="result", border_style="blue"))
                else:
                    console.print(Panel("Non-text output (image/HTML). Open in Jupyter to view.", title="result", border_style="blue"))
            elif otype == "error":
                ename = out.get("ename", "")
                evalue = out.get("evalue", "")
                tb = "\n".join(out.get("traceback", []))
                msg = f"{ename}: {evalue}\n{tb}"
                console.print(Panel(msg, title="error", border_style="red"))

    console.print(Panel.fit("[bold green]Done.[/bold green]"))
    return 0


def main():
    parser = argparse.ArgumentParser(
        prog="mech-eng",
        description="Run the bundled Jupyter notebook for the Mechanical Engineering course."
    )
    parser.add_argument(
        "--nb",
        default="notebooks/course.ipynb",
        help="Notebook path inside the installed package (default: notebooks/course.ipynb)",
    )
    parser.add_argument("--timeout", type=int, default=180, help="Cell execution timeout in seconds")
    args = parser.parse_args()

    here = Path(__file__).parent
    nb_path = (here / args.nb).resolve()

    code = execute_notebook(nb_path, timeout=args.timeout)
    raise SystemExit(code)
