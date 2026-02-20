## D8.9 Logical Address Tagging

| R MWZSJ   | All statements in this section require implementation of FEAT_MTE2.                                                                                                                      |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R RYFYK   | For the purposes of address translation, when Logical Address Tagging is enabled in a translation regime, bits[59:56] of the VAare ignored, and instead form a Logical Address Tag.      |
| R HYJDX   | If all of the following are true, then the VA, bits[63:60], can be used to hold a PAC: • Logical Address Tagging is enabled. • Address tagging is disabled. • FEAT_PAuth is implemented. |

## D8.9.1 Logical Address Tag control

RTQHWL

RSHNLM

For a stage 1 translation that supports a single V A range, all of the following determine whether Logical Address Tagging is enabled:

- TCR\_ELx.TBI n .
- If FEAT\_MTE\_NO\_ADDRESS\_TAGS is implemented, then TCR\_ELx.MTX n .

For a stage 1 translation that supports two V A ranges, all of the following determine whether Logical Address Tagging is enabled:

- For the lower address range:
- -TCR\_ELx.TBI0.
- -If FEAT\_MTE\_NO\_ADDRESS\_TAGS is implemented, then TCR\_ELx.MTX0.
- For the upper address range:
- -TCR\_ELx.TBI1.
- -If FEAT\_MTE\_NO\_ADDRESS\_TAGS is implemented, then TCR\_ELx.MTX1.

RPXNMX The TCR\_ELx.TBI{n} bit, and if FEAT\_MTE\_NO\_ADDRESS\_TAGS the TCR\_ELx.MTX{n} bit, controls Logical Address Tagging whether or not the corresponding stage 1 translation is enabled.

IQVQJP

RNPYMC

IBBHPM

When Address tagging is enabled for an address range, whether Logical Address Tagging is enabled has no effect on a PE other than for use in:

- Tag Checking.
- Access to Allocation Tags in memory.

If Logical Address Tagging is enabled and Address tagging is disabled, then bits[59:56] of the V A have all of the following properties:

- For a stage 1 translation that supports a single V A range, the bits are treated as 0b0000 in all of the following cases:
- -During address translation.
- -If the translation system is enabled, then when determining whether the address is out of range and therefore generates a Translation fault.
- -If the translation system is not enabled, then when determining whether the address is out of range and therefore generates an Address size fault.
- For a stage 1 translation that supports two V A ranges, the bits are treated as a sign-extension of V A bit[55] in all of the following cases:
- -During address translation.
- -If the translation system is enabled, then when determining whether the address is out of range and therefore generates a Translation fault.
- -If the translation system is not enabled, then when determining whether the address is out of range and therefore generates an Address size fault.

For the properties of V A bits[59:56] when Address tagging is enabled, see Address tagging.

RPKRBM

RWCTSR

## D8.9.1.1 Effect of Logical Address Tagging on address translation and cache maintenance instructions

For the purpose of determining whether bits [59:56] hold a Logical Address Tag, all address translation instructions and cache maintenance instructions that perform address translation are treated as memory accesses.

## D8.9.1.2 Effect of Logical Address Tagging on the PC

When an address is used as an instruction address and not for a data access, Logical Address Tagging is treated as disabled when loading an address into the PC in all of the following cases:

- Abranch or procedure return within an Exception level.
- Taking an exception to an Exception level.
- Exception return to an Exception level.
- Exit from Debug state to an Exception level.

RHTSLR If FEAT\_PAuth is implemented, Logical Address Tagging is treated as disabled on execution of any of the following instructions that operate on a PAC field within an instruction address:

- AUTI* .
- PACI* .
- XPACI .
- XPACLRI .