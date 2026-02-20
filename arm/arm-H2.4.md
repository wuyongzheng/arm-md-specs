## H2.4 Behavior in Debug state

Instructions are executed in Debug state from the Instruction Transfer Register, ITR. The debugger controls which instructions are executed in Debug state by writing the instructions to the External Debug Instruction Transfer register, EDITR.

The Execution state of the PE determines which instruction set is executed:

- If the PE is in AArch64 state it executes A64 instructions.
- If the PE is in AArch32 state it executes T32 instructions:
- -For a 32-bit T32 instruction, EDITR[15:0] specifies the first halfword and EDITR[31:16] specifies the second halfword.
- -For a 16-bit T32 instruction, EDITR[15:0] contains the instruction and EDITR[31:16] is ignored. All 16-bit T32 instructions are UNPREDICTABLE in Debug state.

The PE does not execute A32 instructions in Debug state.

Some instructions are available only in Debug state. See Debug state operations, DCPS, DRPS, MRS, MSR. In Non-debug state these instructions are UNDEFINED.

The following sections describe behavior in Debug state:

- PSTATE in Debug state.
- Executing instructions in Debug state.
- Decode tables.
- Security in Debug state.
- Privilege in Debug state.
- Debug state operations, DCPS, DRPS, MRS, MSR.
- Exceptions in Debug state.
- Accessing registers in Debug state.
- Accessing memory in Debug state.

This section specifies the CONSTRAINED UNPREDICTABLE behaviors that apply in Debug state, but see Changing the value of EDECR.SS when not in Debug state for a change in Non-debug state that causes CONSTRAINED UNPREDICTABLE behavior.

## H2.4.1 PSTATE in Debug state

PSTATE.{N, Z, C, V, Q, IT, GE, SS, ALLINT, SSBS, BTYPE, D, A, I, F, T, PM} are all ignored in Debug state:

- There are no conditional instructions in Debug state.
- In AArch32 state, the PE executes only T32 instructions and PSTATE.IT is ignored.
- Software step is inactive.
- Asynchronous exceptions and debug events are ignored.
- If FEAT\_SSBS is implemented, then hardware is permitted to load or store speculatively, regardless of the value of PSTATE.SSBS.
- In AArch64 state, PSTATE.BTYPE is treated as 0b00 .

Instructions executed in Debug state indirectly read PSTATE.{TCO, UAO, PAN, IL, E, M, nRW, EL, SP} as they would in Non-debug state.

Note

PSTATE.DIT is not guaranteed to have any effect in Debug state.

In Debug state:

- PSTATE.PAN is set to 1 by:

- -A DCPS&lt;n&gt; instruction to EL1 using AArch64 if SCTLR\_EL1.SPAN == 0.
- -A DCPS&lt;n&gt; instruction to EL2 using AArch64 if SCTLR\_EL2.SPAN == 0.
- PSTATE.UINJ is set to 0 by a DCPS&lt;n&gt; instruction to AArch64 state.
- PSTATE.UAO is set to 0 by a DCPS&lt;n&gt; instruction to AArch64 state.
- PSTATE.TCO is set to 1 by a DCPS&lt;n&gt; instruction to AArch64 state.
- PSTATE.EXLOCK is set to 0 by a DCPS&lt;n&gt; instruction to AArch64 state.
- If FEAT\_SSBS is implemented, the DCPS&lt;n&gt; instruction leaves the PSTATE.SSBS bit UNKNOWN.
- If FEAT\_PAuth\_LR is implemented, the DCPS&lt;n&gt; instruction sets the PSTATE.PACM bit to 0.

PSTATE can also be changed by taking exceptions in Debug state, and by the execution of DCPS&lt;n&gt; and DRPS instructions.

When FEAT\_MTE is implemented, if Memory access mode is enabled and PSTATE.TCO is 0, reads and writes to the external debug interface DTR registers are CONSTRAINED UNPREDICTABLE, with the following permitted behaviors:

- The PE behaves as if PSTATE.TCO is 0. That is, the load or store operation performs the tag check if required.
- The PE behaves as if PSTATE.TCO is 1. That is, the load or store operation does not perform the tag check.

For more information, see The Memory Tagging Extension.

## H2.4.2 Executing instructions in Debug state

The instructions executed in Debug state must be either A64 instructions or T32 instructions, depending on the current Execution state.

Each instruction falls into one of the following groups:

- Debug state instructions. These are instructions that are changed in Debug state. See A64 instructions that are changed in Debug state and T32 instructions that are changed in Debug state.
- Instructions that are unchanged in Debug state. See A64 instructions that are unchanged in Debug state and T32 instructions that are unchanged in Debug state. Where these sections describe the behavior of an instruction as unchanged in Debug state, or having the same behavior as in Non-debug state, and that instruction would generate an exception in Non-debug state, then the behavior of the exception is as described in Exceptions in Debug state.
- Instructions that are UNPREDICTABLE or CONSTRAINED UNPREDICTABLE in Debug state. See A64 instructions that are CONSTRAINED UNPREDICTABLE in Debug state and T32 instructions that are CONSTRAINED UNPREDICTABLE in Debug state.

All T32 instructions are treated as unconditional, regardless of PSTATE.IT. See PSTATE in Debug state.

If FEAT\_RME is implemented and EDSCR.SDD == 1, then exceptions from Non-secure, Secure, Realm state are never taken to Root state. If FEAT\_RME is not implemented and EDSCR.SDD == 1, then an exception from Non-secure state is never taken to Secure state.

See Security in Debug state.

## H2.4.2.1 Executing A64 instructions in Debug state

The following sections describe the behavior of the A64 instructions in Debug state:

- A64 instructions that are changed in Debug state.
- A64 instructions that are unchanged in Debug state.
- A64 instructions that are CONSTRAINED UNPREDICTABLE in Debug state.

## H2.4.2.1.1 A64 instructions that are changed in Debug state

The following instructions are defined in Debug state, but are UNDEFINED in Non-debug state:

- DCPS .

Note

DCPS can be UNDEFINED in certain conditions in Debug state. See DCPS&lt;n&gt;.

- DRPS .

- MRS (DLR\_EL0), MRS (DSPSR\_EL0), MSR (DLR\_EL0), MSR (DSPSR\_EL0)

- If FEAT\_SME2 is implemented, then MOVT (table to scalar) and MOVT (scalar to table).

The following instructions are defined in both Non-Debug and Debug states and have changed behavior in Debug state:

- If FEAT\_SVE is implemented, then CMPNE (immediate) with byte element size.

Note

In Debug state, CMPNE (immediate) with byte element size sets DLR\_EL0 and DSPSR\_EL0 to UNKNOWN values. However, the instruction is unchanged with respect to the SVE vector and SVE predicate source and destination registers.

For more information, see Debug state operations, DCPS, DRPS, MRS, MSR.

## H2.4.2.1.2 A64 instructions that are unchanged in Debug state

The following list shows the instructions that are unchanged in Debug state:

## Any instruction that is UNDEFINED in Non-debug state

This list of instructions excludes:

- Any instruction listed in A64 instructions that are changed in Debug state.

- Any instruction listed in A64 instructions that are CONSTRAINED UNPREDICTABLE in Debug state that is UNDEFINED because an enable or disable bit is not RES0 or RES1

## Instructions that move System or Special-purpose registers to or from a general-purpose register

This list of instructions:

- Includes the instructions to transfer a general-purpose register to or from the DTR, which can be executed at any Exception level.

- Excludes PSTATE access instructions.

These instructions are:

- MRS &lt;special\_reg&gt; , MSR &lt;special\_reg&gt; .

Note

This does not include NZCV, DAIF, DAIFSet, DAIFClr, SPSel, CurrentEL, PAN, UAO, DIT, TCO, and PM.

- MRS &lt;system\_reg&gt; , MSR &lt;system\_reg&gt; .

- If FEAT\_SYSREG128 is implemented, then MRRS &lt;system\_reg&gt; , MSRR &lt;system\_reg&gt; .

## Floating-point moves between a SIMD&amp;FP register and a general-purpose register

These instructions are:

- FMOV (between a general-purpose register and a half-precision register).

- FMOV (between a general-purpose register and a single-precision register).

- FMOV (between a general-purpose register and a double-precision register).

- FMOV (between a general-purpose register and a SIMD element).

## SIMD moves between a SIMD&amp;FP register and a general-purpose register

## These instructions are:

- INS (from a general-purpose register to a SIMD element).
- UMOV (from a SIMD element to a general-purpose register).

## SVE instructions

If FEAT\_SVE is implemented, then these instructions are:

- CPY (immediate, zeroing) with byte element size and a shift amount of 0.
- DUP (scalar).
- EXT , destructive variant.
- INSR (scalar).
- PMOV (to predicate).
- PMOV (to vector).
- PTRUE with ALL constraint and byte element size.
- RDFFR (unpredicated).
- RDVL .
- WRFFR .

## SMEinstructions

If FEAT\_SME is implemented, then these instructions are:

- MOVA (tile to vector, single), MOVA (vector to tile, single).
- MRS SVCR , MSR SVCR .
- RDSVL .

## Barriers These instructions are:

- DMB .
- DSB .
- ISB .
- CSDB .
- SSBB .
- PSSBB .
- If FEAT\_SB is implemented, then SB .
- If FEAT\_SPE is implemented, then PSB .
- If FEAT\_TRBE is implemented, then TSB .
- If FEAT\_RAS is implemented, then ESB .

## Memory access instructions at various access sizes

The following constraints apply:

- General purpose-registers only.
- One of the following addressing modes:
- -Unscaled (9-bit signed) immediate offset.
- -Immediate (9-bit signed) post-indexed.
- -Immediate (9-bit signed) pre-indexed.
- -Unprivileged (9-bit signed).
- Not literal.
- One of the following types:
- -(Single) register.
- -Exclusive.
- -Exclusive pair.

- -Acquire/Release.
- -Acquire/Release Exclusive.
- -Acquire/Release Exclusive pair.
- 32-bit and 64-bit target register variants.

## These instructions are:

- LDR , LDRB , LDRH , LDRSB , LDRSH , LDRSW (immediate, not literal).
- LDUR , LDURB , LDURH , LDURSB , LDURSH , LDURSW (immediate).
- LDTR , LDTRB , LDTRH , LDTRSB , LDTRSH , LDTRSW (immediate).
- LDAR , LDARB , LDARH , LDXR , LDXRB , LDXRH , LDAXR , LDAXRB , LDAXRH .
- LDXP , LDAXP .
- STR , STRB , STRH (immediate).
- STUR , STURB , STURH (immediate).
- STTR , STTRB , STTRH (immediate).
- STLR , STLRB , STLRH , STXR , STXRB , STXRH , STLXR , STLXRB , STLXRH .
- STXP , STLXP .
- If FEAT\_LOR is implemented, then:
- -LDLAR , LDLARB , LDLARH .
- -STLLR , STLLRBB , STLLRH .
- If FEAT\_LSE is implemented, then:
- -CAS , CASB , CASH , CASP .
- -SWP , SWPB , SWPH .
- -LDADD , LDADDB , LDADDH .
- -LDCLR , LDCLRB , LDCLRH .
- -LDEOR , LDEORB , LDEORH .
- -LDSET , LDSETB , LDSETH .
- -LDSMAX , LDSMAXB , LDSMAXH .
- -LDSMIN , LDSMINB , LDSMINH .
- -LDUMAX , LDUMAXB , LDUMAXH .
- -LDUMIN , LDUMINB , LDUMINH .
- -STADD , STADDB , STADDH .
- -STCLR , STCLB , STCLRH .
- -STEOR , STEORB , STEORH .
- -STSET , STSETB , STSETH .
- -STSMAX , STSMAXB , STSMAXH .
- -STSMIN , STSMINB , STSMINH .
- -STUMAX , STUMAXB , STUMAXH .
- -STUMIN , STUMINB , STUMINH .
- If FEAT\_LSE128 is implemented, then:
- -LDCLRP .
- -LDSETP .
- -SWPP .
- If FEAT\_LRCPC is implemented, then LDAPR, LDAPRB, LDAPRH .
- If FEAT\_LRCPC2 is implemented, then:
- -LDAPURH, LDAPURSH, LDAPUR, LDAPURSW, LDAPURSB, LDAPURB .
- -STLUR, STLURH, STLURB .
- If FEAT\_LRCPC3 is implemented, then:
- -LDAP1 (SIMD&amp;FP), LDAPR, LDAPUR (SIMD&amp;FP), LDAPUR , LDIAPP, STLR .
- -STL1 (SIMD&amp;FP), STILP , STLUR (SIMD&amp;FP).
- If FEAT\_LS64 is implemented, regardless of whether FEAT\_LS64WB is implemented, then:
- -LD64B .
- -ST64B .
- If FEAT\_LS64\_V is implemented, then ST64BV .
- If FEAT\_LS64\_ACCDATA is implemented, then ST64BV0 .

## Move immediate to general-purpose register

These instructions are:

- MOVZ , MOVN , MOVK (immediate).
- MOV (between a general-purpose register and the stack pointer).

## System instructions, Send Event, NOP, Clear Exclusive, and Prediction

In this context, the System instructions are the Cache maintenance instructions, TLB maintenance instructions, Address translation instructions, the prediction restriction instructions, and the check feature instruction.

## These instructions are:

- IC .
- DC .
- TLBI and, if FEAT\_D128 is implemented, then TLBIP .
- AT .
- SEV , SEVL .
- NOP .
- If FEAT\_CLRBHB is implemented, then CLRBHB .
- CLREX .
- CFP .
- If FEAT\_SPECRES2 is implemented, then COSP .
- CPP .
- DVP .
- If FEAT\_CHK is implemented, then CHKFEAT .

## Pointer authentication instructions

These instructions are:

- If FEAT\_PAuth is implemented, then:
- -AUTIA , AUTIAZ , AUTIZA .
- -AUTIB , AUTIBZ , AUTIZB .
- -AUTDA , AUTDZA .
- -AUTDB , AUTDZB .
- -PACIA , PACIAZ , PACIZA .
- -PACIB , PACIBZ , PACIZB .
- -PACDA , PACDZA .
- -PACDB , PACDZB .
- -PACGA .
- -XPACD , XPACI , XPACLRI .
- If FEAT\_PAuth\_LR is not implemented or PSTATE.PACM is 0, then:
- -AUTIASP , AUTIA1716 .
- -AUTIBSP , AUTIB1716 .
- -PACIASP , PACIA1716 .
- -PACIBSP , PACIB1716 .
- If FEAT\_PAuth\_LR is implemented, then:
- -PACIA171615 and PACIB171615 .
- -AUTIA171615 and AUTIB171615 .

## Memory Tagging Extension instructions

These instructions are:

- If FEAT\_MTE is implemented, then:
- -ADDG .

- -SUBG .
- -STG (signed offset).
- -STZG (signed offset).
- -ST2G (signed offset).
- -STZ2G (signed offset) .
- -STGP (signed offset) .
- -LDG .
- If FEAT\_MTE2 is implemented, then:
- -LDGM .
- -STGM .
- -STZGM .

## BRBEinstructions

These instructions are:

- If FEAT\_BRBE is implemented, then:
- -BRB IALL .
- -BRB INJ .

## GCSinstructions

These instructions are:

- If FEAT\_GCS is implemented, then:
- -GCSB .
- -GCSPUSHM, GCSPOPM .
- -GCSPUSHX, GCSPOPX .
- -GCSSS1, GCSSS2 .
- -GCSSTR, GCSSTTR .

## H2.4.2.1.3 A64 instructions that are CONSTRAINED UNPREDICTABLE in Debug state

This subsection describes all instructions that are not listed in either:

- A64 instructions that are changed in Debug state.
- A64 instructions that are unchanged in Debug state.

These instructions are CONSTRAINED UNPREDICTABLE in Debug state. In general, the permissible behaviors are:

- The instruction is UNDEFINED.
- The instruction executes as a NOP .
- If the instruction reads the PC or PSTATE, it uses an UNKNOWN value.
- If the instruction modifies the PC or PSTATE, other than by advancing the PC to the sequentially next instruction, it sets DLR\_EL0 and DSPSR\_EL0 to UNKNOWN values.
- If the instruction is similar to a Debug state instruction, it executes as that Debug state instruction.
- The instruction has the same behavior as in Non-debug state.

The following list shows the permissible behaviors for A64 instruction in Debug state. An instruction might appear multiple times in the list, in which case the choice of permissible behaviors is any of those listed. An example of this is CCMP .

## Exception-generating instructions

These instructions are:

- SVC .
- HVC .
- SMC .

- BRK .

- HLT .

These instructions behave in one of the following ways:

- They are UNDEFINED.

- They execute as a NOP .

- SVC behaves as DCPS1 .

- HVC behaves as DCPS2 .

- SMC behaves as DCPS3 .

- They generate the exception that the instruction would generate in Non-debug state. The exception is taken as described in Exceptions in Debug state.

Note

SMC does not generate a Secure Monitor Call exception if EDSCR.SDD is 1.

## Instructions that explicitly write to the PC (branches)

## These instructions are:

- B , B.cond , BL , BLR , BR , CBZ , CBNZ , RET , TBZ , TBNZ .
- If FEAT\_HBC is implemented, then BC.cond .
- If FEAT\_PAuth is implemented, then RETAA , RETAB , BRAA , BRAB , BLRAA , BLRAB , BLRAAZ , BLRABZ .
- If FEAT\_PAuth\_LR is implemented, then RETAASPPC , RETABSPPC , RETAASPPCR , RETABSPPCR .

These instructions behave in one of the following ways:

- They are UNDEFINED.
- They execute as a NOP .
- They execute as in Non-debug state without branching and set DSPSR\_EL0 and DLR\_EL0 to UNKNOWN values.

## Exception return and related instructions

These instructions are:

- ERET .
- If FEAT\_PAuth is implemented, then ERETAA , ERETAB .

These instructions behave in one of the following ways:

- They are UNDEFINED.
- They execute as a NOP .
- They execute as in Non-debug state without branching, set DSPSR\_EL0 and DLR\_EL0 to UNKNOWN values, and either:
- -Execute the DRPS operation instead of performing an exception return, using UNKNOWN SPSR values.
- -Do not change the Exception level.

## Instructions that request entry to a low-power state

These instructions are:

- WFE , WFI .
- If FEAT\_WFxT is implemented, then WFET , WFIT .

These instructions behave in one of the following ways:

- They are UNDEFINED.
- They execute as a NOP .

- They generate a synchronous exception if the corresponding instruction would be trapped in Non-debug state. See Configurable instruction controls.
- A WFE instruction clears the Event register if it is set.

Note

This means that these instructions must not suspend execution.

## Instructions that read the PC

## These instructions are:

- LDR (literal), LDRSW (literal).
- ADR , ADRP .
- PRFM (literal).
- If FEAT\_PAuth\_LR is implemented, then:
- -AUTIASPPC (immediate), AUTIBSPPC (immediate).
- -PACIASPPC , PACIBSPPC .
- -PACNBIASPPC , PACNBIBSPPC .
- -RETAASPPC , RETABSPPC .

## These instructions behave in one of the following ways:

- They are UNDEFINED.
- They execute as a NOP .
- They execute as in Non-debug state, using an UNKNOWN value for the PC operand.

## Instructions that explicitly modify PSTATE, other than DCPS and DRPS

## These instructions are:

- ADDS , SUBS , ADCS , SBCS , ANDS , BICS , CCMN , CCMP .
- FCMP , FCMPE , FCCMP , FCCMPE .
- MSR DAIFSet (immediate), MSR DAIFClr (immediate), MSR SPSel (immediate).
- MSR NZCV (register), MSR DAIF (register), MSR SPSel (register).
- If FEAT\_PAN is implemented, then:
- -MSR PAN (immediate).
- -MSR PAN (register).
- If FEAT\_UAO is implemented, then:
- -MSR UAO (immediate).
- -MSR UAO (register).
- If FEAT\_FlagM is implemented, then:
- -CFINV .
- -RMIF .
- -SETF8 .
- -SETF16 .
- If FEAT\_DIT is implemented, then MSR DIT .
- If FEAT\_FlagM2 is implemented, then:
- -AXFLAG . -XAFLAG .
- If FEAT\_MTE is implemented, then MSR TCO .
- If FEAT\_RNG is implemented, then:
- -MRS RNDR .
- -MRS RNDRRS .
- If FEAT\_NMI is implemented, then:
- -MSR ALLINT (immediate).
- -MSR ALLINT (register).
- If FEAT\_EBEP is implemented, then:

- -MSR PM (immediate).
- -MSR PM (register).
- If FEAT\_MOPS is implemented, then:
- -CPYFP , CPYFPN , CPYFPRN , CPYFPRT , CPYFPRTN , CPYFPRTRN , CPYFPRTWN , CPYFPT , CPYFPTN , CPYFPTRN , CPYFPTWN , CPYFPWN , CPYFPWT , CPYFPWTN , CPYFPWTRN , CPYFPWTWN .
- -CPYP , CPYPN , CPYPRN , CPYPRT , CPYPRTN , CPYPRTRN , CPYPRTWN , CPYPT , CPYPTN , CPYPTRN , CPYPTWN , CPYPWN , CPYPWT , CPYPWTN , CPYPWTRN , CPYPWTWN .
- -SETP , SETPN , SETPT , SETPTN .
- -SETGP , SETGPN , SETGPT , SETGPTN .
- If FEAT\_SVE is implemented, then:
- -ANDS , BICS , EORS , NANDS , NORS , ORNS , ORRS , PTEST .
- -BRKAS , BRKBS , BRKNS , BRKPAS , BRKPBS .
- -CMPEQ , CMPGE , CMPGT , CMPHI , CMPHS , CMPLE , CMPLO , CMPLS , CMPLT , CMPNE .
- -MATCH , NMATCH .
- -PFIRST , PNEXT , CTERMEQ , CTERMNE .
- -PTRUES .
- -RDFFRS .
- -WHILEGE , WHILEGT , WHILEHI , WHILEHS (predicate).
- -WHILELE , WHILELO , WHILELS , WHILELT (predicate).
- -WHILERW , WHILEWR .
- If FEAT\_SME2 or FEAT\_SVE2p1 is implemented, then:
- -WHILEGE , WHILEGT , WHILEHI , WHILEHS (predicate pair).
- -WHILELE , WHILELO , WHILELS , WHILELT (predicate pair).
- -WHILEGE , WHILEGT , WHILEHI , WHILEHS (predicate as counter).
- -WHILELE , WHILELO , WHILELS , WHILELT (predicate as counter).
- If FEAT\_PAuth\_LR is implemented, then:
- -PACM .

These instructions behave in one of the following ways:

- They are UNDEFINED.
- They execute as a NOP .
- They execute as in Non-debug state, setting DSPSR\_EL0, DLR\_EL0, and any PSTATE field written by the instruction to UNKNOWN values.

## Instructions that read PSTATE.{N, Z, C, V} or other PSTATE fields

## These instructions are:

- CSEL , CSINC , CSINV , CSNEG , CCMN , CCMP , FCSEL , FCCMP , FCCMPE .
- ADC , ADCS , SBC , SBCS .
- MRS NZCV , MRS DAIF , MRS SPSel , MRS CurrentEL .
- If FEAT\_PAN is implemented, then MRS PAN .
- If FEAT\_UAO is implemented, then MRS UAO .
- If FEAT\_FlagM is implemented, then CFINV .
- If FEAT\_FlagM2 is implemented, then AXFLAG , XAFLAG .
- If FEAT\_DIT is implemented, then MRS DIT .
- If FEAT\_MTE is implemented, then MRS TCO .
- If FEAT\_NMI is implemented, then MRS ALLINT .
- If FEAT\_EBEP is implemented, then MRS PM .
- If FEAT\_MOPS is implemented, then:
- -CPYFM , CPYFMN , CPYFMRN , CPYFMRT , CPYFMRTN , CPYFMRTRN , CPYFMRTWN , CPYFMT , CPYFMTN , CPYFMTRN , CPYFMTWN , CPYFMWN , CPYFMWT , CPYFMWTN , CPYFMWTRN , CPYFMWTWN .
- -CPYFE , CPYFEN , CPYFERN , CPYFERT , CPYFERTN , CPYFERTRN , CPYFERTWN , CPYFET , CPYFETN , CPYFETRN , CPYFETWN , CPYFEWN , CPYFEWT , CPYFEWTN , CPYFEWTRN , CPYFEWTWN .

## Hint instructions

If FEAT\_DGH is implemented, then this instruction is:

- DGH .

This instruction behaves in one of the following ways:

- It executes as a NOP .
- It executes as in Non-debug state.

## All other instructions

These instructions behave in one of the following ways:

- They are UNDEFINED.
- They execute as a NOP .
- They execute as in Non-debug state.

Note

This includes instructions defined as UNPREDICTABLE or CONSTRAINED UNPREDICTABLE in Non-debug state. These instructions are UNPREDICTABLE or CONSTRAINED UNPREDICTABLE in Debug state.

## H2.4.2.2 Executing T32 instructions in Debug state

The following sections describe the behavior of the T32 instructions in Debug state:

- T32 instructions that are changed in Debug state.
- T32 instructions that are unchanged in Debug state.
- T32 instructions that are CONSTRAINED UNPREDICTABLE in Debug state.

## H2.4.2.2.1 T32 instructions that are changed in Debug state

The following T32 instructions are defined in Debug state, but are UNDEFINED in Non-debug state:

- DCPS .
- -CPYM , CPYMN , CPYMRN , CPYMRT , CPYMRTN , CPYMRTRN , CPYMRTWN , CPYMT , CPYMTN , CPYMTRN , CPYMTWN , CPYMWN , CPYMWT , CPYMWTN , CPYMWTRN , CPYMWTWN .
- -CPYE , CPYEN , CPYERN , CPYERT , CPYERTN , CPYERTRN , CPYERTWN , CPYET , CPYETN , CPYETRN , CPYETWN , CPYEWN , CPYEWT , CPYEWTN , CPYEWTRN , CPYEWTWN .
- -SETM , SETMN , SETMT , SETMTN .
- -SETE , SETEN , SETET , SETETN .
- -SETGM , SETGMN , SETGMT , SETGMTN .
- -SETGE , SETGEN , SETGET , SETGETN .
- If FEAT\_SVE is implemented, then all SVE instructions that use a predicate.
- If FEAT\_THE is implemented, then RCW and RCWS .
- If FEAT\_PAuth\_LR is implemented, then:
- -If PSTATE.PACM is 1, then PACIASP , PACIBSP , PACIA1716 , PACIB1716 , AUTIASP , AUTIBSP , AUTIA1716 , AUTIB1716 , RETAA , and RETAB .

These instructions behave in one of the following ways:

- They are UNDEFINED.
- They execute as a NOP .
- They execute as in Non-debug state:
- -For the conditional operations and those that use Condition flags as an input, these instructions use UNKNOWN values for the Condition flag.
- -For the MRS instruction, they return an UNKNOWN value.
- -For the RCW and RCWS instructions, they return an UNKNOWN value.
- -For the PACIASP and PACIBSP instructions when PSTATE.PACM is 1, they use an UNKNOWN value for the PC operand.

Note

DCPS can be UNDEFINED in certain conditions in Debug state. See DCPS&lt;n&gt;.

- MRC p15,3,&lt;Rt&gt;,c4,c5,0 (DSPSR).
- MCR p15,3,&lt;Rt&gt;,c4,c5,0 (DSPSR).
- MRC p15,3,&lt;Rt&gt;,c4,c5,1 (DLR).
- MCR p15,3,&lt;Rt&gt;,c4,c5,1 (DLR).

In addition, ERET executes the DRPS operation in Debug state.

For more information, see Debug state operations, DCPS, DRPS, MRS, MSR.

## H2.4.2.2.2 T32 instructions that are unchanged in Debug state

The following list shows the instructions that are unchanged in Debug state. Any T32 instruction that uses the PC or APSR.{N, Z, C, V} as the source or destination register is not included in the list. Moreover, the list includes only the 32-bit T32 encodings.

## Any instruction that is UNDEFINED in Non-debug state

The list of instructions:

- Excludes any instruction listed in T32 instructions that are changed in Debug state.
- Excludes any instruction listed in T32 instructions that are CONSTRAINED UNPREDICTABLE in Debug state that is UNDEFINED because an enable or disable bit is not RES0 or RES1.

## Instructions that move System or Special-purpose registers to or from a general-purpose register

## The list of instructions:

- Includes the instructions to transfer a general-purpose register to or from the DTR, which can be executed at any Exception level.
- Excludes APSR and CPSR access instructions.
- Excludes instructions for accessing banked registers for the current mode.

These instructions are:

- MRS &lt;banked\_reg&gt;, MSR &lt;banked\_reg&gt; .

Note

This does not apply to cases which are UNPREDICTABLE or CONSTRAINED UNPREDICTABLE in Non-debug state in the current mode.

- MRC, MCR .

Note

This includes all allocated System registers in the ( coproc == 0b111x ) encoding space other than an MRC move to APSR\_nzcv.

- MRS SPSR , MSR SPSR\_fsxc (register).

- VMRS &lt;vfp\_system\_reg&gt;, VMSR &lt;vfp\_system\_reg&gt; .

Note

This includes all allocated Advanced SIMD and floating-point System registers, other than an a VMRS move to APSR\_nzcv.

## Floating-point moves between a SIMD&amp;FP register and a general-purpose register

These instructions are:

- VMOV (between a general-purpose register and a single-precision register).
- VMOV (between a general-purpose register and a doubleword floating-point register).

## SIMD moves between a SIMD&amp;FP register and a general-purpose register

## These instructions are:

- VMOV (between a general-purpose register and a scalar).

## Barriers These instructions are:

- CSDB .
- DMB .
- DSB .
- ISB .
- PSSBB .
- SSBB .
- If FEAT\_RAS is implemented, then ESB .
- If FEAT\_SB is implemented, then SB .

## Memory access instructions at various access sizes

The following constraints apply:

- General purpose-registers only.
- One of the following addressing modes:
- -Immediate (8-bit or 12-bit) offset.
- -Immediate (8-bit) post-indexed.
- -Immediate (8-bit) pre-indexed.
- -Unprivileged (8-bit).
- Not literal.
- One of the following types:
- -(Single) register.
- -Dual.
- -Exclusive.
- -Exclusive doubleword.
- -Acquire/Release.
- -Acquire/Release Exclusive.
- -Acquire/Release Exclusive doubleword.

## These instructions are:

- LDR.W, LDRB.W, LDRH.W, LDRD, LDRSB.W, LDRSH.W (immediate, not literal).
- LDRT, LDRBT, LDRHT, LDRSBT, LDRSHT (immediate).
- LDREX, LDREXB, LDREXH, LDA, LDAB, LDAH, LDAEX, LDAEXB, LDAEXH .
- LDREXD, LDAEXD .
- STR.W, STRB.W, STRH.W, STRD (immediate).
- STRT, STRBT, STRHT ( immediate).
- STREX, STREXB, STREXH, STL, STLB, STLH, STLEX, STLEXB, STLEXH .
- STREXD, STLEXD .

## Move to general-purpose register

These instructions are:

- MOVW , MOVT (immediate).

## System instructions, Send Event, NOP , and Clear Exclusive

The System instructions are Cache maintenance instructions, TLB maintenance instructions, and Address translation instructions. These are encoded in the ( coproc == 0b1111 ) System register encoding space.

These instructions are:

- ICIALLU, ICIALLUIS, ICIMVAU.

- DCCIMVAC, DCCISW, DCCMVAC, DCCMVAU, DCCSW, DCIMVAC, DCISW.
- TLBIALL, TLBIALLH, TLBIALLHIS, TLBIALLIS, TLBIALLNSNH, TLBIALLNSNHIS, TLBIASID, TLBIASIDIS, TLBIIPAS2, TLBIIPAS2IS, TLBIIPAS2L, TLBIIPAS2LIS, TLBIMVA, TLBIMVAA, TLBIMVAAIS, TLBIMVAAL, TLBIMVAALIS, TLBIMVAH, TLBIMVAHIS, TLBIMVAIS, TLBIMVAL, TLBIMVALH, TLBIMVALHIS, TLBIMVALIS.
- ATS12NSOPR, ATS12NSOPW, ATS12NSOUR, ATS12NSOUW, ATS1CPR, ATS1CPW. ATS1CUR, ATS1CUW, ATS1HR, ATS1HW.
- BPIALL, BPIALLIS, BPIMVA.
- SEV.W , SEVL.W .
- NOP.W .
- CLREX .

## H2.4.2.2.3 T32 instructions that are CONSTRAINED UNPREDICTABLE in Debug state

This subsection describes all instruction not listed in either:

- T32 instructions that are changed in Debug state.
- T32 instructions that are unchanged in Debug state.

These instructions are CONSTRAINED UNPREDICTABLE in Debug state. In general, the permissible behaviors are:

- The instruction generates an Undefined Instruction exception.
- The instruction executes as a NOP .
- If the instruction reads the PC or PSTATE, it uses an UNKNOWN value.
- If the instruction modifies the PC or PSTATE, other than by advancing the PC to the sequentially next instruction, it sets DLR, DSPSR, and if FEAT\_Debugv8p9 is implemented, DSPSR2, to UNKNOWN values.
- If the instruction is similar to a Debug state instruction, it executes as that Debug state instruction.
- The instruction has the same behavior as in Non-debug state.

The following list shows the permissible behaviors for T32 instruction in Debug state. An instruction might appear multiple times in the list, in which case the choice of permissible behaviors is any of those listed.

## Exception-generating instructions

These instructions are:

- SVC .

- HVC .

- SMC .

- UDF .

- BKPT .

- HLT .

These instructions behave in one of the following ways:

- They are UNDEFINED.

- They execute as a NOP .

- SVC behaves as DCPS1 .

- HVC behaves as DCPS2 .

- SMC behaves as DCPS3 .

- They generate the exception the instruction would generate in Non-debug state. The exception is taken as described in Exceptions in Debug state.

- [ ] Note

SMC must not generate a Secure Monitor Call exception if EDSCR.SDD is 1.

## Instructions that explicitly write to the PC (branches)

These instructions are:

- B, B (conditional), CBZ, CBNZ BL .
- BX, BLX ( register or immediate).
- BXJ, TBB, TBH .
- MOV pc and related instructions.
- LDR pc, LDM (with a register list includes the PC), POP (with a register list that includes the PC).

These instructions behave in one of the following ways:

- They are UNDEFINED.
- They execute as a NOP .
- They execute as in Non-debug state without branching and set DLR, DSPSR, and if FEAT\_Debugv8p9 is implemented, DSPSR2, to UNKNOWN values.

## Exception return and related instructions, other than ERET

These instructions are:

- SRS, RFE, SUBS pc, 1r , and related instructions.

These instructions behave in one of the following ways:

- They are UNDEFINED.
- They execute as a NOP .
- They execute as in Non-debug state without branching, setting DLR, DSPSR, and if FEAT\_Debugv8p9 is implemented, DSPSR2, to UNKNOWN values, and either:
- -Execute the DRPS operation instead of performing an exception return, using UNKNOWN SPSR values.
- -Not changing Exception level or PE mode.

## Instructions that request entry to a low-power state

These instructions are:

- WFE , WFI , WFET , WFIT

These instructions behave in one of the following ways:

- They are UNDEFINED.
- They execute as a NOP .
- They generate a synchronous exception if the corresponding instruction would be trapped in Non-debug state. See Configurable instruction controls.
- A WFE instruction is permitted to clear the Event register if it is set.

Note

This means that these instructions must not suspend execution.

## Instructions that read the PC

These instructions are:

- LDR (literal), LDRB (literal), LDRH (literal), LDRSB (literal), LDRSH (literal).
- ADR , ADRL, ADRH .
- PLD (literal), PLI (literal).

These instructions behave in one of the following ways:

- They are UNDEFINED.
- They execute as a NOP .
- They execute as in Non-debug state using an UNKNOWN value for the PC operand.

Instructions that explicitly modify PSTATE, other than DCPS and ERET

These instructions are:

- CMP, TST, TEQ, CMN .
- &lt;opc&gt;S .
- MRC p14,0,APSR\_nzcv,c0,c1,0 (accessing DBGDSCRint).
- CPS, SETEND, IT .
- MSR CPSR (immediate), MSR CPSR (register), MSR APSR (immediate), MSR APSR (register).
- VMRS APSR\_nzcv,FPSCR .
- QADD, QDADD, QSUB, QDSUB .
- SMLABB , SMLABT , SMLATB , SMLATT , SMLAD , SMLAWB , SMLAWT , SMLSD , SMUAD .
- SSAT, SSAT16, USAT, USAT16 .
- SADD , SADD8 , SADD16 , SASX , SSAX , SSUB , SSUB8 , SSUB16 .
- UADD , UADD8 , UADD16 , UASX , USAX , USAUB , USUN8 , USUB16 .
- If FEAT\_PAN is implemented, then SETPAN .

These instructions behave in one of the following ways:

- They are UNDEFINED.
- They execute as a NOP .
- They execute as in Non-debug state, setting DLR, DSPSR, and if FEAT\_Debugv8p9 is implemented, DSPSR2, and any PSTATE field written by the instruction to UNKNOWN values.

## Instructions that read PSTATE.{N, Z, C, V} or other PSTATE fields

These instructions are:

- SEL , VSEL .
- ADC , SBC , all instructions with an RRX shift.
- MRS CPSR '.

These instructions behave in one of the following ways:

- They are UNDEFINED.
- They execute as a NOP .
- They execute as in Non-debug state:
- -For the conditional operations and those using the PSTATE.C flag as an input, these instructions use an UNKNOWN value for the Condition flag.
- -For the MRS instruction, they return an UNKNOWN value.

## All other instructions

These instructions behave in one of the following ways:

- They are UNDEFINED.
- They execute as a NOP .
- They have the same behavior as in Non-debug state.

## H2.4.3 Decode tables

Note

This includes instructions defined as UNPREDICTABLE or CONSTRAINED UNPREDICTABLE in Non-debug state. These instructions are CONSTRAINED UNPREDICTABLE in Debug state. This includes some T32 instructions that specify R15 as a destination or source register.

Architectural Constraints on UNPREDICTABLE Behaviors describes the CONSTRAINED UNPREDICTABLE behavior for these instructions. In Debug state these CONSTRAINED UNPREDICTABLE choices are further restricted:

- Instructions that specify R15 as a destination register:

- Are not permitted to branch, because the architecture does not define a branch operation in Debug state.

- Might set DLR, DSPSR, and if FEAT\_Debugv8p9 is implemented, DSPSR2, to UNKNOWN values.

- Might have any of the other permitted behaviors.

- Instructions that specify R15 as a source operand:

- Cannot use PC + offset, because there is no architecturally-defined PC in Debug state.

- Might have any of the other permitted behaviors, including using an UNKNOWN value.

The syntax in the decode tables is defined as follows:

- 1 The bit has a fixed value of 1.

- 0 The bit has a fixed value of 0.

- != The field has any value other than the value or values specified. The field might be an encoding field in the instruction whose value is supplied by the debugger.

Note

The instruction encodings in A64 Base Instruction Descriptions and T32 and A32 Base Instruction Set Instruction Descriptions might show these bits as (0) or (1). A debugger must set these bits to 0 or 1, as appropriate.

Any other value indicates an encoding field in the instruction whose value is supplied by the debugger. Some values might be reserved or UNDEFINED, in which case the instruction is UNDEFINED or CONSTRAINED UNPREDICTABLE in Debug state, as it is in Non-debug state.

For more information about the instruction encodings, see:

- A64 Base Instruction Descriptions.

- T32 and A32 Base Instruction Set Instruction Descriptions.

For information about the syntax used in Figure H2-1, Figure H2-2, Figure H2-3, and Figure H2-4, see:

- Common syntax terms.

- Assembler symbols.

## H2.4.3.1 A64 instructions that are modified in Debug state

Figure H2-1 shows the A64 instructions that are modified in Debug state. For information of how these are packed in the EDITR, see the register description.

Figure H2-1 Modified A64 instructions in Debug state

<!-- image -->

|    |    | 31302928   |     |       | 27262524   |    |       |            |            | 232221201918171615141312   |            |           |           | 111098    |           | 7 6 5     | 4         | 3    |     |                                  |                                  | 210Description                   |
|----|----|------------|-----|-------|------------|----|-------|------------|------------|----------------------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|------|-----|----------------------------------|----------------------------------|----------------------------------|
|  1 |  1 | 0          | 1   | 0 1   | 0          |  0 | 1 0   | 1 imm16 0  | 1 imm16 0  | 1 imm16 0                  | 1 imm16 0  | 1 imm16 0 | 1 imm16 0 | 1 imm16 0 | 1 imm16 0 | 1 imm16 0 | 1 imm16 0 | 0    | 0   | 1 imm16 0                        | !=00 pCPS<opt>                   | !=00 pCPS<opt>                   |
|  1 |  1 | 0          | 1   | 0 1   | 0          |  1 | 0 0   | L          | 1          | 1 0 1                      | 1 0        | 1 0       | 0         | 0 1       | 01        | 0 0       | 0 Rt      | 0 Rt |     | MRS&#124;MSR accessing DSPSR_ELO | MRS&#124;MSR accessing DSPSR_ELO | MRS&#124;MSR accessing DSPSR_ELO |
|  1 |  1 | 0          | 1   | 0 1   | 0          |  1 | 0 0   | L          | 1          | 1 0                        | 1 0        | 1 0       | 0         | 0 1       | 0 1       | 0 0       | 1         | Rt   | Rt  |                                  | MRSIMSR accessing DLR_ELO        | MRSIMSR accessing DLR_ELO        |
|  1 |  1 | 0          | 1   | 0 1   | 1          |  0 | 1 0   | 1          | 1          | 1 1 1                      | 1 0        | 0 0       | 0         | 0 0       | 1 1       | 1 1 1     | 0         | 0 0  | 0 0 |                                  | DRPS                             | DRPS                             |
|  0 |  0 | 1          | 0   | 0 1   | 0          |  1 | size  | 0 imm5 1 0 | 0 imm5 1 0 | 0 imm5 1 0                 | 0 imm5 1 0 | 0         | Pg        |           | Zn 1      | Zn 1      | Zn 1      | Zn 1 | Pd  | Pd                               | CMPNE (immediate)                | CMPNE (immediate)                |
|  1 |  1 | 0          | 0   | 0 0   | 0          |  0 | 0 1   | 0          | 0          | 1 1 1                      | 0 0        | off3      | 0 0       | 1         | 1         | 1 1 1     | Rt        | Rt   | Rt  | MOVT (scalar to table)           | MOVT (scalar to table)           | MOVT (scalar to table)           |
|  1 |  1 |            | 0 0 | 0 0 0 |            |  0 | 0 1 0 |            | 0          | 1 1 0                      | 0 0        | off3      | 0         | 0 1       | 1         | 1 1 1     |           | Rt   | Rt  | scalar)                          | MOVT (table to                   | MOVT (table to                   |

## H2.4.3.2 T32 instructions that are modified in Debug state

Figure H2-2 shows the T32 instructions that are modified in Debug state, with the first halfword on the left side and the second halfword on the right side. For information of how these are packed in the EDITR, see the register description.

Figure H2-2 Modified T32 instructions in Debug state

<!-- image -->

|    |    |     |    |        |        |        |        | 15141312111098765432101514131211109876543210Description   |         |      |     |      |    |          |                             |
|----|----|-----|----|--------|--------|--------|--------|-----------------------------------------------------------|---------|------|-----|------|----|----------|-----------------------------|
| 1  |  1 | 1 0 |  1 | 1 10   | 0 11 L | 0 100  |        | !=1111                                                    | 1 1     |      | (0  | 0 0  | 1  | 0        | 1O1MRCIMCR accessing  DSPSR |
| 一  |  1 | 1   |  0 | 1 1 10 | 0 11   | L 0    | 100    | !=1111                                                    | 1       | 11 1 | 0   | 011  | 0  | 101      | MRC IMCR accessing DLR.     |
| 1  |  1 | 1   |  1 | 0 0 11 | 1 .101 |        | 1110 1 | 0 0                                                       | 0 1     | 111  | 0   | 0 00 |    | 0OOOERET |                             |
| 1  |  1 | 1   |  0 | 111    | 1 1000 | 1 1111 | 1 1 0  | 0                                                         | 0 0 0 0 |      | 0 0 | 00   |    | 00       | !=0ODCPS<opt>               |

## H2.4.3.3 A64 instructions that are unchanged in Debug state

This section shows the A64 instructions that are unchanged in Debug state, other than some unallocated and UNDEFINED instructions.

<!-- image -->

Figure H2-3

<!-- image -->

| 0             |     | 0     | 1 0   | 1   | 0   | 0 1   | 0       | 0 1         | 1 11 1 0   | 0         | 313029282726252423222120191817161514131211109876543210Description   | 111011       | Rt                                                     | GCSSS2                                                                                                    | GCSSS2                                                                                                    | GCSSS2                                                                                                    | GCSSS2                                                                                                    | GCSSS2                                                                                                    | GCSSS2                                                                                                    | GCSSS2                                                                                                    |
|---------------|-----|-------|-------|-----|-----|-------|---------|-------------|------------|-----------|---------------------------------------------------------------------|--------------|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1 1 0         | 1   | 0     | 1 0   | 1   | 0   | 0 L   | 1 0     | op1         |            | CRn       | CRm                                                                 | op2          | Rt                                                     | MRSIMSR accessingSystem register                                                                          | MRSIMSR accessingSystem register                                                                          | MRSIMSR accessingSystem register                                                                          | MRSIMSR accessingSystem register                                                                          | MRSIMSR accessingSystem register                                                                          | MRSIMSR accessingSystem register                                                                          | MRSIMSR accessingSystem register                                                                          |
| 1 0           | 1 0 | 1     | 0     | 1   | 0   |       | L 1 1   | [do         |            | !=0100    | CRm                                                                 | op2          | Rt                                                     | MRS&#124;MSR accessing System register                                                                    | MRS&#124;MSR accessing System register                                                                    | MRS&#124;MSR accessing System register                                                                    | MRS&#124;MSR accessing System register                                                                    | MRS&#124;MSR accessing System register                                                                    | MRS&#124;MSR accessing System register                                                                    | MRS&#124;MSR accessing System register                                                                    |
| 1 1 0         | 1   | 0 1   | 0     | 1   | 0   | 0     | 0       | 0 0         | 1          | 0 １0      | 0                                                                   | 01x000       |                                                        | 11111MSR PM,#<imm>                                                                                        | 11111MSR PM,#<imm>                                                                                        | 11111MSR PM,#<imm>                                                                                        | 11111MSR PM,#<imm>                                                                                        | 11111MSR PM,#<imm>                                                                                        | 11111MSR PM,#<imm>                                                                                        | 11111MSR PM,#<imm>                                                                                        |
| 1 0           | 1   | 0     | 1 0   | 1   | 0   | 0     | 0 1 00  |             | op1        | CRn       | CRm                                                                 | op2          | Rt                                                     | MRSIMSR accessing PM                                                                                      | MRSIMSR accessing PM                                                                                      | MRSIMSR accessing PM                                                                                      | MRSIMSR accessing PM                                                                                      | MRSIMSR accessing PM                                                                                      | MRSIMSR accessing PM                                                                                      | MRSIMSR accessing PM                                                                                      |
| 1 1 0         | 1   | 0     | 1 0   | 1   | 0   | 0     | L 1 1   | 0 1         | 1 0        | 0 1       | 0                                                                   | 0010010      | Rt                                                     | MRSIMSR accessing SVCR                                                                                    | MRSIMSR accessing SVCR                                                                                    | MRSIMSR accessing SVCR                                                                                    | MRSIMSR accessing SVCR                                                                                    | MRSIMSR accessing SVCR                                                                                    | MRSIMSR accessing SVCR                                                                                    | MRSIMSR accessing SVCR                                                                                    |
| 1 1           | 0   | 0     | 1 0   | 1   |     | 0     | L 1 1   | op1         | 0          | 0         | 0 !=0010                                                            | op2          | Rt                                                     | MRSIMSR accessing Special-purpose register                                                                | MRSIMSR accessing Special-purpose register                                                                | MRSIMSR accessing Special-purpose register                                                                | MRSIMSR accessing Special-purpose register                                                                | MRSIMSR accessing Special-purpose register                                                                | MRSIMSR accessing Special-purpose register                                                                | MRSIMSR accessing Special-purpose register                                                                |
| 1 1 0         | 1   | 0     | 1 0   | 1   | 0   |       | L 1 0   | [do         |            | CRn       | CRm                                                                 | op2          |                                                        | MRRSIMSRR                                                                                                 | MRRSIMSRR                                                                                                 | MRRSIMSRR                                                                                                 | MRRSIMSRR                                                                                                 | MRRSIMSRR                                                                                                 | MRRSIMSRR                                                                                                 | MRRSIMSRR                                                                                                 |
| 1 1 1 1 0     | 0   | 0 0   | 1 1 1 | 0 0 | 0   | 1 0   | 0 1 0   | 1 1 1 1 1 1 | 1 0 0 0    | 0 0 1 0 0 | 0 1 1 M1111                                                         | M1111 1 1    |                                                        | 11111RETAA, RETAB                                                                                         | 11111RETAA, RETAB                                                                                         | 11111ERETAA, ERETAB                                                                                       | 11111RETAA, RETAB                                                                                         | 11111RETAA, RETAB                                                                                         | 11111RETAA, RETAB                                                                                         | 11111RETAA, RETAB                                                                                         |
| 1 1 0         |     | 0     | 1 1   | 1   | 0   | 0     | 0       | 1 1         | 1 1 0 0    | 1 0       | 0 1 M                                                               | Rn           | Rm                                                     | BRAA，BRAB                                                                                                 | BRAA，BRAB                                                                                                 | BRAA，BRAB                                                                                                 | BRAA，BRAB                                                                                                 | BRAA，BRAB                                                                                                 | BRAA，BRAB                                                                                                 | BRAA，BRAB                                                                                                 |
| 1 1 0         |     | 0     | 1     | Z   | 0   | 0     | 1       | 1           | 1          | 0 0 0     | 0 1 M                                                               | Rn           | Rm                                                     | BLRAA，BLRAB，BLRAAZ，BLRABZ                                                                                 | BLRAA，BLRAB，BLRAAZ，BLRABZ                                                                                 | BLRAA，BLRAB，BLRAAZ，BLRABZ                                                                                 | BLRAA，BLRAB，BLRAAZ，BLRABZ                                                                                 | BLRAA，BLRAB，BLRAAZ，BLRABZ                                                                                 | BLRAA，BLRAB，BLRAAZ，BLRABZ                                                                                 | BLRAA，BLRAB，BLRAAZ，BLRABZ                                                                                 |
| 0             |     | 1     | 0     | 0   |     |       | 0 0     | 0 0         | 0 1 0      | 0 0       | opc                                                                 | Rn           | Rd                                                     | PAC(IA&#124;IB&#124;DA&#124;DB),                                                                          | PAC(IA&#124;IB&#124;DA&#124;DB),                                                                          | PAC(IA&#124;IB&#124;DA&#124;DB),                                                                          | PAC(IA&#124;IB&#124;DA&#124;DB),                                                                          | PAC(IA&#124;IB&#124;DA&#124;DB),                                                                          | PAC(IA&#124;IB&#124;DA&#124;DB),                                                                          | PAC(IA&#124;IB&#124;DA&#124;DB),                                                                          |
| 0             | 1   |       | 0     | 0   |     |       |         |             | 1 1        | 0         | opc                                                                 |              |                                                        | AUT(IA&#124;IB&#124;DA&#124;DB)                                                                           | AUT(IA&#124;IB&#124;DA&#124;DB)                                                                           | AUT(IA&#124;IB&#124;DA&#124;DB)                                                                           | AUT(IA&#124;IB&#124;DA&#124;DB)                                                                           | AUT(IA&#124;IB&#124;DA&#124;DB)                                                                           | AUT(IA&#124;IB&#124;DA&#124;DB)                                                                           | AUT(IA&#124;IB&#124;DA&#124;DB)                                                                           |
| 1 0           |     |       | 1     |     |     | 1 1   | 0       | 00（         | 00         | 0         |                                                                     | 1111 1       | Rd                                                     | PAC(IZA&#124;IZB&#124;DZA&#124;DZB), AUT(IZA&#124;IZB &#124;DZA&#124;DZB)                                 | PAC(IZA&#124;IZB&#124;DZA&#124;DZB), AUT(IZA&#124;IZB &#124;DZA&#124;DZB)                                 | PAC(IZA&#124;IZB&#124;DZA&#124;DZB), AUT(IZA&#124;IZB &#124;DZA&#124;DZB)                                 | PAC(IZA&#124;IZB&#124;DZA&#124;DZB), AUT(IZA&#124;IZB &#124;DZA&#124;DZB)                                 | PAC(IZA&#124;IZB&#124;DZA&#124;DZB), AUT(IZA&#124;IZB &#124;DZA&#124;DZB)                                 | PAC(IZA&#124;IZB&#124;DZA&#124;DZB), AUT(IZA&#124;IZB &#124;DZA&#124;DZB)                                 | PAC(IZA&#124;IZB&#124;DZA&#124;DZB), AUT(IZA&#124;IZB &#124;DZA&#124;DZB)                                 |
| 1 一 1 0       | 1 1 | 1 0 1 | 1 0 1 | 0 0 |     | 1     | 0 0 0 0 | 0 0 0 0 0   | 1 0 1 1    | 1 0 0     | 0 0 0 op                                                            | op1111 1 1   | Rd                                                     | XPAC(IID) Rd PACI(A&#124;B)171615                                                                         | XPAC(IID) Rd PACI(A&#124;B)171615                                                                         | XPAC(IID) Rd PACI(A&#124;B)171615                                                                         | XPAC(IID) Rd PACI(A&#124;B)171615                                                                         | XPAC(IID) Rd PACI(A&#124;B)171615                                                                         | XPAC(IID) Rd PACI(A&#124;B)171615                                                                         | XPAC(IID) Rd PACI(A&#124;B)171615                                                                         |
| 1 1 0         | 1   | 1     | 0 1   | 0   |     |       | 0 0     | 0 0         | 0 1 1 1    | 0 1 0     | 1 op                                                                | 1111 01111 1 | Rd                                                     | AUTI(A&#124;B)171615                                                                                      | AUTI(A&#124;B)171615                                                                                      | AUTI(A&#124;B)171615                                                                                      | AUTI(A&#124;B)171615                                                                                      | AUTI(A&#124;B)171615                                                                                      | AUTI(A&#124;B)171615                                                                                      | AUTI(A&#124;B)171615                                                                                      |
| size 0        | 0   | 1     | 0 0   | 0   | 02  | L     | 0       | Rs          |            | o0        | Rt2                                                                 | Rn           | Rt                                                     | LD(A&#124;LA&#124;X&#124;AX)R{B &#124;H}, ST(LILLIX&#124;LX)R{B&#124;H}, CAS{A&#124;L&#124;AL}H{B&#124;H} | LD(A&#124;LA&#124;X&#124;AX)R{B &#124;H}, ST(LILLIX&#124;LX)R{B&#124;H}, CAS{A&#124;L&#124;AL}H{B&#124;H} | LD(A&#124;LA&#124;X&#124;AX)R{B &#124;H}, ST(LILLIX&#124;LX)R{B&#124;H}, CAS{A&#124;L&#124;AL}H{B&#124;H} | LD(A&#124;LA&#124;X&#124;AX)R{B &#124;H}, ST(LILLIX&#124;LX)R{B&#124;H}, CAS{A&#124;L&#124;AL}H{B&#124;H} | LD(A&#124;LA&#124;X&#124;AX)R{B &#124;H}, ST(LILLIX&#124;LX)R{B&#124;H}, CAS{A&#124;L&#124;AL}H{B&#124;H} | LD(A&#124;LA&#124;X&#124;AX)R{B &#124;H}, ST(LILLIX&#124;LX)R{B&#124;H}, CAS{A&#124;L&#124;AL}H{B&#124;H} | LD(A&#124;LA&#124;X&#124;AX)R{B &#124;H}, ST(LILLIX&#124;LX)R{B&#124;H}, CAS{A&#124;L&#124;AL}H{B&#124;H} |
| size          |     | [ol   | 0     | 0   |     | 02 L  | 1       | Rs          |            | 0         | Rt2                                                                 | Rn           |                                                        | LD{A}XP, ST{L}XP, CASP[A&#124;L[AL}                                                                       | LD{A}XP, ST{L}XP, CASP[A&#124;L[AL}                                                                       | LD{A}XP, ST{L}XP, CASP[A&#124;L[AL}                                                                       | LD{A}XP, ST{L}XP, CASP[A&#124;L[AL}                                                                       | LD{A}XP, ST{L}XP, CASP[A&#124;L[AL}                                                                       | LD{A}XP, ST{L}XP, CASP[A&#124;L[AL}                                                                       | LD{A}XP, ST{L}XP, CASP[A&#124;L[AL}                                                                       |
| X 0           | 1   | 1     | 0     |     |     | opc   | 0       |             | imm9       |           | 0 0                                                                 | Rn           | Rt                                                     | LDAPUR(BIHISB&#124;SH), STLUR(B&#124;H)                                                                   | LDAPUR(BIHISB&#124;SH), STLUR(B&#124;H)                                                                   | LDAPUR(BIHISB&#124;SH), STLUR(B&#124;H)                                                                   | LDAPUR(BIHISB&#124;SH), STLUR(B&#124;H)                                                                   | LDAPUR(BIHISB&#124;SH), STLUR(B&#124;H)                                                                   | LDAPUR(BIHISB&#124;SH), STLUR(B&#124;H)                                                                   | LDAPUR(BIHISB&#124;SH), STLUR(B&#124;H)                                                                   |
| 0 1 0 0       | 1   | 1 o   | 0     | 1   |     | !=11  | 0       |             | imm9       |           | 0 0                                                                 | Rn           |                                                        | LDAPUR{SW}, STLUR                                                                                         | LDAPUR{SW}, STLUR                                                                                         | LDAPUR{SW}, STLUR                                                                                         | LDAPUR{SW}, STLUR                                                                                         | LDAPUR{SW}, STLUR                                                                                         | LDAPUR{SW}, STLUR                                                                                         | LDAPUR{SW}, STLUR                                                                                         |
| 1 1           | 0 1 | 1     | 0 0   |     | 1   | !=1x  | 0       |             | imm9       |           | 0 0                                                                 | Rn           | Rt                                                     | LDAPUR, STLUR                                                                                             | LDAPUR, STLUR                                                                                             | LDAPUR, STLUR                                                                                             | LDAPUR, STLUR                                                                                             | LDAPUR, STLUR                                                                                             | LDAPUR, STLUR                                                                                             | LDAPUR, STLUR                                                                                             |
| 0 X           | 1   |       | 0 0   | 0   |     | opc   | 0       |             | imm9       |           | 0 0                                                                 | Rn           |                                                        | LDUR(B&#124;H&#124;SB &#124;SH) , STUR(B&#124;H)                                                          | LDUR(B&#124;H&#124;SB &#124;SH) , STUR(B&#124;H)                                                          | LDUR(B&#124;H&#124;SB &#124;SH) , STUR(B&#124;H)                                                          | LDUR(B&#124;H&#124;SB &#124;SH) , STUR(B&#124;H)                                                          | LDUR(B&#124;H&#124;SB &#124;SH) , STUR(B&#124;H)                                                          | LDUR(B&#124;H&#124;SB &#124;SH) , STUR(B&#124;H)                                                          | LDUR(B&#124;H&#124;SB &#124;SH) , STUR(B&#124;H)                                                          |
| 1 1 0         | 1 1 | 1     | o 0   | 0   |     | !=11  | 0       |             | imm9       |           | 0 0                                                                 | Rn           |                                                        | LDUR{SW},STUR                                                                                             | LDUR{SW},STUR                                                                                             | LDUR{SW},STUR                                                                                             | LDUR{SW},STUR                                                                                             | LDUR{SW},STUR                                                                                             | LDUR{SW},STUR                                                                                             | LDUR{SW},STUR                                                                                             |
| 1 1           | 1 1 |       | [ol 0 | 0   |     | !=lx  | 0       |             | imm9       |           | 0                                                                   | Rn           | Rn                                                     | Rt                                                                                                        | LDUR, STUR                                                                                                | LDUR, STUR                                                                                                | LDUR, STUR                                                                                                | LDUR, STUR                                                                                                | LDUR, STUR                                                                                                | LDUR, STUR                                                                                                |
| 1 size 1      | 1 1 |       | 0 0   | 0   |     | opc   | 0       |             | imm9       |           | 1 0                                                                 | Rt           | LDTR{B&#124;H&#124;SB&#124;SH&#124;SW}, STTR{B&#124;H} | LDTR{B&#124;H&#124;SB&#124;SH&#124;SW}, STTR{B&#124;H}                                                    | LDTR{B&#124;H&#124;SB&#124;SH&#124;SW}, STTR{B&#124;H}                                                    | LDTR{B&#124;H&#124;SB&#124;SH&#124;SW}, STTR{B&#124;H}                                                    | LDTR{B&#124;H&#124;SB&#124;SH&#124;SW}, STTR{B&#124;H}                                                    | LDTR{B&#124;H&#124;SB&#124;SH&#124;SW}, STTR{B&#124;H}                                                    | LDTR{B&#124;H&#124;SB&#124;SH&#124;SW}, STTR{B&#124;H}                                                    | LDTR{B&#124;H&#124;SB&#124;SH&#124;SW}, STTR{B&#124;H}                                                    |
| size 1        |     | 1     | 0 0   | 0   |     | opc   | 0       |             | imm9       |           | P                                                                   | Rn           | Rt                                                     | LDR{B&#124;H&#124;SB&#124;SH&#124;SW}, STR{B&#124;H}                                                      | LDR{B&#124;H&#124;SB&#124;SH&#124;SW}, STR{B&#124;H}                                                      | LDR{B&#124;H&#124;SB&#124;SH&#124;SW}, STR{B&#124;H}                                                      | LDR{B&#124;H&#124;SB&#124;SH&#124;SW}, STR{B&#124;H}                                                      | LDR{B&#124;H&#124;SB&#124;SH&#124;SW}, STR{B&#124;H}                                                      | LDR{B&#124;H&#124;SB&#124;SH&#124;SW}, STR{B&#124;H}                                                      | LDR{B&#124;H&#124;SB&#124;SH&#124;SW}, STR{B&#124;H}                                                      |
| 1             | 1   | 1 0   | 0     | 0   | A   | R     | 1       | Rs          | opc        | 0         | 0                                                                   | Rn           |                                                        | LD<op>{A&#124;L&#124;AL}HB[H},                                                                            | LD<op>{A&#124;L&#124;AL}HB[H},                                                                            | LD<op>{A&#124;L&#124;AL}HB[H},                                                                            | LD<op>{A&#124;L&#124;AL}HB[H},                                                                            | LD<op>{A&#124;L&#124;AL}HB[H},                                                                            | LD<op>{A&#124;L&#124;AL}HB[H},                                                                            | LD<op>{A&#124;L&#124;AL}HB[H},                                                                            |
| size          |     | 1     |       |     |     |       | 1       | Rs          | 0          | 1 0       | 0 0 0                                                               | Rn           | Rt                                                     | ST<op>{A&#124;L&#124;AL}{B[H} SWP[A&#124;L&#124;AL}{B[H}                                                  | ST<op>{A&#124;L&#124;AL}{B[H} SWP[A&#124;L&#124;AL}{B[H}                                                  | ST<op>{A&#124;L&#124;AL}{B[H} SWP[A&#124;L&#124;AL}{B[H}                                                  | ST<op>{A&#124;L&#124;AL}{B[H} SWP[A&#124;L&#124;AL}{B[H}                                                  | ST<op>{A&#124;L&#124;AL}{B[H} SWP[A&#124;L&#124;AL}{B[H}                                                  | ST<op>{A&#124;L&#124;AL}{B[H} SWP[A&#124;L&#124;AL}{B[H}                                                  | ST<op>{A&#124;L&#124;AL}{B[H} SWP[A&#124;L&#124;AL}{B[H}                                                  |
| size 1 size 1 | 1 1 | 1 ol  | 0     | 0 0 | A 1 | R 0   | 1       | Rs          | 0          | 1 1       | 0 0 0                                                               | Rn           | Rt                                                     | LDAPR[B&#124;H}                                                                                           | LDAPR[B&#124;H}                                                                                           | LDAPR[B&#124;H}                                                                                           | LDAPR[B&#124;H}                                                                                           | LDAPR[B&#124;H}                                                                                           | LDAPR[B&#124;H}                                                                                           | LDAPR[B&#124;H}                                                                                           |
| 0             | 0 0 | 1 1   | 1     | 0   |     | 0     | 0       | imm5        | 0          | 0 0       | 1 1 1                                                               | Rn           | Rd                                                     | <u><y>'[<xapuL>]<s1>'<pA>SN1                                                                              | <u><y>'[<xapuL>]<s1>'<pA>SN1                                                                              | <u><y>'[<xapuL>]<s1>'<pA>SN1                                                                              | <u><y>'[<xapuL>]<s1>'<pA>SN1                                                                              | <u><y>'[<xapuL>]<s1>'<pA>SN1                                                                              | <u><y>'[<xapuL>]<s1>'<pA>SN1                                                                              | <u><y>'[<xapuL>]<s1>'<pA>SN1                                                                              |
| 0 Q 0 0       | 0 0 | 1 1   | 1     | 0   | 0   | 0     | 0       | imm5        | 1          | 0 0       | 1 1 1                                                               | Rn           | Rd                                                     | [<xapu>]<s1>'<u>'<p><y> Aown                                                                              | [<xapu>]<s1>'<u>'<p><y> Aown                                                                              | [<xapu>]<s1>'<u>'<p><y> Aown                                                                              | [<xapu>]<s1>'<u>'<p><y> Aown                                                                              | [<xapu>]<s1>'<u>'<p><y> Aown                                                                              | [<xapu>]<s1>'<u>'<p><y> Aown                                                                              | [<xapu>]<s1>'<u>'<p><y> Aown                                                                              |
| 0             |     |       | 1     | 0   | 0   | 0     | 1 0     | 0 1 1       | op 0       | 0 0       | 0 0 0                                                               | Rn           | Rd                                                     | ‘<uM>'<pS> NOWH <US>'<PM> NOWH                                                                            | ‘<uM>'<pS> NOWH <US>'<PM> NOWH                                                                            | ‘<uM>'<pS> NOWH <US>'<PM> NOWH                                                                            | ‘<uM>'<pS> NOWH <US>'<PM> NOWH                                                                            | ‘<uM>'<pS> NOWH <US>'<PM> NOWH                                                                            | ‘<uM>'<pS> NOWH <US>'<PM> NOWH                                                                            | ‘<uM>'<pS> NOWH <US>'<PM> NOWH                                                                            |
| 0             |     |       |       | 0   |     |       | 0       |             |            | 0         | 0                                                                   |              |                                                        | FMOV <Hd>, <Wn>,                                                                                          | FMOV <Hd>, <Wn>,                                                                                          | FMOV <Hd>, <Wn>,                                                                                          | FMOV <Hd>, <Wn>,                                                                                          | FMOV <Hd>, <Wn>,                                                                                          | FMOV <Hd>, <Wn>,                                                                                          | FMOV <Hd>, <Wn>,                                                                                          |
|               |     |       |       |     |     |       |         | op          |            |           | 0                                                                   | Rn           | Rd                                                     |                                                                                                           |                                                                                                           |                                                                                                           |                                                                                                           |                                                                                                           |                                                                                                           |                                                                                                           |
|               | 0   |       |       |     |     |       |         |             |            |           |                                                                     |              |                                                        |                                                                                                           |                                                                                                           |                                                                                                           |                                                                                                           |                                                                                                           |                                                                                                           |                                                                                                           |
| 0             |     |       |       |     |     |       | 0       |             |            |           |                                                                     |              | <UH>‘<PM> AOWH                                         | <UH>‘<PM> AOWH                                                                                            | <UH>‘<PM> AOWH                                                                                            | <UH>‘<PM> AOWH                                                                                            | <UH>‘<PM> AOWH                                                                                            | <UH>‘<PM> AOWH                                                                                            | <UH>‘<PM> AOWH                                                                                            | <UH>‘<PM> AOWH                                                                                            |

<!-- image -->

|     |     |       |     |       |     |       |     |     |           |      |        |     |      |       |       |    |       |           | 313029282726252423222120191817161514131211109876543210Description   | 313029282726252423222120191817161514131211109876543210Description   |
|-----|-----|-------|-----|-------|-----|-------|-----|-----|-----------|------|--------|-----|------|-------|-------|----|-------|-----------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| 0   | S 0 | 1     | 1   | 0 0   | 1   | A R   | 1   |     | Rs        | 0    | 0      | 0   | 0    | 1     | X     | Rn |       | Rt        | RCW{S}CAS{PH{AILIAL}                                                | RCW{S}CAS{PH{AILIAL}                                                |
| 0   | S   | 0 1   | 1   | 0 0   | 1   | A R   | 1   |     | Rt2       |      | 1 0    | 1   | 0    | 0     |       | 0  | Rn    | Rt        | RCW{S}SWPP[AILIAL}                                                  | RCW{S}SWPP[AILIAL}                                                  |
| 0   | S   | 0     | 1 1 | 0 0   | 1   | A R   | 1   |     | Rt2       |      | 1      | 0   | X    | 1     | 0 0   |    | Rn    | Rt        | RCW{S}(CLRPISETP) {A[L[AL}                                          | RCW{S}(CLRPISETP) {A[L[AL}                                          |
| 0   | X   | 1     | 1 1 | 0 0   | 0   | A R   | 1   |     | Rs        |      | 1      | 0 1 | 0    | 0     | 0     |    | Rn    | Rt        | RCW{S}SWP{AIL[AL}                                                   | RCW{S}SWP{AIL[AL}                                                   |
| 0   | X   | 1 1   | 1   | 0 0   | 0   | A R   | 1   |     | Rs        |      | 1      | 0   | X    | 1 0   | 0     |    | Rn    | Rt        | RCW{S}(CLR&#124;SET) {A[L[AL}                                       | RCW{S}(CLR&#124;SET) {A[L[AL}                                       |
| 1   | 0   | 0     | 1   | 1 1   | 0   | 1 1   | 1   | 0   | 0 1       | 1    | op 0   | 0   | 0    | 0     | 0     | 0  | Rn    | Rd        | FMOV <Dd&#124;Hd>,<Xn>, FMOV <Xd>,<Dn&#124;Hn>                      | FMOV <Dd&#124;Hd>,<Xn>, FMOV <Xd>,<Dn&#124;Hn>                      |
| 1   | 0   | 0     | 1   |       | 0   | 0     | 1   | 0   | 1         | 1    | op     | 0   | 0 00 | 0     | 0     |    | Rn    | Rd        | FMOV <Vd>.D[1],<Xn> FMOV <Xd>,<Vn>.D[1]                             | FMOV <Vd>.D[1],<Xn> FMOV <Xd>,<Vn>.D[1]                             |
| 1   | 0   | 0 1   | 0   | 0 0   | 1   | 1     | 0   |     | uimm6     |      | (0)(0) |     |      | uimm4 |       |    | UX    | PX        | ADDG                                                                | ADDG                                                                |
| 1   | 1   | 0 0   | 0   | 0 0   | 0   | 0     | 0 0 | 0   | 0 0       | 0    | Q V    |     | Rs   |       | Pg    |    | Zn    | 0         | MovA (vector to tile, single)                                       | MovA (vector to tile, single)                                       |
| 1   | 1   | 0 0   | 0   | 0 0   | 0   | 0     | 0 0 | 0   | 0 0       | 1    | Q      | V   | Rs   | Pg    |       |    | #0    | Zd        | MoVA (tile to vector, single)                                       | MoVA (tile to vector, single)                                       |
|     |     | 0     |     | 0 0   |     | 0 0   | 1   |     |           |      | imm9   |     |      | 1     | 0     |    | UX    | PX        | STG - Signed offset                                                 | STG - Signed offset                                                 |
|     | 1   | 0 1   | 1   | 0 0   | 1   | 1     | 0 1 | 0   | 0 0       | 0    | 0 0    | 0 0 | 0    | 0     | 0     |    | Xn    | PX        | STGM                                                                | STGM                                                                |
|     | 1   | 0 1   | 1   | 0 0   | 1   | 1 0   | 1   |     |           |      | imm9   |     |      | 1     | 0     |    | Xn    | PX        | ST2G - Signed offset                                                | ST2G - Signed offset                                                |
| 1   | 1   | 0 1   | 1   | 0 0   | 1   | 0     | 1 1 |     |           | imm9 |        |     |      | 1     | 0     |    | UX    | PX        | STZG - Signed offset                                                | STZG - Signed offset                                                |
| 1   | 1   | 0 1   | 1   | 0 0   | 1   | 1     | 1   | 1   |           | imm9 |        |     |      | 1     | 0     |    | Xn    | PX        | STZ2G - Signed offset                                               | STZ2G - Signed offset                                               |
| 1   | 1   | 0     | 1   | 0 0   | 1   | 0     | 0 1 | 0   | 0 0 simm7 | 0 0  | 0      | 0   | Xt2  | 0     | 0     | 0  | UX    | PX        | STZGM                                                               | STZGM                                                               |
| 0   | 1   | 1 0   | 1   | 0 0   | 1   | 0 0   | 0   |     | uimm6     |      |        |     |      |       |       |    | Xn    | X         | STGP - Signed offset                                                | STGP - Signed offset                                                |
| 1   | 1   | 0 1   | 0   | 0 0   | 1   | 1     |     |     |           | imm9 |        | op3 |      |       |       |    | Xn    | PX        | SUBG                                                                | SUBG                                                                |
| 1   | 1   | 0 1   | 1   | 0 0   | 1   | 0 1 1 | 1 1 | 1 0 | 0 0       |      | 0      | 0   | 0 0  | 0     | 0 0 0 |    | Xn    | PX        | LDG                                                                 | LDG                                                                 |
| 1   | 1   | 0 1 1 | 1 1 | 0 0 0 | 1   |       | 0 1 |     | 1 1       | 0    |        | 0 1 | 0 0  | 1     | 0 0   |    | Xn Rn | PX        | LDGM                                                                | LDGM                                                                |
| 1 1 | 1 1 | 1 1 1 | 1   | 0 0 0 | 0 0 | 0 0   | 0 1 | 1   | Rs        | 1 1  |        | 0 1 | 1    | 0 0   | 0     |    | Rn    | Rt        | ST64B Rt                                                            | ST64B Rt                                                            |
| 1   | 1   | 1     | 1 1 | 0 0   | 0   | 0 0   | 1   | 1   | Rs        |      |        | 1   | 0    | 1 1   | 0     | 0  | Rn    | Rt ST64BV | ST64BV0                                                             | ST64BV0                                                             |
|     |     |       |     | 0     |     |       | 0   |     | 1         | 1    | 1      | 1   |      | 0     | 0     | 0  | Rn    |           |                                                                     |                                                                     |
| 1   | 1   | 1     |     | 0     | 0   | 0     |     | 1   |           |      |        |     |      | 1     |       |    |       | Rt        |                                                                     | LD64B                                                               |

## H2.4.3.4 T32 instructions that are unchanged in Debug state

Figure H2-4 shows the T32 instructions that are unchanged in Debug state, other than some unallocated and UNDEFINED instructions. It shows the T32 instructions with the first halfword on the left side and the second halfword on the right side.

Figure H2-4 T32 instructions that are unchanged in Debug state

<!-- image -->

|    |    |     | 15141312111098   |    |     | 7   |               | 6543210   | 0             | 15141312      |               |    |           |            |                           | 11109876543210Description VMOV <Dm>,<Rt>,<Rt2>       |
|----|----|-----|------------------|----|-----|-----|---------------|-----------|---------------|---------------|---------------|----|-----------|------------|---------------------------|------------------------------------------------------|
| 1  |  1 | 1 0 | 1                |  1 | 00  | 0   | 1 0 op        | !=1111    |               | !=1111        | 1             |    | 01100M1   | Vm         |                           | VMOV <Rt>,<Rt2>,<Dm>                                 |
|    |  1 | 1 0 | 1                |  1 | 10  | 0   | 0 0 op        |           | Vn            | !=1111        | 1             |    |           |            |                           | 0 1 0 No 0 10 0 00VMoV <Sn>,<Rt>, VMOV <Rt>,<Sn>     |
| 1  |  1 | 1 0 | 1                |  1 | 1   | 0 0 | opc           | 0         | Vd            | !=1111        | 1             | 0  | 1         | Dopc2 1    |                           | 0 0 00VMoV.<size> <Dd>[<x>],<Rt>                     |
| 1  |  1 | 1 0 | 1                |  1 | 1   | 0 n | opc           | 1         | Vn            | !=1111        | 1             | 0  | 11 D opc2 |            |                           | 0 0 00VMoV.<dt> <Rt>,<Dd>[<x>]                       |
| 1  |  1 | 1 0 | 1                |  1 | 1   | 0 1 | 1 1           | OP        | reg           | !=1111        | 1             | 0  | 1 0       | 000 1      |                           | 0 000VMRS, VMSR                                      |
| 1  |  1 | 1 0 | 1                |  1 | 0   | 0 0 | 1 0           | p         | !=1111        | !=1111        | 1             | 1  | 1 CP      | opc1       | CRm                       | MCRR&#124;MRRC accessing System registers            |
| 1  |  1 | 1 0 | 1                |  1 | √   | 0   | opc1          |           | CRn           | !=1111        | 1             | 1  | 1 cp      | opc2 1     | CRm                       | MCRIMRC accessing System registers                   |
| 1  |  1 | 1 0 | 1                |  0 | 0   | 0 0 | 1 0           | L         | !=1111        | !=1111        |               |    | Rd        | imm8       |                           | LDREX, STREX                                         |
| 1  |  1 | 1 0 | 1                |  0 | 0   | 0 1 | 1 0           | L         | !=1111        | !=1111        |               |    | Rt2       | 01!=10Rd   |                           | LDREX(B&#124;H&#124;D), STREX(B&#124;H&#124;D)       |
| 1  |  1 | 1 0 | 1                |  0 |     | 00  | 11 0          | L         | !=1111        |               | !=1111        |    | Rt2       | 1 op3      | Rd                        | LDA{EX}H{B&#124;H&#124;D}, STL{EX}H{B&#124;H&#124;D} |
| 1  |  1 | 1   | 0 1              |  0 | 0   |     | !=0x10 !=xx0x | L         | !=1111        |               | !=1111        |    | !=1111    |            | imm8                      | LDRD, STRD                                           |
| 1  |  1 | 1 1 | 0                |  1 | 1   | 0 T | 1 0           | 0         | imm4          |               | imm3          |    | !=1111    | imm8       |                           | MOVw, MOVT                                           |
| 1  |  1 | 1   | 1 0              |  0 | 1   | 1 1 | 0 0           | R         | !=1111        | 1 0           | 0             | 0  | M1        | 00         |                           | M0 0 00MSR <spec_reg><mode>,<Rn>                     |
| 1  |  1 | 1   | 1 0              |  0 | 1   | 1 < | 0 0           | 1         | !=1111        | 1 0           | 0 0           |    | 1 1 1 1   |            | 000O00OOMSRSPSR，<Rn>      |                                                      |
| 1  |  1 | 1   | 1 0              |  0 | 1   | 1 1 | 0 1           | 0         | 1 1 1         | 1 1           | 0 0           | 0  | 0 0       | 0          | 0000O0OONOP.W             |                                                      |
| 1  |  1 | 1 1 | 0                |  0 | 1   | 1 1 | 0 1           | 0 1       | 1 1           | 1 1 0         | 0             | 0  | 0 0 0 0   |            | 0000 01 0LSEV.W,SEVL.W    |                                                      |
| 1  |  1 | 1 1 | 0                |  0 | 1   | 1 1 | 0 1           | 0 1       | √ 1           | 1 1 0         | 0 0           | 0  | 0         |            | 0 00 010op00ESB, CSDB     |                                                      |
| 1  |  1 | 1 1 | 0                |  0 | 1   | 1 1 | 0 1           | 1 1       | 1 1           | 1 1 0         | 0 0           | 1  | 1 1 1     | 0          | 00 11 11CLREX             |                                                      |
| 1  |  1 | 1 1 | 0                |  0 | 1   | 1 1 | 0 1           | 1 1       | 1             | 1 1 1         | 0 0           | 0  | 1 1       | [o 1 op    |                           | Option DSB, DMB, ISB, SSBB, PSSBB, SB                |
| 1  |  1 | 1   | 0                |  0 | 1   | 1 1 | 1 1           | R         | M1            | 1 0           | 0             | 0  | !=1111    | 00         |                           | MO 0 00MRS <Rd>,<spec_reg><mode>                     |
| 1  |  1 | 1   | 1 0              |  0 | 1   | 1 1 | 1 1           | 1 1       | 1             | 1 1 1         | 0 0           |    | !=1111    |            | 0 0 0 00 0 0OMRS<Rd>,SPSR |                                                      |
| 1  |  1 | 1   | 1                |  0 | 0   | 0 1 | !=11          | 0         | !=1111        |               | 0             |    |           | imm12      |                           | STR{B&#124;H} .W (12-bit immediate)                  |
| 1  |  1 | 1   | 1 1              |  0 | 0   | 0 0 | !=11          | 0         | !=1111        |               | !=1111 !=1111 |    |           | imm8       |                           | STR{B&#124;H&#124;HT} (8-bit immediate)              |
| 1  |  1 | 1   | 1 1              |  0 |     | S 1 | !=11          | 1         |               |               |               | 1  | !=000     |            |                           | LDR{SB&#124;SH&#124;B&#124;H}.W (12-bit immediate)   |
| 1  |  1 | 1   | 1 1              |  0 | 0 0 | S 0 | !=11          | 1         | !=1111 !=1111 | !=1111 !=1111 |               | 1  | !=000     | imm12 imm8 |                           | LDR{SB&#124;SH&#124;B&#124;H}{T} (8-bit immediate)   |

## H2.4.4 Security in Debug state

If EL3 is implemented or the implemented Security state is Secure state, security in Debug state is governed by EDSCR.SDD.

## Onentry to Debug state

If FEAT\_RME is implemented, EDSCR.SDD is the EL3 debug disabled flag. If entering Debug state from EL3, EDSCR.SDD is set to 0. Otherwise:

- If ExternalRootInvasiveDebugEnabled() == TRUE, EDSCR.SDD is set to 0.
- If ExternalRootInvasiveDebugEnabled() == FALSE, EDSCR.SDD is set to 1.

If FEAT\_RME is not implemented, EDSCR.SDD is the Secure debug disabled flag. If entering Debug state from Secure state, EDSCR.SDD is set to 0. Otherwise:

- If ExternalSecureInvasiveDebugEnabled() == TRUE, EDSCR.SDD is set to 0.
- If ExternalSecureInvasiveDebugEnabled() == FALSE, EDSCR.SDD is set to 1.

Note

If halting is prohibited in a Security state, it is not possible to enter Debug state from that Security state. However, because changes to the authentication signals require a Context Synchronization event to guarantee their effect, there is a period during which the PE might halt even though the authentication signals prohibit halting.

The value of EDSCR.SDD does not change, even if ExternalRootInvasiveDebugEnabled() or ExternalSecureInvasiveDebugEnabled() changes.

Note

- DBGAUTHSTATUS\_EL1 is not frozen in Debug state. However, a Context Synchronization event is required to guarantee that changes are visible in DBGAUTHSTATUS\_EL1.
- If EDSCR.SDD is 1 in Debug state, there is no means to enter a Security state where halting was prohibited on entry to Debug state. This means that it is not possible for the PE to be in such a Security state when EDSCR.SDD is 1. This is a general principle of behavior in Debug state.

## In Non-debug state

If FEAT\_RME is implemented, then EDSCR.SDD returns the inverse of ExternalRootInvasiveDebugEnabled() .

If FEAT\_RME is not implemented, then EDSCR.SDD returns the inverse of

ExternalSecureInvasiveDebugEnabled() . If the authentication signals that control ExternalRootInvasiveDebugEnabled() or ExternalSecureInvasiveDebugEnabled() change, a Context Synchronization event is required to guarantee their effect.

## Note

- In Non-debug state, EDSCR.SDD is unaffected by the Security state of the PE.
- AContext Synchronization event is also required to guarantee that changes in the authentication signals are visible in DBGAUTHSTATUS\_EL1.

If EL3 is not implemented and the implemented Security state is Non-Secure state, EDSCR.SDD is RES1.

## In Debug state

## H2.4.5 Privilege in Debug state

The only additional privileges offered to Debug state are:

- The privilege to execute Debug state operations, DCPS, DRPS, MRS, MSR.
- The privilege to execute DTR access instructions regardless of the Exception level and traps.

The DTR access instructions can be executed at any Exception level, including EL0, regardless of any control register settings that might force these instructions to be UNDEFINED or trapped in Non-debug state. These instruction are:

- The MRS and MSR instructions that access DBGDTR\_EL0, DBGDTRTX\_EL0, and DBGDTRRX\_EL0 in AArch64 state.
- The MRC and MCR instructions that access DBGDTRTXint and DBGDTRRXint in AArch32 state.

All other instructions operate with the privilege determined by the current Exception level and Security state. This applies to all Special-purpose and System registers accesses, memory accesses, and UNDEFINED instructions, and includes generating exceptions when the System registers trap or disable an instruction.

## H2.4.6 Debug state operations, DCPS, DRPS, MRS, MSR

The architecture defines operations to change between Exception levels in Debug state. These operations can also change the mode at the current Exception level.

## H2.4.6.1 DCPS&lt;n&gt;

Executing a DCPS &lt;n&gt; instruction in Debug state moves the PE to a higher Exception level or to a specific mode at the current Exception level.

If the DCPS&lt;n&gt; instruction is executed in AArch32 state and the target Exception level is using AArch64:

- The current instruction set switches from T32 to A64.
- The effect on registers that are not visible or only partially visible in AArch32 state is the same as for system calls in Non-debug state. See Execution state.

Otherwise, the instruction set state does not change.

If the target Exception level is the same as the current Exception level, then the PE does not change Exception level. However, the PE might change mode.

The effect on endianness is the same as for exceptions and exception returns in Non-debug state:

- In AArch64 state the current endianness is determined by the value of SCTLR\_ELx.EE for the target Exception level.
- In AArch32 state the current endianness is determined by the value of SCTLR.EE or HSCTLR.EE for the target Exception level.

The DCPS&lt;n&gt; instructions are:

## In AArch64 state

- DCPS1
- DCPS2
- •

DCPS3

## In AArch32 state, in the T32 instruction set only

- •

DCPS1

- DCPS2
- •

DCPS3

The DCPS instructions are UNDEFINED in Non-debug state.

Table H2-2 shows the target of the instruction. In Table H2-2, the entries have the following meaning:

## EL1h/Svc

This means that the target is:

- EL1h if EL1 is using AArch64.

- EL1 and Supervisor mode if EL1 is using AArch32.

EL2h/Hyp

## This means that the target is:

- EL2h if EL2 is using AArch64.

- EL2 and Hyp mode if EL2 is using AArch32.

## EL3h/Monitor This means that the target is:

- EL3h if EL3 is using AArch64.

- EL3 and Monitor mode if EL3 is using AArch32.

Svc

Secure Supervisor mode, in EL3 using AArch32.

Monitor

Secure Monitor mode, in EL3 using AArch32.

## Table H2-2 Target for DCPS instructions in Debug state

| Instruction   | Target when DCPS instruction executed at stated Exception level:   | Target when DCPS instruction executed at stated Exception level:   | Target when DCPS instruction executed at stated Exception level:   | Target when DCPS instruction executed at stated Exception level:   | Target when DCPS instruction executed at stated Exception level:   |
|---------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
|               | EL0                                                                | EL1                                                                | EL2                                                                | EL3 (AArch64)                                                      | EL3 (AArch32)                                                      |
| DCPS1         | EL1h/Svc                                                           | EL1h/Svc                                                           | EL2h/Hyp                                                           | EL3h                                                               | Svc, clears SCR.NS to 0                                            |
| DCPS2         | EL2h/Hyp                                                           | EL2h/Hyp                                                           | EL2h/Hyp                                                           | EL3h                                                               | UNDEFINED                                                          |
| DCPS3         | EL3h/Monitor                                                       | EL3h/Monitor                                                       | EL3h/Monitor                                                       | EL3h                                                               | Monitor, clears SCR.NS to 0                                        |

In AArch32 Monitor mode, DCPS1 and DCPS3 clear SCR.NS to 0.

Note

In AArch64 state, at EL3, DCPS&lt;n&gt; does not change SCR\_EL3.NS.

## However:

- DCPS1 is UNDEFINED at EL0 if either:
- -EL2 is implemented and enabled in the current Security state, and is using AArch64 and HCR\_EL2.TGE == 1.
- -In Non-secure state, EL2 is implemented and using AArch32 and HCR.TGE == 1.
- DCPS2 is UNDEFINED at all Exception levels if EL2 is not implemented.
- DCPS2 is UNDEFINED at the following Exception levels if EL2 is implemented:
- -At EL0 and EL1 in Secure state if EL2 is disabled in the current Security state.
- -At EL3 if EL3 is using AArch32.
- DCPS3 is UNDEFINED at all Exception levels if either:
- -EDSCR.SDD == 1.
- -EL3 is not implemented.

Note

The references to DCPS1 , DCPS2 , and DCPS3 in this section link to the descriptions of the instructions in the A64 instruction set.

The DCPS&lt;n&gt; instructions are also defined in the T32 instruction set, see DCPS1 , DCPS2 , DCPS3 . These instructions are not defined in the A32 instruction set, because A32 instructions cannot be executed in Debug state.

On executing a DCPS instruction:

- If the target Exception level is using AArch64:
- -ELR\_ELx of the target Exception level becomes UNKNOWN.
- -SPSR\_ELx of the target Exception level becomes UNKNOWN.
- -ESR\_ELx of the target Exception level becomes UNKNOWN.
- -DLR\_EL0 and DSPSR\_EL0 become UNKNOWN.
- If the target Exception level is using AArch32, DLR, DSPSR, and if FEAT\_Debugv8p9 is implemented, DSPSR2, become UNKNOWN and:
- -If the target Exception level is EL1 or EL3, the LR and SPSR of the target mode become UNKNOWN.
- -If the target Exception level is EL2, then ELR\_hyp, SPSR\_hyp, and HSR become UNKNOWN.

If the target Exception level is using AArch32, and the target Exception level is EL1 or EL3, the LR and SPSR of the target mode become UNKNOWN.

The DCPSInstruction() function is described in A-profile Architecture Pseudocode.

## H2.4.6.2 DRPS

Executing the DRPS operation in Debug state moves the PE to a lower Exception level, or the current Exception level, by copying the current SPSR to PSTATE.

If DRPS is executed in AArch64 state and the target Exception level is using AArch32:

- The current instruction set switches from A64 to T32.
- The effect on registers that are not visible or only partially visible in AArch32 state is the same as for exception returns in Non-debug state. See Execution state.

Otherwise, the instruction set state does not change.

If the target Exception level is the current Exception level, then the PE does not change Exception level. However, the PE might change mode.

The effect on endianness is the same as for exceptions and exception returns in Non-debug state:

- If targeting an Exception level using AArch64, current endianness is set according to SCTLR\_ELx.EE, or SCTLR\_EL1.E0E for the target Exception level.
- If targeting an Exception level using AArch32, current endianness is set by SPSR.E as appropriate.

The DRPS instructions are:

In AArch64 state

•

DRPS

In AArch32 state, in the T32 instruction set only

•

ERET

If the SPSR specifies an illegal exception return, then PSTATE.{M, nRW, EL, SP} are unchanged, PSTATE.UINJ is set to 0, and PSTATE.IL is set to 1. For further information on illegal exception returns, see Illegal exception returns from AArch64 state.

Some PSTATE fields are ignored in Debug state. The effect of the DRPS operation on them is to set them to an UNKNOWN value that might be the value from the SPSR. For more information, see PSTATE in Debug state.

All other PSTATE fields are copied from SPSR.

DRPS is UNDEFINED at EL0 and in Non-debug state.

Note

Unlike an exception return, the DRPS operation has no architecturally-defined effect on the Event Register and Exclusives monitors. DRPS might set the Event Register or clear the Exclusives monitors, or both, but this is not a requirement and debuggers must not rely on any IMPLEMENTATION SPECIFIC behavior.

On executing a DRPS instruction:

- If the target Exception level is using AArch64, then DLR\_EL0 and DSPSR\_EL0 become UNKNOWN.
- If the target Exception level is using AArch32, then DLR, DSPSR, and if FEAT\_Debugv8p9 is implemented, DSPSR2, become UNKNOWN.
- If FEAT\_PAuth\_LR is implemented, then:
- -For a trivial implementation of PSTATE.PACM, PSTATE.PACM is set to 0.
- -If the effects of PACM instructions are disabled at the target Exception level indicated in SPSR\_ELx, PSTATE.PACM is set to 0.
- -Otherwise, PSTATE.PACM is copied from SPSR\_ELx.PACM.

The DRPSInstruction() function is described in A-profile Architecture Pseudocode.

## H2.4.6.3 MRS and MSR

The other Debug state instructions are used to read or write DLR\_EL0 and DSPSR\_EL0.

These instructions are:

## In AArch64 state

- MRS
- MSR (register)

| MRS <Xt>, DLR_EL0   | ; Copy DLR_EL0 to <Xt>   |
|---------------------|--------------------------|
| MRS <Xt>, DSPSR_EL0 | ; Copy DSPSR_EL0 to <Xt> |
| MSR DLR_EL0, <Xt>   | ; Copy <Xt> to DLR_EL0   |
| MSR DSPSR_EL0, <Xt> | ; Copy <Xt> to DSPSR_EL0 |

## In AArch32 state

- MRC
- MCR

| MRC <Rn>, DLR   | ; Copy DLR to <Rn>   |
|-----------------|----------------------|
| MRC <Rn>, DSPSR | ; Copy DSPSR to <Rn> |
| MCR DLR, <Rn>   | ; Copy <Rn> to DLR   |
| MCR DSPSR, <Rn> | ; Copy <Rn> to DSPSR |

## If FEAT\_Debugv8p9 is implemented:

| MRC <Rn>, DSPSR2   | ; Copy DSPSR2 to <Rn>   |
|--------------------|-------------------------|
| MCR DSPSR2, <Rn>   | ; Copy <Rn> to DSPSR2   |

These instructions can be executed at any Exception level when in Debug state, including EL0. They are UNDEFINED in Non-debug state.

## H2.4.7 Exceptions in Debug state

The following sections describe how exceptions are handled in Debug state:

- Generating exceptions when in Debug state.
- Taking exceptions when in Debug state.
- Reset in Debug state.

## H2.4.7.1 Generating exceptions when in Debug state

In Debug state:

- Instruction Abort exceptions cannot happen because instructions are not fetched from memory.
- Interrupts, including SError and virtual interrupts are ignored and remain pending:
- -The pending interrupt remains visible in ISR.
- Debug exceptions and debug events are ignored.
- SCR.EA is treated as 0, regardless of its actual state, other than for the purpose of a direct read.
- Any attempt to execute an instruction bit pattern that is an allocated instruction at the current Exception level, but is listed in Executing instructions in Debug state as UNDEFINED in Debug state, generates an exception.

Note

If the exception is taken to an Exception level that is using AArch32 then it is taken as an Undefined Instruction exception.

The priority and syndrome for these exceptions is the same as for executing an encoding that does not have an allocated instruction.

- Instructions executed at EL2, EL1 and EL0 that are configured by EL3 control registers to trap to EL3:
- -When the value of EDSCR.SDD is 0, generate the appropriate trap exception that is taken to EL3.
- -When the value of EDSCR.SDD is 1, are treated as UNDEFINED and generate an exception. If the exception is taken to an Exception level using AArch64 or to AArch32 Hyp mode, then it is reported with an EC syndrome value of 0x00 .
- If FEAT\_RME is implemented and EDSCR.SDD is 1, SCR\_EL3.GPF is treated as 0, regardless of its actual state, other than for the purpose of a direct read.

Otherwise, synchronous exceptions are generated as they would be in Non-debug state and taken to the appropriate Exception level in Debug state.

Note

If FEAT\_RME is implemented and EDSCR.SDD == 1, then exceptions from Non-secure, Secure, and Realm state are never taken to Root state. If FEAT\_RME is not implemented and EDSCR.SDD == 1, then an exception from Non-secure state is never taken to Secure state. See Security in Debug state.

## H2.4.7.2 Taking exceptions when in Debug state

When the PE is in Debug state, all exceptions are synchronous. When an exception is generated, it is taken to Debug state. This means that:

- The target Exception level is as defined for the exception in Non-debug state.
- If the target Exception level is using AArch32 then the target PE mode is as defined for the exception in Non-debug state.
- The exception syndrome is reported as defined for the exception in Non-debug state, except for the case described in Data Aborts in Memory access mode for which the reporting requirements are relaxed. The exception syndrome is reported using the syndrome register or registers for the target Exception level. In AArch64 state, these are ESR\_ELx, and FAR\_ELx, and if FEAT\_RME is implemented, MFAR\_EL3. In AArch32 state, these are DFSR, DFAR, HSR, HDFAR, and HPFAR. For example:
- -If a Data Abort exception is taken to Abort mode at EL1 or EL3 and the exception is taken from AArch32 state and using the Short-descriptor translation table format, the DFSR reports the exception using the Short-descriptor format fault encoding. For exceptions other than Data Abort exceptions taken to Abort mode, DFSR is not updated.

- -If an instruction is trapped to an Exception level using AArch64 due to a configurable trap, disable, or enable, the exception code reported is the same as it would be in Non-debug state.

The effect on auxiliary syndrome registers, such as AFSR, is IMPLEMENTATION DEFINED.

Note

Generally, the AArch32 Fault Address Registers (FARs) and Fault Status Registers (FSRs) are not described as syndrome registers , although the term is appropriate to their function.

- The PE remains in Debug state and changes to the target mode.
- If EL3 is using AArch32 and the exception is taken from Monitor mode, SCR.NS is cleared to 0.
- If the exception is taken to an Exception level using AArch32, the PE continues to execute T32 instructions, regardless of the TE bit in the System register for the target Exception level.
- The endianness switches to that indicated by the EE bit of the System register for the target Exception level.
- The SPSR for the target Exception level or mode is corrupted and becomes UNKNOWN.
- ELR\_ELx for the target Exception level becomes UNKNOWN.
- If the target Exception level is EL2 using AArch32, ELR\_hyp becomes UNKNOWN.
- If the target Exception level is EL1 or EL3 using AArch32, LR\_&lt;mode&gt; for the target mode becomes UNKNOWN.
- DLRand DSPSR become UNKNOWN.
- The cumulative error flag, EDSCR.ERR, is set to 1. See Cumulative error flag.
- PSTATE.IL is cleared to 0.
- If FEAT\_UINJ is implemented, PSTATE.UINJ is cleared to 0.
- PSTATE.{IT, T, SS, D, A, I, F, ALLINT} are set to UNKNOWN values, and PSTATE.{N, Z, C, V, Q, GE} are unchanged. However, these fields are ignored and are not observable in Debug state. For more information, see PSTATE in Debug state.

The debugger must save any state that can be corrupted by an exception before executing an instruction that might generate another exception.

## H2.4.7.3 Pseudocode description of taking exceptions in Debug state

AArch64.TakeException() shows the behavior when the PE takes an exception to an Exception level using AArch64 in Non-debug state. In Debug state, this redirects to AArch64.TakeExceptionInDebugState() .

AArch32.EnterMode() , AArch32.EnterHypMode() , and AArch32.EnterMonitorMode() show the behavior when the PE takes an exception to an Exception level using AArch32 in Non-debug state. In Debug state:

- AArch32.EnterMode() redirects to AArch32.EnterModeInDebugState() .
- AArch32.EnterHypMode() redirects to AArch32.EnterHypModeInDebugState() .
- AArch32.EnterMonitorMode() redirects to AArch32.EnterMonitorModeInDebugState() .

## H2.4.7.4 Reset in Debug state

If the PE is reset when in Debug state, it exits Debug state and enters Non-debug reset state. When the PE is in reset state, EDSCR.STATUS == 0b000010 and writes to EDITR are ignored.

Note

If EDECR.RCE == 1 or CTIDEVCTL.RCE ==1, meaning that a Reset Catch debug event is programmed, and if halting is allowed on exiting reset state, then on exiting reset state the PE halts and re-enters Debug state. See Reset Catch debug events. All PE registers have taken their reset values, which might be UNKNOWN.

## H2.4.8 Accessing registers in Debug state

Register accesses are unchanged in Debug state. The view of each register is determined by either the current Exception level or the mode, or both, and accesses might be disabled or trapped by controls at a higher Exception level.

## H2.4.8.1 General-purpose register access, other than AArch64 state SP access

Asingle general-purpose register can be read by issuing an MSR instruction through the ITR to write DBGDTR\_EL0 in AArch64 state, or an MCR instruction through the ITR to write DBGDTRTXint in AArch32 state. The debugger can then read the DTR register or registers through the external debug interface. The reverse sequence writes to a general-purpose register.

Figure H2-5 shows the reading and writing of general-purpose registers, other than SP, in Debug state in AArch64 state.

Figure H2-5 Reading and writing general-purpose registers, other than SP, in Debug state in AArch64 state

<!-- image -->

Figure H2-6 shows the reading and writing of general-purpose registers in Debug state in AArch32 state.

Figure H2-6 Reading and writing general-purpose registers in Debug state in AArch32 state

<!-- image -->

## H2.4.8.2 PC and PSTATE access

The debugger reads the Program Counter and PSTATE of the process being debugged through the DLR\_EL0 and DSPSR\_EL0 System registers. The actual values of PC and PSTATE cannot be directly observed in Debug state:

- Instructions that are used for direct reads and writes of PC and PSTATE in Non-debug state are CONSTRAINED UNPREDICTABLE in Debug state.
- On taking an exception, ELR\_ELx and SPSR\_ELx at the target Exception level are UNKNOWN. They do not record the PC and PSTATE.

PSTATE.{TCO, UAO, PAN, IL, E, M, nRW, EL, SP} are indirectly read by instructions executed in Debug state, but all other PSTATE fields are ignored and cannot be observed. See also:

- PSTATE in Debug state.
- Executing instructions in Debug state.
- Exceptions in Debug state.

## H2.4.8.3 Other register accesses

To access other registers, the debugger can use the operations described in General-purpose register access, other than AArch64 state SP access and the operations described below to build a sequence of operations to move the registers to or from a general-purpose register.

To access a SIMD&amp;FP, SP, or System register, the debugger can use an instruction from the following list to transfer the register to or from a general-purpose register:

- The UMOV instruction in AArch64 state or the VMOV instruction in AArch32 state for SIMD transfers from SIMD&amp;FP registers.
- The FMOV instruction in AArch64 state or the VMOV instruction in AArch32 state for floating-point transfers to or from SIMD&amp;FP registers.
- MOV (to/from SP) SP,Xs and MOV (to/from SP) Xd,SP instructions in AArch64 state for transfers to or from the SP register.
- MSR , MSRR , MRRS , and MRS instructions in AArch64 state or MCR , MCRR , MRRC , and MRC instructions in AArch32 state for transfers to or from System registers.

To access an SVE scalable vector register, the debugger can use the following instruction sequences to transfer the register to or from a general-purpose register, 64 bits at a time:

- To read, the following sequence to copy the 64-bit element 0 of Vs to general-purpose register Xd amd rotate Zs register right by 64 bits:
- To write, the INSR ZD.D,Xs instruction to shift vector register Zd left by one 64-bit element and copy general-purpose register Xs to the 64-bit element 0.

```
UMOV Xd, Vs.D[0] EXT Zs.B, Zs.B,
```

```
Zs.B, #8
```

To access an SVE predicate register, the debugger can use a sequence from the following list to transfer the register to or from an SVE scalable vector register:

- If FEAT\_SVE2p1 is implemented or FEAT\_SME2p1 is implemented, the PMOV Zd,Ps.B and PMOV Pd.B,Zs instructions.
- If FEAT\_SVE2p1 is not implemented and FEAT\_SME2p1 is not implemented:
- -To read, the CPY Zd.B,Ps/Z,#1 instruction to expand predicate elementes in PS into zero and one 8-bit element values in Zd .
- -To write, the following sequence to convert zero and non-zero 8-bit elements in Zs to a corresponding 1-bit predicate elemts in Pd :

```
PTRUE Pd.B CMPNE Pd.B, Pd/Z, Zs.B, #0
```

To access the SVE First Fault Register, FFR, the debugger can use the RDFFR and WRFFR instructions to transfer the register to or from an SVE predicate register.

To access the SME ZA storage, the debugger can use the MOVA (tile to vector, single) and MOVA (vector to tile, single) instructions to transfer to or from an SVE scalable vector register.

To access the SME ZT0 register, the debugger can use the MOVT (table to scalar) and MOVT (scalar to table) instructions to transfer to or from a general-purpose register, 64 bits at a time.

## H2.4.9 Accessing memory in Debug state

How the PE accesses memory is unchanged in Debug state. This includes:

- The operation of the MMU, including address translation, tagged address handling, access permissions, memory attribute determination, and the operation of any TLBs.
- The operation of any caches and coherency mechanisms.
- Alignment support.
- Endianness support.
- The Memory order model.
- The operation of the MPU, including accesse permissions and memory attribute determination.

## H2.4.9.1 Simple memory transfers

Simple memory accesses can be performed in Debug state by issuing memory access instructions through the ITR and passing data through the DTR registers. Executing instructions in Debug state lists the memory access instructions that are supported in Debug state.

## H2.4.9.2 Bulk memory transfers

Memory access mode can accelerate bulk memory transfers in Debug state. See DCC and ITR access modes.