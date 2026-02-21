## 3.8 Virtualization

Devices can be put under direct guest control with stage 2-only mappings, without requiring guest interaction with the SMMU. To the guest OS, they appear as though the device is directly connected and might request DMA to PAs (IPAs) directly.

The SMMU does not provide programming interfaces for use directly by virtual machines. Arm expects that, where stage 1 facilities are required for use by a guest in virtualization scenarios, this is supported using hypervisor emulation of a virtual SMMU, or a similar interface for use by a virtual machine.

Implementations might provide an IMPLEMENTATION DEFINED number of extra hardware interfaces that are located in an IMPLEMENTATION DEFINED manner but are otherwise compatible with the SMMUv3 programming interface. Each interface might be mapped through to a guest VM for it to use directly, for example appearing as a stage 1-only interface to the guest while the hypervisor interface appears as stage 2-only. The management of such an implementation is beyond the scope of this specification.