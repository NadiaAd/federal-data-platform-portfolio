# AWS Labs Screenshots

This page collects screenshots from my AWS hands-on labs. Together they show that I can build and operate core cloud infrastructure: VPCs, EC2, load balancers, RDS, IAM, CloudWatch, Lambda, Auto Scaling, and S3.

## Networking and VPC

- VPC with 172.31.0.0/16 CIDR, DNS resolution and hostnames enabled.  
- Public and private subnets created in the same VPC for two-tier architecture.  
- Route tables configured with an Internet Gateway for public subnets and restricted routes for private subnets.

## EC2 Instances

- EC2 instance in a public subnet with a public IP for admin / bastion access.  
- EC2 instance in a private subnet without a public IP, reachable only from within the VPC.  
- Instances tagged clearly for lab identification and monitoring.

## Load Balancing and Auto Scaling

- Application Load Balancer fronting EC2 instances in public subnets.  
- Target group configured with health checks and HTTP listener on port 80.  
- Auto Scaling Group created from a launch template, with minimum, maximum, and desired capacities set for scale-out/scale-in behavior.

## Storage and Databases

- S3 bucket created for storing lab artifacts and screenshots.  
- RDS / Aurora MySQL database instance running in private subnets with separate writer/reader endpoints.  
- Security groups limiting database access to application instances only.

## Monitoring and Alarms

- CloudWatch CPUUtilization alarm created for an EC2 instance, with threshold-based email notifications via SNS.  
- Custom metric values pushed from CloudShell to simulate load and verify alarm transitions (OK → ALARM → OK).  
- Alarm notification email from AWS confirming the alarm state change.

## Serverless and Automation

- Lambda function created with a simple Python handler returning “Hello from Lambda!”.  
- Test event executed successfully, with logs showing function execution details.  

## Identity and Access Management (IAM)

- IAM dashboard showing root user without active access keys and MFA enabled.  
- IAM user and role setup for least-privilege access during labs.

These screenshots support the written descriptions in the `01-cloud` folder and demonstrate real, hands-on use of AWS services rather than just theoretical knowledge.
