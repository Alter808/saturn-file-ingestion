# Saturn Excel File Ingestion

Serverless service to ingest Excel files, validate their structure and content, and insert the data into an RDS database.

Designed to receive Excel files from external applications (e.g. Laravel/PHP), perform validations, normalize values, and persist the data securely in AWS.

---

## What This Service Does

This API:

1. Receives an Excel file via HTTP (`multipart/form-data`)
2. Validates request metadata
3. Validates Excel sheets and required columns
4. Parses and normalizes rows
5. Inserts valid records into an RDS database
6. Returns ingestion results

The Excel files are manually created and may contain:

- Multiple sheets
- Optional / nullable fields
- Mixed data types

The service is tolerant but enforces required structure where needed.

---

## Tech Stack

- AWS Lambda (Python 3.10)
- API Gateway (REST)
- AWS Secrets Manager
- RDS (MySQL / Aurora MySQL)
- Terraform (Infrastructure as Code)
- AWS SAM (Local development)
- GitHub Actions (CI/CD via OIDC)

---

## Project Structure

## Project Structure

```text
saturn-file-ingestion/
├── app.py                     # Lambda entry point
├── constants.py               # Global constants
├── multipart_parser.py        # Multipart/form-data parsing
├── excel_service.py           # Excel processing logic
├── validators/                # Request, sheet and row validation
├── mappers/                   # Row normalization and casting
├── repositories/              # Database access (PyMySQL)
├── services/                  # AWS helpers (Secrets Manager)
├── terraform/                 # Infrastructure (IAM, roles, policies)
├── requirements.txt
└── README.md
```

---

## API Usage

### Endpoint

## POST /ingest

### Headers

Content-Type: multipart/form-data
x-api-key: <api-key>

### Form Data

source=api
uploaded_by=<your-name>
file_type=excel
file=<file.xlsx>

---

## Ingestion Flow

1. Validate required metadata fields
2. Save uploaded Excel file to `/tmp`
3. Validate sheets and required columns
4. Parse rows and normalize values (trim strings, cast numbers)
5. Insert valid rows into the database
6. Return ingestion summary

---

## Local Development

```bash
sam build
sam local start-api
```

## Local endpoint:

http://127.0.0.1:3000/ingest
