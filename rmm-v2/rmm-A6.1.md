## A6.1 Realm interrupts

This section describes the programming model for a REC's GIC CPU interface.

On REC entry, the values of the following registers are preserved:

- ICH\_AP0R&lt;n&gt;\_EL2
- ICH\_AP1R&lt;n&gt;\_EL2
- ICH\_LR&lt;n&gt;\_EL2
- ICH\_VMCR\_EL2
- ICH\_HCR\_EL2

REC entry fails if ICH\_LR&lt;n&gt;\_EL2.HW == '1' for any implemented value of n .

The GICv3 architecture states that, if HW == '1' then the virtual interrupt must be linked to a physical interrupt whose state is Active, otherwise behavior is undefined. The RMM is unable to validate that invariant, so it imposes the constraint that HW == '0' .

A REC exit due to IRQ is not generated for an interrupt which is masked by the value of ICC\_PMR\_EL1 at the time of REC entry.

On REC exit, the values of the following registers are preserved:




· ICH\_AP0R&lt;n&gt;\_EL2 · ICH\_AP1R&lt;n&gt;\_EL2 · ICH\_LR&lt;n&gt;\_EL2 · ICH\_VMCR\_EL2 · ICH\_HCR\_EL2 On REC exit, ICH\_HCR\_EL2.En == '0' . Disabling the virtual GIC CPU interface ensures that the caller does not receive unexpected GIC maintenance interrupts. A stronger constraint, for example stating that all GIC virtualization control system registers are zero on REC exit, was considered. However, this was rejected on the basis that it may preclude future optimisations, such as returning early from execution of RMI\_REC\_ENTER, without needing to first write zero to all GIC virtualization control system registers, if an interrupt is pending. Realm write access to any of the following registers results in a REC exit due to System register access:

- ICC\_ASGI1R\_EL1
- ICC\_SGI0R\_EL1
- ICC\_SGI1R\_EL1

Realm access to ICC\_*\_EL1 except for the following registers results in a REC exit due to System register access if the corresponding trap was set in ICH\_HCR\_EL2 at the time of the REC entry:

- ICC\_ASGI1R\_EL1
- ICC\_SGI0R\_EL1
- ICC\_SGI1R\_EL1

## See also:

- Arm Generic Interrupt Controller (GIC) Architecture Specification version 3 and version 4 [6]
- A4.2 REC entry
- A4.3 REC exit
- A10.4 Planes interrupts
- B4.5.14 RMI\_FEATURES command
- B4.5.51 RMI\_REC\_ENTER command
- B4.6.64 RmiRecEnter type
- B4.6.66 RmiRecExit type
- D1.6.1 Interrupt flow