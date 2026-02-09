# federal-data-platform-portfolio

This repository showcases my hands-on experience in cloud architecture, data engineering, monitoring, and automation for a Solutions Architect / Data Engineer role supporting a federal agency. It combines AWS infrastructure labs, Python/SQL data workflows, observability setups, and application projects.

---

## About Me

I am a Junior Cloud / Data Engineer with experience designing and operating AWS-based environments (EC2, VPC, S3, IAM, RDS, Lambda, CloudWatch) plus SQL- and Python-driven data analysis and reporting. I have worked with NIST-aligned cloud risk management training, data quality monitoring in production environments, and full‑stack e‑commerce projects.

This portfolio highlights how I approach:

- Secure VPC and subnet design with public and private tiers.
- Building and scaling compute (EC2, Auto Scaling, load balancing).
- Designing data pipelines with SQL and Python ETL.
- Monitoring and alerting with CloudWatch and Lambda automation.
- Integrating applications, analytics, and ML‑ready workflows.
- Moving toward infrastructure-as-code and CI/CD.

---

## Repository Structure

### `01-architecture-vpc-networking/`

Network and architecture foundations:

- VPC, public and private subnets, route tables, and internet access patterns.
- EC2 instances in public and private subnets, IAM and security group considerations.
- Notes on how this layout supports secure, NIST‑minded architectures for federal workloads.

### `02-compute-and-containers/`

Compute and orchestration concepts:

- EC2 instances and Auto Scaling patterns for highly available services.
- Load balancer concepts (application load balancer fronting EC2).
- Kubernetes-style deployment ideas and how they would map to EKS/AKS.

### `03-data-pipelines-and-etl/`

Data engineering and ETL:

- Example SQL scripts for data quality checks, anomaly detection, and reporting.
- Python ETL script to extract from source data, transform it, and load into a relational database.
- Discussion of how these pieces would be orchestrated (Airflow, Step Functions, or similar tools).

### `04-observability-and-automation/`

Monitoring, logging, and automation:

- CloudWatch alarms on instance metrics (such as CPUUtilization) with SNS email notifications.
- Examples of using the AWS CLI and CloudShell to push custom metrics and test alarms.
- Lambda automation patterns for reacting to events and performing lightweight remediation.

### `05-applications-and-ml/`

Application and analytics projects that plug into a data platform:

- **Data Science Ecosystem** – Jupyter-based environment for data wrangling, analysis, and basic modeling.  
- **Fruta e Pan (E‑commerce)** – Full‑stack e‑commerce site demonstrating product, cart, and order flows.  
- **Burger My Bun (E‑commerce)** – Restaurant ordering app, suitable as a front end to a cloud-hosted API and database.  
- **Skillup Burger Shop** – Practice burger shop app reinforcing component-based design and user flows.

This section explains how these applications would be deployed behind load balancers, integrated with logging/metrics, and connected to data pipelines and ML models.

### `06-iac-and-devops/`

Infrastructure as Code and DevOps foundations:

- Terraform configuration (in progress) to define VPC, subnets, security groups, and compute.
- Git-based workflow examples and CI ideas (linting, tests, Terraform validation).
- Notes on how this would transfer to GitLab-based CI/CD and DevOps practices.

### `assets/`

Supporting diagrams and screenshots:

- AWS console screenshots (VPC, subnets, EC2, S3, RDS, IAM, Lambda, CloudWatch, Auto Scaling, etc.).
- Architecture diagrams showing how components fit together.

### `docs/`

Documentation and resume:

- PDF resume targeted to cloud / data engineering roles.
- Additional notes mapping work history, labs, and projects to architecture and data engineering responsibilities.

---

## Mapping to Solutions Architect / Data Engineer Responsibilities

| Role focus area                                          | Evidence in this repo                                                  |
| -------------------------------------------------------- | ---------------------------------------------------------------------- |
| Scalable, secure cloud architectures                     | `01-architecture-vpc-networking/` – VPC and public/private subnet design |
| Compute, orchestration, and high availability            | `02-compute-and-containers/` – EC2, Auto Scaling, load balancer notes  |
| SQL, Python, ETL, and data pipelines                     | `03-data-pipelines-and-etl/` – SQL checks and Python ETL script        |
| Monitoring, alerting, and automation                     | `04-observability-and-automation/` – CloudWatch alarms and Lambda      |
| Applications, analytics, and ML-ready workflows          | `05-applications-and-ml/` – linked e‑commerce and data science projects |
| Infrastructure-as-code and Git-based DevOps practices    | `06-iac-and-devops/` – Terraform and CI concepts                       |

---

## How to Use This Repository

1. Review the architecture notes in `01-architecture-vpc-networking/`.
2. Explore the ETL and SQL examples in `03-data-pipelines-and-etl/`.
3. Examine the monitoring and alarm flow in `04-observability-and-automation/`.
4. Follow links in `05-applications-and-ml/` to see complete application and data science code.
5. Look at `06-iac-and-devops/` for how this infrastructure can be expressed as code and integrated into CI/CD.

This portfolio is actively evolving; new Terraform modules, ETL jobs, and architecture documentation will be added as I deepen my work in cloud-native data platforms and ML‑ready infrastructures.
