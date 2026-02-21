## Chapter 6 Memory map and registers

## 6.1 Memory map

SMMU registers occupy two consecutive 64KB pages starting from an at least 64KB-aligned boundary. Other OPTIONAL 64KB pages might follow these pages, depending on implemented features:

- If the V ATOS interface is supported, one 64KB page is present containing the V ATOS registers.
- If the Secure V ATOS interface is supported, one 64KB page is present containing the S\_VATOS registers.
- If Enhanced Command queue interfaces are supported, one or more Command queue control pages might be present, each containing one or more ECMDQ interfaces.
- If Enhanced Command queue interfaces are supported for Secure state, one or more Secure Command queue control pages might be present, each containing one or more ECMDQ interfaces.
- Any number of IMPLEMENTATION DEFINED pages might be present.

The presence and base addresses of all OPTIONAL pages are IMPLEMENTATION DEFINED and discoverable:

- The presence of VATOS support can be determined from SMMU\_IDR0.VATOS.
- -The VATOS page's base address is given by SMMU\_IDR2.BA\_VATOS
- -This base address is called O\_VATOS hereafter.
- The presence of Secure VATOS support can be determined from SMMU\_S\_IDR1.SECURE\_IMPL, SMMU\_S\_IDR1.SEL2 and SMMU\_IDR0.VATOS.
- -The Secure VATOS page's base address is given by SMMU\_S\_IDR2.BA\_S\_VATOS.
- -This base address is called O\_S\_VATOS hereafter.
- The presence of Command queue control pages can be determined from SMMU\_IDR1.ECMDQ.
- -The number of pages is discoverable from SMMU\_IDR6.

- -The offset of each page is discoverable from SMMU\_CMDQ\_CONTROL\_PAGE\_BASEn.ADDR.
- -These offsets are referred to as O\_CMDQCPn.
- The presence of Secure Command queue control pages can be determined from SMMU\_S\_IDR0.ECMDQ.
- -The number of pages is discoverable from SMMU\_S\_IDR6.
- -The offset of each page is discoverable from SMMU\_S\_CMDQ\_CONTROL\_PAGE\_BASEn.ADDR.
- -These offsets are referred to as O\_S\_CMDQCPn.
- The presence of the Realm Pages 0 and 1 can be determined from SMMU\_ROOT\_IDR0.REALM\_IMPL.
- -The offset for the Realm Page 0 is discoverable from SMMU\_ROOT\_IDR0.BA\_REALM, and this offset is referred to as O\_REALM.
- -Realm Page 1 is in the 64KB of physical address space immediately higher than Realm Page 0.
- The presence of Realm Command queue control pages can be determined from SMMU\_R\_IDR0.ECMDQ.
- -The number of pages is discoverable from SMMU\_R\_IDR6.
- -The offset of each page is discoverable from SMMU\_R\_CMDQ\_CONTROL\_PAGE\_BASEn.ADDR.
- -These offsets are referred to as O\_R\_CMDQCPn.
- The presence of all IMPLEMENTATION DEFINED register pages can be determined through the Peripheral ID registers and IMPLEMENTATION DEFINED registers, for example SMMU\_IDR4.

The base address of OPTIONAL pages is expressed as an offset from the SMMU extension address 0x20000 , in units of a 64KB page.

An SMMU that does not support any OPTIONAL or IMPLEMENTATION DEFINED register pages will occupy a 128K span of addresses, 0x00000 -0x1FFFF .

The values of all SMMU\_R\_CMDQ\_CONTROL\_PAGE\_BASEn.ADDR are such that the pages occupy a contiguous region of address space within the SMMU register file, and they are arranged in ascending value of n. If Secure Command queue control pages are implemented, this contiguous region of address space is immediately after the contiguous region of address space for the Secure Command queue control pages. Otherwise it is immediately after the contiguous region of address space for the Non-secure Command queue control pages.

| Offset                        | Register page                       |
|-------------------------------|-------------------------------------|
| 0x00000 - 0x0FFFF             | SMMUregisters, Page 0               |
| 0x10000 - 0x1FFFF             | SMMUregisters, Page 1               |
| 0x20000 -END                  | 0 or more OPTIONAL pages            |
| O_VATOS + 0x0000 - 0xFFFF     | VATOS interface registers           |
| O_S_VATOS + 0x0000 - 0xFFFF   | Secure VATOS interface registers    |
| O_CMDQCPn + 0x0000 - 0xFFFF   | Command queue control page n        |
| O_S_CMDQCPn + 0x0000 - 0xFFFF | Secure Command queue control page n |
| O_R_CMDQCPn + 0x0000 - 0xFFFF | Realm Command queue control page n  |
| O_REALM + 0x0000 - 0xFFFF     | Realm registers, Page 0             |
| O_REALM + 0x10000 - 0x1FFFF   | Realm registers, Page 1             |
| IMPLEMENTATION DEFINED        | Root Control Page                   |