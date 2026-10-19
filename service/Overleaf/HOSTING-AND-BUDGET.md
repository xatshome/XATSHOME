# xatshome: hosting and budget considerations

Discussion draft — October 3, 2026

This document records hosting suggestions for xatshome, an assisted ATS3
workspace, including a possible paid parallel compilation service. It complements
[REQUIREMENTS.md](REQUIREMENTS.md). These are proposals, not committed architecture
or customer pricing. Provider prices were checked during the discussion and may
change.

## Initial service

The initial requirements emphasize template discovery, inspection, and project
creation through both a human GUI and an AI-oriented CLI. They do not yet require
a complete browser IDE, online project storage, or hosted compilation.

A low-cost first version could host the website and versioned template catalog
publicly while creating projects and compiling on the user's machine. The website
could offer project ZIP downloads, and the CLI could fetch the same templates and
create ordinary local directories. A local GUI could share the CLI's underlying
project-creation library.

The decisive product question is whether a newcomer must compile their first ATS3
program entirely in the browser, without installing anything. If that experience
is required, a backend and isolated compilation workers belong in the first
milestone.

## Website and API hosting options

| Option | Proposed use | Budget considerations and tradeoffs |
|---|---|---|
| Cloudflare static hosting plus local tools | Public website, documentation, and template catalog | Static asset requests are free; lowest initial operating cost, but users need a local ATS3 environment. |
| Small DigitalOcean server | Website, API, and modest hosted project storage | Droplets start at $4/month. Allow roughly $15–30/month for a small pilot with backups and headroom; server maintenance remains our responsibility. |
| Render | Managed deployment of the website/API, with a database when needed | App compute starts at $7/month. Allow roughly $20–50/month for a small persistent service; database and storage add costs. |
| Google Cloud Run | Containerized API with separate persistent storage | Usage-based billing and automatic scaling; total cost depends on compute and supporting services. |

The budget ranges are planning allowances for a small pilot, not provider quotes.
They exclude hosted compilation, AI inference, domain registration, and maintenance
labor. Depending on features, also budget for project storage, database storage,
backups, email, logs, and network transfers.

Sources: [Cloudflare pricing](https://developers.cloudflare.com/workers/platform/pricing/),
[DigitalOcean pricing](https://www.digitalocean.com/pricing/droplets),
[Render pricing](https://render.com/pricing),
[Cloud Run pricing](https://cloud.google.com/run/pricing).

## Overleaf as a reference point

Overleaf confirms that it uses Google Cloud Platform for data storage, keeps
redundant backups across multiple locations, and uses Google Cloud load balancing.
Its privacy notice says much of its product infrastructure is outside the UK,
including in the United States. The cited page does not identify exact cloud
regions or establish where every component runs.

This is useful context, but xatshome's hosting should follow its own workload and
stage of development. See [Overleaf's published security and privacy information](https://www.overleaf.com/legal).

## Parallel compilation as a paid service

An attraction of ATS3 is the opportunity to compile many files independently.
For example, a build with 100 independent compilation tasks could assign them to
100 workers. The scheduler must still respect any prerequisites and subsequent
linking or assembly steps.

Separate the website/API from compilation capacity. A small application service
can handle projects, accounts, build submissions, and results, while a worker
pool expands with demand. This avoids keeping 100 workers idle merely to support
occasional 100-worker builds.

A worker is a unit of execution, not necessarily a separate machine. Several
multicore machines can run 100 compiler processes. Compare that arrangement with
100 individually provisioned container tasks before choosing a deployment model.

### Total computation versus customer waiting time

If 100 independent files each take 30 seconds on one CPU core, the compilation
requires approximately 50 CPU-minutes whether performed sequentially or in
parallel. Ideal parallel execution reduces compilation elapsed time toward
30 seconds, rather than reducing the amount of computation.

Actual build latency includes queuing, worker startup, fetching inputs,
dependencies, uneven task durations, artifact collection, and final linking.
Parallelism can also add overhead. A 100-worker allocation therefore does not
imply a 100-fold end-to-end speedup.

## Compilation hosting options

| Option | Fit for xatshome | Main tradeoff |
|---|---|---|
| Google Cloud Run Jobs | Initial paid pilot using a compiler container and parallel tasks | Little server administration, but startup and minimum billing can dominate short compilations. |
| Google Cloud Batch | Larger queued builds scheduled across VMs, optionally using Spot capacity | Suitable for burst computation; measure provisioning latency before promising interactive response times. |
| AWS Batch | Alternative managed scheduler using EC2 or Fargate compute, with Spot options where supported | Flexible infrastructure choices, with more configuration to evaluate. |
| Persistent multicore server pool | Fast repeated builds with compiler and dependencies already cached | Idle capacity costs money, and we manage availability and capacity. |

Cloud Run Jobs supports configurable task parallelism; achievable parallelism
depends on regional quotas and CPU/memory allocations. A requested concurrency
of 100 should be tested and quota availability confirmed before it becomes a
customer promise. Google Batch and AWS Batch do not add a separate service fee;
the underlying compute and other resources still incur charges.

Sources: [Cloud Run job configuration](https://docs.cloud.google.com/run/docs/create-jobs),
[Cloud Run quotas](https://cloud.google.com/run/quotas),
[Google Batch](https://cloud.google.com/batch),
[AWS Batch pricing](https://aws.amazon.com/batch/pricing/).

### Suggested progression

1. Benchmark a representative ATS3 project locally and on cloud workers.
2. Try Cloud Run Jobs for an initial paid pilot, measuring actual cost and latency.
3. If customers value consistently quick interactive builds, evaluate a small
   persistent pool with additional cloud workers during bursts.
4. If demand favors large, non-urgent builds, evaluate Google Batch or AWS Batch
   with discounted interruptible capacity.

Keep build descriptions and worker inputs independent of a particular provider
where practical, so the same compiler container can be evaluated on different
execution platforms.

## Illustrative compilation costs

Cloud Run Jobs' listed Iowa (`us-central1`) rates at the time of discussion were:

- CPU: $0.000018 per allocated vCPU-second.
- Memory: $0.000002 per allocated GiB-second.
- Minimum billable lifetime: one minute per started job instance.

At an allocation of one vCPU and one GiB per worker, the combined rate is
$0.000020 per second, or $0.0012 per billable worker-minute.

| Allocation | Approximate worker compute cost |
|---|---:|
| 100 workers, each billed for one minute | $0.12 |
| 100 workers, each billed for five minutes | $0.60 |
| 1,000 builds of the first kind | $120 |

These calculations precede free allowances and exclude storage, orchestration,
network transfers, retries, and other service costs. They assume the stated
billable duration, including any billable startup and shutdown time. Actual ATS3
memory requirements remain to be measured.

The one-minute minimum matters for short tasks: launching 100 instances to
perform one-second compilations may be inefficient. Assigning several small files
to a worker can reduce overhead and billing, at the possible expense of some
parallelism. The scheduler should choose task grouping based on measurements.

Source: [Cloud Run pricing and billing rules](https://cloud.google.com/run/pricing).

## Proposed build workflow

1. Accept an immutable project snapshot, compiler version, and build options
   through the same underlying API used by both GUI and CLI.
2. Identify compilation tasks and their prerequisites.
3. Reuse valid cached artifacts. Cache keys should include source inputs,
   dependencies, compiler/toolchain version, and relevant options. Keep private
   project artifacts subject to the project's access rules.
4. Dispatch remaining work to isolated workers with CPU, memory, and time limits.
5. Collect diagnostics and artifacts, retry eligible infrastructure failures, and
   perform any required final linking.
6. Return build status, results, and usage through the GUI and structured CLI
   output.

Workers handling user inputs should have only the permissions and data needed
for their assigned build. Public compilation and arbitrary user build scripts
require appropriate isolation; ordinary process separation alone should not be
assumed to provide a sufficient tenant boundary.

## Possible customer pricing

Consider a monthly allowance of compilation credits plus a concurrency limit.
Illustrative plan limits could be 4, 16, or 100 simultaneous workers. These are
examples for discussion, not proposed prices or capacity guarantees.

Meter allocated CPU time and memory behind the credits. Charging solely by file
count would be unpredictable because files can differ greatly in compilation
time and memory demand. Customer pricing must also cover idle capacity, storage,
service operation, payment costs, support, and a margin.

Two queue classes could serve different needs:

- **Economy:** lower price for builds that can wait and tolerate retries on
  interruptible Spot capacity.
- **Priority:** regular capacity, higher scheduling priority, and potentially
  workers kept ready to reduce startup delays.

Spot interruptions can require recompilation, so account for retries in both
scheduling and service economics. Define clearly whether customers pay for
infrastructure retries, failed source compilations, and cache hits.

Source: [Google Spot VM pricing and interruption considerations](https://cloud.google.com/spot-vms/pricing).

## Measurements needed before committing

Benchmark representative projects with 1, 8, 32, and 100 workers. Include both
clean builds and incremental builds, and measure:

- End-to-end latency, including queue and startup time.
- Per-file compilation duration and peak memory.
- Total allocated CPU time and memory time.
- Input distribution and artifact collection overhead.
- Cache effectiveness and any serial dependency or linking stages.
- Cost per successful build, including retries.
- Behavior when several customers submit builds concurrently.

These results should determine task grouping, worker size, concurrency limits,
and whether the initial paid offering emphasizes occasional large parallel
builds, consistently fast interactive builds, or both.

The working recommendation is to keep the initial website inexpensive, introduce
parallel compilation as a separate measured service, and choose persistent versus
on-demand worker capacity from observed workload and customer latency needs.
