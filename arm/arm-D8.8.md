## D8.8 Address tagging

| I XWNGB   | When address tagging is enabled, the top eight bits of the VAare ignored for the purposes of address translation and they are instead described as an address tag. An address tag might be used for software purposes, a Logical Address Tag, or both.   |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R LVTFP   | If address tagging is enabled in a translation regime, then the top eight bits of the VA, bits[63:56], have all of the following properties:                                                                                                             |
|           | • Bits[63:56] are the address tag.                                                                                                                                                                                                                       |
|           | • The bits are ignored during address translation.                                                                                                                                                                                                       |
|           | • If the translation system is enabled, then the bits are ignored when determining whether the address is out of range and therefore generates a Translation fault.                                                                                      |
|           | • If the translation system is not enabled, then the bits are ignored when determining whether the address is out of range and therefore generates an Address size fault.                                                                                |
| I PLXWZ   | If Logical Address Tagging is enabled, bits[59:56] are also the Logical Address Tag. For more information, see Logical Address Tagging.                                                                                                                  |

## D8.8.1 Address tag control

ICKLSG

Address tagging is controlled using the Top Byte Ignore (TBI) field in the TCR\_ELx register.

RBLBYZ

For a stage 1 translation that supports a single V A range, TCR\_ELx.TBI{0} determines whether address tagging is enabled.

RLPCSW

For a stage 1 translation that supports two V A ranges, all of the following determine whether address tagging is enabled:

- TCR\_ELx.TBI0 determines whether the lower address range uses address tags.

- TCR\_ELx.TBI1 determines whether the upper address range uses address tags.

RKYBQL

The TCR\_ELx.TBI{ n } bit controls address tagging whether or not the corresponding stage 1 translation is enabled.

IPRTHR

If FEAT\_PAuth is implemented and a TCR\_ELx.TBI{ n } bit enables address tagging, then the corresponding TCR\_ELx.TBID{ n } bit determines whether address tagging applies to both instruction addresses and data addresses, or just data addresses. For more information, see Pointer authentication.

## D8.8.2 Effect of address tagging on the PC

IWKJBM

RBBQKQ

RFWHLV

This section describes how the top byte of an address is considered when address tagging is enabled and an address is propagated to the PC for a branch, procedure return, exception, or exception return occurs.

For a stage 1 translation that supports a single V A range, if address tagging for instruction accesses is enabled in an Exception level, ELx, then bits[63:56] of the address loaded into the PC are forced to 0x00 in all of the following cases:

- Abranch or procedure return within ELx.
- An exception is taken to ELx.
- When an exception return does not generate an Illegal exception return, any exception return to ELx.
- Exiting from Debug state to ELx.

For a stage 1 translation that supports two V A ranges, if address tagging for instruction accesses is enabled in an Exception level, ELx, then bits[63:56] of the address loaded into the PC are a sign-extension of address bit[55] in all of the following cases:

- Abranch or procedure return within ELx.
- An exception is taken to ELx.
- When an exception return does not generate an Illegal exception return, any exception return to ELx.
- Exiting from Debug state to ELx.

## The AArch64 Virtual Memory System Architecture D8.8 Address tagging

ICCGCS

If the value of the SPSR\_ELx.M[4] bit of the saved process state is 1 when an Illegal exception return occurs, indicating a return to AArch32 state, then PC bits[63:32] are UNKNOWN.

RWGTRC

When address tagging is enabled and an address causes a Data Abort or a Watchpoint exception , the address tag is included in the V A returned in the FAR.