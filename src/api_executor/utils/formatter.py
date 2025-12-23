from typing import Dict, Any
import click


def format_api_details(data: Dict[str, Any]) -> str:
    """Format API details for terminal output."""
    output = []
    output.append(click.style(f"\n{data['name']}", bold=True, fg="cyan"))
    output.append(f"  Full Name: {data['full_name']}")
    output.append(f"  Base URL: {data['base_url']}")
    output.append(f"  Description: {data['description']}\n")

    if "methods" in data:
        output.append(click.style("  Methods:", bold=True))
        for method in data["methods"]:
            output.append(f"\n    • {click.style(method['name'], fg='green')} ({method['method']})")
            output.append(f"      Endpoint: {method.get('endpoint', 'N/A')}")
            
            if "parameters" in method:
                output.append(click.style("      Parameters:", bold=True))
                for param in method["parameters"]:
                    param_line = f"        - {click.style(param['name'], fg='yellow')} ({param['type']})"
                    output.append(param_line)
                    if "description" in param:
                        output.append(f"          {param['description']}")
            
            if "response_format" in method:
                output.append(f"      Response: {method['response_format']}")

    return "\n".join(output)
