## D21.1 About MPAM

D21.1.1

IYYSRL

Introduction

In many systems, multiple software execution environments such as applications and virtual machines (VMs) run concurrently, sharing memory system resources such as memory controllers, caches, and interconnects. With no controls on the sharing of resources, software execution environments might cause interference for each other as they try to access resources. This might result in increased latency or reduced bandwidth, or both, for memory accesses for workloads that are performance sensitive.

Memory system resource Partitioning and Monitoring (MPAM) provides software with control mechanisms to apportion the memory system resources between software execution environments. This is done by:

- Memory system resource partitioning.
- Memory system resource usage monitoring, one of the uses of which is to inform adjustment of the partitioning.

## IRKDKZ MPAMprovides all of:

- An extension to the A-profile PE architecture:
- -Amechanism for privileged software executing in a PE to attach a Partition Identifier (PARTID) label, and a monitoring property called a Performance Monitoring Group (PMG), to a software execution environment in that PE.
- -If FEAT\_MPAM\_PE\_BW\_CTRL is implemented, then the PE implements a mechanism for software to impose a maximum limit on the bandwidth that requests from the PE itself can use. See MPAM PE-side Maximum-bandwidth limit injection control.
- For the system:
- -Adescription of the propagation of PARTIDs, PMGs, and PARTID spaces, through the system.
- -Aframework for implementing MPAMresource controls in Memory System Components (MSCs). These are the controls that partition the resources of MSCs.
- -An extension to that framework, for implementing MPAMresource monitors in MSCs.
- -An extension to that framework, for MPAM MSCs to have performance monitoring that is sensitive to a combination of PARTID and PMG.
- -Some implementation-independent, memory-mapped interfaces to memory system component controls for performance resource controls most likely to be deployed in systems.
- -Some implementation-independent, memory-mapped interfaces to memory system component resource monitoring that might be required to monitor the partitioning of memory system resources.

IPKXWQ When designing an SoC, the designer makes several or all the following SoC components MPAM-compliant , meaning that they implement one of the FEAT\_MPAM versions:

- Requester component types, for example PEs, DSPs, and DMA controllers.
- Components that provide shared memory system resources that it is possible to partition, for example shared caches, shared interconnects and buffers, Memory Management Units (MMUs), and memory channel controllers.

There is no requirement to make all components in an SoC MPAM-compliant.

## INJBFK In this chapter:

- An MPAMRequester is any type of MPAM-compliant Requester component. This chapter categorizes MPAM Requesters into:
- -MPAMPERequesters , also called MPAMPEs .
- -MPAMNon-PE Requesters .
- An MPAMMemory System Component (MPAM MSC) is an MPAM-compliant component that provides shared memory system resources.

This chapter describes MPAM PE Requesters, and Arm ® Memory System Resource Partitioning and Monitoring (MPAM) System Component Specification describes MPAM MSCs. The architecture does not describe MPAM Non-PE Requesters.

The architecture permits an MPAM MSC to be implemented as part of another system component. For example, an MPAMPEcancontain caches that are MPAM MSCs.

If an MPAM PE contains MPAM MSCs, it must have memory-mapped registers to identify and configure those MPAM MSCs.

IHRMSG

RSMNGB

## D21.1.2 MPAM information bundles

RBDJXQ

MPAMRequesters label every request to the memory system with an MPAMinformation bundle , comprising:

- Two items that together identify a single partition:
- -Anumber called the Partition Identifier (PARTID).
- -The PARTID space, for example Secure or Non-secure physical PARTID space.

Each PARTID space defines a set of PARTIDs.

Each PARTID corresponds to one partition.

- APerformance Monitoring Group (PMG).

## D21.1.3 Memory system resource partitioning

RDDGSM

Each MPAM MSC implements zero or more MPAMresource controls .

IGPWRB

Each MPAM resource control has settings for each PARTID.

IDTCTY

When an MPAM Requester sends a request, the PARTID space and PARTID in the MPAM information bundle are used as an index into a table in the MPAM MSC, to select the entry that holds the settings for that partition. Those settings configure how the shared partitionable resource is apportioned to that partition.

IMHDHR

See also:

- MPAMPE-side Maximum-bandwidth limit injection control for MPAM PE-side bandwidth regulation controls.

- For more detail, Arm ® Memory System Resource Partitioning and Monitoring (MPAM) System Component Specification .

## D21.1.4 Memory system resource usage monitoring

RRBCMK

Each MPAM MSC implements zero or more MPAMresource monitors .

ILDRSM

An MPAM resource monitor is associated with a shared partitionable resource in an MPAM MSC, and is able to measure how much a software execution environment is using that resource, by either:

- For a memory-bandwidth usage monitor, counting payload bytes that are passing where the monitor is placed.

- For a cache-storage usage monitor, counting bytes of the cache storage used.

IHQBLT

An MPAM resource monitor must be configured and enabled before it can be queried for usage of the MPAM MSC resource. Each monitor has a configurable filter register that the monitor uses to filter which bytes are counted. Fields in the filter register are writes, reads, PARTID, PMG, and other criteria. For example, a monitor can be configured to be sensitive to a PARTID, a PMG, or both.

ILWKZR

The architecture permits a resource monitor to be implemented as part of an MPAM PE.

RBGTCC

If an MPAM PE contains MPAM resource monitors, it must have memory-mapped registers to identify and configure those monitors.

IBGGWJ

See also:

- For more detail, Arm ® Memory System Resource Partitioning and Monitoring (MPAM) System Component Specification .

## D21.1.5 MPAMn\_ELx register naming convention

IFFCGH

In an MPAM PE, MPAMn\_ELx registers contain the PARTIDs and PMGs that the MPAM PE sends as part of MPAM information bundles. The naming convention of these registers is:

- The n in MPAMn\_ELx is the Exception level the register holds PARTIDs and PMGs for. That is, the register supplies PARTIDs and PMGs for execution at ELn.
- The x means that ELx and higher can access the register.

RCSQBF

The following table shows which MPAMn\_ELx register supplies PARTIDs and PMGs for which Exception level:

| MPAMn_ELx register   | Supplies PARTID and PMG when executing at                                                                          |
|----------------------|--------------------------------------------------------------------------------------------------------------------|
| MPAM0_EL1            | EL0 when MPAMHCR_EL2.GSTAPP_PLK is 0.                                                                              |
| MPAM1_EL1            | EL1, and EL0 when MPAMHCR_EL2.GSTAPP_PLK is 1. See Single PARTID for an EL1 guest OS and all its EL0 applications. |
| MPAM2_EL2            | EL2                                                                                                                |
| MPAM3_EL3            | EL3                                                                                                                |

## D21.1.6 The MPAM enable control

RXBYGC

IKRBMV

The MPAMn\_ELx.MPAMEN field at the highest implemented Exception level is the writable MPAMenable control . At all lower Exception levels, all other instances of MPAMn\_ELx.MPAMEN are read-only copies. For example:

- If EL3 is the highest implemented Exception level, MPAM3\_EL3.MPAMEN is the writeable MPAM enable control, and MPAM2\_EL2.MPAMEN and MPAM1\_EL1.MPAMEN are read-only copies.

MPAM0\_EL1 does not contain an MPAMEN field.

See the following for the behavior when MPAM is disabled:

- The Default PARTID.
- The Default PMG.
- Interaction of MPAM3\_EL3.SDEFLT and the MPAM enable control.

## D21.1.7 AArch32 interoperability

IRSTCB

MPAMSystem registers are not accessible from AArch32 state. Therefore, a higher Exception level must set the PARTIDs and PMGs for any Exception level that uses AArch32 state.

## D21.1.8 FEAT\_MPAM versions

RYSNTG

An MPAM PE implements one of these MPAM versions:

| Version   | Major version reported by ID_AA64PFR0_EL1.MPAM   | Minor version reported by ID_AA64PFR1_EL1.MPAM_frac   |
|-----------|--------------------------------------------------|-------------------------------------------------------|
| v0p1      | 0b0000                                           | 0b0001                                                |
| v1p0      | 0b0001                                           | 0b0000                                                |
| v1p1      | 0b0001                                           | 0b0001                                                |

ITGCKZ

v1p0 is the base version. v0p1 and v1p1 include features beyond the base version and are the same except that v0p1 implements the Force Secure PARTIDs to Non-secure feature.

RKTQFR

The MPAM PE features by MPAM version are:

## Table D21-3 MPAM PE features by MPAM version

| MPAM PE feature                     | MPAMIDR_EL1 ID field   | v0p1       | v1p0       | v1p1       | MPAM for RME   |
|-------------------------------------|------------------------|------------|------------|------------|----------------|
| PARTID virtualization a             | HAS_HCR                | Optional   | Optional   | Optional   | Optional       |
| Force Secure PARTID to Non-secure b | HAS_FORCE_NS           | Required   | Prohibited | Prohibited | Prohibited     |
| Secure Default PARTID b             | HAS_SDEFLT             | Optional   | Prohibited | Optional   | Optional       |
| TIDR in MPAM2_EL2                   | HAS_TIDR               | Required   | Prohibited | Required   | Required       |
| Four PARTID spaces                  | SP4                    | Prohibited | Prohibited | Prohibited | Required       |
| Alternative PARTID spaces c         | HAS_ALTSP              | Prohibited | Prohibited | Prohibited | Required       |
| FEAT_MPAM_PE_BW_CTRL d              | HAS_BW_CTRL            | Optional   | Prohibited | Optional   | Optional       |

RMQDXN

The system features by MPAM version are:

## Table D21-4 MPAM system features by MPAM version

| MPAM system feature   | v0p1       | v1p0       | v1p1       | MPAM for RME   |
|-----------------------|------------|------------|------------|----------------|
| MPAM_NSsignal a       | Required   | Required   | Required   | Prohibited     |
| MPAM_SP signal a      | Prohibited | Prohibited | Prohibited | Required       |

a. See See Encoding PARTID spaces onto PARTID space signals.

| I VQQHN   | MPAMfor RMEsupports the Realm Management Extension (RME) in systems, MPAMPEs, and MPAMMemory System Components (MPAM MSCs).                                         |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R ZDLYQ   | MPAMfor RMEis required in a PE that implements both RMEand MPAM.                                                                                                    |
|           | D21.1.8.1 Interoperation of SoC components implementing different MPAM versions                                                                                     |
| I JVGNT   | There is no requirement for all MPAMPEsin an SoC to implement the same MPAMversion. However, eachMPAMPE having a different MPAMversion might cause software issues. |
| I JCHFV   | There is no required relationship between the MPAMversion of an MPAMPEandthe MPAMversion ofanMPAM MSCaccessed by that MPAMPE.                                       |
| I KGCTV   | For more information, see:                                                                                                                                          |