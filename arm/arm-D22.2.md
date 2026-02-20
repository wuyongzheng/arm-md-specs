## D22.2 SME traps and exceptions

IQZNRN

This section provides additional details for SME-related exceptions. For a list of exception priorities, see RZFGJP.

RJZTCQ

RGTKQD

If FEAT\_SME is not implemented, then SME and SME2 instructions are UNDEFINED.

If FEAT\_SME2 is not implemented, then SME2 instructions are UNDEFINED.

RPLYVH If any of the following is true, an SVE instruction is UNDEFINED:

- FEAT\_SME is not implemented and FEAT\_SVE is not implemented.
- FEAT\_SVE is not implemented and the instruction is illegal when the PE is in Streaming SVE mode.

DDMBHW The SME-related instructions are:

- SMEdata-processing instructions.
- SMSTART and SMSTOP instructions.
- AArch64 MRS and MSR instructions which directly access any of the SVCR, SMCR\_EL1, SMCR\_EL2, or SMCR\_EL3 registers.

IBLTMB The CPACR\_EL1.SMEN, CPTR\_EL2.{SMEN, TSM}, CPTR\_EL3.ESM trap and enable controls apply to all SME-related instructions.

- IRGBVJ The SMCR\_ELx.EZT0 enable controls apply to the following SME2 instructions that access the ZT0 register:
- LDR (table) .
- LUTI2 , LUTI4 .
- MOVT .
- STR (table) .
- ZERO (table) .

FEAT\_SME adds an SME exception syndrome in ESR\_ELx to identify instructions that are trapped because of any of:

- The SME trap controls in CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3.
- The SME2 trap controls SMCR\_ELx.EZT0.
- The PSTATE.SM and PSTATE.ZA modes.
- INWNQZ When the PE is in Streaming SVE mode or when FEAT\_SVE is not implemented, the CPACR\_EL1.SMEN, CPTR\_EL2.{SMEN,TSM}, CPTR\_EL3.ESM controls configure SVE instructions to trap, and the CPACR\_EL1.ZEN, CPTR\_EL2.{ZEN, TZ}, CPTR\_EL3.EZ controls do not cause any SVE instructions to be trapped.
- IPKGPR When the PE is not in Streaming SVE mode and FEAT\_SVE is implemented, the CPACR\_EL1.ZEN, CPTR\_EL2.{ZEN, TZ}, CPTR\_EL3.EZ controls configure SVE instructions to trap, and the CPACR\_EL1.SMEN, CPTR\_EL2.{SMEN, TSM}, CPTR\_EL3.ESM controls do not cause any SVE instructions to be trapped.

RGGLFV When an SVE MOVPRFX instruction predictably prefixes an SVE instruction that is illegal due to the current value of PSTATE.SM or PSTATE.ZA, then the execution of either of the instructions generates an exception due to SME functionality, consistent with the behaviors defined by RRWVTR.

IXKMKY