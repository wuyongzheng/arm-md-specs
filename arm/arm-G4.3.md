## G4.3 Mixed-endian support in AArch32

Table G4-2 shows the endianness of explicit data accesses and translation table walks.

## Table G4-2 Endianness support

| Exception level   | Explicit data accesses   | Stage 1 translation table walks   | Stage 2 translation table walks   |
|-------------------|--------------------------|-----------------------------------|-----------------------------------|
| EL0               | PSTATE.E                 | SCTLR(S/NS).EE                    | HSCTLR.EE                         |
| EL1               | PSTATE.E                 | SCTLR(S/NS).EE                    | HSCTLR.EE                         |
| EL2               | PSTATE.E                 | HSCTLR.EE                         | n/a                               |
| EL3               | PSTATE.E                 | SCTLR(S).EE                       | n/a                               |

AArch32 state provides the following options for endianness support:

- All Exception levels support mixed-endianness:
- -SCTLR(S/NS).EE, HSCTLR.EE, and PSTATE.E are RW.
- Only EL0 supports mixed-endianness and EL1, EL2, and EL3 support only little-endianness:
- -SCTLR(S/NS).EE and HSCTLR.EE are RES0. PSTATE.E is RW when in EL0 and RES0 when in EL1, EL2, or EL3. SPSR.E is also RES0 when not returning to EL0.
- Only EL0 supports mixed-endianness and EL1, EL2, and EL3 support only big-endianness:
- -SCTLR(S/NS).EE and HSCTLR.EE are RES1. PSTATE.E is RW when in EL0 and RES1 when in EL1, EL2, or EL3. SPSR.E is also RES1 when not returning to EL0.
- •
- All Exception levels support only little-endianness:
- -Each of SCTLR(S/NS).EE, HSCTLR.EE, PSTATE.E, and SPSR.E is RES0.
- All Exception levels support only big-endianness:
- -Each of SCTLR(S/NS).EE, HSCTLR.EE, PSTATE.E, and SPSR.E is RES1.

If mixed endian support is implemented for an Exception level using AArch32, endianness is controlled by PSTATE.E. For exception returns to AArch32 state, PSTATE.E is copied from SPSR\_ELx.E. If the target Exception level supports only little-endian accesses, SPSR\_ELx.E is RES0. If the target Exception level supports only big-endian accesses, SPSR\_ELx.E is RES1.

## Note

- When using AArch32, Arm deprecates PSTATE.E having a different value from the equivalent System register EE bit when in EL1, EL2 or EL3. The use of the SETEND instruction is also deprecated.
- If the higher Exception levels are using AArch64, the corresponding registers are:
- -SCTLR\_EL1 for SCTLR(NS).
- -SCTLR\_EL2 for HSCTLR.
- -SCTLR\_EL3 for SCTLR(S).

The BigEndian() function determines whether the current Exception level and Execution state is using big-endian data.

For more information about endianness in the Arm architecture, see Endian support.