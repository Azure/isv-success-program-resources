---
layout: default
title: Commercial marketplace
description: "Get help with the commercial marketplace."
nav_exclude: true
---

# Commercial marketplace

## Get help selecting the right transactable offer type

There are three transactable offer types in the Azure Marketplace.

<!-- no toc -->
- [Virtual Machines offers ](#virtual-machine-offers)
- [SaaS offers](#saas-offers)
- [Azure Managed Application offers](#azure-managed-application-offers)

### Microsoft Docs

[Publishing guide by offer type](https://docs.microsoft.com/azure/marketplace/publisher-guide-by-offer-type)

[Transact overview](https://docs.microsoft.com/en-us/azure/marketplace/marketplace-commercial-transaction-capabilities-and-considerations#transact-overview) helps you understand some of the differences between transactable offer types.

### Transactable offer types detail

The following offer types address only the offer types that are transactable on the Azure Marketplace.

#### Virtual Machine offers 

Virtual Machine offers allow publishers to install their software on a virtual machine.  

- Runs in the customer’s tenant and subscription
- Pricing is based on usage of the product 
- Does not support metered billing

[Learn more about Virtual Machine offers here](create-or-maintain-a-virtual-machine-offer)

#### SaaS offers 

SaaS offers allow for software that is delivered as SaaS to be transacted on the Azure Marketplace. 

- Ideally, a SaaS offer integrates with a multi-tenant application, but this is not required.
- A SaaS offer runs in the publisher's tenant.

[Learn more about SaaS offers here](create-or-maintain-saas-offer)

#### Azure Managed Application offers

- Runs in the customer's tenant
- Enables the publisher to manage the resources in the customer's tenant
- Deploys via an ARM template

[Learn more about Managed Application offers here](create-or-maintain-azure-managed-application-offer)