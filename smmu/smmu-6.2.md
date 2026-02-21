## 6.2 Register overview

Unless specified otherwise, all registers are 32-bit, little-endian and allow read and write (R/W) accesses.

For all pages except Page 1, undefined register locations are RES0. For Page 1, access to undefined/Reserved register locations is CONSTRAINED UNPREDICTABLE and an implementation has one of the following behaviors:

- The location has the same behavior as RES0.
- The access has the same effect as would an access to the same offset in Page 0, that is Page 0 and 1 are permitted to alias.

The equivalent Page 0 offsets of registers that are defined on Page 1 are Reserved and Arm recommends that they are not accessed. Access to these offsets is CONSTRAINED UNPREDICTABLE and (depending on the implementation of Page 1) has one of the following behaviors:

- The location aliases the corresponding register in Page 1.
- The access has RAZ/WI behavior.

When SMMU\_S\_IDR1.SECURE\_IMPL == 1, SMMU\_S\_* registers are RAZ/WI to Non-secure access. See section 3.11 Reset, Enable and initialization regarding Non-secure access to SMMU\_S\_INIT. All other registers are accessible to both Secure and Non-secure accesses.

When SMMU\_S\_IDR1.SECURE\_IMPL == 0, SMMU\_S\_* registers are RES0.

In an SMMU with RME, all of the following apply:

- All SMMU registers that are specified to be accessible only in Secure PA space in this specification are additionally accessible in Root PA space in an SMMU with RME.
- All SMMU registers that are specified to be accessible in Non-secure PA space in this specification are additionally accessible in Root and Realm PA spaces in an SMMU with RME.

All SMMU ID registers (those that report the presence or scope of features) hold constant values after reset.

Reserved or undefined bit positions in defined registers are RES0: they read as zero and must not be written with non-zero values.

An implementation must support aligned 32-bit word access to 32-bit registers, and to both 32-bit halves of 64-bit registers. The SMMU supports aligned 64-bit access to 64-bit registers. Support for other access sizes is IMPLEMENTATION DEFINED.

The following constitute an illegal register access:

- An access of an unsupported size.
- Unaligned accesses, that is an access that does not start on a boundary equal to the access size.

An illegal register access is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- The access is RAZ/WI.
- The access is observed by the register or registers spanned by the access and:
- -Write access will write any value to this register or registers including to fields of this register or registers outside of the access. This behavior does not enable a Non-secure access to affect registers that are not otherwise accessible to Non-secure accesses.
- -Read access returns an UNKNOWN value.
- The access is terminated with an abort.

A 64-bit access to two adjacent 32-bit registers is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- The access is RAZ/WI.
- A read returns the value of both registers and a write updates both registers, as though two 32-bit accesses were performed in an UNPREDICTABLE order.

- One of the pair of registers is read or written and the other register is RAZ/WI, as though a single 32-bit access was performed to an UNPREDICTABLE one of the pair of registers.
- The access is terminated with an abort.

Note: Arm strongly recommends not to abort accesses to registers that might be used by software that is associated with lower exception levels on the PE, such as the SMMU\_VATOS\_* or PMCG registers.

It is IMPLEMENTATION DEFINED whether a 64-bit access to a 64-bit register is single-copy atomic. An SMMU implementation might internally observe the access in two 32-bit halves. An aligned 32-bit word access is single-copy atomic.

All 64-bit fields are composed of two separately-writable 32-bit register halves, with bits[63:32] at offset +4 and [31:0] at offset +0.

Some register fields have a dependency on another register field, and are described as Guarded by the other field. A Guarded register field is not permitted to be changed by software unless the field by which it is Guarded is in a certain state (and is not in the process of being Updated to or from that state). For example, SMMU\_CMDQ\_BASE is Guarded by SMMU\_CR0.CMDQEN so that software is only permitted to change SMMU\_CMDQ\_BASE if SMMU\_CR0.CMDQEN == 0.

Note: Software must use an appropriate barrier to ensure initialization of Guarded register fields is visible to the SMMUbefore the SMMU observes a set of the field by which they are Guarded.

Registers are not required to support being the target of exclusive or atomic read-modify-write update operations.

In this specification, read-only means that writes are ignored.

## 6.2.1 Registers in Page 0

| Offset   | Register    | Notes      |
|----------|-------------|------------|
| 0x0000   | SMMU_IDR0   | 32-bit, RO |
| 0x0004   | SMMU_IDR1   | 32-bit, RO |
| 0x0008   | SMMU_IDR2   | 32-bit, RO |
| 0x000C   | SMMU_IDR3   | 32-bit, RO |
| 0x0010   | SMMU_IDR4   | 32-bit, RO |
| 0x0014   | SMMU_IDR5   | 32-bit, RO |
| 0x0018   | SMMU_IIDR   | 32-bit, RO |
| 0x001C   | SMMU_AIDR   | 32-bit, RO |
| 0x0020   | SMMU_CR0    | 32-bit,RW  |
| 0x0024   | SMMU_CR0ACK | 32-bit, RO |
| 0x0028   | SMMU_CR1    | 32-bit,RW  |
| 0x002C   | SMMU_CR2    | 32-bit,RW  |
| 0x0030   | SMMU_S2PII  | 64-bit,RW  |

Chapter 6.

6.2. Register overview

| Offset   | Register                                             | Notes      |
|----------|------------------------------------------------------|------------|
| 0x0040   | SMMU_STATUSR                                         | 32-bit, RO |
| 0x0044   | SMMU_GBPA                                            | 32-bit,RW  |
| 0x0048   | SMMU_AGBPA                                           | 32-bit,RW  |
| 0x0050   | SMMU_IRQ_CTRL                                        | 32-bit,RW  |
| 0x0054   | SMMU_IRQ_CTRLACK                                     | 32-bit, RO |
| 0x0060   | SMMU_GERROR                                          | 32-bit, RO |
| 0x0064   | SMMU_GERRORN                                         | 32-bit,RW  |
| 0x0068   | SMMU_GERROR_IRQ_CFG0                                 | 64-bit,RW  |
| 0x0070   | SMMU_GERROR_IRQ_CFG1                                 | 32-bit,RW  |
| 0x0074   | SMMU_GERROR_IRQ_CFG2                                 | 32-bit,RW  |
| 0x0080   | SMMU_STRTAB_BASE                                     | 64-bit,RW  |
| 0x0088   | SMMU_STRTAB_BASE_CFG                                 | 32-bit,RW  |
| 0x0090   | SMMU_CMDQ_BASE                                       | 64-bit,RW  |
| 0x0098   | SMMU_CMDQ_PROD                                       | 32-bit,RW  |
| 0x009C   | SMMU_CMDQ_CONS                                       | 32-bit,RW  |
| 0x00A0   | SMMU_EVENTQ_BASE                                     | 64-bit,RW  |
| 0x00A8   | Optional alias of SMMU_EVENTQ_PROD, otherwise RAZ/WI |            |
| 0x00AC   | Optional alias of SMMU_EVENTQ_CONS, otherwise RAZ/WI |            |
| 0x00B0   | SMMU_EVENTQ_IRQ_CFG0                                 | 64-bit,RW  |
| 0x00B8   | SMMU_EVENTQ_IRQ_CFG1                                 | 32-bit,RW  |
| 0x00BC   | SMMU_EVENTQ_IRQ_CFG2                                 | 32-bit,RW  |
| 0x00C0   | SMMU_PRIQ_BASE                                       | 64-bit,RW  |
| 0x00C8   | Optional alias of SMMU_PRIQ_PROD, otherwise RAZ/WI   | 32-bit,RW  |
| 0x00CC   | Optional alias of SMMU_PRIQ_CONS, otherwise RAZ/WI   | 32-bit,RW  |
| 0x00D0   | SMMU_PRIQ_IRQ_CFG0                                   | 64-bit,RW  |
| 0x00D8   | SMMU_PRIQ_IRQ_CFG1                                   | 32-bit,RW  |
| 0x00DC   | SMMU_PRIQ_IRQ_CFG2                                   | 32-bit,RW  |

6.2. Register overview

| Offset          | Register                                 | Notes                  |
|-----------------|------------------------------------------|------------------------|
| 0x0100          | SMMU_GATOS_CTRL                          | 32-bit,RW              |
| 0x0108          | SMMU_GATOS_SID                           | 64-bit,RW              |
| 0x0110          | SMMU_GATOS_ADDR                          | 64-bit,RW              |
| 0x0118          | SMMU_GATOS_PAR                           | 64-bit, RO             |
| 0x0130          | SMMU_MPAMIDR                             | 32-bit, RO             |
| 0x0138          | SMMU_GMPAM                               | 32-bit,RW              |
| 0x013C          | SMMU_GBPMPAM                             | 32-bit,RW              |
| 0x0180          | SMMU_VATOS_SEL                           | 32-bit,RW              |
| 0x0190          | SMMU_IDR6                                | 32-bit, RO             |
| 0x0200          | SMMU_DPT_BASE                            | 64-bit,RW              |
| 0x0208          | SMMU_DPT_BASE_CFG                        | 32-bit,RW              |
| 0x0210          | SMMU_DPT_CFG_FAR                         | 64-bit,RW              |
| 0x0E00 - 0x0EFF | IMPLEMENTATION DEFINED                   | IMPLEMENTATION DEFINED |
| 0x0FD0- 0x0FFC  | ID_REGS - identification register space. | IMPLEMENTATION DEFINED |
| 0x1000 - 0x3FFF | IMPLEMENTATION DEFINED                   | IMPLEMENTATION DEFINED |
| 0x4000 + 32*n   | SMMU_CMDQ_CONTROL_PAGE_BASEn             | 64-bit, RO             |
| 0x4008 + 32*n   | SMMU_CMDQ_CONTROL_PAGE_CFGn              | 32-bit, RO             |
| 0x400C + 32*n   | SMMU_CMDQ_CONTROL_PAGE_STATUSn           | 32-bit, RO             |
| 0x8000          | SMMU_S_IDR0                              | 32-bit, Secure, RO     |
| 0x8004          | SMMU_S_IDR1                              | 32-bit, Secure, RO     |
| 0x8008          | SMMU_S_IDR2                              | 32-bit, Secure, RO     |
| 0x800C          | SMMU_S_IDR3                              | 32-bit, Secure, RO     |
| 0x8010          | SMMU_S_IDR4                              | 32-bit, Secure, RO     |

Chapter 6. 6.2. Register overview

| Offset   | Register               | Notes              |
|----------|------------------------|--------------------|
| 0x8020   | SMMU_S_CR0             | 32-bit, Secure,RW  |
| 0x8024   | SMMU_S_CR0ACK          | 32-bit, Secure, RO |
| 0x8028   | SMMU_S_CR1             | 32-bit, Secure,RW  |
| 0x802C   | SMMU_S_CR2             | 32-bit, Secure,RW  |
| 0x8030   | SMMU_S_S2PII           | 64-bit, Secure,RW  |
| 0x803C   | SMMU_S_INIT            | 32-bit, Secure,RW  |
| 0x8044   | SMMU_S_GBPA            | 32-bit, Secure,RW  |
| 0x8048   | SMMU_S_AGBPA           | 32-bit, Secure,RW  |
| 0x8050   | SMMU_S_IRQ_CTRL        | 32-bit, Secure,RW  |
| 0x8054   | SMMU_S_IRQ_CTRLACK     | 32-bit, Secure, RO |
| 0x8060   | SMMU_S_GERROR          | 32-bit, Secure, RO |
| 0x8064   | SMMU_S_GERRORN         | 32-bit, Secure,RW  |
| 0x8068   | SMMU_S_GERROR_IRQ_CFG0 | 64-bit, Secure,RW  |
| 0x8070   | SMMU_S_GERROR_IRQ_CFG1 | 32-bit, Secure,RW  |
| 0x8074   | SMMU_S_GERROR_IRQ_CFG2 | 32-bit, Secure,RW  |
| 0x8080   | SMMU_S_STRTAB_BASE     | 64-bit, Secure,RW  |
| 0x8088   | SMMU_S_STRTAB_BASE_CFG | 32-bit, Secure,RW  |
| 0x8090   | SMMU_S_CMDQ_BASE       | 64-bit, Secure,RW  |
| 0x8098   | SMMU_S_CMDQ_PROD       | 32-bit, Secure,RW  |
| 0x809C   | SMMU_S_CMDQ_CONS       | 32-bit, Secure,RW  |
| 0x80A0   | SMMU_S_EVENTQ_BASE     | 64-bit, Secure,RW  |
| 0x80A8   | SMMU_S_EVENTQ_PROD     | 32-bit, Secure,RW  |
| 0x80AC   | SMMU_S_EVENTQ_CONS     | 32-bit, Secure,RW  |
| 0x80B0   | SMMU_S_EVENTQ_IRQ_CFG0 | 64-bit, Secure,RW  |
| 0x80B8   | SMMU_S_EVENTQ_IRQ_CFG1 | 32-bit, Secure,RW  |
| 0x80BC   | SMMU_S_EVENTQ_IRQ_CFG2 | 32-bit, Secure,RW  |
| 0x8100   | SMMU_S_GATOS_CTRL      | 32-bit, Secure,RW  |

| Offset          | Register                         | Notes                          |
|-----------------|----------------------------------|--------------------------------|
| 0x8108          | SMMU_S_GATOS_SID                 | 64-bit, Secure,RW              |
| 0x8110          | SMMU_S_GATOS_ADDR                | 64-bit, Secure,RW              |
| 0x8118          | SMMU_S_GATOS_PAR                 | 64-bit, Secure, RO             |
| 0x8130          | SMMU_S_MPAMIDR                   | 32-bit, Secure, RO             |
| 0x8138          | SMMU_S_GMPAM                     | 32-bit, Secure,RW              |
| 0x813C          | SMMU_S_GBPMPAM                   | 32-bit, Secure,RW              |
| 0x8180          | SMMU_S_VATOS_SEL                 | 32-bit, Secure,RW              |
| 0x8190          | SMMU_S_IDR6                      | 32-bit, Secure, RO             |
| 0x8E00 -        | IMPLEMENTATION DEFINED, Secure   | IMPLEMENTATION DEFINED, Secure |
| 0x9000 - 0xBFFF | IMPLEMENTATION DEFINED, Secure   | IMPLEMENTATION DEFINED, Secure |
| 0xC000 + 32*n   | SMMU_S_CMDQ_CONTROL_PAGE_BASEn   | 64-bit, Secure, RO             |
| 0xC008 + 32*n   | SMMU_S_CMDQ_CONTROL_PAGE_CFGn    | 32-bit, Secure, RO             |
| 0xC00C + 32*n   | SMMU_S_CMDQ_CONTROL_PAGE_STATUSn | 32-bit, Secure, RO             |

## 6.2.2 Registers in Page 1

Offsets are relative to the base of Page 1, 0x10000 .

| Offset   | Register         | Notes     |
|----------|------------------|-----------|
| 0x00A8   | SMMU_EVENTQ_PROD | 32-bit,RW |
| 0x00AC   | SMMU_EVENTQ_CONS | 32-bit,RW |
| 0x00C8   | SMMU_PRIQ_PROD   | 32-bit,RW |
| 0x00CC   | SMMU_PRIQ_CONS   | 32-bit,RW |

## 6.2.3 Registers in the VATOS page

When SMMU\_IDR0.VATOS == 1, the VATOS page is present.

Offsets are relative to the base of the V ATOS page, O\_VATOS . See SMMU\_IDR2.

6.2.

| Offset   | Register               | Notes      |
|----------|------------------------|------------|
| 0x0A00   | SMMU_VATOS_CTRL        | 32-bit,RW  |
| 0x0A08   | SMMU_VATOS_SID         | 64-bit,RW  |
| 0x0A10   | SMMU_VATOS_ADDR        | 64-bit,RW  |
| 0x0A18   | SMMU_VATOS_PAR         | 64-bit, RO |
| 0x0E00 - | IMPLEMENTATION DEFINED |            |
| 0x0EFF   |                        |            |

## 6.2.4 Registers in the S\_VATOS page

When Secure state is supported and SMMU\_S\_IDR1.SEL2 == 1 and SMMU\_IDR0.VATOS == 1, the S\_VATOS page is present.

The base address of the S\_VATOS page is determined from SMMU\_S\_IDR2.BA\_S\_VATOS and referred to as O\_S\_VATOS :

```
O_S_VATOS = SMMU_BASE + 0x20000 + (SMMU_S_IDR2.BA_S_VATOS * 0x10000)
```

The offsets below are relative to the base of the S\_V ATOS page, O\_S\_VATOS .

| Offset   | Register               | Notes              |
|----------|------------------------|--------------------|
| 0x0A00   | SMMU_S_VATOS_CTRL      | 32-bit, Secure,RW  |
| 0x0A08   | SMMU_S_VATOS_SID       | 64-bit, Secure,RW  |
| 0x0A10   | SMMU_S_VATOS_ADDR      | 64-bit, Secure,RW  |
| 0x0A18   | SMMU_S_VATOS_PAR       | 64-bit, Secure, RO |
| 0x0E00 - | IMPLEMENTATION DEFINED | Secure             |
| 0x0EFF   |                        |                    |

## 6.2.5 Registers in a Command queue control page

When SMMU\_IDR1.ECMDQ == 1, one or more Command queue control pages are present.

A Command queue control page contains the ECMDQ interfaces specified in section 3.5.6 Enhanced Command queue interfaces .

The number of ECMDQs in a Command queue control page is between 1 and 256, according to the value of:

- SMMU\_IDR6.CMDQ\_CONTROL\_PAGE\_LOG2NUMQ for Non-secure state.
- SMMU\_S\_IDR6.CMDQ\_CONTROL\_PAGE\_LOG2NUMQ for Secure state.
- SMMU\_R\_IDR6.CMDQ\_CONTROL\_PAGE\_LOG2NUMQ for Realm state.

The size of a Command queue control page is 64KB. A Command queue control page is aligned in PA space to 64KB.

A Command queue control page is implemented as registers.

The ECMDQs are spaced evenly throughout a Command queue control page.

For example, if a control page has 128 ECMDQs, the interfaces are spaced at 512 byte intervals throughout the page.

There are therefore many copies of the following three registers within a Command queue control page:

| Offset   | Register        | Notes     |
|----------|-----------------|-----------|
| 0x00     | SMMU_ECMDQ_BASE | 64-bit,RW |
| 0x08     | SMMU_ECMDQ_PROD | 32-bit,RW |
| 0x0C     | SMMU_ECMDQ_CONS | 32-bit,RW |

## 6.2.6 Root Control Page

When SMMU\_ROOT\_IDR0.ROOT\_IMPL == 1, the SMMU Root Control Page is present.

Access to the SMMU Root Control Page is bounded by the following rules:

- The base address is IMPLEMENTATION DEFINED.
- The base address is 64KB aligned.
- The page is accessible only in the Root PA space.
- Accesses in any PA space other than Root are completed as RAZ/WI.
- The Root Control Page base address is distinct from addresses of registers accessible in other PA spaces.

Address map:

| Offset          | Register                  | Notes                  |
|-----------------|---------------------------|------------------------|
| 0x0000          | SMMU_ROOT_IDR0            | 32-bit, RO             |
| 0x0008          | SMMU_ROOT_IIDR            | 32-bit, RO             |
| 0x0020          | SMMU_ROOT_CR0             | 32-bit, R/W            |
| 0x0024          | SMMU_ROOT_CR0ACK          | 32-bit, RO             |
| 0x0028          | SMMU_ROOT_GPT_BASE        | 64-bit, R/W            |
| 0x0030          | SMMU_ROOT_GPT_BASE_CFG    | 64-bit, R/W            |
| 0x0038          | SMMU_ROOT_GPF_FAR         | 64-bit, R/W            |
| 0x0040          | SMMU_ROOT_GPT_CFG_FAR     | 64-bit, R/W            |
| 0x0050          | SMMU_ROOT_TLBI            | 64-bit, R/W, OPTIONAL  |
| 0x0058          | SMMU_ROOT_TLBI_CTRL       | 32-bit, R/W, OPTIONAL  |
| 0x0060          | SMMU_ROOT_GPT_BASE2       | 64-bit, R/W            |
| 0x0068          | SMMU_ROOT_GPT_BASE_UPDATE | 32-bit, R/W            |
| 0x0E00 - 0x0EFF | IMPLEMENTATION DEFINED    | IMPLEMENTATION DEFINED |

Locations in the SMMU Root Control Page that are not associated with a register are RES0.

## 6.2.7 Realm Register Pages

The two SMMUv3 Realm Register Pages have the following properties:

- The two pages are adjacent and together occupy a naturally-aligned 128KB region of physical address space.
- The registers are only accessible in Realm and Root PA spaces. Non-secure and Secure accesses to the page are RAZ/WI.
- Addresses configured in these registers are treated as Realm physical addresses by default. Some of the configuration registers have an NS override bit, which selects Non-secure physical address space if set.
- If SMMU\_IDR1.QUEUES\_PRESET is 1 and SMMU\_IDR1.REL is 1, then the preset address values in all of the SMMU\_R\_{CMDQ,EVENTQ,PRIQ}\_BASE registers are relative to the base address of the Non-secure SMMUregister Page 0.
- If SMMU\_IDR1.TABLES\_PRESET is 1 and SMMU\_IDR1.REL is 1, then the preset address value in the SMMU\_R\_STRTAB\_BASE register is relative to the base address of the Non-secure SMMU register Page 0.

## 6.2.8 Registers in Realm Page 0

When SMMU\_ROOT\_IDR0.REALM\_IMPL == 1, the SMMU Realm Page 0 is present.

The layout of Realm Page 0 is as follows:

| Offset   | Register name          | Notes                                                                                      |
|----------|------------------------|--------------------------------------------------------------------------------------------|
| 0x0000   | SMMU_R_IDR0            | 32-bit, RO                                                                                 |
| 0x0004   | SMMU_R_IDR1            | 32-bit, RO                                                                                 |
| 0x0008   | SMMU_R_IDR2            | 32-bit, RO                                                                                 |
| 0x000C   | SMMU_R_IDR3            | 32-bit, RO                                                                                 |
| 0x0010   | SMMU_R_IDR4            | 32-bit, RO                                                                                 |
| 0x0018   | Reserved, RES0.        | Implementation identification is described in SMMU_IIDR. There is no SMMU_R_IIDR register. |
| 0x001C   | SMMU_R_AIDR            | 32-bit, RO                                                                                 |
| 0x0020   | SMMU_R_CR0             | 32-bit,RW                                                                                  |
| 0x0024   | SMMU_R_CR0ACK          | 32-bit, RO                                                                                 |
| 0x0028   | SMMU_R_CR1             | 32-bit,RW                                                                                  |
| 0x002C   | SMMU_R_CR2             | 32-bit,RW                                                                                  |
| 0x0030   | SMMU_R_S2PII           | 64-bit,RW                                                                                  |
| 0x0044   | SMMU_R_GBPA            | 32-bit, RO                                                                                 |
| 0x0048   | SMMU_R_AGBPA           | 32-bit,RW                                                                                  |
| 0x0050   | SMMU_R_IRQ_CTRL        | 32-bit,RW                                                                                  |
| 0x0054   | SMMU_R_IRQ_CTRLACK     | 32-bit, RO                                                                                 |
| 0x0060   | SMMU_R_GERROR          | 32-bit, RO                                                                                 |
| 0x0064   | SMMU_R_GERRORN         | 32-bit,RW                                                                                  |
| 0x0068   | SMMU_R_GERROR_IRQ_CFG0 | 64-bit, RW. When SMMU_R_IDR0.MSI == 1.                                                     |
| 0x0070   | SMMU_R_GERROR_IRQ_CFG1 | 32-bit, RW. When SMMU_R_IDR0.MSI == 1.                                                     |
| 0x0074   | SMMU_R_GERROR_IRQ_CFG2 | 32-bit, RW. When SMMU_R_IDR0.MSI == 1.                                                     |

| 0x0080           | SMMU_R_STRTAB_BASE               | 64-bit,RW                                                                                                    |
|------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------|
| 0x0088           | SMMU_R_STRTAB_BASE_CFG           | 32-bit,RW                                                                                                    |
| 0x0090           | SMMU_R_CMDQ_BASE                 | 64-bit,RW                                                                                                    |
| 0x0098           | SMMU_R_CMDQ_PROD                 | 32-bit,RW                                                                                                    |
| 0x009C           | SMMU_R_CMDQ_CONS                 | 32-bit,RW                                                                                                    |
| 0x00A0           | SMMU_R_EVENTQ_BASE               | 64-bit,RW                                                                                                    |
| 0x00A8           |                                  | Optional alias of SMMU_R_EVENTQ_PROD.                                                                        |
| 0x00AC           |                                  | Optional alias of SMMU_R_EVENTQ_CONS.                                                                        |
| 0x00B0           | SMMU_R_EVENTQ_IRQ_CFG0           | 64-bit, RW. When SMMU_R_IDR0.MSI == 1.                                                                       |
| 0x00B8           | SMMU_R_EVENTQ_IRQ_CFG1           | 32-bit, RW. When SMMU_R_IDR0.MSI == 1.                                                                       |
| 0x00BC           | SMMU_R_EVENTQ_IRQ_CFG2           | 32-bit, RW. When SMMU_R_IDR0.MSI == 1.                                                                       |
| 0x00C0           | SMMU_R_PRIQ_BASE                 | 64-bit, RW. When SMMU_R_IDR0.PRI == 1.                                                                       |
| 0x00C8           |                                  | Optional alias of SMMU_R_PRIQ_PROD.                                                                          |
| 0x00CC           |                                  | Optional alias of SMMU_R_PRIQ_CONS.                                                                          |
| 0x00D0           | SMMU_R_PRIQ_IRQ_CFG0             | 64-bit, RW. When SMMU_R_IDR0.MSI == 1 and SMMU_R_IDR0.PRI == 1.                                              |
| 0x00D8           | SMMU_R_PRIQ_IRQ_CFG1             | 32-bit, RW. When SMMU_R_IDR0.MSI == 1 and SMMU_R_IDR0.PRI == 1.                                              |
| 0x00DC           | SMMU_R_PRIQ_IRQ_CFG2             | 32-bit, RW. When SMMU_R_IDR0.MSI == 1 and SMMU_R_IDR0.PRI == 1.                                              |
| 0x0130           | SMMU_R_MPAMIDR                   | 32-bit, RO. When SMMU_IDR3.MPAM == 1.                                                                        |
| 0x0138           | SMMU_R_GMPAM                     | 32-bit, RW. When SMMU_IDR3.MPAM == 1.                                                                        |
| 0x013C           | Reserved, RES0                   | SMMU_R_GBPA.ABORT and SMMU_R_CR0.ATSCHK are RES1, therefore there is no need for an SMMU_R_GBPMPAM register. |
| 0x0190           | SMMU_R_IDR6                      | 32-bit, RO. When SMMU_R_IDR0.ECMDQ == 1.                                                                     |
| 0x0200           | SMMU_R_DPT_BASE                  | 64-bit, RW. When SMMU_R_IDR3.DPT == 1.                                                                       |
| 0x0208           | SMMU_R_DPT_BASE_CFG              | 32-bit, RW. When SMMU_R_IDR3.DPT == 1.                                                                       |
| 0x0210           | SMMU_R_DPT_CFG_FAR               | 64-bit, RW. When SMMU_R_IDR3.DPT == 1.                                                                       |
| 0x0220           | SMMU_R_MECIDR                    | 32-bit, RO. When SMMU_R_IDR3.MEC == 1.                                                                       |
| 0x0228           | SMMU_R_GMECID                    | 32-bit, RO. When SMMU_R_IDR3.MEC == 1.                                                                       |
| 0x4000 + (32\*n) | SMMU_R_CMDQ_CONTROL_PAGE_BASEn   | 64-bit, RO. When SMMU_R_IDR0.ECDMQ == 1.                                                                     |
| 0x4008 + (32\*n) | SMMU_R_CMDQ_CONTROL_PAGE_CFGn    | 32-bit, RO. When SMMU_R_IDR0.ECDMQ == 1.                                                                     |
| 0x400C + (32\*n) | SMMU_R_CMDQ_CONTROL_PAGE_STATUSn | 32-bit, RO. When SMMU_R_IDR0.ECDMQ == 1.                                                                     |

IMPLEMENTATION DEFINED

## 6.2.9 Registers in Realm Page 1

When SMMU\_ROOT\_IDR0.REALM\_IMPL == 1, the SMMU Realm Page 1 is present.

The layout of Realm Page 1 is as follows:

| Offset   | Register name      | Details                         |
|----------|--------------------|---------------------------------|
| 0x00A8   | SMMU_R_EVENTQ_PROD | Equivalent to SMMU_EVENTQ_PROD. |
| 0x00AC   | SMMU_R_EVENTQ_CONS | Equivalent to SMMU_EVENTQ_CONS. |
| 0x00C8   | SMMU_R_PRIQ_PROD   | Equivalent to SMMU_PRIQ_PROD.   |
| 0x00CC   | SMMU_R_PRIQ_CONS   | Equivalent to SMMU_PRIQ_CONS.   |

IMPLEMENTATION DEFINED