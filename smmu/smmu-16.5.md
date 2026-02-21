## 16.5 System software

Note: Software must:

- Not assume that both stage 1 and stage 2 are implemented.
- Support systems in which broadcast TLB invalidation messages are not supported so do not invalidate SMMU TLB entries, that is fall back to software TLB invalidation messages.
- Discover StreamID and SubstreamID sizes and capabilities.
- Probe SMMU\_IDR1 for PRESET configuration table and queue base pointers, only allocating memory for pointers that require initialization.
- Discover the maximum table sizes of the SMMU rather than using fixed-size tables.
- Not make assumptions about which SMMU Security state or states it is interacting with, and not make assumptions about which Security states are supported in the SMMU.
- Present system-specific StreamIDs as part of firmware descriptions for each device, as the StreamIDs associated with a physical device are system-specific.
- Ensure that when HTTU is not used, descriptors mapping DMA memory are marked Accessed (and not Read-Only, if DMA writes are expected) in order to avoid faults.