## 3.15 Coherency considerations and memory access types

Arm anticipates that the SMMU will access all in-memory structures and queues in a manner that does not require software cache maintenance of the PE caches. Arm expects that this be IO-coherent access to normal shared memory, but in implementations that cannot support cache coherency, this might be non-cached access. Some Embedded Implementations might require use of memory mapped addresses as non-cached by the PEs, see section 3.16 Embedded Implementations below. The degree to which the different memory access types and attributes are supported is IMPLEMENTATION DEFINED.

All in-memory structures and queues are accessed using Normal memory types. Configuration fields exist for Stream table, Context Descriptor and translation table fetches to govern Cacheability and Shareability of such accesses. MSI writes can be configured to make Device-type accesses.

If hardware update of the Access flag or the dirty state of a page is supported, atomic access is required to update translation tables that are shared between the PE and SMMU. Support for atomic access using local monitors requires a fully-coherent interconnect port.

If the memory system supports Armv8.1 [2] atomic operations, the SMMU might support atomic updates without local monitors, and not require a fully-coherent port. Because different SMMU implementations might use different mechanisms for atomic update of the flags, and because local monitors require coherent cacheable access, behavior is IMPLEMENTATION DEFINED if hardware flag updates are enabled on translation tables configured to be accessed as Non-cacheable.

To limit complexity, the SMMU might respond to snoops from the system only as much as required for atomic updates to translation tables with local monitors, if required. This means that all other memory access by the SMMUmight be IO-coherent. That is, SMMU configuration caches are not required to be snooped by PE accesses. When configuration data structures are changed, software is required to issue invalidation commands to the SMMU.

The SMMU respects the same single-copy atomicity rules as PEs regarding 64-bit translation table descriptor accesses, or 128-bit translation table descriptor accesses if VMASv9-128 is in use.

When configured by software, that is when not fixed in Embedded Implementations, Arm recommends that the in-memory data structures and queues are treated as Normal memory cached by the PE when the SMMU implementation is able to access them IO-coherently.

Note: This might be useful to avoid explicit cache maintenance on the PE side. When an SMMU is not able to make IO-coherent access, a similar programming model might be achieved using normal non-cached mappings from the PE.

Note: The configuration structure invalidation commands might be used by a hypervisor to maintain coherency between guest and shadow structures that it might use.

When a system supports IO-coherent accesses from the SMMU for access to configuration structures, translation tables, queues and CMD\_SYNC, GERROR, Event queue and PRI queue MSIs, this is presented to software using SMMU\_IDR0.COHACC == 1. If a system does not support IO-coherent access from the SMMU, SMMU\_IDR0.COHACC must be 0.

## 3.15.1 Client devices

SMMU translation is supported for Cache maintenance operations sent from client devices into the system. TLB-maintenance operations sent from client devices into the system are not permitted and are never propagated by the SMMU.

SMMU clients might contain caches that are fully-coherent with the rest of the system. Fully-coherent traffic uses physical addresses for both memory and snoop requests on either direction. For example, client access to the cache and writebacks from the cache might use addresses that were obtained from the SMMU using ATS or obtained from a TLB in the client that is filled from the SMMU. The latter case might arise where an SMMU is implemented as part of a complex device.

Devices might contain caches that do not support hardware coherency and which might be filled using non-physical addresses through an SMMU.

In distributed systems, different client devices might have different paths through the SMMU into the system, and these can differ in their ability to perform IO-coherent access. These paths might also differ from those used by the SMMUfor its own configuration access, hence SMMU\_IDR0.COHACC does not indicate whether client devices can also make IO-coherent accesses. Arm recommends that whether a given client device is capable of performing IO-coherent access is described to system software in a system-specific manner.

## 3.15.1.1 Fully-coherent client devices

For a fully-coherent SMMU client the following behaviors apply:

- Granule protection checks (GPC) apply to fully-coherent requests.
- DPT checks apply to fully-coherent requests, with the following exception:
- -The DPT W bit is permitted to be treated as 1 for a fully-coherent client, where this is required by the coherency protocol.
- Client-originated snoop requests bypass the SMMU and are not subject to DPT checks or GPC. Such requests might be terminated by a system-specific policy.
- -Note: The forwarding of snoop requests from the system to an SMMU fully-coherent client is IMPLEMENTATION DEFINED and must meet the security requirements of the system.
- A fully-coherent SMMU client is permitted to be either a StreamID client or a NoStreamID client.

Related definitions in this context:

- A client-originated fully-coherent request allows a cache line to be allocated into a coherent cache in an SMMUclient, or relates to a previously allocated cache line.
- A client-originated snoop request allows retrieving cache line data and/or modifying cache line state at a coherent cache, for cache lines that are managed by a home agent in an SMMU client.
- -Note: An SMMU client device might include a home agent in cases where the device is the backing store for memory that is coherently accessible to observers in the system.