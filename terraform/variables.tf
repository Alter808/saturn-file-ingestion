variable "aws_region" {
  type        = string
  description = "AWS region"
  default     = "us-east-1"
}

variable "aws_profile" {
  type        = string
  description = "AWS CLI profile to use"
}

variable "environment" {
  type        = string
  description = "Environment name (dev, qa, prod)"
  default     = "dev"
}

variable "project_name" {
  type        = string
  description = "Project name"
  default     = "saturn-excel-ingestion"
}
