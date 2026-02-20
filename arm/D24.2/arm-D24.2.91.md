## D24.2.91 ID\_AA64MMFR3\_EL1, AArch64 Memory Model Feature Register 3

The ID\_AA64MMFR3\_EL1 characteristics are:

## Purpose

Provides information about the implemented memory model and memory management support in AArch64 state.

## Configuration

Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64MMFR3\_EL1 are UNDEFINED.

## Attributes

ID\_AA64MMFR3\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63         | 60 59   | 56 55   | 52 51   | 48 47   | 44 43   | 40 39   | 36 35   | 32   |    |
|------------|---------|---------|---------|---------|---------|---------|---------|------|----|
| Spec_FPACC | ADERR   | SDERR   | RES0    | ANERR   | SNERR   | D128_2  |         | D128 |    |
| 31         | 28 27   | 24 23   | 20 19   | 16 15   | 12 11   | 8 7     | 4       | 3    | 0  |
| MEC        | AIE     | S2POE   | S1POE   | S2PIE   | S1PIE   |         | SCTLRX  | TCRX |    |

Spec\_FPACC, bits [63:60]

## When FEAT\_FPACCOMBINE is implemented:

Speculative behavior in the event of a PAC authentication failure in an implementation that includes FEAT\_FPACCOMBINE.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Spec_FPACC   | Meaning                                                                                                                                                                                                                                                 |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000       | The implementation does not disclose whether the speculative use of pointers processed by a PAC Authentication is materially different in terms of the impact on cached microarchitectural state between passing and failing of the PAC Authentication. |
| 0b0001       | The speculative use of pointers processed by a PAC Authentication is not materially different in terms of the impact on cached microarchitectural state between passing and failing of the PAC Authentication.                                          |

All other values are reserved.

For the purpose of this definition, cached microarchitecture state is the state of caching agents such as instruction caches, data caches and TLBs which can be altered as a result of speculation caused by a mispredicted execution, but is not restored to the state prior to the speculation when the misprediction is corrected.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## ADERR, bits [59:56]

Asynchronous Device error exceptions. With ID\_AA64MMFR3\_EL1.SDERR, describes the PE behavior for External aborts signaled on Device memory loads.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ADERR   | Meaning                                                                                                                                                                                                                                                                                                      |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000  | If FEAT_RASv2 is not implemented and ID_AA64MMFR3_EL1.SDERR is 0b0000 , then the behavior is not described. Otherwise, the behavior is described by ID_AA64MMFR3_EL1.SDERR.                                                                                                                                  |
| 0b0001  | All External aborts on Device memory loads are handled asynchronously.                                                                                                                                                                                                                                       |
| 0b0010  | FEAT_ADERR is implemented. SCTLR2_ELx.EnADERR and HCRX_EL2.EnSDERR are implemented. If FEAT_ANERR is also implemented, then software should ensure that all the following apply: • SCTLR2_ELx.EnADERR is set to the value of SCTLR2_ELx.EnANERR. • HCRX_EL2.EnSDERR is set to the value of HCRX_EL2.EnSNERR. |
| 0b0011  | FEAT_ADERR is implemented. SCTLR2_ELx.EnADERR and HCRX_EL2.EnSDERR are implemented. If FEAT_ANERR is also implemented, then SCTLR2_ELx.EnADERR and HCRX_EL2.EnSDERR operate independently of SCTLR2_ELx.EnANERR and HCRX_EL2.EnSNERR.                                                                        |

All other values are reserved.

Implementation-specific exceptions to applications of this field are described in 'Taking error exceptions'.

When FEAT\_RASv2 is implemented and ID\_AA64MMFR3\_EL1.SDERR is 0b0000 , the value of this field is 0b0001 .

When ID\_AA64MMFR3\_EL1.SDERR is 0b0001 , the value of this field is 0b0000 .

When ID\_AA64MMFR3\_EL1.SDERR is 0b0010 , the value of this field is 0b0010 .

When ID\_AA64MMFR3\_EL1.SDERR is 0b0011 , the value of this field is 0b0011 .

FEAT\_ADERR implements the functionality described by the value 0b0010 .

Access to this field is RO.

## SDERR, bits [55:52]

Synchronous Device error exceptions. With ID\_AA64MMFR3\_EL1.ADERR, describes the PE behavior for External aborts signaled on Device memory loads.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SDERR   | Meaning                                                                                                                                                                     |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000  | If FEAT_RASv2 is not implemented and ID_AA64MMFR3_EL1.ADERR is 0b0000 , then the behavior is not described. Otherwise, the behavior is described by ID_AA64MMFR3_EL1.ADERR. |
| 0b0001  | All External aborts on Device memory loads are handled synchronously.                                                                                                       |

| SDERR   | Meaning                                                                                                                                                                                                                                                                                                      |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0010  | FEAT_ADERR is implemented. SCTLR2_ELx.EnADERR and HCRX_EL2.EnSDERR are implemented. If FEAT_ANERR is also implemented, then software should ensure that all the following apply: • SCTLR2_ELx.EnADERR is set to the value of SCTLR2_ELx.EnANERR. • HCRX_EL2.EnSDERR is set to the value of HCRX_EL2.EnSNERR. |
| 0b0011  | FEAT_ADERR is implemented. SCTLR2_ELx.EnADERR and HCRX_EL2.EnSDERR are implemented. If FEAT_ANERR is also implemented, then SCTLR2_ELx.EnADERR and HCRX_EL2.EnSDERR operate independently of SCTLR2_ELx.EnANERR and HCRX_EL2.EnSNERR.                                                                        |

All other values are reserved.

Implementation-specific exceptions to applications of this field are described in 'Taking error exceptions'.

When FEAT\_RASv2 is implemented and ID\_AA64MMFR3\_EL1.ADERR is 0b0000 , the value of this field is 0b0001 .

When ID\_AA64MMFR3\_EL1.ADERR is 0b0001 , the value of this field is 0b0000 .

When ID\_AA64MMFR3\_EL1.ADERR is 0b0010 , the value of this field is 0b0010 .

When ID\_AA64MMFR3\_EL1.ADERR is 0b0011 , the value of this field is 0b0011 .

FEAT\_ADERR implements the functionality described by the value 0b0010 .

Access to this field is RO.

## Bits [51:48]

Reserved, RES0.

## ANERR, bits [47:44]

Asynchronous Normal error exceptions. With ID\_AA64MMFR3\_EL1.SNERR, describes the PE behavior for External aborts signaled on Normal memory loads.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ANERR   | Meaning                                                                                                                                                                                                                                                                                                      |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000  | If FEAT_RASv2 is not implemented and ID_AA64MMFR3_EL1.SNERR is 0b0000 , then the behavior is not described. Otherwise, the behavior is described by ID_AA64MMFR3_EL1.SNERR.                                                                                                                                  |
| 0b0001  | All External aborts on Normal memory loads are handled asynchronously.                                                                                                                                                                                                                                       |
| 0b0010  | FEAT_ANERR is implemented. SCTLR2_ELx.EnANERR and HCRX_EL2.EnSNERR are implemented. If FEAT_ADERR is also implemented, then software should ensure that all the following apply: • SCTLR2_ELx.EnANERR is set to the value of SCTLR2_ELx.EnADERR. • HCRX_EL2.EnSNERR is set to the value of HCRX_EL2.EnSDERR. |
| 0b0011  | FEAT_ANERR is implemented. SCTLR2_ELx.EnANERR and HCRX_EL2.EnSNERR are implemented. If FEAT_ADERR is also implemented, then SCTLR2_ELx.EnANERR and HCRX_EL2.EnSNERR operate independently of SCTLR2_ELx.EnADERR and HCRX_EL2.EnSDERR.                                                                        |

All other values are reserved.

Implementation-specific exceptions to applications of this field are described in 'Taking error exceptions'.

When FEAT\_RASv2 is implemented and ID\_AA64MMFR3\_EL1.SNERR is 0b0000 , the value of this field is 0b0001 .

When ID\_AA64MMFR3\_EL1.SNERR is 0b0001 , the value of this field is 0b0000 .

When ID\_AA64MMFR3\_EL1.SNERR is 0b0010 , the value of this field is 0b0010 .

When ID\_AA64MMFR3\_EL1.SNERR is 0b0011 , the value of this field is 0b0011 .

FEAT\_ANERR implements the functionality described by the value 0b0010 .

Access to this field is RO.

## SNERR, bits [43:40]

Synchronous Normal error exceptions. With ID\_AA64MMFR3\_EL1.ANERR, describes the PE behavior for External aborts signaled on Normal memory loads.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SNERR   | Meaning                                                                                                                                                                                                                                                                                                      |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000  | If FEAT_RASv2 is not implemented and ID_AA64MMFR3_EL1.ANERR is 0b0000 , then the behavior is not described. Otherwise, the behavior is described by ID_AA64MMFR3_EL1.ANERR.                                                                                                                                  |
| 0b0001  | All External aborts on Normal memory loads are handled synchronously.                                                                                                                                                                                                                                        |
| 0b0010  | FEAT_ANERR is implemented. SCTLR2_ELx.EnANERR and HCRX_EL2.EnSNERR are implemented. If FEAT_ADERR is also implemented, then software should ensure that all the following apply: • SCTLR2_ELx.EnANERR is set to the value of SCTLR2_ELx.EnADERR. • HCRX_EL2.EnSNERR is set to the value of HCRX_EL2.EnSDERR. |
| 0b0011  | FEAT_ANERR is implemented. SCTLR2_ELx.EnANERR and HCRX_EL2.EnSNERR are implemented. If FEAT_ADERR is also implemented, then SCTLR2_ELx.EnANERR and HCRX_EL2.EnSNERR operate independently of SCTLR2_ELx.EnADERR and HCRX_EL2.EnSDERR.                                                                        |

All other values are reserved.

Implementation-specific exceptions to applications of this field are described in 'Taking error exceptions'.

When FEAT\_RASv2 is implemented and ID\_AA64MMFR3\_EL1.ANERR is 0b0000 , the value of this field is 0b0001 .

When ID\_AA64MMFR3\_EL1.ANERR is 0b0001 , the value of this field is 0b0000 .

When ID\_AA64MMFR3\_EL1.ANERR is 0b0010 , the value of this field is 0b0010 .

When ID\_AA64MMFR3\_EL1.ANERR is 0b0011 , the value of this field is 0b0011 .

FEAT\_ANERR implements the functionality described by the value 0b0010 .

Access to this field is RO.

## D128\_2, bits [39:36]

128-bit translation table descriptor at stage 2. Indicates support for 128-bit translation table descriptor at stage 2.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| D128_2   | Meaning                                                                     |
|----------|-----------------------------------------------------------------------------|
| 0b0000   | 128-bit translation table descriptor Extension at stage 2 is not supported. |
| 0b0001   | 128-bit translation table descriptor Extension at stage 2 is supported.     |

All other values are reserved.

Access to this field is RO.

## D128, bits [35:32]

128-bit translation table descriptor. Indicates support for 128-bit translation table descriptor.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| D128   | Meaning                                                          |
|--------|------------------------------------------------------------------|
| 0b0000 | 128-bit translation table descriptor Extension is not supported. |
| 0b0001 | 128-bit translation table descriptor Extension is supported.     |

All other values are reserved.

Access to this field is RO.

## MEC, bits [31:28]

Indicates support for Memory Encryption Contexts.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MEC    | Meaning                                                                                              |
|--------|------------------------------------------------------------------------------------------------------|
| 0b0000 | Memory Encryption Contexts is not supported.                                                         |
| 0b0001 | Memory Encryption Contexts is supported, with multiple contexts in the Realm physical address space. |

All other values are reserved.

FEAT\_MEC implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## AIE, bits [27:24]

Attribute Indexing. Indicates support for the Attribute Index Enhancement.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AIE    | Meaning                                           |
|--------|---------------------------------------------------|
| 0b0000 | The Attribute Index Enhancement is not supported. |

| 0b0001   | The Attribute Index Enhancement at stage 1 is supported.   |
|----------|------------------------------------------------------------|

All other values are reserved.

FEAT\_AIE implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## S2POE, bits [23:20]

Stage 2 Permission Overlay. Indicates support for Permission Overlay at stage 2.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| S2POE   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0000  | Permission Overlay at stage 2 is not supported. |
| 0b0001  | Permission Overlay at stage 2 is supported.     |

All other values are reserved.

FEAT\_S2POE implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## S1POE, bits [19:16]

Stage 1 Permission Overlay. Indicates support for Permission Overlay at stage 1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| S1POE   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0000  | Permission Overlay at stage 1 is not supported. |
| 0b0001  | Permission Overlay at stage 1 is supported.     |

All other values are reserved.

FEAT\_S1POE implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## S2PIE, bits [15:12]

Stage 2 Permission Indirection. Indicates support for Permission Indirection at stage 2.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| S2PIE   | Meaning                                             |
|---------|-----------------------------------------------------|
| 0b0000  | Permission Indirection at stage 2 is not supported. |

| 0b0001   | Permission Indirection at stage 2 is supported.   |
|----------|---------------------------------------------------|

All other values are reserved.

FEAT\_S2PIE implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## S1PIE, bits [11:8]

Stage 1 Permission Indirection. Indicates support for Permission Indirection at stage 1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| S1PIE   | Meaning                                             |
|---------|-----------------------------------------------------|
| 0b0000  | Permission Indirection at stage 1 is not supported. |
| 0b0001  | Permission Indirection at stage 1 is supported.     |

All other values are reserved.

FEAT\_S1PIE implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## SCTLRX, bits [7:4]

SCTLR Extension. Indicates support for extension of SCTLR\_ELx.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SCTLRX   | Meaning                                                                                               |
|----------|-------------------------------------------------------------------------------------------------------|
| 0b0000   | SCTLR2_EL1, SCTLR2_EL2, SCTLR2_EL3 registers, and their associated trap controls are not implemented. |
| 0b0001   | SCTLR2_EL1, SCTLR2_EL2, SCTLR2_EL3 resisters, and their associated trap controls are implemented.     |

All other values are reserved.

From Armv8.9, the value 0b0000 is not permitted.

FEAT\_SCTLR2 implements the functionality described by the value 0b0001 .

Access to this field is RO.

## TCRX, bits [3:0]

TCR Extension. Indicates support for extension of TCR\_ELx.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TCRX   | Meaning                                                                     |
|--------|-----------------------------------------------------------------------------|
| 0b0000 | TCR2_EL1, TCR2_EL2, and their associated trap controls are not implemented. |
| 0b0001 | TCR2_EL1, TCR2_EL2, and their associated trap controls are implemented.     |

All other values are reserved.

From Armv8.9, the value 0b0000 is not permitted.

FEAT\_TCR2 implements the functionality described by the value 0b0001 .

Access to this field is RO.

## Accessing ID\_AA64MMFR3\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_AA64MMFR3\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0111 | 0b011 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_AA64MMFR3_EL1) || boolean ↪ → IMPLEMENTATION_DEFINED "ID_AA64MMFR3_EL1 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64MMFR3_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64MMFR3_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64MMFR3_EL1;
```