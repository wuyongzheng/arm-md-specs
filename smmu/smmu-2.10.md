## 2.10 System placement

Figure 2.2: SMMU placement in an example system

<!-- image -->

Two example uses of an SMMU are shown in Figure 2.2. One SMMU interfaces incoming traffic from two client devices to the system interconnect. The devices can perform DMA using virtual, IPA or other bus address schemes and the SMMU translates these addresses to PAs. The second example SMMU interfaces one to one to a PCIe Root Complex (which itself hosts a network of devices). This illustrates an additional interface specified in this specification, an ATS port to support PCIe ATS and PRI (or similar functionality for compatible non-PCIe devices).

Outgoing accesses to the system interconnect and Completer devices do not pass through an additional SMMU. In general, Requesters are behind an SMMU (or, in the case of PEs, have an inbuilt MMU), so outgoing accesses to the system interconnect and Completer devices are mediated by the MMU of the Requester. If a Requester has no MMU, it has full-system access. Therefore, its DMA must be mediated by software, and in this case only the most privileged system software can program it.

In this specification, a Requester associated with an SMMU is referred to as a client device of the SMMU.

The SMMU has a programming interface that receives accesses from system software for setup and maintenance. The SMMU also makes accesses of its own (as a Requester) to configuration structures, for example to perform translation table walks. Whether the traffic originating from the SMMU itself shares the same interconnect resources as traffic passed through from device clients is IMPLEMENTATION SPECIFIC.

Each SMMU is configured separately to any others that might exist in the system.

Note: Arm recommends that SMMUs bridge I/O device DMA addresses onto system or physical addresses.

Arm recommends that SMMUs are placed between a device Requester port (or I/O interconnect) and system interconnect. Generally, Arm recommends that SMMUs are not placed in series and that the path of an SMMU to memory or other Completer devices does not pass through another SMMU, whether for fetch of SMMU configuration data or client transactions.

Note: Interconnect-specific channels to support cache coherency are not shown in Figure 2.2.

The SMMU interface to the system interconnect is intended to be IO-coherent, and provide either IO-coherent or fully-coherent access for the client devices of the SMMU.

Note: It is feasible to implement an SMMU as part of a complex device containing fully coherent caches in the same way that the MMU of a PE is paired to fully coherent PE caches. Practically, this means the caches must be tagged with physical addresses.

Figure 2.3: Example SMMU implementations

<!-- image -->

Figure 2.3 shows three example implementations of SMMU.

- SMMUAisimplemented as part of a complex device, providing translation for accesses from that device only. Arm expects this implementation to have an SMMU programming interface in addition to device-specific control. This design can provide dedicated contention-free translation and TLBs.
- SMMUBis a monolithic block that combines translation, programming interface and translation table walk facilities. Two client devices use this SMMU as their path for DMA into the system.
- SMMUCis distributed and provides multiple paths into the system for higher bandwidth. It comprises of:
- -A central translation table walker, which has its own Requester interface to fetch translation and configuration structures and queues and a Completer interface to receive programming accesses. This

unit might contain a macro-TLB and caches of configuration.

* The central translation table walker also provides an ATS interface to the Root Complex, so that the PCIe Devices can use ATS to make translation requests through to the central unit.
- -Remote TLB units which, on a miss, make translation requests to the central unit and cache the results locally. Two units are shown, supporting a set of three devices through one port, and a PCIe Root Complex through another.
- Finally, a smart device is shown, which embeds a TLB and makes translation requests to the central unit of SMMUC. To software, this looks identical to a simple device connected behind a discrete TLB unit. This design provides a dedicated TLB for the device, but uses the programming interface and translation facilities of the central unit, reducing complexity of the device.

In all cases, it appears to software as though a device is connected behind a logically-separate SMMU (similar to Device 0/1 on SMMU B). All implementations give the illusion of simple read/write transactions arriving from a client device to a discrete SMMU, even if physically it is the device performing the read/write transactions directly into the system, using translations provided by an SMMU.

Note: This allows a single SMMU driver to be used for radically different SMMU implementations.

Note: Devices might integrate a TLB, or whole SMMU, for performance reasons, but a closely-coupled TLB might also be used to provide physical addresses suitable for fully coherent device caches.

Regardless of the implementation style, this specification uses the abstraction of client device transactions arriving at an SMMU. The boundary of SMMU might contain a single module or several distributed subcomponents but these must all behave consistently.