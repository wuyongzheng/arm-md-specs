## 4.6 DPT maintenance

## 4.6.1 CMD\_DPTI\_ALL

<!-- image -->

Removes all cached DPT information associated with the target Security state. The target Security state is:

- Realm state when issued to a Realm command queue.
- Non-secure state when issued to a Non-secure command queue.
- Non-secure state when issued to a Secure command queue and SMMU\_S\_IDR3.SAMS = 0.

This command results in CERROR\_ILL for each of the following conditions:

- If issued on a Realm command queue when SMMU\_R\_IDR3.DPT = 0.
- If issued on a Non-secure command queue when SMMU\_IDR3.DPT = 0.
- If issued on a Secure command queue when SMMU\_IDR3.DPT = 0 or SMMU\_S\_IDR3.SAMS = 1.

## 4.6.2 CMD\_DPTI\_PA

<!-- image -->

Removes cached DPT information for the aligned region of length SIZE, starting from the base address specified in Physical Address, for the target Security state. The target Security state is:

- Realm state when issued to a Realm command queue.
- Non-secure state when issued to a Non-secure command queue.
- Non-secure state when issued to a Secure command queue and SMMU\_S\_IDR3.SAMS = 0.

If the address is not aligned to the effective size of the invalidation, no entries are required to be invalidated.

Bits [11:0] of the base address are treated as 0.

Bits of the base address above the implemented output address size, advertised in SMMU\_IDR5.OAS, are treated as 0.

The encoding of the SIZE field is:

| Value   | Meaning   |
|---------|-----------|
| 0b0000  | 4KB       |
| 0b0001  | 16KB      |
| 0b0010  | 64KB      |
| 0b0011  | 2MB       |
| 0b0100  | 32MB      |
| 0b0101  | 512MB     |
| 0b0110  | 1GB       |
| 0b0111  | 16GB      |
| 0b1000  | 64GB      |
| 0b1001  | 512GB     |

Other values are Reserved. If SIZE selects a Reserved value, the SMMU is not required to invalidate any entries.

A DPT TLB entry is only guaranteed to be invalidated by this command if SIZE selects a value equal to or greater than the region size of the DPT TLB entry.

The encoding of the Leaf field is:

| Value   | Meaning                                                 |
|---------|---------------------------------------------------------|
| 0b0     | Invalidate information from all levels of the walk.     |
| 0b1     | Invalidate entries from the final level of lookup only. |

This command results in CERROR\_ILL for each of the following conditions:

- If issued on a Realm command queue when SMMU\_R\_IDR3.DPT = 0.
- If issued on a Non-secure command queue when SMMU\_IDR3.DPT = 0.
- If issued on a Secure command queue when SMMU\_IDR3.DPT = 0 or SMMU\_S\_IDR3.SAMS = 1.