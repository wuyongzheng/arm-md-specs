## 6.3.24 SMMU\_STRTAB\_BASE

The SMMU\_STRTAB\_BASE characteristics are:

## Purpose

Configuration of Stream table base address.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_STRTAB\_BASE is a 64-bit register.

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

Physical address of Stream table base, bits [55:6].

- Address bits above and below this field range are implied as zero.
- High-order bits of the ADDR field above the system physical address size, as reported by SMMU\_IDR5.OAS, are RES0.
- -Note: An implementation is not required to store these bits.

- When a Linear Stream table is used, that is when SMMU\_STRTAB\_BASE\_CFG.FMT == 0b00 , the effective base address is aligned by the SMMU to the table size, ignoring the least-significant bits in the ADDR range as required to do so:
- When a 2-level Stream table is used, that is when SMMU\_STRTAB\_BASE\_CFG.FMT == 0b01 , the effective base address is aligned by the SMMU to the larger of 64 bytes or the first-level table size:

```
ADDR[LOG2SIZE + 5:0] = 0 .
```

```
ADDR[MAX(5, (LOG2SIZE SPLIT -1 + 3)):0] = 0 .
```

The alignment of ADDR is affected by the literal value of the respective SMMU\_STRTAB\_BASE\_CFG.LOG2SIZE field and is not limited by SIDSIZE.

Note: This means that configuring a table that is larger than required by the incoming StreamID span results in some entries being unreachable, but the table is still aligned to the configured size.

The reset behavior of this field is:

- When SMMU\_IDR1.TABLES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## Bits [5:0]

Reserved, RES0.

## Additional Information

Access attributes of the Stream table are set using the SMMU\_CR1.TABLE\_* fields, a Read-Allocate hint is provided for Stream table accesses with the RA field.

## Accessing SMMU\_STRTAB\_BASE

SMMU\_STRTAB\_BASE is Guarded by SMMU\_CR0.SMMUEN and must only be written when SMMU\_CR0.SMMUEN == 0.

These update conditions are common for all SMMU\_(S\_)STRTAB\_* registers in the SMMU with respect to their corresponding SMMUEN.

In SMMUv3.1 and earlier, a write while SMMU\_CR0.SMMUEN == 1 is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- The register takes on any value, which might cause STEs to be fetched from an UNPREDICTABLE address.
- The write is ignored.
- A read following such a write will return an UNKNOWN value.

In SMMUv3.2 and later, a write while SMMU\_CR0.SMMUEN == 1 is IGNORED.

Accesses to this register use the following encodings:

Accessible at offset 0x0080 from SMMUv3\_PAGE\_0

- When SMMU\_IDR1.TABLES\_PRESET == 1, accesses to this register are RO.
- When SMMU\_CR0.SMMUEN == 0 and SMMU\_CR0ACK.SMMUEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.