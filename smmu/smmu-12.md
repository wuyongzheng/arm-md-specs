## Chapter 12 Reliability, Availability and Serviceability (RAS)

Note: In this chapter, the term RAS fault is used to distinguish a fault in the sense defined by the RAS architecture from an SMMU translation fault.

The SMMU might support optional RAS features as part of the overall Arm RAS System Architecture, which is described in [11]. The Arm RAS System Architecture:

- Describes the following concepts:
- -Faults, errors, and failures.
- -Error correction, error propagation, poisoning, and error containment.
- Defines the following classifications for errors:
- -Corrected error (CE).
- -Deferred error (DE).
- -Uncorrected errors (UE), which are further classified as and Uncontainable (UC), Unrecoverable (UEU), Recoverable (UER), and Restartable (UEO) errors.
- Defines standards for:
- -Error recovery and fault handling interrupts.
- -A standard error record, with a memory-mapped interface for a group of error records for one or more components (nodes).

Arm recommends that SMMUv3 implementations that include RAS features implement RAS System Architecture , as specified in [11].

When supported, RAS fault handling registers according to the Arm RAS System Architecture are present, into which errors are recorded.

If the SMMU does not support RAS but the system does, it is possible for the SMMU to consume an external error which is presented to the SMMU driver software as an external abort.

The SMMU might, but is not required to, record errors that it does not itself consume or detect, such as those reported directly from the system to a client device, for example, a device reading a memory location that translates without issue, but ultimately causes the device to consume corrupt data.