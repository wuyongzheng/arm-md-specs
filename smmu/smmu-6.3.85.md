## 6.3.85 SMMU\_S\_GATOS\_ADDR

The SMMU\_S\_GATOS\_ADDR characteristics are:

## Purpose

Secure Global ATOS translation address register.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1 and SMMU\_IDR0.ATOS == 1. Otherwise, direct accesses to SMMU\_S\_GATOS\_ADDR are RES0.

## Attributes

SMMU\_S\_GATOS\_ADDR is a 64-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## ADDR, bits [63:12]

Requested input address, bits [63:12].

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## TYPE, bits [11:10]

Request type.

| TYPE   | Meaning                         |
|--------|---------------------------------|
| 0b00   | Reserved.                       |
| 0b01   | Stage 1 (VA to IPA).            |
| 0b10   | Stage 2 (IPA to PA).            |
| 0b11   | Stage 1 and stage 2 (VA to PA). |

- Use of a Reserved value results in an INV\_REQ ATOS error.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## PnU, bit [9]

Privileged or User access.

| PnU   | Meaning       |
|-------|---------------|
| 0b0   | Unprivileged. |
| 0b1   | Privileged.   |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## RnW, bit [8]

Read/Write access.

| RnW   | Meaning   |
|-------|-----------|
| 0b0   | Write.    |
| 0b1   | Read.     |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## InD, bit [7]

Instruction/Data access.

| InD   | Meaning      |
|-------|--------------|
| 0b0   | Data.        |
| 0b1   | Instruction. |

- This bit is IGNORED if RnW == 0, and the effective InD for writes is Data.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## HTTUI, bit [6]

Inhibit hardware update of the Access flag and dirty state.

| HTTUI   | Meaning                                                                                                                              |
|---------|--------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Flag update (HTTU) might occur, where supported by the SMMU, according to the HA and HD configuration fields at stage 1 and stage 2. |
| 0b1     | HTTU is inhibited, regardless of HA and HD configuration. • The ATOS operation causes no state change.                               |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bit [5]

Reserved, RES0.

## NS, bit [4]

## When SMMU\_S\_IDR1.SEL2 == 1:

Input NS attribute.

- This bit is used in the scenario where the selected stream is Secure and one of the following applies:
- -The stream is configured for stage 1 and stage 2 translation and an ATOS lookup is made for stage 1 and stage 2, but stage 1 translation is bypassed due to STE.S1DSS.
- -The stream is configured for stage 1 and stage 2 translation and an ATOS lookup is made for stage 2 only.
- -The stream is configured for stage 2 translation only and an ATOS lookup is made for stage 2 only.
- In these scenarios, this bit provides the IPA space determination required for a Secure stage 2 translation.
- This bit is ignored when stage 2 translation is not performed or when stage 1 translation is performed.
- Note: When stage 1 translation is performed, the IPA space determination provided to stage 2 comes from stage 1 translation tables.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [3:0]

Reserved, RES0.

## Accessing SMMU\_S\_GATOS\_ADDR

This register is Guarded by SMMU\_S\_GATOS\_CTRL.RUN and must only be altered when RUN == 0.

See SMMU\_GATOS\_CTRL for more detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x8110 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_S\_GATOS\_CTRL.RUN == 1, accesses to this register are RO.
- Otherwise, accesses to this register are RW.