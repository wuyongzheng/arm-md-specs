## Chapter 14 External interfaces

## 14.1 Data path ingress/egress ports

Along with read/write data/address, the following information is supplied with an incoming transaction:

- StreamID
- Optionally, SubstreamID (PASID) and a SubstreamID-Valid flag, SSV.
- StreamID is qualified by a SEC\_SID identifier to indicate the Security state of the StreamID. If the SMMU supports only Non-secure state, then SEC\_SID might be absent and it is treated as always Non-secure.
- StreamID is passed through the SMMU into the memory system, to create a DeviceID that enables the GICv3 ITS to differentiate interrupts by stream.
- -An internal StreamID is generated for MSIs originating from the SMMU.
* Note: The StreamID generated for MSIs must have a different value to those associated with client devices, so that the GICv3 ITS can differentiate SMMU MSIs from those originating from client devices.
- ATS Translated/Untranslated tag to control bypass.
- Instruction/Data/NS permission attributes and Memory type/Shareability/allocation hints from upstream device (optional, can be overridden in STE). See Chapter 13 Attribute Transformation .

If the ability to perform HTTU atomic updates using local monitors is required, the SMMU would need to attach to the system using a fully-coherent interconnect port. However, if HTTU is not implemented or the downstream system provides far atomic facilities which do not require a fully-coherent port, an IO-coherent interconnect port might be used.

As the SMMU does not translate outgoing coherency or broadcast invalidation traffic, there is no requirement to

## Chapter 14. External interfaces

## 14.1. Data path ingress/egress ports

use an interconnect supporting cache coherency or DVM between the SMMU and client devices. Client devices might connect to the SMMU using an IO-coherent interconnect port.