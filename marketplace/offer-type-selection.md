---
layout: default
title: Commercial marketplace
description: "Get help with the commercial marketplace."
nav_exclude: true
---

# Commercial marketplace

## Get help selecting the right transactable offer type

There are three transactable offer types in the Azure Marketplace.

- Virtual Machines offers 
- SaaS offers 
- Azure Managed Application offers

[This document](https://docs.microsoft.com/en-us/azure/marketplace/marketplace-commercial-transaction-capabilities-and-considerations#transact-overview) helps you understand some of the differences.

### Virtual Machine offers 

Virtual Machine offers allow publishers to install their software on a virtual machine.  

- Runs in the customer’s tenant and subscription
- Pricing is based on usage of the product 
- Does not support metered billing

[Learn more about Virtual Machine offers here](create-or-maintain-a-virtual-machine-offer.md)

### SaaS offers 

SaaS offers allow for software that is delivered as SaaS to be transacted on the Azure Marketplace. 

- Ideally, a SaaS offer integrates with a multi-tenant application, but this is not required.
- A SaaS offer runs in the publisher's tenant.

[Learn more about SaaS offers here](create-or-maintain-saas-offer.md)

### Azure Managed Applications

- Runs in the customer's tenant
- Enables the publisher to manage the resources in the customer's tenant
- Deploys via an ARM template

[Learn more about Managed Application offers here](create-or-maintain-azure-managed-application-offer.md)