# Sample AWS Architecture Notes

## Two-tier VPC layout

- VPC CIDR: 172.31.0.0/16
- Public subnets: host an Application Load Balancer and bastion/utility instances.
- Private subnets: host EC2 application servers and RDS database instances.
- Internet Gateway: attached to the VPC; route tables send public subnet traffic to it.
- NAT Gateway: allows private subnet instances to reach the internet for updates without being directly exposed.

## Security considerations

- Security groups:
  - ALB: inbound HTTP/HTTPS from the internet, outbound to app instances.
  - App instances: inbound only from ALB security group and bastion, outbound to RDS and external APIs.
  - RDS: inbound only from app instance security group on the database port.
- IAM:
  - Roles for EC2 and Lambda to access S3, CloudWatch Logs, and other services without long‑lived credentials.

## Monitoring and alerts

- CloudWatch metrics: CPUUtilization, NetworkIn/Out, StatusCheckFailed.
- CloudWatch alarms:
  - High CPU on app instances triggers an alarm notification.
  - Status check failures indicate underlying hardware or networking issues.
- SNS topic: sends email alerts when alarms enter ALARM state.
