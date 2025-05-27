"""
main.py – Orchestrates the InsightAgents pipeline:
1. Collects data
2. Analyzes insights
3. Generates & logs reports to BigQuery
"""

from agents.data_collector import DataCollectorAgent
from agents.insight_analyzer import InsightAnalyzerAgent
from agents.report_generator import ReportGeneratorAgent

def run_pipeline():
    print("\n🚀 Starting InsightAgents Pipeline...\n")

    # Step 1: Initialize agents
    collector = DataCollectorAgent()
    analyzer = InsightAnalyzerAgent()
    reporter = ReportGeneratorAgent()

    # Step 2: Collect data
    print("📥 Collecting data...")
    data = collector.collect()

    # Step 3: Analyze data
    print("🔍 Analyzing data for insights...")
    insights = analyzer.analyze(data)

    # Step 4: Generate and log report
    print("📝 Generating report...")
    report = reporter.generate(insights)

    # Final output
    print("\n✅ Pipeline complete. Final Report:")
    print(report)

if __name__ == "__main__":
    run_pipeline()
