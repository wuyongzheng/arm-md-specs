## 6.3.40 SMMU\_GATOS\_PAR

The SMMU\_GATOS\_PAR characteristics are:

## Purpose

Global ATOS translation results register.

This result register encodes both successful results and error results. The format is determined by the FAULT field.

## Configuration

This register is present only when SMMU\_IDR0.ATOS == 1. Otherwise, direct accesses to SMMU\_GATOS\_PAR are RES0.

## Attributes

SMMU\_GATOS\_PAR is a 64-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

## When SMMU\_GATOS\_PAR.FAULT == 0:

<!-- image -->

When FAULT == 0, a successful result is present:

## ATTR, bits [63:56]

Memory attributes, in MAIR format.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## ADDR, bits [55:12]

Result address, bits [55:12].

- Address bits above and below [55:12] are treated as zero.
- Bits above the implemented OA size, reported in SMMU\_IDR5.OAS, are RES0.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Size, bit [11]

Translation page/block size flag.

| Size   | Meaning                                                              |
|--------|----------------------------------------------------------------------|
| 0b0    | Translation is 4KB.                                                  |
| 0b1    | Translation is determined by position of lowest 1 bit in ADDR field. |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bit [10]

Reserved, RES0.

## SH, bits [9:8]

Shareability attribute.

| SH   | Meaning          |
|------|------------------|
| 0b00 | Non-shareable.   |
| 0b01 | Reserved.        |
| 0b10 | Outer Shareable. |
| 0b11 | Inner Shareable. |

- Note: Shareability is returned as Outer Shareable when ATTR selects any Device type.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [7:1]

Reserved, RES0.

## FAULT, bit [0]

Fault/error status.

| FAULT   | Meaning   |
|---------|-----------|
| 0b0     | No fault. |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information for When SMMU\_GATOS\_PAR.FAULT == 0

The Size field allows the size of the translation to be determined, using an encoding in the ADDR field.

The translated address is aligned to the translation size (appropriate number of LSBs zeroed) and then, if the size is greater than 4KB, a single bit is set such that its position, N, denotes the translation size, where 2 (N+1) == size in bytes.

Note: For example, if Size == 1 and ADDR[14:12] == 0 and ADDR[15] == 1, the lowest set bit is 15 so the translation size is 2 15+1 , or 64KB. In this case, the actual output address must be aligned to 64KB by masking out bit 15. Similarly, an output address with ADDR[13:12] == 0b10 denotes a page of size 2 13+1 , or 16KB, and the output address is taken from ADDR[14] upwards.

An implementation that does not support all of the defined attributes is permitted to return the behavior that the cache supports, instead of the exact value from the translation table entries. Similarly, an implementation might return the translation page/block size that is cached rather than the size that is determined from the translation table entries.

The memory attributes and Shareability that are returned in ATTR and SH are determined from the translation tables without including STE overrides that might be configured for the given stream:

- When ATOS\_ADDR.TYPE == stage 1, the stage 1 translation table attributes are returned.
- When ATOS\_ADDR.TYPE == stage 2, the stage 2 translation table attributes are returned. In this case, the allocation and transient hints in ATTR are:
- -RA == WA == 1.
- -TR == 0.
- -Note: The stage 2 TTD.MemAttr[3:0] field does not encode RA/WA/TR.
- When ATOS\_ADDR.TYPE == stage 1 and stage 2, the attributes returned are those from stage 1 combined with stage 2 (where combined is as defined in Chapter 13 Attribute Transformation ).

## When SMMU\_GATOS\_PAR.FAULT == 1:

<!-- image -->

When FAULT == 1, the translation has failed and a fault syndrome is present:

## IMPLEMENTATION DEFINED, bits [63:60]

IMPLEMENTATION DEFINED fault data.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [59:56]

Reserved, RES0.

## FADDR, bits [55:12]

Stage 2 fault page address, bits [55:12].

- The value returned in FADDR depends on the cause of the fault. See section 9.1.4 ATOS\_PAR for details.
- Bits above the implemented OA size, reported in SMMU\_IDR5.OAS, are RES0.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## FAULTCODE, bits [11:4]

Fault/error code.

- See section 9.1.4 ATOS\_PAR for details.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bit [3]

Reserved, RES0.

## REASON, bits [2:1]

Class of activity causing fault.

- This indicates the stage and reason for the fault. See section 9.1.4 ATOS\_PAR for details.

| REASON   | Meaning                                                                                                                                                                                         |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00     | Stage 1 translation-related fault occurred, or miscellaneous non-translation fault not attributable to a translation stage (for example, F_BAD_STE).                                            |
| 0b01     | CD: Stage 2 fault occurred because of a CD fetch.                                                                                                                                               |
| 0b10     | TT: Stage 2 fault occurred because of a stage 1 translation table walk.                                                                                                                         |
| 0b11     | IN: Stage 2 fault occurred because of the input address to stage 2 (output address from successful stage 1 translation table walk, or address given in ATOS_ADDR for stage 2-only translation). |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## FAULT, bit [0]

Fault/error status.

| FAULT   | Meaning                     |
|---------|-----------------------------|
| 0b1     | Fault or translation error. |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Accessing SMMU\_GATOS\_PAR

The content of ATOS\_PAR registers is UNKNOWN if values in the ATOS register group are modified after a translation has been initiated by setting ATOS\_CTRL.RUN == 1. See section 9.1.4 ATOS\_PAR .

This register has an UNKNOWN value if read when SMMU\_GATOS\_CTRL.RUN == 1.

Accesses to this register use the following encodings:

Accessible at offset 0x0118 from SMMUv3\_PAGE\_0

Accesses to this register are RO.