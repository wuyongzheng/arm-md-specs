## 6.3.39 SMMU\_GATOS\_ADDR

The SMMU\_GATOS\_ADDR characteristics are:

## Purpose

Global ATOS translation address register.

## Configuration

This register is present only when SMMU\_IDR0.ATOS == 1. Otherwise, direct accesses to SMMU\_GATOS\_ADDR are RES0.

## Attributes

SMMU\_GATOS\_ADDR is a 64-bit register.

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

Read/write access.

| RnW   | Meaning   |
|-------|-----------|
| 0b0   | Write.    |
| 0b1   | Read.     |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## InD, bit [7]

Instruction/data access.

| InD   | Meaning      |
|-------|--------------|
| 0b0   | Data.        |
| 0b1   | Instruction. |

- This bit is IGNORED if RnW == 0, and the effective InD for writes is Data.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## HTTUI, bit [6]

Inhibit hardware update of the Access flag and dirty state.

| HTTUI   | Meaning                                                                                                                      |
|---------|------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Flag update (HTTU) might occur, where supported by the SMMU, according to HA:HD configuration fields at stage 1 and stage 2. |
| 0b1     | HTTU is inhibited, regardless of HA/HD configuration. • The ATOS operation causes no state change and is passive.            |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [5:0]

Reserved, RES0.

## Additional Information

The PnU and InD attributes are not affected by the STE.INSTCFG or STE.PRIVCFG overrides.

## Accessing SMMU\_GATOS\_ADDR

This register is Guarded by SMMU\_GATOS\_CTRL.RUN and must only be altered when RUN == 0.

See SMMU\_GATOS\_CTRL for more detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x0110 from SMMUv3\_PAGE\_0

- When SMMU\_GATOS\_CTRL.RUN == 1, accesses to this register are RO.
- Otherwise, accesses to this register are RW.