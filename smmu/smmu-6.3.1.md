## 6.3.1 SMMU\_IDR0

The SMMU\_IDR0 characteristics are:

## Purpose

Provides information about the features implemented for the SMMU Non-secure programming interface.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_IDR0 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bit [31]

Reserved, RES0.

## RME\_IMPL, bit [30]

Indicates support for SMMUv3.3-RME\_IMPL.

| RME_IMPL   | Meaning                                                                                                                                                           |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | RME features not supported for Non-secure, Secure or Realm programming interfaces.                                                                                |
| 0b1        | RME features supported for Non-secure programming interface, for Secure programming interface if implemented, and for Realm programming interface if implemented. |

If this field is 1, it is possible to report each of F\_STE\_FETCH, F\_CD\_FETCH, F\_VMS\_FETCH, and F\_WALK\_EABT with GPCF == 1 in Event queues.

If this field is 1, then SMMU\_ROOT\_IDR0.ROOT\_IMPL is 1.

## Bit [29]

Reserved, RES0.

## ST\_LEVEL, bits [28:27]

Multi-level Stream table support.

| ST_LEVEL   | Meaning                                                            |
|------------|--------------------------------------------------------------------|
| 0b00       | Linear Stream table supported.                                     |
| 0b01       | 2-level Stream table supported in addition to Linear Stream table. |
| 0b1x       | Reserved.                                                          |

## TERM\_MODEL, bit [26]

Terminate model behavior.

| TERM_MODEL   | Meaning                                                                                                                                                                                                                                                                                             |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | CD.A flag determines Abort or RAZ/WI behavior of a terminated transaction. • The act of terminating a transaction might be configured using the CD.A flag to successfully complete the transaction with RAZ/WI behavior or abort the transaction. Terminating a transaction with RAZ/WI behavior is |
| 0b1          | not supported, CD.A must be 1. • This means that a terminated transaction will always be aborted.                                                                                                                                                                                                   |

## STALL\_MODEL, bits [25:24]

Stall model support.

| STALL_MODEL   | Meaning                                                                                                                                     |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00          | Stall and Terminate models supported.                                                                                                       |
| 0b01          | Stall is not supported, all faults terminate transaction and STE.S2S and CD.S must be 0. • CMD_RESUME and CMD_STALL_TERM are not available. |
| 0b10          | Stall is forced (all faults eligible to stall cause stall), STE.S2S and CD.S must be 1.                                                     |
| 0b11          | Reserved.                                                                                                                                   |

- Note: STE.S2S must be in the states above only if stage 2 translation was enabled.
- When SMMU\_S\_IDR1.SECURE\_IMPL == 0, this field reports whether an implementation supports the Stall model.

When SMMU\_S\_IDR1.SECURE\_IMPL == 1, this field reports SMMU\_S\_IDR0.STALL\_MODEL unless SMMU\_S\_IDR0.STALL\_MODEL == 0b00 and SMMU\_S\_CR0.NSSTALLD == 1 in which case Non-secure use of Stall is prevented and this field's value is 0b01 . See section 3.12 Fault models, recording and reporting .

- Note: When SMMU\_S\_IDR1.SECURE\_IMPL == 1, this field is related to SMMU\_S\_IDR0.STALL\_MODEL and might be modified by SMMU\_S\_CR0.NSSTALLD. See section 3.12 Fault models, recording and reporting .

- Note: An SMMU associated with a PCI system must not have STALL\_MODEL == 0b10 .

## ATSRECERR, bit [23]

Indicates support for recording Configuration-related errors for ATS and PRI.

| ATSRECERR   | Meaning                                                                              |
|-------------|--------------------------------------------------------------------------------------|
| 0b0         | SMMUsupports recording only the base set of Events for ATS-related and PRI requests. |
| 0b1         | SMMUsupports recording some additional Events for ATS-related and PRI requests.      |

See section 3.9.1.2 Responses to ATS Translation Requests and section 8.1 PRI queue overflow for details of which events are recorded or not.

See SMMU\_CR2.REC\_CFG\_ATS for control details.

This bit is RES0 if SMMU\_IDR0.ATS == 0.

## TTENDIAN, bits [22:21]

Endianness support for translation table walks.

| TTENDIAN   | Meaning                                                                                                                     |
|------------|-----------------------------------------------------------------------------------------------------------------------------|
| 0b00       | Mixed-endian: CD.ENDI and STE.S2ENDI are each permitted to select either endianness, and do not have to have the same value |
| 0b01       | Reserved                                                                                                                    |
| 0b10       | Little-endian: CD.ENDI and STE.S2ENDI must select little-endian                                                             |
| 0b11       | Big-endian: CD.ENDI and STE.S2ENDI must select big-endian                                                                   |

- Arm strongly recommends that a general-purpose SMMU implementation supports mixed-endian translation table walks.

## VATOS, bit [20]

Virtual ATOS page interface supported.

| VATOS   | Meaning                                                                                                                        |
|---------|--------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Virtual ATOS page interface not supported.                                                                                     |
| 0b1     | Virtual ATOS page interface supported. • ATOS must also be supported • Stage 1 and stage 2 translation must also be supported. |

## CD2L, bit [19]

2-level Context descriptor table supported.

| CD2L   | Meaning                         |
|--------|---------------------------------|
| 0b0    | 2-level CD table not supported. |
| 0b1    | 2-level CD table supported.     |

## VMID16, bit [18]

16-bit VMID supported.

| VMID16   | Meaning                                                                                               |
|----------|-------------------------------------------------------------------------------------------------------|
| 0b0      | 16-bit VMID not supported. • VMID[15:8] is RES0 in command parameters and must be zero in STE.S2VMID. |
| 0b1      | 16-bit VMID supported.                                                                                |

- Note: The value of this field is irrelevant to software unless SMMU\_IDR0.S2P == 1.

## VMW, bit [17]

VMID wildcard-matching supported for TLB invalidation.

| VMW   | Meaning                                                    |
|-------|------------------------------------------------------------|
| 0b0   | VMID wildcard-matching not supported for TLB invalidation. |
| 0b1   | VMID wildcard-matching supported for TLB invalidation.     |

- When SMMU\_IDR0.S2P == 0 this field is RES0

## PRI, bit [16]

Page Request Interface supported.

| PRI   | Meaning                                                                        |
|-------|--------------------------------------------------------------------------------|
| 0b0   | Page Request Interface not supported • All SMMU_PRIQ_* registers are Reserved. |
| 0b1   | Page Request Interface supported                                               |

- When SMMU\_IDR0.ATS == 0 this field is RES0.
- See section 3.9 Support for PCI Express, PASIDs, PRI, and ATS .

## ATOS, bit [15]

Address Translation Operations supported.

| ATOS   | Meaning                                                                                                                  |
|--------|--------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Address Translation Operations not supported. • SMMU_IDR0.VATOS is RES0 and all SMMU_(S_)GATOS_* registers are Reserved. |

| ATOS   | Meaning                                  |
|--------|------------------------------------------|
| 0b1    | Address Translation Operations supported |

## SEV, bit [14]

SMMU, and system, support generation of WFE wake-up events to PE.

| SEV   | Meaning                                                                                                                                        |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | SMMU, and system, do not support generation of WFE wake-up events to PE.                                                                       |
| 0b1   | SMMU, and system, support generation of WFE wake-up events to PE. • Note: WFE might be used on the PE to wait for CMD_SYNC command completion. |

- This bit must reflect the ability of the system, and SMMU implementation, to convey events to all PEs that are expected to run SMMU maintenance software.

## MSI, bit [13]

Message Signalled Interrupts are supported.

| MSI   | Meaning                                                                                                                                                         |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The implementation supports wired interrupt notifications only. • The MSI fields in SMMU_EVENTQ_IRQ_CFGn, SMMU_PRIQ_IRQ_CFGn and SMMU_GERROR_IRQ_CFGn are RES0. |
| 0b1   | Message Signalled Interrupts are supported.                                                                                                                     |

- Note: The SMMU\_PRIQ\_IRQ\_CFG2.LO bit is not affected by whether MSIs are implemented or not.

## ASID16, bit [12]

16-bit ASID support.

| ASID16   | Meaning                                                                                                                      |
|----------|------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | 16-bit ASID not supported. • ASID[15:8] is RES0 in command parameters and must be zero in CD.ASID. 16-bit ASID is supported. |
| 0b1      |                                                                                                                              |

Note: The value of this bit is irrelevant to software unless SMMU\_IDR0.S1P == 1.

## NS1ATS, bit [11]

Split-stage (stage 1-only) ATS not supported.

| NS1ATS   | Meaning                                   |
|----------|-------------------------------------------|
| 0b0      | Split-stage (stage 1-only) ATS supported. |

| NS1ATS   | Meaning                                                                                                                 |
|----------|-------------------------------------------------------------------------------------------------------------------------|
| 0b1      | Split-stage (stage 1-only) ATS not supported. • Split-stage ATS set by STE.EATS == 0b10 is not supported. See STE.EATS. |

- RES0 when SMMU\_IDR0.ATS == 0 or SMMU\_IDR0.S1P == 0 or SMMU\_IDR0.S2P == 0.
- Note: The value of this field is only relevant to software when ATS and both stages of translation are supported.
- See section 3.9 Support for PCI Express, PASIDs, PRI, and ATS .

## ATS, bit [10]

PCIe ATS supported by SMMU.

| ATS   | Meaning                         |
|-------|---------------------------------|
| 0b0   | PCIe ATS not supported by SMMU. |
| 0b1   | PCIe ATS supported by SMMU.     |

- The support provided by an implementation for ATS and PRI influences interpretation of STE.EATS, ATS and PRI-related commands and SMMU\_PRIQ\_* registers. It does not guarantee that client devices and intermediate components also support ATS and this must be determined separately.

See section 3.9 Support for PCI Express, PASIDs, PRI, and ATS .

## Hyp, bit [9]

Hypervisor stage 1 contexts supported.

This flag indicates whether TLB entries might be tagged as EL2/EL2-E2H - see STE.STRW.

| Hyp   | Meaning                                    |
|-------|--------------------------------------------|
| 0b0   | Hypervisor stage 1 contexts not supported. |
| 0b1   | Hypervisor stage 1 contexts supported.     |

RES0 when S1P == 0 or S2P == 0.

- Arm recommends the implementation of Hyp/EL2 support when S1P == 1 &amp;&amp; S2P == 1, that is when both stages of translations are supported.

Note: The Hyp bit indicates support for Non-secure EL2 only. If the Secure state is supported, SMMU\_S\_IDR1.SEL2 indicates support for both S-EL2 and Secure stage 2.

Note: There is no SMMU equivalent of the Armv8.4 [2] SCR\_EL3.EEL2 flag to enable Secure EL2.

Hyp == 1 is mandatory in implementations of SMMUv3.2 or later, if S1P == 1 and S2P == 1.

## DORMHINT, bit [8]

Dormant Hint supported.

| DORMHINT   | Meaning                     |
|------------|-----------------------------|
| 0b0        | Dormant hint not supported. |
| 0b1        | Dormant hint supported.     |

## HTTU, bits [7:6]

H/W translation table Access flag and Dirty state of the page updates supported.

| HTTU   | Meaning                                                                       |
|--------|-------------------------------------------------------------------------------|
| 0b00   | No flag updates supported.                                                    |
| 0b01   | Access flag update supported.                                                 |
| 0b10   | Access flag and Dirty state of the page update supported.                     |
| 0b11   | Access flag and Dirty state, and Access flag for Table descriptors supported. |

- This field reflects the ability of the system, and SMMU implementation, to support hardware update.

Note: HTTU is a feature of an SMMU implementation, but the system design also bears upon whether HTTU can be supported.

For instance, HTTU requires coherent atomic updates to translation table data which need to be supported by an external interconnect.

An SMMU that internally supports HTTU but does not have requisite system support must mark HTTU as 0b00 in this field.

## BTM, bit [5]

Broadcast TLB Maintenance. Indicates support for receiving broadcast TLBI operations issued by Arm PEs in the system.

| BTM   | Meaning                                  |
|-------|------------------------------------------|
| 0b0   | Broadcast TLB maintenance not supported. |
| 0b1   | Boradcast TLB maintenance supported.     |

- This bit reflects the ability of the system, and SMMU implementation, to support broadcast maintenance. If either the SMMU, or the system, or the interconnect cannot fully support broadcast TLB maintenance, this bit reads as 0.

## COHACC, bit [4]

Coherent access supported to translations, structures and queues.

| COHACC   | Meaning                                                                   |
|----------|---------------------------------------------------------------------------|
| 0b0      | Coherent access for translations, structures and queues is not supported. |

| COHACC   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1      | IO-coherent access is supported for: • Translation table walks. • Fetches of L1STD, STE, L1CD and CD. • Command queue, Event queue and PRI queue access. • GERROR, CMD_SYNC, Event queue and PRI queue MSIs, if supported. • Whether a specific access is performed in a cacheable shareable manner is dependent on the access type configured for access to structures, queues and translation table walks. |

- This bit reflects the ability of the system, and SMMU implementation, to support IO-Coherent access to memory shared coherently with the PE. If either the SMMU or system cannot fully support IO-coherent access to SMMU structures/queues/translations, this reads as 0.
- Note: This bit only pertains to accesses made directly by the SMMU in response to internal operations. It does not indicate that transactions from client devices are also IO-coherent, this capability must be determined in a system-specific manner, for example using the CCA field specified in the IO Remapping Table [9].
- Note: For embedded implementations using preset tables or queues, this bit only pertains to accesses made outside of the preset structures.

## TTF, bits [3:2]

Translation table formats supported at both stage 1 and stage 2.

| TTF   | Meaning                       |
|-------|-------------------------------|
| 0b00  | Reserved.                     |
| 0b01  | VMSAv8-32 LPAE.               |
| 0b10  | VMSAv8-64.                    |
| 0b11  | VMSAv8-32 LPAE and VMSAv8-64. |

TTF[0] is 0 in implementations where either SMMU\_IDR3.DPT is 1 or SMMU\_R\_IDR3.DPT is 1.

## S1P, bit [1]

Stage1 translation supported.

| S1P   | Meaning                            |
|-------|------------------------------------|
| 0b0   | Stage 1 translation not supported. |
| 0b1   | Stage 1 translation supported.     |

## S2P, bit [0]

Stage2 translation supported.

| S2P   | Meaning                            |
|-------|------------------------------------|
| 0b0   | Stage 2 translation not supported. |
| 0b1   | Stage 2 translation supported.     |

## Accessing SMMU\_IDR0

Accesses to this register use the following encodings:

Accessible at offset 0x0000 from SMMUv3\_PAGE\_0

Accesses to this register are RO.