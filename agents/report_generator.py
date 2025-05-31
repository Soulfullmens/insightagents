from google.cloud import bigquery
from datetime import datetime

class ReportGeneratorAgent:
    def __init__(self):
        print("✅ ReportGeneratorAgent initialized")
        self.bq_client = bigquery.Client()
        self.table_id = "robust-atrium-460918-b1.insight_data.reports"

    def generate(self, insights):
        print("📄 Generating report...")
        report = f"Report based on: {insights}"

        row = {
            "timestamp": datetime.utcnow().isoformat(),
            "report": report
        }

        errors = self.bq_client.insert_rows_json(self.table_id, [row])
        if errors:
            print(f"❌ BigQuery insert error: {errors}")
        else:
            print("✅ Report logged to BigQuery")

        return report
