## 16.4 System integration

- The SMMU must be in the same Shareability domain as any other agents that might use DVM with the SMMU.
- -In systems implementing architectures prior to Armv8.4, DVM messages are only broadcast over the Inner Shareable domain.
- -Some systems implementing Armv8.4 may broadcast DVM messages over the Outer Shareable domain.
- In general, Arm does not expect SMMUs to be connected in series.

Note: This topology needs special software support, particularly when different software modules manage different SMMUs. This must not be used to construct two stages of translation using two SMMU implementations that support only one stage, as it is programmed differently to an SMMU that supports both stages.

- When used with a PCIe subsystem, an SMMU implementation must support at least the full (16-bit) range of PCI RequesterIDs and the system must ensure that a Root Complex generates StreamIDs from PCI RequesterIDs (BDF) in a one to one or linear fashion so that StreamID[15:0] == RequesterID[15:0]. A larger StreamID might be constructed by concatenating the RequesterIDs from multiple PCI domains (or 'segments' in ACPI terminology), for example:
- -StreamID[17:0] == { pci\_rc\_id[1:0], pci\_bus[7:0], pci\_dev[4:0], pci\_fn[2:0] };

that is, StreamID[17:0] == { pci\_domain[1:0], RequesterID[15:0] };

When used with a PCIe system supporting PASIDs, Arm recommends that the SMMU supports the same number of (or fewer) PASID bits supported by client Root Complexes so that software is able to detect end-to-end SubstreamID capabilities through the SMMU.

- If accesses from a device are expected to experience page faults and the Stall model is used, Arm recommends that a system does not depend on other devices on the same SMMU path as the device in order to resolve the faults. Because a stalled transaction occupies an input buffer resource, the SMMU might not guarantee to pass traffic whether faulting or not, and any new request for device DMA might deadlock.
- Streams belonging to PCIe endpoints must not be stalled. The Terminate model is the only useful option. Stalling PCIe transactions risks either timeouts from the PCIe endpoint (which might be difficult to recover from), or deadlock in certain scenarios. A system is permitted to enforce this, for safety reasons. See section 3.12 Fault models, recording and reporting .
- Specifically, PCIe traffic (especially if configured to Terminate, architecturally not stalling) must not be held up waiting for any PE action, including draining the Event queue or restarting stalled transactions. PCIe traffic must always make forward progress without unbounded delays dependent on software. An implementation must ensure that transactions to be terminated are not blocked by any other users of the SMMUwhich might consume resources or stall transactions for an indefinite time.

## 16.4.1 System integration for an SMMU with RME DA

## 16.4.1.1 StreamID

For a device interface that might operate in a trusted or untrusted mode (that is, such that SEC\_SID = Non-secure or Realm), the StreamID presented to the SMMU is the same across the two modes.

## 16.4.1.2 DeviceID

According to the PCIe specification regarding the TDISP feature [1], a TDISP-compliant device might issue MSIs in two manners:

1. If the MSI is configured via the MSI capability in configuration space, it is sent to the host SoC with T = 0 and therefore presented to the SMMU with SEC\_SID = Non-secure.
2. If the MSI is configured via the MSI-X capability in the protected MMIO region of the device interface, it is sent to the host SoC with T = 1 and therefore presented to the SMMU with SEC\_SID = Realm.

MSIs from a single device interface are presented to the GIC ITS interface with the same DeviceID regardless of which MSI mechanism is used.

Note: The target PA space of an MSI is determined from configuration in translation tables, the DPT and the configuration structures for the programming interface, StreamID and address for the target of the MSI, consistent with the behavior for any client-originated access. See 3.18 Interrupts and notifications , 3.10.1 StreamID Security state (SEC\_SID) , and 3.10.2 Support for Secure state .