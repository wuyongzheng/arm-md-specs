## 6.3.106 SMMU\_S\_VATOS\_PAR

The SMMU\_S\_VATOS\_PAR characteristics are:

## Purpose

Secure VATOS translation operation results register.

This result register encodes both successful results and error results. The format is determined by the FAULT field.

Unless otherwise specified, the fields of SMMU\_S\_VATOS\_PAR behave in an equivalent manner to the fields of SMMU\_VATOS\_PAR.

## Configuration

This register is present only when SMMU\_IDR0.VATOS == 1 and SMMU\_S\_IDR1.SEL2 == 1. Otherwise, direct accesses to SMMU\_S\_VATOS\_PAR are RES0.

## Attributes

SMMU\_S\_VATOS\_PAR is a 64-bit register.

This register is part of the SMMUv3\_S\_VATOS block.

## Field descriptions

When SMMU\_S\_VATOS\_PAR.FAULT == 0:

<!-- image -->

When FAULT == 0, a successful result is present:

This register has a similar encoding and behavior to SMMU\_VATOS\_PAR, except it applies to the Secure Virtual ATOS interface.

- Note: Because the ATOS\_PAR.FADDR field returns a fault IPA only when an ATOS\_ADDR.TYPE == 0b10 request is made, and VATOS\_ADDR.TYPE must be 0b01 , the SMMU\_S\_VATOS\_PAR.FADDR and SMMU\_S\_VATOS\_PAR.NSIPA fields are always 0.
- See Chapter 9 Address Translation Operations for details.

This result register encodes both successful results and error results. The format is determined by the FAULT field.

## ATTR, bits [63:56]

Memory attributes, in MAIR format.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## ADDR, bits [55:12]

Result address, bits [55:12].

- Address bits above and below [55:12] are treated as zero.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Size, bit [11]

Translation page/block size flag.

The Size field allows the size of the translation to be determined, using an encoding in the ADDR field. The Size flag indicates that:

| Size   | Meaning                                                              |
|--------|----------------------------------------------------------------------|
| 0b0    | Translation is 4KB.                                                  |
| 0b1    | Translation is determined by position of lowest 1 bit in ADDR field. |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## NS, bit [10]

Final NS attribute.

- Note: This bit is RES0 in SMMU\_GATOS\_PAR and SMMU\_VATOS\_PAR.
- Note: As Secure VATOS translations are for stage 1 only, there is no need to supply an input NS attribute value. Input NS attributes are not considered when stage 1 is configured for translation. If stage 1 is configured for bypass, the output NS attribute is IMPLEMENTATION DEFINED. See Section 9.1.3 ATOS\_ADDR .

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

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

## When SMMU\_S\_VATOS\_PAR.FAULT == 1:

<!-- image -->

When FAULT == 1, the translation has failed and a fault syndrome is present:

## IMPLEMENTATION DEFINED, bits [63:60]

IMPLEMENTATION DEFINED fault data.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [59:56]

Reserved, RES0.

## FADDR, bits [55:12]

Fault page address, bits [55:12].

- Note: Because the ATOS\_PAR.FADDR field returns a fault IPA only when an ATOS\_ADDR.TYPE == 0b10 request is made, and VATOS\_ADDR.TYPE must be 0b01 , this field is always 0.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## FAULTCODE, bits [11:4]

Fault/error code.

- See section 9.1.4 ATOS\_PAR for details.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## NSIPA, bit [3]

Fault IPA NS attribute.

- Note: Because the ATOS\_PAR.FADDR field returns a fault IPA only when an ATOS\_ADDR.TYPE == 0b10 request is made, and VATOS\_ADDR.TYPE must be 0b01 , this field is always 0. See section 9.1.4 ATOS\_PAR for details.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## REASON, bits [2:1]

Class of activity causing fault.

- This indicates the stage and reason for the fault. The only value permitted in SMMU\_S\_VATOS\_PAR.REASON is 0b00 . See section 9.1.4 ATOS\_PAR for details.

| REASON   | Meaning                                                                                                                                              |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00     | Stage 1 translation-related fault occurred, or miscellaneous non-translation fault not attributable to a translation stage (for example, F_BAD_STE). |
| 0b01     | Reserved.                                                                                                                                            |
| 0b10     | Reserved.                                                                                                                                            |
| 0b11     | Reserved.                                                                                                                                            |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## FAULT, bit [0]

Fault/error status.

| FAULT   | Meaning                     |
|---------|-----------------------------|
| 0b1     | Fault or translation error. |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Accessing SMMU\_S\_VATOS\_PAR

The content of ATOS\_PAR registers is UNKNOWN if values in the ATOS register group are modified after a translation has been initiated by setting ATOS\_CTRL.RUN == 1. See section 9.1.4 ATOS\_PAR .

This register has an UNKNOWN value if read when SMMU\_S\_VATOS\_CTRL.RUN == 1.

Accesses to this register use the following encodings:

Accessible at offset 0x0A18 from SMMUv3\_S\_VATOS

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.