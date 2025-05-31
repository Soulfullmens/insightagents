from dotenv import load_dotenv
load_dotenv()
from rich import print
from agents.data_collector import DataCollectorAgent
from agents.insight_analyzer import InsightAnalyzerAgent
from agents.report_generator import ReportGeneratorAgent

import os
print(f"[bold cyan]Using Project:[/bold cyan] {os.getenv('GOOGLE_CLOUD_PROJECT')}")

def main():
    data_collector = DataCollectorAgent()
    print("[bold cyan][INFO][/bold cyan] DataCollectorAgent initialized.")
    data = data_collector.collect()
    print(f"[bold cyan][INFO][/bold cyan] Collected mock data: {data}")

    analyzer = InsightAnalyzerAgent()
    print("[bold cyan][INFO][/bold cyan] InsightAnalyzerAgent initialized.")
    insights = analyzer.analyze(data)  # ✅ Fixed variable name
    print(f"[bold cyan][INFO][/bold cyan] Insights: {insights}")

    reporter = ReportGeneratorAgent()
    print("[bold cyan][INFO][/bold cyan] ReportGeneratorAgent initialized.")
    reporter.generate(insights)  # ✅ Correct method name (was .store())
    print("[bold cyan][INFO][/bold cyan] Report generated successfully.")

if __name__ == "__main__":
    main()