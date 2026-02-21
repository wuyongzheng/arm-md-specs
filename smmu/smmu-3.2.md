## 3.2 Stream numbering

An incoming transaction has an address, size, and attributes such as read/write, Secure/Non-secure, Shareability, Cacheability. If more than one client device uses the SMMU traffic must also have a sideband StreamID so the sources can be differentiated. How a StreamID is constructed and carried through the system is IMPLEMENTATION DEFINED. Logically, a StreamID corresponds to a device that initiated a transaction.

Note: The mapping of a physical device to StreamID must be described to system software.

Arm recommends that StreamID be a dense namespace starting at 0. The StreamID namespace is per-SMMU. Devices assigned the same StreamID but behind different SMMUs are seen to be different sources. A device might emit traffic with more than one StreamID, representing data streams differentiated by device-specific state.

StreamID is of IMPLEMENTATION DEFINED size, between 0 bits and 32 bits.

The StreamID is used to select a Stream Table Entry (STE) in a Stream table, which contains per-device configuration. The maximum size of in-memory configuration structures relates to the maximum StreamID span (see 3.3 Data structures and translation procedure below), with a maximum of 2 StreamIDSize entries in the Stream table.

Another property, SubstreamID, might optionally be provided to an SMMU implementing stage 1 translation. The SubstreamID is of IMPLEMENTATION DEFINED size, between 0 bits and 20 bits, and differentiates streams of traffic originating from the same logical block to associate different application address translations to each.

Note: An example would be a compute accelerator with 8 contexts that might each map to a different user process, but where the single device has common configuration meaning it must be assigned to a VM whole.

Note: The SubstreamID is equivalent to a PCIe PASID. Because the concept can be applied to non-PCIe systems, it has been given a more generic name in the SMMU. The maximum size of SubstreamID, 20 bits, matches the maximum size of a PCIe PASID.

The incoming transaction flags whether a SubstreamID is supplied and this might differ on a per-transaction basis.

Both of these properties and sizes are discoverable through the SMMU\_IDR1 register. See section 16.4 System integration for recommendations on StreamID and SubstreamID sizing.

The StreamID is the key that identifies all configuration for a transaction. A StreamID is configured to bypass or be subject to translation and such configuration determines which stage 1 or stage 2 translation to apply. The SubstreamID provides a modifier that selects between a set of stage 1 translations indicated by the StreamID but has no effect on the stage 2 translation which is selected by the StreamID only.

A stage 2-only implementation does not take a SubstreamID input. An implementation with stage 1 is not required to support substreams, therefore is not required to take a SubstreamID input.

The SMMU optionally supports Secure state and, if supported, the StreamID input to the SMMU is qualified by a SEC\_SID flag that determines whether the input StreamID value refers to the Secure or Non-secure StreamID namespace. A Non-secure StreamID identifies an STE within the Non-secure Stream table and a Secure StreamID identifies an STE within the Secure Stream table. In this specification, the term StreamID implicitly refers to the StreamID disambiguated by SEC\_SID (if present) and does not refer solely to a literal StreamID input value (which would be associated with two STEs when Secure state is supported) unless explicitly stated otherwise. See section 3.10.2 Support for Secure state .

Arm expects that, for PCI, StreamID is generated from the PCI RequesterID so that StreamID[15:0] == RequesterID[15:0]. When more than one PCIe hierarchy is hosted by one SMMU, Arm recommends that the 16-bit RequesterID namespaces are arranged into a larger StreamID namespace by using upper bits of StreamID to differentiate the contiguous RequesterID namespaces, so that StreamID[N:16] indicates which Root Complex (PCIe domain/segment) is the source of the stream source. In PCIe systems, the SubstreamID is intended to be directly provided from the PASID [1] in a one to one fashion.

Therefore, for SMMU implementations intended for use with PCI clients, supported StreamID size must be at least 16 bits.