---
title: Microsoft Ignite | The Tour: Amsterdam — day one
date: 2019-03-20
tags: [azure, cloud, devops, serverless, tools]
---

Microsoft Ignite | The Tour: Amsterdam is a two day tech conference organized by
Microsoft. On this first day I attended the talks in the "Building your
application for the cloud" learning path.

(On the [second day](/weblog/2019/03/21/microsoft-ignite-the-tour-amsterdam-day-two/)
I followed the sessions of the "Operating applications and infrastructure in the
cloud" learning path.)

![Welcome to Microsoft Ignite | The Tour: Amsterdam](/images/mitta2019_welcome.jpg)

_Note: the sheets listed at the end of the notes for a talk are the ones listed
on the [Microsoft Ignite | The Tour Content](https://techcommunity.microsoft.com/t5/Microsoft-Ignite-The-Tour/bd-p/MicrosoftIgniteTourContent)
site. They may be different from the actual presentations used during the
Amsterdam event._


# Designing resilient cloud applications --- Jeremy Likness

Most of the things in this talk allow you to scale your app without changing
your application itself.

We want to design for security. So instead of relying on e.g. environment
variables to distribute secrets, you are better off using a centralized solution,
like [Azure Key Vault](https://azure.microsoft.com/en-us/services/key-vault/).

Some of its features:

- You can version your secrets
- Manage all secrets in one place
- Manage secrets across environments (dev, QA, production)
- Easy to integrate

Use [Managed identities](https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview)
(formerly "Managed Service Identity" or MSI) on your VM, app service or function
to authenticate to Azure Key Vault.

To make your database more resilient, you can use
[Cosmos DB](https://azure.microsoft.com/en-us/services/cosmos-db/),
which has features like:

- Global distribution (get the DB as close to you as possible, without having to
  change connection strings)
- Elastic scale
- Consistency ranging from strong (wait until every replica is up to date) to
  "eventually consistent" (it might take a while until all the replicas are up to
  date).

Failovers can be done automatically and manually. But whatever you choose, you
don't have to touch your application. It is possible (and easy) to have a multi
master setup. (It is more expensive though.)

There are several extensions for VS Code to connect to e.g. Cosmos DB from
within VS Code. This means you could e.g. edit data from within VS Code.
However, it might be better to hand out read-only credentials for your
production database.

[Azure App Service](https://azure.microsoft.com/en-us/services/app-service/) is
a managed platform that makes it easy to run your application (like .NET, .NET
Core, Node.js, Java or Python). It makes scaling up and scaling out on the fly
easy. Even better: you can configure your application to autoscale.

Check out the [Azure Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-azureextensionpack)
extension for VS Code. It has a lot of useful features like connecting with
your Cosmos DB, as mentioned above, but you can also do things like deploying
your application from within your editor.

[Azure Storage](https://azure.microsoft.com/en-us/services/storage/) is useful
for static things you want stored in the cloud, e.g. blobs, tables, files and
queues. [Azure Static Sites](https://azure.microsoft.com/en-us/blog/static-websites-on-azure-storage-now-generally-available/)
are currently in preview. It allows you to serve static files via a web server.
Even the right MIME types are returned.

![Jeremy Likness about the Azure Front Door Service](/images/mitta2019_jeremy_likness_1.jpg)

To have a resilient architecture, you'll have to have the service available
across multiple regions. Use [Azure Front Door Service](https://azure.microsoft.com/en-us/services/frontdoor/)
(currently in preview). It can be used with [Traffic Manager](https://azure.microsoft.com/en-us/services/traffic-manager/).
In the Front Door designer there are "frontend hosts" (domains the service is
hosted on), "backend pools" (the available backends) and "routing rules" which
map frontend hosts to backend pools based on path patterns (e.g.
`/api/products/.*`).

Additional resources:

- [Sheets (PPTX)](https://aka.ms/TechCommunity/MicrosoftIgniteTour/DEV10)
- [Code](https://github.com/Microsoft/IgniteTheTour/tree/master/DEV%20-%20Building%20your%20Applications%20for%20the%20Cloud/DEV10)
- [Manage secrets in your server apps with Azure Key Vault](https://docs.microsoft.com/en-us/learn/modules/manage-secrets-with-azure-key-vault/)
- [Azure Front Door Documentation](https://docs.microsoft.com/en-us/azure/frontdoor/)


# Deploying your application faster and safer --- Damian Brady

Damian Brady uses the analogy of a pit stop in 1905 compared to one in 2013.
Summary: much faster, more people involved.

What is "DevOps"? There are a number of different definitions. At Microsoft it
is defined as:

> DevOps is the union of people, process and products to enable continuous
> delivery of value to our end users.

Why DevOps is important:

- Increases velocity
- Decreases downtime and human error
- Your competitors are already doing this

Have a look at the [State of DevOps Report](https://puppet.com/resources/whitepaper/state-of-devops-report). It is
a yearly report full of interesting information. The report compares the high
performing teams with low performing teams. The high performers have a 46
times higher deployment frequency, fail less frequently, fix failures 2555 times
faster, etc. It's a great report to convince your manager to change things.

Development used to toss software over the wall to the operations team. When
things go wrong, people tend to blame the other team. Developers want change but
operations want to have stability (in other words: not change anything)---the
teams have opposite incentives.

To change this, you'll need a process. And you'll need good products to help you
with the process. [Azure DevOps](https://azure.microsoft.com/en-us/services/devops/) can everything you need.  Fortunately
Microsoft does allow you to use your current products as well.

![Damian Brady showing Azure DevOps can be used in combination with many other products](/images/mitta2019_damian_brady.jpg)

Azure DevOps components:

- [Azure Boards](https://azure.microsoft.com/en-us/services/devops/boards/): track work
- [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/): CI/CD
- [Azure Repos](https://azure.microsoft.com/en-us/services/devops/repos/): Git repos
- [Azure Test Plans](https://azure.microsoft.com/en-us/services/devops/test-plans/): coordinate your testing efforts
- [Azure Artifacts](https://azure.microsoft.com/en-us/services/devops/artifacts/): build artifacts storage

This talk will demo Azure Pipelines.

Azure Pipelines is on the [GitHub Marketplace](https://github.com/marketplace/azure-pipelines).
It is free, assuming you stay within the limits set.

You can configure your Pipeline in your browser and by doing so, a file called
`azure-pipelines.yml` is created in your repository. This immediately creates a
build check in GitHub.

Build configuration is similar to deployment configuration.

You can have multiple stages and have pre-deployment conditions between them.
This way you can for instance make sure that person X or group Y has to approve
the deployment to production.

You can have build artifacts, which you can use in your build pipeline. These
artifacts are not available externally---they are part of the release pipeline.
If you need more persistent artifacts, you'll want to use Azure Artifacts.

You can configure canary deployments and do so in different ways. In this demo
"deployment slots" are used. They allow you to create a duplicate deployment and
direct a part of the traffic to the cloned slot (canary environment).

[LaunchDarkly](https://launchdarkly.com/) allows you to roll out based on many
more criteria (e.g. regional, a specific customer, etc). Note that this is a
paid service.

Manual approval can be replaced by a so called deployment gate. These deployment
gates are automated approval processes. You can perform a number of checks
(security and compliance assessment, work items, Azure Monitor Alerts or invoke
a REST API or Azure Function). When they are successful, the application is deployed,
otherwise not. This makes deployment faster and safer.

Additional resources:

- [Sheets (PPTX)](https://aka.ms/TechCommunity/MicrosoftIgniteTour/DEV20)
- [Code](https://github.com/Microsoft/IgniteTheTour/tree/master/DEV%20-%20Building%20your%20Applications%20for%20the%20Cloud/DEV20)
- [Azure DevOps documentation](https://docs.microsoft.com/en-us/azure/devops/index)
- [DevOps Resource Center](https://docs.microsoft.com/en-us/azure/devops/learn/)


# Detecting application anomalies with Telemetry --- Jason Hand

Demonstration of [Azure Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview).

Jason Hand is using the analogy of a car: if it breaks down (e.g. runs out of
gas), it becomes useless. You'll want to prevent this. Cars have dashboards to
warn if things go out of bounds.

![Jason Hand about cars that have dashboards to warn if things go out of bounds](/images/mitta2019_jason_hand_1.jpg)

Application Insights has a lot of tools to help you monitor your application. Going back to the car analogy: it's like having a mechanic with tools in the vehicle with you. It
has, among other things, [Smart Detection](https://docs.microsoft.com/en-us/azure/azure-monitor/app/proactive-diagnostics)
to warn about performance problems and failures. Something else it provides is
[Application Map](https://azure.microsoft.com/en-us/services/azure-maps/) where
you can more easily spot performance issues.

More in depth information in his other talks:

- [Monitoring your infrastructure and applications in production](/weblog/2019/03/21/microsoft-ignite-the-tour-amsterdam-day-two/#monitoring-your-infrastructure-and-applications-in-production-jason-hand)
- [Troubleshooting failure in the cloud](/weblog/2019/03/21/microsoft-ignite-the-tour-amsterdam-day-two/#troubleshooting-failure-in-the-cloud-jason-hand)

Additional resources:

- [Sheets PPTX](https://aka.ms/TechCommunity/MicrosoftIgniteTour/DEV30)
- [Application Insights documentation](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)
- [Manage an Azure Traffic Manager profile](https://docs.microsoft.com/en-us/azure/traffic-manager/traffic-manager-manage-profiles)
- [Analytics in Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/analytics)
- [Design for efficiency and operations in Azure](https://docs.microsoft.com/en-us/learn/modules/design-for-efficiency-and-operations-in-azure/)


# Selecting the right data storage strategy for your cloud application --- Jeramiah Dooley

It is important to think about your data storage. The benefits of having a
storage strategy:

- It facilitates an upgrade of legacy processes without running past the
  operational teams supporting this.
- It provides guardrails to keep everyone aligned.
- To build a strategy, you have to break things down into manageable pieces.
  This will help you down the line.
- A strategy can function as a plan on how to swap pieces in and out.
- If everyone is on board on the strategy it is easier to maintain security
  posture.

Azure might give you a different way to look at data storage. There are a number
of different storage options. Do note that storage is only a small part of the
whole.

![Jeramiah Dooley](/images/mitta2019_jeramiah_dooley_1.jpg)

Storage and compute are abstracted away more and more these days, but everything
eventually depends on the storage sitting beneath it. If your storage breaks,
you will have a bad day.

Why not use a relational database to store all data? By using other options, we
may make the application more granular to deploy and/or give developers more
control.

Different kinds of data:

- Structured data: this is where we came from with relational databases.
- Semi-structured data: this is data that _is_ structured, but cannot be fit
  into a table that easily.
- Unstructured data: for example video and images.

Different properties of data:

- Volume: how big is it going to be?
- Velocity: how much is it going to change?
- Variety: how much different kinds of data will you have?

Strategies:

- Storage driven: the operations team or the business decides on the storage and
  development will have to use it. This means developers need to know a lot of
  low-level details about the storage. And we probably don't want that.
- Cloud-driven: deploy storage to what makes sense. Not much better for
  development, the main difference is that the storage is not on premise.
- Function-driven: build what you need, storage comes with it.

An example of function driven approach is building a search functionality. We
could implement it as full-text search on our existing SQL database. However,
this has an impact on the production database. If we would use [Azure
Search](https://azure.microsoft.com/en-us/services/search/)
(search-as-a-service), we would not have to worry about the storage or paying
for storage we don't use.

Data architectures summary:

- More complex and more options than in the past
- Easier to choose, especially based on function
- More direct access by developers
- More control over experience and cost

Additional resources:

- [Sheets (PPTX)](https://aka.ms/TechCommunity/MicrosoftIgniteTour/DEV40)
- [Choose a data storage approach in Azure](https://docs.microsoft.com/en-us/learn/modules/choose-storage-approach-in-azure/index)
- [Azure Search Documentation](https://docs.microsoft.com/en-us/azure/search)
- [Introduction to Azure Cosmos DB: Gremlin API](https://docs.microsoft.com/en-us/azure/cosmos-db/graph-introduction)
- [Azure Data Lake Analytics Documentation](https://docs.microsoft.com/en-us/azure/data-lake-analytics/)


# Investing in Serverless: less servers, more code --- Jeremy Likness

On premise infrastructure requires you to answer a lot of questions, like:

- What media should I use to keep backups?
- How can I scale my app?
- Who monitors my servers?
- What happens if the power goes out?
- Who has physical access to my servers?

Moving to infrastructure as a service still means dealing with a bunch of
questions, but less lower level. You pay for the service of someone else
worrying about the hardware, access, etc. You are left with questions like:

- How can I scale my app?
- How often should I patch my servers?
- How do I deploy new code to my servers?

Platform as a service means even higher level questions:

- What is the right size of my server
- How many servers do I need?

With serverless, you are down to a single question: how do I architect my app?
You focus on the event that happened (a request was sent to an endpoint) not on
the whole infrastructure to make that happen.

What is serverless (according to Jeremy)?

- Abstraction of servers
- Event driven / instant scale
- Micro-billing (focus on what you are using)

Checklist to determine if something is serverless:

- Is it capable of running entirely in the cloud?
- Does it run and scale without configuring a VM/cluster?
- Do I only get billed for active invocations?

![Jeremy Likness with an overview of serverless components in Azure](/images/mitta2019_jeremy_likness_2.jpg)

## Functions

Functions: you pay for functions that get called and consume memory, not for
servers. You don't care how much machines are needed to handle the number of
requests.

Functions have triggers and bindings. Triggers are things like blob storage,
Cosmos DB, HTTP, timer and a webhook. Bindings allow you to work with resources
(like files, tables, emails, notifications).

Example: a file is added to storage, a function parses and transforms the file
and stores a chart graphic.

## Event grid

Managing events is cumbersome. Event grid can help you. It offers:

- Fully managed event routing to get a message from A to B.
- Near real-time event delivery at scale.
- Broad coverage within Azure and beyond.

You can focus on the messages. The infrastructure ensures reliability and
performance. It can, for instance, handle ten million events per second per
region.

Event grid delivers the event to you; you never have to go out to grab events.

Scenarios:

- Serverless apps
- Ops automation
- Application integration

Durable functions are an extension to functions for stuff that e.g. has to wait
for an asynchronous event. They are paused, but state is stored. And you are
only billed for the time the function is actually doing things; you don't pay
when the function is paused.

Durable function patterns:

- Sequential asynchronous calls
- Fan out / fan in
- Human approval
- Ongoing monitoring

## Logic apps

Logic apps are the integration engine that connect things together. They allow
you to design workflows and processes. For example: when a new product is added,
an email is sent to the products team to add an image, etc.

Logic apps also have triggers.

Additional resources:

- [Sheets (PPTX)](https://aka.ms/TechCommunity/MicrosoftIgniteTour/DEV50)
- [Code](https://github.com/Microsoft/IgniteTheTour/tree/master/DEV%20-%20Building%20your%20Applications%20for%20the%20Cloud/DEV50)
