# Azure
Achieve your goals with the freedom and flexibility to build, manage, and deploy your applications anywhere. Use your preferred languages, frameworks, and infrastructure—even your own datacenter and other clouds—to solve challenges large and small.
With help from Azure, you have everything you need to build your next great solution.

## **General Azure Resources**
Below are some key resources for Azure:
| Resource            | 
|---------------------|
| [Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/) |
| [Directory of Azure Services](https://azure.microsoft.com/en-us/services/) |
| [Azure Charts](https://azurecharts.com/) |
| [Azure Microsoft Learn](https://docs.microsoft.com/en-us/learn/azure/) |
| [Azure Product Documentation](https://docs.microsoft.com/en-us/azure/?product=featured) |
| [Azure Tech Community](https://techcommunity.microsoft.com/t5/azure/ct-p/Azure) |
| [Azure Well-Architected Framework (WAF)](https://docs.microsoft.com/en-us/azure/architecture/framework/) |
| [Cloud Adoption Framework (CAF) for Azure](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/) |
| [Azure Code Samples](https://docs.microsoft.com/en-us/samples/browse/?products=azure) |
| [Channel 9 Azure Friday](https://channel9.msdn.com/) |
| [Microsoft Azure YouTube Channel](https://www.youtube.com/user/windowsazure) |
| [Azure Support](https://azure.microsoft.com/en-us/support/options/) |
| [Microsoft Certifications](https://docs.microsoft.com/en-us/learn/certifications/) |

## **Resources by Scenario**
## Is your solution Single Tenant or Multi-Tenant?
### Multi-Tenancy
| Topic        | Link         |
|--------------|--------------|
| Shared Capacity Solutions | [Get started with autoscale in Azure - Azure Monitor](https://docs.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-get-started)<br>[Subscription decision guide - Cloud Adoption Framework](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/decision-guides/subscriptions/) |
| Dedicated Capacity Solutions | [Infrastructure as code](https://docs.microsoft.com/en-us/dotnet/architecture/cloud-native/infrastructure-as-code)<br>[Cross-tenant management experiences - Azure Lighthouse](https://docs.microsoft.com/en-us/azure/lighthouse/concepts/cross-tenant-management-experience) |
| Hybrid Capacity Solutions |  |

## How is your solution hosted?
### Build my new solution on Azure
| Topic        | Link         |
|--------------|--------------|
| Validate my architecture | [Assessments](https://docs.microsoft.com/en-us/assessments/) |
| Deploy Proof of Concept on Azure | [What is an Azure landing zone? - Cloud Adoption Framework](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/) |
### Migrate/Replicate my solution to Azure from another cloud
| Topic        | Link         |
|--------------|--------------|
| Understand the equivalent services on Azure (AWS, GCP) | [Azure for AWS professionals - Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/)<br>[Azure for GCP professionals - Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/gcp-professional/) |
| Understand how to leverage Kubernetes on Azure | [Kubernetes on Azure](https://azure.microsoft.com/en-us/overview/kubernetes-on-azure/)  |
### Migrate my solution to Azure from on-premises
| Topic        | Link         |
|--------------|--------------|
| Lift and Shift my solution to Azure | [Choosing Azure compute platforms for container-based applications](https://docs.microsoft.com/en-us/dotnet/architecture/modernize-with-azure-containers/modernize-existing-apps-to-cloud-optimized/choosing-azure-compute-options-for-container-based-applications)<br>[Java on Azure](https://docs.microsoft.com/en-us/learn/paths/java-on-azure/) |
| Modernize my solution as I migrate to Azure | [Modernize Existing .NET Applications With Azure Cloud and Windows Containers](https://docs.microsoft.com/en-us/dotnet/architecture/modernize-with-azure-containers/)<br>[Modernize Windows Server Apps on Microsoft Azure using Containers with Windows Admin Center and AKS!](https://techcommunity.microsoft.com/t5/itops-talk-blog/modernize-windows-server-apps-on-microsoft-azure-using/ba-p/1947588)|
| Data Migration | [Microsoft Database Migration Guide](https://datamigration.microsoft.com/) |
| Publish a traditional Windows desktop application to customers in a hosted environment | [Windows Virtual Desktop documentation](https://docs.microsoft.com/en-us/azure/virtual-desktop/) |
| Understand Azure Arc for hybrid management | [Manage hybrid infrastructure with Azure Arc](https://docs.microsoft.com/en-us/learn/paths/manage-hybrid-infrastructure-with-azure-arc/) |

## What outcome(s) are you focused on for your solution?
### Scale my solution to support more customers
| Topic        | Link         |
|--------------|--------------|
| Scale VM based solution | [Azure virtual machine scale sets overview - Azure Virtual Machine Scale Sets](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview)<br>[Build a scalable application with virtual machine scale sets - Learn](https://docs.microsoft.com/en-us/learn/modules/build-app-with-scale-sets/) |
| Modernize VM solution to microservices, containers, Kubernetes | [Modernize Existing .NET Applications With Azure Cloud and Windows Containers](https://docs.microsoft.com/en-us/dotnet/architecture/modernize-with-azure-containers/)<br>[Modernize Windows Server Apps on Microsoft Azure using Containers with Windows Admin Center and AKS!](https://techcommunity.microsoft.com/t5/itops-talk-blog/modernize-windows-server-apps-on-microsoft-azure-using/ba-p/1947588)<br>[Choosing Azure compute platforms for container-based applications](https://docs.microsoft.com/en-us/dotnet/architecture/modernize-with-azure-containers/modernize-existing-apps-to-cloud-optimized/choosing-azure-compute-options-for-container-based-applications) |
| Move my solution to a SaaS model | [Multi-tenant SaaS patterns - Azure SQL Database](https://docs.microsoft.com/en-us/azure/azure-sql/database/saas-tenancy-app-design-patterns) |
| Scale my databases | [Scale single database resources - Azure SQL Database](https://docs.microsoft.com/en-us/azure/azure-sql/database/single-database-scale)<br>[What is the Hyperscale service tier? - Azure SQL Database](https://docs.microsoft.com/en-us/azure/azure-sql/database/service-tier-hyperscale) |
| Scale my solution to additional geos | [Choose the Right Azure Region for You](https://azure.microsoft.com/en-us/global-infrastructure/geographies/)<br>[Azure regions decision guide - Cloud Adoption Framework](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/migrate/azure-best-practices/multiple-regions#:~:text=Sovereignty:%20Certain%20regions%20are%20dedicated%20to%20specific%20sovereign,certain%20types%20of%20customers.%20These%20sovereign%20regions%20are:)<br>[Data Residency in Azure](https://azure.microsoft.com/en-us/global-infrastructure/data-residency/) |
| Partitioning (across subscriptions, etc.) | [Azure Subscription Limits](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits) |

### Improve my solution's security & compliance (WAF-Security)
| Topic | Sub-Topic | Link |
|-------|-----------|------|
| Security Best Practices |  | [Azure Security Center documentation](https://docs.microsoft.com/en-us/azure/security-center/) |
| Compliance/Certification Requirements |  | [Compliance in the trusted cloud](https://azure.microsoft.com/en-us/overview/trusted-cloud/compliance/) |
| Data Residency/Sovereignty |  | [Choose the Right Azure Region for You](https://azure.microsoft.com/en-us/global-infrastructure/geographies/)<br>[Azure regions decision guide - Cloud Adoption Framework](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/migrate/azure-best-practices/multiple-regions#:~:text=Sovereignty:%20Certain%20regions%20are%20dedicated%20to%20specific%20sovereign,certain%20types%20of%20customers.%20These%20sovereign%20regions%20are:)<br>[Data Residency in Azure](https://azure.microsoft.com/en-us/global-infrastructure/data-residency/) |
| Govern my Azure Environment(s) | Azure Blueprints | [Overview of Azure Blueprints - Azure Blueprints](https://docs.microsoft.com/en-us/azure/governance/blueprints/overview)  |
|  | Azure Policy | [What is Azure Policy?](https://docs.microsoft.com/en-us/azure/governance/policy/overview) |
|  | Management Groups | [Organize your resources with management groups - Azure Governance - Azure governance](https://docs.microsoft.com/en-us/azure/governance/management-groups/overview) |
|  | Azure Role-Based Access Control | [What is Azure role-based access control (Azure RBAC)?](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview)  |
| SIEM/SOAR | Azure Sentinel | [Cloud-native security operations with Azure Sentinel - Learn](https://docs.microsoft.com/en-us/learn/paths/security-ops-sentinel/)<br>[Azure Sentinel – Cloud-native SIEM Solution](https://azure.microsoft.com/en-us/services/azure-sentinel/#product-overview) |
| Network (Layer 4) Security | Network Security Groups | [Create, change, or delete an Azure network security group](https://docs.microsoft.com/en-us/azure/virtual-network/manage-network-security-group) |
|  |  Hybrid (VPN, ExpressRoute, etc.) | [Azure ExpressRoute Overview: Connect over a private connection](https://docs.microsoft.com/en-us/azure/expressroute/expressroute-introduction)  |
| Application (Layer 7) Security | Identity as the new security perimeter | [Azure identity & access security best practices](https://docs.microsoft.com/en-us/azure/security/fundamentals/identity-management-best-practices#treat-identity-as-the-primary-security-perimeter)  |
|  | SSL, TLS, certificate management | [Add and manage TLS/SSL certificates - Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/configure-ssl-certificate) |
|  | OWASP attacks, WAF, etc. | [Web Application Firewall documentation](https://docs.microsoft.com/en-us/azure/web-application-firewall/)<br>[What is Azure Web Application Firewall on Azure Application Gateway? - Azure Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview#waf-policy-and-rules) |
| Shared responsibility |  | [Shared responsibility in the cloud - Microsoft Azure](https://docs.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility)<br>[Describe the shared responsibility model - Learn](https://docs.microsoft.com/en-us/learn/modules/describe-security-concepts-methodologies/3-describe-shared-responsibility-model?ns-enrollment-type=LearningPath&ns-enrollment-id=learn.wwl.describe-concepts-of-security-compliance-identity) |

### Increase my solution's reliability and performance (WAF-Performnace Efficiency & Reliability)
| Topic | Sub-Topic | Link |
|-------|-----------|------|
| VM reliability and performance |  | [Building solutions for high availability using Availability Zones - High Availability](https://docs.microsoft.com/en-us/azure/architecture/high-availability/building-solutions-for-high-availability) |
| Database reliability and performance |  | [Data Management for Reliability - Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/framework/resiliency/data-management) |
| Container reliability and performance |  | [Baseline architecture for an Azure Kubernetes Service (AKS) cluster - Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks/secure-baseline-aks#business-continuity-decisions)
| SLA, RTO, RPO metric-driven design, including "number of nines" |  | [Business Metrics - Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/framework/resiliency/business-metrics)<br>[Azure SLA Board (azurecharts.com)](https://azurecharts.com/sla)<br>[Choose the right Azure services by examining SLAs and service lifecycle](https://docs.microsoft.com/en-us/learn/modules/choose-azure-services-sla-lifecycle/) |
| Business continuity and disaster recovery (BCDR) |  | [Baseline architecture for an Azure Kubernetes Service (AKS) cluster - Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks/secure-baseline-aks#disaster-recovery) |
| Mean Time To Recover (MTTR) v. Mean Time Between Failures (MTBF) |  | [Business Metrics - Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/framework/resiliency/business-metrics) |
| Decoupling through message brokering |  | [Architect message brokering and serverless applications in Azure - Learn](https://docs.microsoft.com/en-us/learn/paths/architect-messaging-serverless/)<br>[Connect your services together - Learn](https://docs.microsoft.com/en-us/learn/paths/connect-your-services-together/)<br>[Asynchronous messaging options in Azure](https://docs.microsoft.com/en-us/azure/architecture/guide/technology-choices/messaging)<br>[Choose between Azure messaging services - Event Grid, Event Hubs, and Service Bus](https://docs.microsoft.com/en-us/azure/event-grid/compare-messaging-services) |
|  | Azure Queue Storage | [Introduction to Azure Queue Storage - Azure Storage](https://docs.microsoft.com/en-us/azure/storage/queues/storage-queues-introduction#:~:text=Azure%20Queue%20Storage%20is%20a%20service%20for%20storing,the%20total%20capacity%20limit%20of%20a%20storage%20account.) |
|  | Azure Service Bus | [Azure Service Bus messaging overview - Azure Service Bus](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview) |
|  | Azure Event Hub | [Azure Event Hubs documentation](https://docs.microsoft.com/en-us/azure/event-hubs/) |
|  | Azure Event Grid | [Azure Event Grid documentation](https://docs.microsoft.com/en-us/azure/event-grid/)  |
|  | Azure Redis | [Azure Cache for Redis Documentation](https://docs.microsoft.com/en-us/azure/azure-cache-for-redis/) |
| Designing for availability and reliability |  | [Reliability patterns - Cloud Design Patterns](https://docs.microsoft.com/en-us/azure/architecture/framework/resiliency/reliability-patterns) |

### Streamline my deployments on Azure (WAF-Operational excellence)
| Topic | Sub-Topic | Link |
|-------|-----------|------|
| Agile Planning |   | [What is Agile? - Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/learn/agile/what-is-agile)<br>[What is Agile Development? - Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/learn/agile/what-is-agile-development) |
|  | Azure Boards | [Understand what you get with Azure Boards - Azure Boards](https://docs.microsoft.com/en-us/azure/devops/boards/get-started/what-is-azure-boards?view=azure-devops&tabs=agile-process) |
|  | GitHub Project Management | [Features · Project management · GitHub](https://github.com/features/project-management) |
| Source Management (Git) |  | [What is Git? - Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/learn/git/what-is-git) |
|  | Azure Repos | [Azure Repos Documentation](https://docs.microsoft.com/en-us/azure/devops/repos/?view=azure-devops) |
|  | GitHub | [Using Git - GitHub Docs](https://docs.github.com/en/github/getting-started-with-github) |
|  | TFVC to Git | [Migrate from TFVC to Git - Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/learn/git/migrate-from-tfvc-to-git)<br>[Git and TFVC version control - Azure Repos](https://docs.microsoft.com/en-us/azure/devops/repos/tfvc/comparison-git-tfvc?view=azure-devops) |
| CI/CD |  | [Design a CI/CD pipeline using Azure DevOps - Azure Example Scenarios](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/apps/devops-dotnet-webapp)<br>[Release Engineering Continuous integration - Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/framework/devops/release-engineering-ci) |
|  | Azure Pipelines | [Azure Pipelines documentation](https://docs.microsoft.com/en-us/azure/devops/pipelines/?view=azure-devops)<br>[Learn how to build and deploy your apps - Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/get-started/?view=azure-devops<br>[AZ-400: Define and implement continuous integration - Learn](https://docs.microsoft.com/en-us/learn/paths/az-400-define-implement-continuous-integration/)<br>[Automate your deployments with Azure DevOps learning path - Learn](https://docs.microsoft.com/en-us/learn/paths/automate-deployments-azure-devops/) |
|  | Jenkins, CircleCI, etc. (OSS) | [Jenkins on Azure documentation - Jenkins](https://docs.microsoft.com/en-us/azure/developer/jenkins/) |
|  | Environment management | [Progressively expose your releases using deployment rings - Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/migrate/phase-rollout-with-rings?view=azure-devops)<br>[Set up staging environments - Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/deploy-staging-slots) |
|  | Configuration management | [What is Azure App Configuration?](https://docs.microsoft.com/en-us/azure/azure-app-configuration/overview)<br>[Managing Configuration and App Settings for Multiple Environments in Your CD Pipeline](https://devblogs.microsoft.com/devops/managing-configuration-app-settings-for-multiple-environments-in-your-cd-pipeline/) |


### Optimize my cloud spend on Azure (WAF-Cost Optimization)
### Add capabilities to my solution on Azure

