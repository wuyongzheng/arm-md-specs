## 6.3.72 SMMU\_S\_STRTAB\_BASE

The SMMU\_S\_STRTAB\_BASE characteristics are:

## Purpose

Stream Table Base address register in Secure state.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_STRTAB\_BASE are RES0.

## Attributes

SMMU\_S\_STRTAB\_BASE is a 64-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bit [63]

Reserved, RES0.

## RA, bit [62]

Read-Allocate hint.

| RA   | Meaning           |
|------|-------------------|
| 0b0  | No Read-Allocate. |
| 0b1  | Read-Allocate.    |

The reset behavior of this field is:

- When SMMU\_IDR1.TABLES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## Bits [61:56]

Reserved, RES0.

## ADDR, bits [55:6]

Physical address of Secure Stream table base, bits [55:6].

- Address bits above and below this field range are treated as zero.
- High-order bits of the ADDR field above the system physical address size, as reported by SMMU\_IDR5.OAS, are RES0.
- -Note: An implementation is not required to store these bits.

- When a Linear Stream table is used, that is when SMMU\_S\_STRTAB\_BASE\_CFG.FMT == 0b00 , the effective base address is aligned by the SMMU to the table size, ignoring the least-significant bits in the ADDR range as required to do so:
- When a 2-level Stream table is used, that is when SMMU\_S\_STRTAB\_BASE\_CFG.FMT == 0b01 , the effective base address is aligned by the SMMU to the larger of 64 bytes or the first-level table size:

```
ADDR[LOG2SIZE + 5:0] = 0 .
```

```
ADDR[MAX(5, (LOG2SIZE SPLIT -1 + 3)):0] = 0 .
```

The alignment of ADDR is affected by the literal value of the respective SMMU\_S\_STRTAB\_BASE\_CFG.LOG2SIZE field and is not limited by S\_SIDSIZE.

Note: This means that configuring a table that is larger than required by the incoming StreamID span results in some entries being unreachable, but the table is still aligned to the configured size.

The reset behavior of this field is:

- When SMMU\_IDR1.TABLES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## Bits [5:0]

Reserved, RES0.

## Additional Information

Access attributes of the Stream table are set using the SMMU\_S\_CR1.TABLE\_* fields, a Read-Allocate hint is provided for Stream table accesses with the RA field.

## Accessing SMMU\_S\_STRTAB\_BASE

SMMU\_S\_STRTAB\_BASE is Guarded by SMMU\_S\_CR0.SMMUEN and must only be written when SMMU\_S\_CR0.SMMUEN == 0.

See SMMU\_STRTAB\_BASE for detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x8080 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_IDR1.TABLES\_PRESET == 1, accesses to this register are RO.
- When SMMU\_S\_CR0.SMMUEN == 0 and SMMU\_S\_CR0ACK.SMMUEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.