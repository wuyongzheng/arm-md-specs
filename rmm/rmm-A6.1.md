## A6.1 Realm interrupts

This section describes the programming model for a REC's GIC CPU interface.

- DXZVGB The value of enter.gicv3\_lrs[n] is valid if all of the following are true:
- The value is an architecturally valid encoding of ICH\_LR&lt;n&gt;\_EL2 according to Arm Generic Interrupt Controller (GIC) Architecture Specification version 3 and version 4 [5].
- HW == '0' .
- XDMSDZ The GICv3 architecture states that, if HW == '1' then the virtual interrupt must be linked to a physical interrupt whose state is Active, otherwise behavior is undefined. The RMM is unable to validate that invariant, so it imposes the constraint that HW == '0' .
- DCPLDX The value of enter.gicv3\_hcr is valid if the value is an architecturally valid encoding of ICH\_HCR\_EL2 according to Arm Generic Interrupt Controller (GIC) Architecture Specification version 3 and version 4 [5].
- RHLFRY REC entry fails if the value of any enter.gicv3\_* attribute is invalid.
- RWNFRW On REC entry, ICH\_LR&lt;n&gt;\_EL2 is set to enter.gicv3\_lrs[n] , for all values of n supported by the PE.
- RWVGFJ On REC entry, the following fields in ICH\_HCR\_EL2 are set to the corresponding values in enter.gicv3\_hcr :
- UIE
- LRENPIE
- NPIE
- VGrp0EIE
- VGrp0DIE
- VGrp1EIE
- VGrp1DIE
- TDIR
- On REC entry, fields in enter.gicv3\_hcr must be set to '0' except for the following:
- UIE
- LRENPIE
- NPIE
- VGrp0EIE
- VGrp0DIE
- VGrp1EIE
- VGrp1DIE
- TDIR

If any other field in enter.gicv3\_hcr is set to '1', then RMI\_REC\_ENTER fails.

- XLMXCX The RMM provides access to the GIC virtual CPU interface to the Realm and therefore controls the enable bit and most trap bits in ICH\_HCR\_EL2 . The maintenance interrupt control bits are controlled by the Host, because the maintenance interrupts are provided as hints to the hypervisor to allocate List Registers optimally and to correctly emulate GICv3 behavior. The TDIR bit is also controlled by the Host because it is used when supporting EOImode == '1' in the Realm. This mode is used to allow deactivation of virtual interrupts across RECs. This deactivation must be handled by the Host because the RMM can only operate on a single REC during execution of RMI\_REC\_ENTER.
- RLNQRL A REC exit due to IRQ is not generated for an interrupt which is masked by the value of ICC\_PMR\_EL1 at the time of REC entry.
- UGXCHC The RMM should preserve the value of ICC\_PMR\_EL1 during REC entry.
- RNKPNC On REC exit, exit.gicv3\_vmcr contains the value of ICH\_VMCR\_EL2 at the time of the Realm exit.
- RSKQNF On REC exit, exit.gicv3\_misr contains the value of ICH\_MISR\_EL2 at the time of the Realm exit.

## Chapter A6. Realm interrupts and timers A6.1. Realm interrupts

- XDBGXB The Host could in principle infer the value of ICH\_MISR\_EL2 at the time of the Realm exit from the combination of exit.gicv3\_lrs[n] and exit.gicv3\_hcr . However, this would be cumbersome, error-prone, and diverge from the design of existing hypervisor software.
- RQKZXD On REC exit, exit.gicv3\_lrs[n] contains the value of ICH\_LR&lt;n&gt;\_EL2 at the time of the Realm exit, for all values of n supported by the PE.
- RSNVZH On REC exit, the following fields in exit.gicv3\_hcr contains the value of the corresponding field in ICH\_HCR\_EL2 at the time of the Realm exit:
- EOIcount
- UIE
- LRENPIE
- NPIE
- VGrp0EIE
- VGrp0DIE
- VGrp1EIE
- VGrp1DIE
- TDIR

All other fields contain zero.

- RFGQXT On REC exit, the values of the following registers may have changed:
- ICH\_AP0R&lt;n&gt;\_EL2
- ICH\_AP1R&lt;n&gt;\_EL2
- ICH\_LR&lt;n&gt;\_EL2
- ICH\_VMCR\_EL2
- ICH\_HCR\_EL2
- SQMJVJ It is the responsibility of the caller to save and restore GIC virtualization system control registers if their value needs to be preserved following execution of RMI\_REC\_ENTER.
- XKDGHF On REC entry, the values of the GIC virtualization control system registers are overwritten. The Non-secure hypervisor runs at EL2 and therefore does not make direct use of the virtual GIC CPU interface for its own execution. This means that saving / restoring the caller's GIC virtualization control system registers would typically not be required and would add additional runtime overhead for each execution of RMI\_REC\_ENTER.
- RVSBBS On REC exit, ICH\_HCR\_EL2.En == '0' .
- XWLTBX Disabling the virtual GIC CPU interface ensures that the caller does not receive unexpected GIC maintenance interrupts. A stronger constraint, for example stating that all GIC virtualization control system registers are zero on REC exit, was considered. However, this was rejected on the basis that it may preclude future optimisations, such as returning early from execution of RMI\_REC\_ENTER, without needing to first write zero to all GIC virtualization control system registers, if an interrupt is pending.

See also:

- Arm Generic Interrupt Controller (GIC) Architecture Specification version 3 and version 4 [5]
- A4.2 REC entry
- A4.3 REC exit
- B4.3.14 RMI\_REC\_ENTER command
- B4.4.14 RmiRecEnter type
- B4.4.16 RmiRecExit type
- D1.6.1 Interrupt flow