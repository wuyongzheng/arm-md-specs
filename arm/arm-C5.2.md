## C5.2 Special-purpose registers

This section describes the following Special-purpose registers:

- ALLINT, that holds the PSTATE.ALLINT bit.
- CurrentEL, that holds PSTATE.EL, and that software can read to determine the current Exception level.
- DAIF, that holds the current PSTATE.{D, A, I, F} interrupt mask bits.
- DIT, that holds the PSTATE.DIT bit.
- ELR\_EL1, that holds the address to return to for an exception return from EL1.
- ELR\_EL2, that holds the address to return to for an exception return from EL2.
- ELR\_EL3, that holds the address to return to for an exception return from EL3.
- FPCR, that provides control of floating-point operation.
- FPMR, that controls behaviors of the FP8 instructions.
- FPSR, that provides floating-point status information.
- NZCV, that holds the PSTATE.{N, Z, C, V} condition flags.
- PAN, that holds the PSTATE.PAN state bit.
- PM, that provides access to the Profiling exception mask bit.
- SP\_EL0, that holds the stack pointer for EL0.
- SP\_EL1, that holds the stack pointer for EL1.
- SP\_EL2, that holds the stack pointer for EL2.
- SP\_EL3, that holds the stack pointer for EL3.
- SPSel, that holds PSTATE.SP, that at EL1 or higher selects the current SP.
- SPSR\_abt, that holds process state on taking an exception to AArch32 Abort mode.
- SPSR\_EL1, that holds process state on taking an exception to AArch64 EL1.
- SPSR\_EL2, that holds process state on taking an exception to AArch64 EL2.
- SPSR\_EL3, that holds process state on taking an exception to AArch64 EL3.
- SPSR\_fiq, that holds process state on taking an exception to AArch32 FIQ mode.
- SPSR\_irq, that holds process state on taking an exception to AArch32 IRQ mode.
- SPSR\_und, that holds process state on taking an exception to AArch32 Undefined mode.
- SSBS, that holds the PSTATE.SSBS bit.
- SVCR, controls Streaming SVE mode and SME behavior.
- TCO, that holds the PSTATE.TCO bit.
- UAO, that holds the PSTATE.UAO bit.

The following registers are also Special-purpose registers:

- DLR\_EL0, that holds the address to return to for a return from Debug state.
- DSPSR\_EL0, that holds process state on entry to Debug state.

## C5.2.1 ALLINT, All Interrupt Mask Bit

The ALLINT characteristics are:

## Purpose

Allows access to the all interrupt mask bit.

## Configuration

This register is present only when FEAT\_NMI is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to ALLINT are UNDEFINED.

## Attributes

ALLINT is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:14]

Reserved, RES0.

## ALLINT, bit [13]

All interrupt mask. An interrupt is controlled by PSTATE.ALLINT when all of the following apply:

- SCTLR\_ELx.NMI is 1.
- The interrupt is targeted at ELx.
- Execution is at ELx.

| ALLINT   | Meaning                                                                                                                                   |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | This control does not cause any interrupts to be masked.                                                                                  |
| 0b1      | If SCTLR_ELx.NMI is 1 and execution is at ELx, an IRQ or FIQ interrupt that is targeted to ELx, with or without Superpriority, is masked. |

The value of this bit is set to the inverse value in the SCTLR\_ELx.SPINTMASK field on taking an exception to ELx.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [12:0]

Reserved, RES0.

## Accessing ALLINT

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ALLINT

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0011 | 0b000 |

if !(IsFeatureImplemented(FEAT\_NMI) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then X[t, 64] = Zeros(50):PSTATE.ALLINT:Zeros(13); elsif PSTATE.EL == EL2 then X[t, 64] = Zeros(50):PSTATE.ALLINT:Zeros(13); elsif PSTATE.EL == EL3 then X[t, 64] = Zeros(50):PSTATE.ALLINT:Zeros(13);

MSR ALLINT, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0011 | 0b000 |

if !(IsFeatureImplemented(FEAT\_NMI) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then AArch64.SystemAccessTrap(EL2, 0x18); else PSTATE.ALLINT = X[t, 64]&lt;13&gt;; elsif PSTATE.EL == EL2 then PSTATE.ALLINT = X[t, 64]&lt;13&gt;; elsif PSTATE.EL == EL3 then PSTATE.ALLINT = X[t, 64]&lt;13&gt;;

if EL2Enabled() &amp;&amp; IsHCRXEL2Enabled() &amp;&amp; HCRX\_EL2.TALLINT == '1' then

MSR ALLINT, #&lt;imm&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b00  | 0b001 | 0b0100 | 0b000x | 0b000 |

## C5.2.2 CurrentEL, Current Exception Level

The CurrentEL characteristics are:

## Purpose

Holds the current Exception level.

## Configuration

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CurrentEL are UNDEFINED.

## Attributes

CurrentEL is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:4]

Reserved, RES0.

## EL, bits [3:2]

Current Exception level.

| EL   | Meaning   |
|------|-----------|
| 0b00 | EL0.      |
| 0b01 | EL1.      |
| 0b10 | EL2.      |
| 0b11 | EL3.      |

When the Effective value of HCR\_EL2.NV is 1, EL1 read accesses to the CurrentEL register return the value of 0b10 in this field.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '01' .
- When the highest implemented Exception level is EL2, this field resets to '10' .
- Otherwise, this field resets to '11' .

## Bits [1:0]

Reserved, RES0.

## Accessing CurrentEL

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CurrentEL

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0010 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then X[t, 64] = Zeros(60):'10':Zeros(2); else X[t, 64] = Zeros(60):PSTATE.EL:Zeros(2); elsif PSTATE.EL == EL2 then X[t, 64] = Zeros(60):PSTATE.EL:Zeros(2); elsif PSTATE.EL == EL3 then X[t, 64] = Zeros(60):PSTATE.EL:Zeros(2);
```

## C5.2.3 DAIF, Interrupt Mask Bits

The DAIF characteristics are:

## Purpose

Allows access to the interrupt mask bits.

## Configuration

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to DAIF are UNDEFINED.

## Attributes

DAIF is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:10]

Reserved, RES0.

## D, bit [9]

Process state D mask.

| D   | Meaning                                                                                                      |
|-----|--------------------------------------------------------------------------------------------------------------|
| 0b0 | Watchpoint, Breakpoint, and Software Step exceptions targeted at the current Exception level are not masked. |
| 0b1 | Watchpoint, Breakpoint, and Software Step exceptions targeted at the current Exception level are masked.     |

When the target Exception level of the debug exception is higher than the current Exception level, the exception is not masked by this bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to '1' .

## A, bit [8]

SError exception mask bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to '1' .

## I, bit [7]

IRQ mask bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to '1' .

## F, bit [6]

FIQ mask bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to '1' .

## Bits [5:0]

Reserved, RES0.

## Accessing DAIF

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, DAIF

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0010 | 0b001 |

| A   | Meaning               |
|-----|-----------------------|
| 0b0 | Exception not masked. |
| 0b1 | Exception masked.     |

| I   | Meaning               |
|-----|-----------------------|
| 0b0 | Exception not masked. |
| 0b1 | Exception masked.     |

| F   | Meaning               |
|-----|-----------------------|
| 0b0 | Exception not masked. |
| 0b1 | Exception masked.     |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if ELIsInHost(EL0) || SCTLR_EL1.UMA == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else X[t, 64] = Zeros(54):PSTATE.<D,A,I,F>:Zeros(6); elsif PSTATE.EL == EL1 then X[t, 64] = Zeros(54):PSTATE.<D,A,I,F>:Zeros(6); elsif PSTATE.EL == EL2 then X[t, 64] = Zeros(54):PSTATE.<D,A,I,F>:Zeros(6); elsif PSTATE.EL == EL3 then X[t, 64] = Zeros(54):PSTATE.<D,A,I,F>:Zeros(6);
```

MSR DAIF, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0010 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if ELIsInHost(EL0) || SCTLR_EL1.UMA == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else PSTATE.<D,A,I,F> = X[t, 64]<9:6>; elsif PSTATE.EL == EL1 then PSTATE.<D,A,I,F> = X[t, 64]<9:6>; elsif PSTATE.EL == EL2 then PSTATE.<D,A,I,F> = X[t, 64]<9:6>; elsif PSTATE.EL == EL3 then PSTATE.<D,A,I,F> = X[t, 64]<9:6>;
```

MSR DAIFSet, #&lt;imm&gt;

| op0   | op1   | CRn    | op2   |
|-------|-------|--------|-------|
| 0b00  | 0b011 | 0b0100 | 0b110 |

MSR DAIFClr, #&lt;imm&gt;

| op0   | op1   | CRn    | op2   |
|-------|-------|--------|-------|
| 0b00  | 0b011 | 0b0100 | 0b111 |

## C5.2.4 DIT, Data Independent Timing

The DIT characteristics are:

## Purpose

Allows access to the Data Independent Timing bit.

## Configuration

This register is present only when FEAT\_DIT is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to DIT are UNDEFINED.

## Attributes

DIT is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:25]

Reserved, RES0.

## DIT, bit [24]

Data Independent Timing.

| DIT   | Meaning                                                                                                                                                                                            |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The architecture makes no statement about the timing properties of any instructions.                                                                                                               |
| 0b1   | The architecture requires that the execution time of a data-independent-time sequence of code must be independent of all data-independent-time values. For more information, see About PSTATE.DIT. |

The list of data-independent-time instructions is:

- Flag Manipulation: CFINV .
- Data Processing - Immediate:
- Add/subtract (immediate): ADD , ADDS , SUB , and SUBS .
- Bitfield: BFM , SBFM , and UBFM .
- Extract: EXTR .
- Logical (immediate): AND , ANDS , EOR , and ORR .
- Min/max (immediate): SMAX , SMIN , UMAX , and UMIN .
- Data Processing - Register:
- Add/subtract (extended register): ADD , ADDS , SUB , and SUBS .
- Add/subtract (shifted register): ADD , ADDS , SUB , and SUBS .
- Add/subtract (with carry): ADC , ADCS , SBC , and SBCS .
- Conditional compare (immediate): CCMN , and CCMP .
- Conditional compare (register): CCMN , and CCMP .
- Conditional select: CSEL , CSINC , CSINV , and CSNEG .

- Data-processing (1 source): ABS , CLS , CLZ , CNT , CTZ , RBIT , REV16 , REV32 , and REV .
- Data-processing (2 source): ASRV , CRC32B , CRC32CB , CRC32CH , CRC32CW , CRC32CX , CRC32H , CRC32W , CRC32X , LSLV , LSRV , RORV , SMAX , SMIN , UMAX , and UMIN .
- Data-processing (3 source): MADD , MSUB , SMADDL , SMSUBL , SMULH , UMADDL , UMSUBL , and UMULH .
- Evaluate into flags: SETF16 , and SETF8 .
- Logical (shifted register): AND , ANDS , BIC , BICS , EON , EOR , ORN , and ORR .
- Rotate right into flags: RMIF .
- Data Processing - Scalar Floating-Point and Advanced SIMD:
- Advanced SIMD across lanes: ADDV , SADDLV , SMAXV , SMINV , UADDLV , UMAXV , and UMINV .
- Advanced SIMD copy: DUP , INS , SMOV , and UMOV .
- Advanced SIMD extract: EXT .
- Advanced SIMD modified immediate: BIC , and ORR .
- Advanced SIMD permute: TRN1 , TRN2 , UZP1 , UZP2 , ZIP1 , and ZIP2 .
- Advanced SIMD scalar copy: DUP .
- Advanced SIMD scalar pairwise: ADDP .
- Advanced SIMD scalar shift by immediate: Advanced SIMD scalar shift by immediate: SHL , SLI , SRSHR , SRI , SRSRA , SSHR , SSRA , URSHR , URSRA , USHR , and USRA .
- Advanced SIMD scalar three same: ADD , CMEQ , CMGE , CMGT , CMHI , CMHS , CMTST , SQDMULH , SQRDMULH , SSHL , SUB , and USHL .
- Advanced SIMD scalar three same extra: SQRDMLAH .
- Advanced SIMD scalar two-register miscellaneous: ABS , CMEQ , CMGE , CMGT , CMLE , CMLT , and NEG .
- Advanced SIMD scalar x indexed element: SQDMULH , SQRDMLAH , and SQRDMULH .
- Advanced SIMD shift by immediate: RSHRN2 , RSHRN , SHL , SHRN2 , SHRN , SLI , SRI , SSHLL2 , SSHLL , SSHR , SSRA , USHLL2 , USHLL , USHR , and USRA .
- Advanced SIMD table lookup: LUTI2 , LUTI4 , TBL , and TBX .
- Advanced SIMD three different: ADDHN2 , ADDHN , PMULL2 , PMULL , RADDHN2 , RADDHN , RSUBHN2 , RSUBHN , SABAL2 , SABAL , SABDL2 , SABDL , SADDL2 , SADDL , SADDW2 , SADDW , SMLAL2 , SMLAL , SMLSL2 , SMLSL , SMULL2 , SMULL , SSUBL2 , SSUBL , SSUBW2 , SSUBW , SUBHN2 , SUBHN , UABAL2 , UABAL , UABDL2 , UABDL , UADDL2 , UADDL , UADDW2 , UADDW , UMLAL2 , UMLAL , UMLSL2 , UMLSL , UMULL2 , UMULL , USUBL2 , USUBL , USUBW2 , and USUBW .
- Advanced SIMD three same: ADD , ADDP , AND , BIC , BIF , BIT , BSL , CMEQ , CMGE , CMGT , CMHI , CMHS , CMTST , EOR , MLA , MLS , MUL , ORN , ORR , PMUL , SABA , SABD , SHADD , SHSUB , SMAX , SMAXP , SMIN , SMINP , SQDMULH , SQRDMULH , SSHL , SUB , UABA , UABD , UHADD , UHSUB , UMAX , UMAXP , UMIN , UMINP , and USHL .
- Advanced SIMD three-register extension: SDOT , SMMLA , SQRDMLAH , UDOT , UMMLA , USDOT , and USMMLA .
- Advanced SIMD two-register miscellaneous: ABS , CLS , CLZ , CMEQ , CMGE , CMGT , CMLE , CMLT , CNT , NEG , NOT , RBIT , REV16 , REV32 , REV64 , SADALP , SADDLP , SHLL2 , SHLL , UADALP , UADDLP , XTN2 , and XTN .
- Advanced SIMD vector x indexed element: MLA , MLS , MUL , SDOT , SMLAL2 , SMLAL , SMLSL2 , SMLSL , SMULL2 , SMULL , SQDMULH , SQRDMLAH , SQRDMULH , SUDOT , UDOT , UMLAL2 , UMLAL , UMLSL2 , UMLSL , UMULL2 , UMULL , and USDOT .
- Cryptographic AES: AESD , AESE , AESIMC , and AESMC .
- Cryptographic four-register: BCAX , EOR3 , and SM3SS1 .
- Cryptographic three-register SHA: SHA1C , SHA1M , SHA1P , SHA1SU0 , SHA256H2 , SHA256H , and SHA256SU1 .
- Cryptographic three-register SHA 512: RAX1 , SHA512H2 , SHA512H , SHA512SU1 , SM3PARTW1 , SM3PARTW2 , and SM4EKEY .
- Cryptographic three-register, imm2: SM3TT1A , SM3TT1B , SM3TT2A , and SM3TT2B .
- Cryptographic three-register, imm6: XAR .
- Cryptographic two-register SHA: SHA1H , SHA1SU1 , and SHA256SU0 .
- Cryptographic two-register SHA 512: SHA512SU0 , and SM4E .
- Floating-point conditional select: FCSEL .
- Loads and Stores:
- 128-bit atomic memory operations: LDCLRP , LDCLRPA , LDCLRPAL , LDCLRPL , LDSETP , LDSETPA , LDSETPAL , LDSETPL , SWPP , SWPPA , SWPPAL , and SWPPL .
- Advanced SIMD load/store multiple structures: LD1 , LD2 , LD3 , LD4 , ST1 , ST2 , ST3 , and ST4 .
- Advanced SIMD load/store multiple structures (post-indexed): LD1 , LD2 , LD3 , LD4 , ST1 , ST2 , ST3 , and ST4 .
- Advanced SIMD load/store single structure: LD1 , LD1R , LD2 , LD2R , LD3 , LD3R , LD4 , LD4R , LDAP1 , ST1 , ST2 , ST3 , ST4 , and STL1 .
- Advanced SIMD load/store single structure (post-indexed): LD1 , LD1R , LD2 , LD2R , LD3 , LD3R , LD4 , LD4R , ST1 , ST2 , ST3 , and ST4 .
- Atomic memory operations: LDADD , LDADDA , LDADDAB , LDADDAH , LDADDAL , LDADDALB , LDADDALH , LDADDB , LDADDH , LDADDL , LDADDLB , LDADDLH , LDAPR , LDAPRB , LDAPRH , LDCLR , LDCLRA , LDCLRAB , LDCLRAH , LDCLRAL , LDCLRALB , LDCLRALH , LDCLRB , LDCLRH , LDCLRL , LDCLRLB , LDCLRLH , LDEOR , LDEORA , LDEORAB , LDEORAH , LDEORAL , LDEORALB , LDEORALH , LDEORB , LDEORH , LDEORL , LDEORLB ,

LDEORLH , LDSET , LDSETA , LDSETAB , LDSETAH , LDSETAL , LDSETALB , LDSETALH , LDSETB , LDSETH , LDSETL , LDSETLB , LDSETLH , LDSMAX , LDSMAXA , LDSMAXAB , LDSMAXAH , LDSMAXAL , LDSMAXALB , LDSMAXALH , LDSMAXB , LDSMAXH , LDSMAXL , LDSMAXLB , LDSMAXLH , LDSMIN , LDSMINA , LDSMINAB , LDSMINAH , LDSMINAL , LDSMINALB , LDSMINALH , LDSMINB , LDSMINH , LDSMINL , LDSMINLB , LDSMINLH , LDUMAX , LDUMAXA , LDUMAXAB , LDUMAXAH , LDUMAXAL , LDUMAXALB , LDUMAXALH , LDUMAXB , LDUMAXH , LDUMAXL , LDUMAXLB , LDUMAXLH , LDUMIN , LDUMINA , LDUMINAB , LDUMINAH , LDUMINAL , LDUMINALB , LDUMINALH , LDUMINB , LDUMINH , LDUMINL , LDUMINLB , and LDUMINLH .

- LDAPR/STLR (SIMD&amp;FP): LDAPUR , and STLUR .
- LDAPR/STLR (unscaled immediate): LDAPUR , LDAPURB , LDAPURH , LDAPURSB , LDAPURSH , LDAPURSW , STLUR , STLURB , and STLURH .
- LDAPR/STLR (writeback): LDAPR , and STLR .
- LDIAPP/STILP: LDIAPP , and STILP .
- Load/store exclusive pair: LDAXP , LDXP , STLXP , and STXP .
- Load/store exclusive register: LDAXR , LDAXRB , LDAXRH , LDXR , LDXRB , LDXRH , STLXR , STLXRB , STLXRH , STXR , STXRB and STXRH .
- Load/store no-allocate pair (offset): LDNP , and STNP .
- Load/store ordered: LDAR , LDARB , LDARH , LDLAR , LDLARB , LDLARH , STLLR , STLLRB , STLLRH , STLR , STLRB , and STLRH .
- Load/store register (immediate post-indexed): LDR , LDRB , LDRH , LDRSB , LDRSH , LDRSW , STR , STRB , and STRH .
- Load/store register (immediate pre-indexed): LDR , LDRB , LDRH , LDRSB , LDRSH , LDRSW , STR , STRB , and STRH .
- Load/store register (pac): LDRAA , and LDRAB .
- Load/store register (register offset): LDR , LDRB , LDRH , LDRSB , LDRSH , LDRSW , STR , STRB , and STRH .
- Load/store register (unprivileged): LDTR , LDTRB , LDTRH , LDTRSB , LDTRSH , LDTRSW , STTR , STTRB , and STTRH .
- Load/store register (unscaled immediate): LDUR , LDURB , LDURH , LDURSB , LDURSH , LDURSW , STUR , STURB , and STURH .
- Load/store register (unsigned immediate): LDR , LDRB , LDRH , LDRSB , LDRSH , LDRSW , STR , STRB , and STRH .
- Load/store register pair (offset): LDP , LDPSW , and STP .
- Load/store register pair (post-indexed): LDP , LDPSW , and STP .
- Load/store register pair (pre-indexed): LDP , LDPSW , and STP .
- If FEAT\_SME is implemented, SME encodings:
- SMEAddVector to Array: ADDHA , and ADDVA .
- SMEInteger Outer Product - 32 bit: SMOPA , SMOPS , SUMOPA , SUMOPS , UMOPA , UMOPS , USMOPA , and USMOPS .
- SMEMemory: LD1B , LD1D , LD1H , LD1Q , LD1W , LDR , ST1B , ST1D , ST1H , ST1Q , ST1W , and STR .
- SMEMove from Array: MOVA , and MOVAZ .
- SMEMove into Array: MOVA .
- SMEOuter Product - 64 bit:
- SMEInt16 outer product: SMOPA , SMOPS , SUMOPA , SUMOPS , UMOPA , UMOPS , USMOPA , and USMOPS .
- SMEzero array: ZERO .
- SME2 Expand Lookup Table (Contiguous): LUTI2 , and LUTI4 .
- SME2 Expand Lookup Table (Non-contiguous): LUTI2 , and LUTI4 .
- SME2 Move Lookup Table: MOVT .
- SME2 Multi-vector - Indexed (Four registers):
- SME2multi-vec indexed long MLA four sources: SMLAL , SMLSL , UMLAL , and UMLSL .
- SME2multi-vec indexed long long MLA four sources 32-bit: SMLALL , SMLSLL , SUMLALL , UMLALL , UMLSLL , and USMLALL .
- SME2multi-vec indexed long long MLA four sources 64-bit: SMLALL , SMLSLL , UMLALL , and UMLSLL .
- SME2multi-vec ternary indexed four registers 32-bit: SDOT , SUDOT , SUVDOT , SVDOT , UDOT , USDOT , USVDOT , and UVDOT .
- SME2multi-vec ternary indexed four registers 64-bit: SDOT , SVDOT , UDOT , and UVDOT .
- SME2 Multi-vector - Indexed (One register):
- SME2multi-vec indexed long MLA one source: SMLAL , SMLSL , UMLAL , and UMLSL .
- SME2multi-vec indexed long long MLA one source 32-bit: SMLALL , SMLSLL , SUMLALL , UMLALL , UMLSLL , and USMLALL .
- SME2multi-vec indexed long long MLA one source 64-bit: SMLALL , SMLSLL , UMLALL , and UMLSLL .
- SME2 Multi-vector - Indexed (Two registers):
- SME2multi-vec indexed long MLA two sources: SMLAL , SMLSL , UMLAL , and UMLSL .

- SME2multi-vec indexed long long MLA two sources 32-bit: SMLALL , SMLSLL , SUMLALL , UMLALL , UMLSLL , and USMLALL .
- SME2multi-vec indexed long long MLA two sources 64-bit: SMLALL , SMLSLL , UMLALL , and UMLSLL .
- SME2multi-vec ternary indexed two registers 32-bit: SDOT , SUDOT , SVDOT , UDOT , USDOT , and UVDOT .
- SME2multi-vec ternary indexed two registers 64-bit: SDOT , and UDOT .
- SME2 Multi-vector - Memory (Contiguous): LD1B , LD1D , LD1H , LD1W , LDNT1B , LDNT1D , LDNT1H , LDNT1W , ST1B , ST1D , ST1H , ST1W , STNT1B , STNT1D , STNT1H , and STNT1W .
- SME2 Multi-vector - Memory (Strided): LD1B , LD1D , LD1H , LD1W , LDNT1B , LDNT1D , LDNT1H , LDNT1W , ST1B , ST1D , ST1H , ST1W , STNT1B , STNT1D , STNT1H , and STNT1W .
- SME2 Multi-vector - Multiple Array Vectors (Four registers):
- SME2multiple vectors binary int four registers: ADD , and SUB .
- SME2multiple vectors four-way dot product four registers: SDOT , and UDOT .
- SME2multiple vectors long MLA four sources: SMLAL , SMLSL , UMLAL , and UMLSL .
- SME2multiple vectors long long MLA four sources: SMLALL , SMLSLL , UMLALL , UMLSLL , and USMLALL .
- SME2multiple vectors mixed dot product four registers: USDOT .
- SME2multiple vectors ternary int four registers: ADD , and SUB .
- SME2multiple vectors two-way dot product four registers: SDOT , and UDOT .
- SME2 Multi-vector - Multiple Array Vectors (Two registers):
- SME2multiple vectors binary int two registers: ADD , and SUB .
- SME2multiple vectors four-way dot product two registers: SDOT , and UDOT .
- SME2multiple vectors long MLA two sources: SMLAL , SMLSL , UMLAL , and UMLSL .
- SME2multiple vectors long long MLA two sources: SMLALL , SMLSLL , UMLALL , UMLSLL , and USMLALL .
- SME2multiple vectors mixed dot product two registers: USDOT .
- SME2multiple vectors ternary int two registers: ADD , and SUB .
- SME2multiple vectors two-way dot product two registers: SDOT , and UDOT .
- SME2 Multi-vector - Multiple Vectors SVE Destructive (Four registers):
- SME2multiple vectors int min/max four registers: SMAX , SMIN , UMAX , and UMIN .
- SME2 Multi-vector - Multiple Vectors SVE Destructive (Two registers):
- SME2multiple vectors int min/max two registers: SMAX , SMIN , UMAX , and UMIN .
- SME2 Multi-vector - Multiple Vectors SVE Saturating Multiply (Four registers): SQDMULH .
- SME2 Multi-vector - Multiple Vectors SVE Saturating Multiply (Two registers): SQDMULH .
- SME2 Multi-vector - Multiple and Single Array Vectors (Four registers):
- SME2single-multi four-way dot product four registers: SDOT , and UDOT .
- SME2single-multi long MLA four sources: SMLAL , SMLSL , UMLAL , and UMLSL .
- SME2single-multi long long MLA four sources: SMLALL , SMLSLL , SUMLALL , UMLALL , UMLSLL , and USMLALL .
- SME2single-multi mixed dot product four registers: SUDOT , and USDOT .
- SME2single-multi ternary int four registers: ADD , and SUB .
- SME2single-multi two-way dot product four registers: SDOT , and UDOT .
- SME2 Multi-vector - Multiple and Single Array Vectors (Two registers):
- SME2multiple and single vector long MLA one source: SMLAL , SMLSL , UMLAL , and UMLSL .
- SME2multiple and single vector long long FMA one source: SMLALL , SMLSLL , UMLALL , UMLSLL , and USMLALL .
- SME2single-multi four-way dot product two registers: SDOT , and UDOT .
- SME2single-multi long MLA two sources: SMLAL , SMLSL , UMLAL , and UMLSL .
- SME2single-multi long long MLA two sources: SMLALL , SMLSLL , SUMLALL , UMLALL , UMLSLL , and USMLALL .
- SME2single-multi mixed dot product two registers: SUDOT , and USDOT .
- SME2single-multi ternary int two registers: ADD , and SUB .
- SME2single-multi two-way dot product two registers: SDOT , and UDOT .
- SME2 Multi-vector - Multiple and Single SVE Destructive (Four registers):
- SME2single-multi add four registers: ADD .
- SME2single-multi int min/max four registers: SMAX , SMIN , UMAX , and UMIN .
- SME2single-multi signed saturating doubling multiply high four registers: SQDMULH .
- SME2 Multi-vector - Multiple and Single SVE Destructive (Two registers):
- SME2single-multi add two registers: ADD .
- SME2single-multi int min/max two registers: SMAX , SMIN , UMAX , and UMIN .
- SME2single-multi signed saturating doubling multiply high two registers: SQDMULH .

- SME2 Multi-vector - SVE Constructive Binary:
- SME2multi-vec CLAMP four registers: SCLAMP , and UCLAMP .
- SME2multi-vec CLAMP two registers: SCLAMP , and UCLAMP .
- SME2multi-vec ZIP two registers: UZP , and ZIP .
- SME2multi-vec quadwords ZIP two registers: UZP , and ZIP .
- SME2 Multi-vector - SVE Constructive Unary:
- SME2multi-vec ZIP four registers: UZP , and ZIP .
- SME2multi-vec quadwords ZIP four registers: UZP , and ZIP .
- SME2multi-vec unpack four registers: SUNPK , and UUNPK .
- SME2multi-vec unpack two registers: SUNPK , and UUNPK .
- SME2 Multi-vector - SVE Select: SEL .
- SME2 Multiple Zero: ZERO .
- SME2 Outer Product - Misc:
- SME232-bit binary outer product: BMOPA , and BMOPS .
- If FEAT\_SVE is implemented, SVE encodings:
- SVE Address Generation: ADR .
- SVE Bitwise Immediate: AND , EOR , and ORR .
- SVE Bitwise Logical - Unpredicated: AND , BCAX , BIC , BSL1N , BSL2N , BSL , EOR3 , EOR , NBSL , ORR , and XAR .
- SVE Bitwise Shift - Predicated:
- SVEbitwise shift by immediate (predicated): ASR , ASRD , LSL , LSR , SRSHR , and URSHR .
- SVEbitwise shift by vector (predicated): ASR , ASRR , LSL , LSLR , LSR , and LSRR .
- SVEbitwise shift by wide elements (predicated): ASR , LSL , and LSR .
- SVE Bitwise Shift - Unpredicated: ASR , LSL , and LSR .
- SVE Element Count:
- SVEinc/dec register by element count: DECB , DECD , DECH , DECW , INCB , INCD , INCH , and INCW .
- SVEinc/dec vector by element count: DECD , DECH , DECW , INCD , INCH , and INCW .
- SVE Integer Arithmetic - Unpredicated:
- SVEinteger add/subtract vectors (unpredicated): ADD , and SUB .
- SVE Integer Binary Arithmetic - Predicated:
- SVEbitwise logical operations (predicated): AND , BIC , EOR , and ORR .
- SVEinteger add/subtract vectors (predicated): ADD , SUB , and SUBR .
- SVEinteger min/max/difference (predicated): SABD , SMAX , SMIN , UABD , UMAX , and UMIN .
- SVEinteger multiply vectors (predicated): MUL , SMULH , and UMULH .
- SVE Integer Compare - Scalars: CTERMEQ , and CTERMNE .
- SVE Integer Compare - Signed Immediate: CMP&lt;cc&gt; .
- SVE Integer Compare - Unsigned Immediate: CMP&lt;cc&gt; .
- SVE Integer Compare - Vectors: CMP&lt;cc&gt; .
- SVE Integer Misc - Unpredicated: MOVPRFX .
- SVE Integer Multiply-Add - Predicated: MAD , MLA , MLS , and MSB .
- SVE Integer Multiply-Add - Unpredicated:
- SVEinteger dot product (unpredicated): SDOT , and UDOT .
- SVEmixed sign dot product: USDOT .
- SVE2complex integer multiply-add: CMLA .
- SVE2integer multiply-add long: SMLALB , SMLALT , SMLSLB , SMLSLT , UMLALB , UMLALT , UMLSLB , and UMLSLT .
- SVE2saturating multiply-add high: SQRDMLAH .
- SVE Integer Reduction: ADDQV , ANDQV , ANDV , EORQV , EORV , MOVPRFX , ORQV , ORV , SADDV , SMAXQV , SMAXV , SMINQV , SMINV , UADDV , UMAXQV , UMAXV , UMINQV , and UMINV .
- SVE Integer Unary Arithmetic - Predicated:
- SVEbitwise unary operations (predicated): CLS , CLZ , CNOT , CNT , and NOT .
- SVEinteger unary operations (predicated): ABS , NEG , SXTB , SXTH , SXTW , UXTB , UXTH , and UXTW .
- SVE Integer Wide Immediate - Unpredicated:
- SVEinteger add/subtract immediate (unpredicated): ADD , SUB , and SUBR .
- SVEinteger min/max immediate (unpredicated): SMAX , SMIN , UMAX , and UMIN .
- SVEinteger multiply immediate (unpredicated): MUL .
- SVE Memory - 32-bit Gather and Unsized Contiguous:
- SVE32-bit gather load (scalar plus 32-bit unscaled offsets): LD1B , LD1H , LD1SB , LD1SH , and LD1W .
- SVE32-bit gather load (vector plus immediate): LD1B , LD1H , LD1SB , LD1SH , and LD1W .
- SVE32-bit gather load halfwords (scalar plus 32-bit scaled offsets): LD1H , and LD1SH .
- SVE32-bit gather load words (scalar plus 32-bit scaled offsets): LD1W .

- SVEload and broadcast element: LD1RB , LD1RD , LD1RH , LD1RSB , LD1RSH , LD1RSW , and LD1RW .
- SVEload vector register: LDR .
- SVE232-bit gather non-temporal load (vector plus scalar): LDNT1B , LDNT1H , LDNT1SB , LDNT1SH , and LDNT1W .
- SVE Memory - 64-bit Gather:
- SVE64-bit gather load (scalar plus 32-bit unpacked scaled offsets): LD1D , LD1H , LD1SH , LD1SW , and LD1W .
- SVE64-bit gather load (scalar plus 64-bit scaled offsets): LD1D , LD1H , LD1SH , LD1SW , and LD1W .
- SVE64-bit gather load (scalar plus 64-bit unscaled offsets): LD1B , LD1D , LD1H , LD1SB , LD1SH , LD1SW , and LD1W .
- SVE64-bit gather load (scalar plus unpacked 32-bit unscaled offsets): LD1B , LD1D , LD1H , LD1SB , LD1SH , LD1SW , and LD1W .
- SVE64-bit gather load (vector plus immediate): LD1B , LD1D , LD1H , LD1SB , LD1SH , LD1SW , and LD1W .
- SVE2128-bit gather load (vector plus scalar): LD1Q .
- SVE264-bit gather non-temporal load (vector plus scalar): LDNT1B , LDNT1D , LDNT1H , LDNT1SB , LDNT1SH , LDNT1SW , and LDNT1W .
- SVE Memory - Contiguous Load:
- SVEcontiguous load (quadwords, scalar plus immediate): LD1D , and LD1W .
- SVEcontiguous load (quadwords, scalar plus scalar): LD1D , and LD1W .
- SVEcontiguous load (scalar plus immediate): LD1B , LD1D , LD1H , LD1SB , LD1SH , LD1SW , and LD1W .
- SVEcontiguous load (scalar plus scalar): LD1B , LD1D , LD1H , LD1SB , LD1SH , LD1SW , and LD1W .
- SVEcontiguous non-temporal load (scalar plus immediate): LDNT1B , LDNT1D , LDNT1H , and LDNT1W .
- SVEcontiguous non-temporal load (scalar plus scalar): LDNT1B , LDNT1D , LDNT1H , and LDNT1W .
- SVEload and broadcast quadword (scalar plus immediate): LD1ROB , LD1ROD , LD1ROH , LD1ROW , LD1RQB , LD1RQD , LD1RQH , and LD1RQW .
- SVEload and broadcast quadword (scalar plus scalar): LD1ROB , LD1ROD , LD1ROH , LD1ROW , LD1RQB , LD1RQD , LD1RQH , and LD1RQW .
- SVEload multiple structures (quadwords, scalar plus immediate): LD2Q , LD3Q , and LD4Q .
- SVEload multiple structures (quadwords, scalar plus scalar): LD2Q , LD3Q , and LD4Q .
- SVEload multiple structures (scalar plus immediate): LD2B , LD2D , LD2H , LD2W , LD3B , LD3D , LD3H , LD3W , LD4B , LD4D , LD4H , and LD4W .
- SVEload multiple structures (scalar plus scalar): LD2B , LD2D , LD2H , LD2W , LD3B , LD3D , LD3H , LD3W , LD4B , LD4D , LD4H , and LD4W .
- SVE Memory - Contiguous Store and Unsized Contiguous: ST1B , ST1D , ST1H , ST1W , ST2Q , ST3Q , and ST4Q .
- SVE Memory - Contiguous Store with Immediate Offset: ST1B , ST1D , ST1H , ST1W , ST2B , ST2D , ST2H , ST2W , ST3B , ST3D , ST3H , ST3W , ST4B , ST4D , ST4H , ST4W , STNT1B , STNT1D , STNT1H , and STNT1W .
- SVE Memory - Non-temporal and Multi-register Contiguous Store: ST2B , ST2D , ST2H , ST2W , ST3B , ST3D , ST3H , ST3W , ST4B , ST4D , ST4H , ST4W , STNT1B , STNT1D , STNT1H , and STNT1W .
- SVE Memory - Non-temporal and Quadword Scatter Store: ST1Q , STNT1B , STNT1D , STNT1H , and STNT1W .
- SVE Memory - Scatter: ST1B , ST1D , ST1H , and ST1W .
- SVE Memory - Scatter with Optional Sign Extend: ST1B , ST1D , ST1H , and ST1W .
- SVE Misc: BDEP , BEXT , BGRP , EORBT , EORTB , SADDLBT , SMMLA , SSHLLB , SSHLLT , SSUBLBT , SSUBLTB , UMMLA , USHLLB , USHLLT , and USMMLA .
- SVE Multiply - Indexed:
- SVEinteger dot product (indexed): SDOT , and UDOT .
- SVEmixed sign dot product (indexed): SUDOT , and USDOT .
- SVE2complex integer multiply-add (indexed): CMLA .
- SVE2integer multiply (indexed): MUL .
- SVE2integer multiply long (indexed): SMULLB , SMULLT , UMULLB , and UMULLT .
- SVE2integer multiply-add (indexed): MLA , and MLS .
- SVE2integer multiply-add long (indexed): SMLALB , SMLALT , SMLSLB , SMLSLT , UMLALB , UMLALT , UMLSLB , and UMLSLT .
- SVE2saturating multiply high (indexed): SQDMULH , and SQRDMULH .
- SVE2saturating multiply-add high (indexed): SQRDMLAH .
- SVE Permute Vector - Extract: EXT .
- SVE Permute Vector - Indexed DUP: DUP .
- SVE Permute Vector - Interleaving: TRN1 , TRN2 , UZP1 , UZP2 , ZIP1 , and ZIP2 .
- SVE Permute Vector - One Source Quadwords: DUPQ , and EXTQ .
- SVE Permute Vector - Predicated:
- SVEcopy SIMD&amp;FP scalar register to vector (predicated): CPY .

- SVEcopy general register to vector (predicated): CPY .
- SVEreverse doublewords: REVD .
- SVEreverse within elements: RBIT , REVB , REVH , and REVW .
- SVE Permute Vector - Segments: TRN1 , TRN2 , UZP1 , UZP2 , ZIP1 , and ZIP2 .
- SVE Permute Vector - TBXQ: TBXQ .
- SVE Permute Vector - Three Sources TBL: TBL , and TBX .
- SVE Permute Vector - Two Sources Quadwords: TBLQ , UZPQ1 , UZPQ2 , ZIPQ1 , and ZIPQ2 .
- SVE Permute Vector - Two Sources TBL: TBL .
- SVE Permute Vector - Unpredicated:
- SVEbroadcast general register: DUP .
- SVEinsert SIMD&amp;FP scalar register: INSR .
- SVEinsert general register: INSR .
- SVEreverse vector elements: REV .
- SVEunpack vector elements: SUNPKHI , SUNPKLO , UUNPKHI , and UUNPKLO .
- SVE Predicate Select: PSEL .
- SVE Stack Allocation: ADDPL , ADDSPL , ADDSVL , and ADDVL .
- SVE Vector Select: SEL .
- SVE integer clamp: SCLAMP , and UCLAMP .
- SVE two-way dot product: SDOT , and UDOT .
- SVE two-way dot product (indexed): SDOT , and UDOT .
- SVE2 Accumulate:
- SVE2bitwise shift and insert: SLI , and SRI .
- SVE2bitwise shift right and accumulate: SRSRA , SSRA , URSRA , and USRA .
- SVE2complex integer add: CADD .
- SVE2integer absolute difference and accumulate: SABA , and UABA .
- SVE2integer absolute difference and accumulate long: SABALB , SABALT , UABALB , and UABALT .
- SVE2integer add/subtract long with carry: ADCLB , ADCLT , SBCLB , and SBCLT .
- SVE2 Crypto Extensions: AESD , AESE , AESIMC , AESMC , RAX1 , SM4E , and SM4EKEY .
- SVE2 Histogram Computation (Segment) and Lookup Table: LUTI2 , and LUTI4 .
- SVE2 Integer - Predicated:
- SVE2integer halving add/subtract (predicated): SHADD , SHSUB , SHSUBR , UHADD , UHSUB ,and UHSUBR .
- SVE2integer pairwise add and accumulate long: SADALP , and UADALP .
- SVE2integer pairwise arithmetic: ADDP , SMAXP , SMINP , UMAXP , and UMINP .
- SVE2 Integer Multiply - Unpredicated: MUL , PMUL , SMULH , SQDMULH , SQRDMULH , and UMULH .
- SVE2 Narrowing:
- SVE2bitwise shift right narrow: RSHRNB , RSHRNT , SHRNB , and SHRNT .
- SVE2integer add/subtract narrow high part: ADDHNB , ADDHNT , RADDHNB , RADDHNT , RSUBHNB , RSUBHNT , SUBHNB , and SUBHNT .
- SVE2 Widening Integer Arithmetic:
- SVE2integer add/subtract long: SABDLB , SABDLT , SADDLB , SADDLT , SSUBLB , SSUBLT , UABDLB , UABDLT , UADDLB , UADDLT , USUBLB , and USUBLT .
- SVE2integer add/subtract wide: SADDWB , SADDWT , SSUBWB , SSUBWT , UADDWB , UADDWT , USUBWB , and USUBWT .
- SVE2integer multiply long: PMULLB , PMULLT , SMULLB , SMULLT , UMULLB , and UMULLT .

## The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Bits [23:0]

Reserved, RES0.

## Accessing DIT

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, DIT

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0010 | 0b101 |

if !(IsFeatureImplemented(FEAT\_DIT) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then X[t, 64] = Zeros(39):PSTATE.DIT:Zeros(24); elsif PSTATE.EL == EL1 then X[t, 64] = Zeros(39):PSTATE.DIT:Zeros(24); elsif PSTATE.EL == EL2 then X[t, 64] = Zeros(39):PSTATE.DIT:Zeros(24); elsif PSTATE.EL == EL3 then X[t, 64] = Zeros(39):PSTATE.DIT:Zeros(24);

MSR DIT, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0010 | 0b101 |

if !(IsFeatureImplemented(FEAT\_DIT) &amp;&amp;

UNDEFINED;

elsif PSTATE.EL == EL0 then

PSTATE.DIT = X[t, 64]&lt;24&gt;;

elsif PSTATE.EL == EL1 then

PSTATE.DIT = X[t, 64]&lt;24&gt;;

elsif PSTATE.EL == EL2 then

PSTATE.DIT = X[t, 64]&lt;24&gt;;

elsif PSTATE.EL == EL3 then

PSTATE.DIT = X[t, 64]&lt;24&gt;;

MSR DIT, #&lt;imm&gt;

| op0   | op1   | CRn    | op2   |
|-------|-------|--------|-------|
| 0b00  | 0b011 | 0b0100 | 0b010 |

IsFeatureImplemented(FEAT\_AA64)) then

## C5.2.5 ELR\_EL1, Exception Link Register (EL1)

The ELR\_EL1 characteristics are:

## Purpose

When taking an exception to EL1, holds the address to return to.

## Configuration

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ELR\_EL1 are UNDEFINED.

## Attributes

ELR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63             | 32             |                |
|----------------|----------------|----------------|
| Return address | Return address | Return address |
| 31             | 0              |                |
| Return address | Return address | Return address |

## ADDR, bits [63:0]

Return address.

An exception return from EL1 using AArch64 makes ELR\_EL1 become UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing ELR\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name ELR\_EL1 or ELR\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ELR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '011' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then
```

```
X[t, 64] = NVMem[0x230]; else X[t, 64] = ELR_EL1; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = ELR_EL2; else X[t, 64] = ELR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ELR_EL1;
```

MSR ELR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' && ↪ → !(EffectiveHCR_EL2_NVx() IN {'x11'}) then EXLOCKException(); elsif EffectiveHCR_EL2_NVx() == '011' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x230] = X[t, 64]; else ELR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' && ↪ → ELIsInHost(EL2) then EXLOCKException(); elsif ELIsInHost(EL2) then ELR_EL2 = X[t, 64]; else ELR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ELR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, ELR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0100 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x230]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = ELR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = ELR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR ELR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0100 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x230] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then ELR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then ELR_EL1 = X[t, 64]; else UNDEFINED;
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, ELR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = ELR_EL1; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then
```

AArch64.SystemAccessTrap(EL2, 0x18);

```
else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = ELR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = ELR_EL2;
```

When FEAT\_VHE is implemented MSR ELR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' ↪ → && EffectiveHCR_EL2_NVx() IN {'xx1'} then EXLOCKException(); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then ELR_EL1 = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' ↪ → then EXLOCKException(); else ELR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then ELR_EL2 = X[t, 64];
```

## C5.2.6 ELR\_EL2, Exception Link Register (EL2)

The ELR\_EL2 characteristics are:

## Purpose

When taking an exception to EL2, holds the address to return to.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register ELR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register ELR\_hyp[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ELR\_EL2 are UNDEFINED.

## Attributes

ELR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## ADDR, bits [63:0]

Return address.

An exception return from EL2 using AArch64 makes ELR\_EL2 become UNKNOWN.

When EL2 is in AArch32 Execution state and an exception is taken from EL0, EL1, or EL2 to EL3 and AArch64 execution, the upper 32-bits of ELR\_EL2 are either set to 0 or hold the same value that they did before AArch32 execution. Which option is adopted is determined by an implementation, and might vary dynamically within an implementation. Correspondingly software must regard the value as being an UNKNOWN choice between the two values.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing ELR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name ELR\_EL2 or ELR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ELR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = ELR_EL1; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = ELR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = ELR_EL2;
```

MSR ELR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' && ↪ → EffectiveHCR_EL2_NVx() IN {'xx1'} then EXLOCKException(); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then ELR_EL1 = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' then EXLOCKException(); else ELR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then ELR_EL2 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, ELR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '011' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x230]; else X[t, 64] = ELR_EL1; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = ELR_EL2; else X[t, 64] = ELR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ELR_EL1;
```

When FEAT\_VHE is implemented MSR ELR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' ↪ → && !(EffectiveHCR_EL2_NVx() IN {'x11'}) then EXLOCKException(); elsif EffectiveHCR_EL2_NVx() == '011' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x230] = X[t, 64]; else ELR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' ↪ → && ELIsInHost(EL2) then EXLOCKException(); elsif ELIsInHost(EL2) then ELR_EL2 = X[t, 64]; else ELR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ELR_EL1 = X[t, 64];
```

## C5.2.7 ELR\_EL3, Exception Link Register (EL3)

The ELR\_EL3 characteristics are:

## Purpose

When taking an exception to EL3, holds the address to return to.

## Configuration

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to ELR\_EL3 are UNDEFINED.

## Attributes

ELR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63             | 32             |                |
|----------------|----------------|----------------|
| Return address | Return address | Return address |
| 31             | 0              |                |
| Return address | Return address | Return address |

## ADDR, bits [63:0]

Return address.

An exception return from EL3 using AArch64 makes ELR\_EL3 become UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing ELR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ELR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0100 | 0b0000 | 0b001 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = ELR_EL3;
```

MSR ELR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0100 | 0b0000 | 0b001 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' then EXLOCKException(); else ELR_EL3 = X[t, 64];
```

## C5.2.8 FPCR, Floating-point Control Register

The FPCR characteristics are:

## Purpose

Controls behavior of the floating-point instructions.

## Configuration

It is IMPLEMENTATION DEFINED whether the Len and Stride fields can be programmed to nonzero values, which will cause some AArch32 floating-point instruction encodings to be UNDEFINED, or whether these fields are RAZ.

AArch64 System register FPCR bits [26:15] are architecturally mapped to AArch32 System register FPSCR[26:15].

AArch64 System register FPCR bits [12:8] are architecturally mapped to AArch32 System register FPSCR[12:8].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to FPCR are UNDEFINED.

## Attributes

FPCR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:27]

Reserved, RES0.

## AHP, bit [26]

Alternative half-precision control bit.

| AHP   | Meaning                                     |
|-------|---------------------------------------------|
| 0b0   | IEEE half-precision format selected.        |
| 0b1   | Alternative half-precision format selected. |

This bit is used only for conversions between half-precision floating-point and other floating-point formats.

The data-processing instructions added as part of the FEAT\_FP16 extension always use the IEEE half-precision format, and ignore the value of this bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## DN, bit [25]

Default NaN use for NaN propagation.

| DN   | Meaning                                                                                                                                                                                                                                                               |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | NaN operands propagate through to the output of a floating-point operation.                                                                                                                                                                                           |
| 0b1  | Any operation involving one or more NaNs returns the Default NaN. This bit has no effect on the output of the FABS and FNEG instructions. This bit has no effect on the output of the FMAX , FMAXP , FMAXV , FMIN , FMINP , and FMINV instructions when FPCR.AH is 1. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## FZ, bit [24]

Flushing denormalized numbers to zero control bit.

| FZ   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | If FPCR.AH is 0, the flushing to zero of single-precision and double-precision denormalized inputs to, and outputs of, floating-point instructions not enabled by this control, but other factors might cause the input denormalized numbers to be flushed to zero. If FPCR.AH is 1, the flushing to zero of single-precision and double-precision denormalized outputs of floating-point instructions not enabled by this control, but other factors might cause the input denormalized numbers to be flushed to zero. |
| 0b1  | If FPCR.AH is 0, denormalized single-precision and double-precision inputs to, and outputs from, floating-point instructions are flushed to zero. If FPCR.AH is 1, denormalized single-precision and double-precision outputs from floating-point instructions are flushed to zero.                                                                                                                                                                                                                                     |

For more information, see 'Flushing denormalized numbers to zero' and the pseudocode of the floating-point instructions.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## RMode, bits [23:22]

Rounding Mode control field.

| RMode   | Meaning                                 |
|---------|-----------------------------------------|
| 0b00    | Round to Nearest (RN) mode.             |
| 0b01    | Round towards Plus Infinity (RP) mode.  |
| 0b10    | Round towards Minus Infinity (RM) mode. |
| 0b11    | Round towards Zero (RZ) mode.           |

If FPCR.AH is 1, then the following instructions use Round to Nearest mode regardless of the value of this bit:

- The FRECPE, FRECPS, FRECPX, FRSQRTE, and FRSQRTS instructions.
- The BFCVT, BFCVTN, BFCVTN2, BFCVTNT, BFMLALB, and BFMLALT instructions.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Stride, bits [21:20]

This field has no function in AArch64 state, and nonzero values are ignored during execution in AArch64 state.

This field is included only for context saving and restoration of the AArch32 FPSCR.Stride field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When an implementation implements FPSCR.LEN,STRIDE as RAZ, access to this field is RAZ/WI.

## FZ16, bit [19]

## When FEAT\_FP16 is implemented:

Flushing denormalized numbers to zero control bit on half-precision data-processing instructions.

| FZ16   | Meaning                                                                                                                                                                                                                                             |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | For some instructions, this bit disables flushing to zero of inputs and outputs that are half-precision denormalized numbers.                                                                                                                       |
| 0b1    | Flushing denormalized numbers to zero enabled. For some instructions that do not convert a half-precision input to a higher precision output, this bit enables flushing to zero of inputs and outputs that are half-precision denormalized numbers. |

For more information, see 'Flushing denormalized numbers to zero' and the pseudocode of the floating-point instructions.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Len, bits [18:16]

This field has no function in AArch64 state, and nonzero values are ignored during execution in AArch64 state.

This field is included only for context saving and restoration of the AArch32 FPSCR.Len field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When an implementation implements FPSCR.LEN,STRIDE as RAZ, access to this field is RAZ/WI.

## IDE, bit [15]

Input Denormal floating-point exception trap enable.

| IDE   | Meaning                                                                                                               |
|-------|-----------------------------------------------------------------------------------------------------------------------|
| 0b0   | Untrapped exception handling selected. If the floating-point exception occurs, the FPSR.IDC bit is set to 1.          |
| 0b1   | Trapped exception handling selected. If the floating-point exception occurs, the PE does not update the FPSR.IDC bit. |

When the PE is in Streaming SVE mode, and FEAT\_SME\_FA64 is not implemented or not enabled, the value of FPCR.IDE is treated as 0 for all purposes other than a direct read or write of the FPCR.

The Effective value of this bit controls both scalar and vector floating-point arithmetic.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When an implementation does not implement trapping of Input Denormal floating-point exceptions, access to this field is RAZ/WI.

## Bit [14]

Reserved, RES0.

## EBF, bit [13]

## When FEAT\_EBF16 is implemented:

The value of this bit controls the numeric behaviors of BFloat16 dot product calculations performed by the BFDOT, BFMMLA, BFMOPA, and BFMOPS instructions. If FEAT\_SME2 is implemented, this also controls BFVDOT instruction.

When ID\_AA64ISAR1\_EL1.BF16 and ID\_AA64ZFR0\_EL1.BF16 are 0b0010 , the PE supports the FPCR.EBF field. Otherwise, FPCR.EBF is RES0.

| EBF   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | These instructions use the standard BFloat16 behaviors: • Ignoring the FPCR.RMode control and using the rounding mode defined for BFloat16. For more information, see 'Round to Odd mode'. • Flushing denormalized inputs and outputs to zero, as if the FPCR.FZ and FPCR.FIZ controls had the value '1'. • Performing unfused multiplies and additions with intermediate rounding of all products and sums.                                                                                                                                                                                                                                                                                                                                                                                      |
| 0b1   | These instructions use the extended BFloat16 behaviors: • Supporting all four IEEE 754 rounding modes selected by the FPCR.RMode control. • Optionally, flushing denormalized inputs and outputs to zero, as governed by the FPCR.FZ and FPCR.FIZ controls. • Performing a fused two-way sum-of-products for each pair of adjacent BFloat16 elements, without intermediate rounding of the products, but rounding the single-precision sum before addition to the accumulator. • Generating the default NaN as intermediate sum-of-products when any multiplier input is a NaN, or any product is infinity × 0.0, or there are infinite products with differing signs. • Generating an intermediate sum-of-products of the same infinity when there are infinite products all with the same sign. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## IXE, bit [12]

Inexact floating-point exception trap enable.

| IXE   | Meaning                                                                                                               |
|-------|-----------------------------------------------------------------------------------------------------------------------|
| 0b0   | Untrapped exception handling selected. If the floating-point exception occurs, the FPSR.IXC bit is set to 1.          |
| 0b1   | Trapped exception handling selected. If the floating-point exception occurs, the PE does not update the FPSR.IXC bit. |

When the PE is in Streaming SVE mode, and FEAT\_SME\_FA64 is not implemented or not enabled, the value of FPCR.IXE is treated as 0 for all purposes other than a direct read or write of the FPCR.

The Effective value of this bit controls both scalar and vector floating-point arithmetic.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When an implementation does not implement trapping of Inexact floating-point exceptions, access to this field is RAZ/WI.

## UFE, bit [11]

Underflow floating-point exception trap enable.

| UFE   | Meaning                                                                                                                                                |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Untrapped exception handling selected. If the floating-point exception occurs, the FPSR.UFC bit is set to 1.                                           |
| 0b1   | Trapped exception handling selected. If the floating-point exception occurs and Flush-to-zero is not enabled, the PE does not update the FPSR.UFC bit. |

When the PE is in Streaming SVE mode, and FEAT\_SME\_FA64 is not implemented or not enabled, the value of FPCR.UFE is treated as 0 for all purposes other than a direct read or write of the FPCR.

The Effective value of this bit controls both scalar and vector floating-point arithmetic.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When an implementation does not implement trapping of Underflow floating-point exceptions, access to this field is RAZ/WI.

## OFE, bit [10]

Overflow floating-point exception trap enable.

| OFE   | Meaning                                                                                                               |
|-------|-----------------------------------------------------------------------------------------------------------------------|
| 0b0   | Untrapped exception handling selected. If the floating-point exception occurs, the FPSR.OFC bit is set to 1.          |
| 0b1   | Trapped exception handling selected. If the floating-point exception occurs, the PE does not update the FPSR.OFC bit. |

When the PE is in Streaming SVE mode, and FEAT\_SME\_FA64 is not implemented or not enabled, the value of FPCR.OFE is treated as 0 for all purposes other than a direct read or write of the FPCR.

The Effective value of this bit controls both scalar and vector floating-point arithmetic.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When an implementation does not implement trapping of Overflow floating-point exceptions, access to this field is RAZ/WI.

## DZE, bit [9]

Divide by Zero floating-point exception trap enable.

| DZE   | Meaning                                                                                                               |
|-------|-----------------------------------------------------------------------------------------------------------------------|
| 0b0   | Untrapped exception handling selected. If the floating-point exception occurs, the FPSR.DZC bit is set to 1.          |
| 0b1   | Trapped exception handling selected. If the floating-point exception occurs, the PE does not update the FPSR.DZC bit. |

When the PE is in Streaming SVE mode, and FEAT\_SME\_FA64 is not implemented or not enabled, the value of FPCR.DZE is treated as 0 for all purposes other than a direct read or write of the FPCR.

The Effective value of this bit controls both scalar and vector floating-point arithmetic.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When an implementation does not implement trapping of Divide by Zero floating-point exceptions, access to this field is RAZ/WI.

## IOE, bit [8]

Invalid Operation floating-point exception trap enable.

| IOE   | Meaning                                                                                                               |
|-------|-----------------------------------------------------------------------------------------------------------------------|
| 0b0   | Untrapped exception handling selected. If the floating-point exception occurs, the FPSR.IOC bit is set to 1.          |
| 0b1   | Trapped exception handling selected. If the floating-point exception occurs, the PE does not update the FPSR.IOC bit. |

When the PE is in Streaming SVE mode, and FEAT\_SME\_FA64 is not implemented or not enabled, the value of FPCR.IOE is treated as 0 for all purposes other than a direct read or write of the FPCR.

The Effective value of this bit controls both scalar and vector floating-point arithmetic.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When an implementation does not implement trapping of Invalid Operation floating-point exceptions, access to this field is RAZ/WI.

## Bits [7:3]

Reserved, RES0.

## NEP, bit [2]

## When FEAT\_AFP is implemented:

Controls how the output elements other than the lowest element of the vector are determined for Advanced SIMD scalar instructions.

| NEP   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Does not affect how the output elements other than the lowest are determined for Advanced SIMD scalar instructions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 0b1   | The output elements other than the lowest are taken from the following registers: • For 3-input scalar versions of the FMLA(by element) and FMLS (by element) instructions, the <Hd>, <Sd>, or <Dd> register. • For 3-input versions of the FMADD, FMSUB, FNMADD, and FNMSUBinstructions, the <Ha>, <Sa>, or <Da> register. • For 2-input scalar versions of the FACGE, FACGT, FCMEQ(register), FCMGE(register), and FCMGT(register) instructions, the <Hm>, <Sm>, or <Dm> register. • For 2-input scalar versions of the FABD, FADD(scalar), FDIV (scalar), FMAX(scalar), FMAXNM(scalar), FMIN (scalar), FMINNM(scalar), FMUL(by element), FMUL(scalar), FMULX(by element), FMULX, FNMUL(scalar), FRECPS, FRSQRTS, and FSUB (scalar) instructions, the <Hn>, <Sn>, or <Dn> register. • For 1-input scalar versions of the following instructions, the <Hd>, <Sd>, or <Dd> register: • The (vector) versions of the FCVTAS, FCVTAU, FCVTMS, FCVTMU, FCVTNS, FCVTNU, FCVTPS, and FCVTPU instructions. • The (vector, fixed-point) and (vector, integer) versions of the FCVTZS, FCVTZU, SCVTF, and UCVTF instructions. • The (scalar) versions of the FABS, FNEG, FRINT32X, FRINT32Z, FRINT64X, FRINT64Z, FRINTA, FRINTI, FRINTM, FRINTN, FRINTP, FRINTX, FRINTZ, and FSQRT instructions. • The (scalar, fixed-point) and (scalar, integer) versions of the SCVTF and UCVTF instructions. |

When the PE is in Streaming SVE mode, and FEAT\_SME\_FA64 is not implemented or not enabled, the value of FPCR.NEP is treated as 0 for all purposes other than a direct read or write of the FPCR.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## AH, bit [1]

## When FEAT\_AFP is implemented:

Alternate Handling. Controls alternate handling of floating-point numbers.

The Arm architecture supports two models for handling some of the corner cases of the floating-point behaviors, such as the nature of flushing of denormalized numbers, the detection of tininess and other exceptions and a range of other behaviors. The value of the FPCR.AH bit selects between these models.

For more information on the FPCR.AH bit, see 'Flushing denormalized numbers to zero', 'Floating-point exceptions and exception traps' and the pseudocode of the floating-point instructions.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FIZ, bit [0]

## When FEAT\_AFP is implemented:

Flush Inputs to Zero. Controls whether single-precision, double-precision and BFloat16 input operands that are denormalized numbers are flushed to zero.

| FIZ   | Meaning                                                                                                                                                                                                                           |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The flushing to zero of single-precision and double-precision denormalized inputs to floating-point instructions not enabled by this control, but other factors might cause the input denormalized numbers to be flushed to zero. |
| 0b1   | Denormalized single-precision and double-precision inputs to most floating-point instructions flushed to zero.                                                                                                                    |

For more information, see 'Flushing denormalized numbers to zero' and the pseudocode of the floating-point instructions.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing FPCR

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, FPCR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0100 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED; elsif !ELIsInHost(EL0) && CPACR_EL1.FPEN != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x00); else AArch64.SystemAccessTrap(EL1, 0x07); elsif ELIsInHost(EL0) && CPTR_EL2.FPEN != '11' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else X[t, 64] = FPCR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED; elsif CPACR_EL1.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL1, 0x07); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else X[t, 64] = FPCR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED; elsif !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else X[t, 64] = FPCR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TFP == '1' then AArch64.SystemAccessTrap(EL3, 0x07); else X[t, 64] = FPCR;
```

MSR FPCR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0100 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED; elsif !ELIsInHost(EL0) && CPACR_EL1.FPEN != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x00); else AArch64.SystemAccessTrap(EL1, 0x07); elsif ELIsInHost(EL0) && CPTR_EL2.FPEN != '11' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else FPCR = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED; elsif CPACR_EL1.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL1, 0x07); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else FPCR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED; elsif !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else FPCR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TFP == '1' then AArch64.SystemAccessTrap(EL3, 0x07); else FPCR = X[t, 64];
```

## C5.2.9 FPMR, Floating-point Mode Register

The FPMR characteristics are:

## Purpose

Controls behaviors of the FP8 instructions.

## Configuration

Adirect or indirect read of this register occurs in program order relative to a direct write of this register without explicit synchronization.

On entry to or exit from Streaming SVE mode, FPMR is set to 0.

This register is present only when FEAT\_FPMR is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to FPMR are UNDEFINED.

## Attributes

FPMRis a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:38]

Reserved, RES0.

## LSCALE2, bits [37:32]

Downscaling value for instructions that convert the second FP8 input data stream to other floating-point formats.

This value is an unsigned integer that is subtracted from the result exponent.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NSCALE, bits [31:24]

Scaling value for instructions that convert other floating-point formats to an FP8 format.

This value is a signed integer that is added to the operand exponent.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [23]

Reserved, RES0.

## LSCALE, bits [22:16]

Downscaling value.

This value is an unsigned integer that is subtracted from:

- The product or the sum-of-products exponent, for multiplication instructions with FP8 operands.
- The result exponent, for instructions that convert the first FP8 input data stream to other floating-point formats.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## OSC, bit [15]

Overflow saturation for FP8 convert instructions. Specifies the result when a floating-point Overflow exception is detected.

| OSC   | Meaning                             |
|-------|-------------------------------------|
| 0b0   | Infinity or NaN is generated.       |
| 0b1   | Maximum normal number is generated. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## OSM, bit [14]

Overflow saturation for FP8 multiplication instructions. Specifies the result when a floating-point Overflow exception is detected.

| OSM   | Meaning                             |
|-------|-------------------------------------|
| 0b0   | Infinity is generated.              |
| 0b1   | Maximum normal number is generated. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [13:9]

Reserved, RES0.

## F8D, bits [8:6]

Destination result format for instructions that convert other floating-point values to an FP8 format.

| F8D   | Meaning           |
|-------|-------------------|
| 0b000 | OFP8 E5M2 format. |
| 0b001 | OFP8 E4M3 format. |

All other values are reserved.

Reserved values identify an unsupported format and behave as described in Reserved values in System and memory-mapped registers and translation table entries.

Additionally, FP8 instructions are permitted to set an FP8 result with an unsupported format to 0xFF and signal an Invalid Operation floating-point exception.

It is software's responsibility to check that a format value is supported in ID\_AA64FPFR0\_EL1[7:0], before writing it to this field.

For more information about the FP8 formats, see the OCP8-bit Floating Point Specification (OFP8) .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F8S2, bits [5:3]

Second FP8 input data stream format for multiplication instructions with FP8 operands, and the corresponding instructions that convert an FP8 format to other floating-point formats.

| F8S2   | Meaning           |
|--------|-------------------|
| 0b000  | OFP8 E5M2 format. |
| 0b001  | OFP8 E4M3 format. |

All other values are reserved.

Reserved values identify an unsupported format and behave as described in Reserved values in System and memory-mapped registers and translation table entries.

Additionally FP8 instructions are permitted to treat FP8 input values with an unsupported format as a signaling NaN.

It is software's responsibility to check that a format value is supported in ID\_AA64FPFR0\_EL1[7:0], before writing it to this field.

For more information about the FP8 formats, see the OCP8-bit Floating Point Specification (OFP8) .

The reset behavior of this field is:

- •
- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F8S1, bits [2:0]

First FP8 input data stream format for multiplication instructions with FP8 operands, and the corresponding instructions that convert an FP8 format to other floating-point formats.

| F8S1   | Meaning           |
|--------|-------------------|
| 0b000  | OFP8 E5M2 format. |
| 0b001  | OFP8 E4M3 format. |

All other values are reserved.

Reserved values identify an unsupported format and behave as described in Reserved values in System and memory-mapped registers and translation table entries.

Additionally FP8 instructions are permitted to treat FP8 input values with an unsupported format as a signaling NaN.

It is software's responsibility to check that a format value is supported in ID\_AA64FPFR0\_EL1[7:0], before writing it to this field.

For more information about the FP8 formats, see the OCP8-bit Floating Point Specification (OFP8) .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing FPMR

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, FPMR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_FPMR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnFPM == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED; elsif !ELIsInHost(EL0) && SCTLR_EL1.EnFPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && SCTLR_EL2.EnFPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && ((HaveEL(EL3) && SCR_EL3.HXEn == '0') || HCRX_EL2.EnFPM == ↪ → '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.EnFPM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !ELIsInHost(EL0) && CPACR_EL1.FPEN != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x00); else AArch64.SystemAccessTrap(EL1, 0x07); elsif ELIsInHost(EL0) && CPTR_EL2.FPEN != '11' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else X[t, 64] = FPMR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnFPM == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED;
```

```
elsif EL2Enabled() && !ELIsInHost(EL0) && ((HaveEL(EL3) && SCR_EL3.HXEn == '0') || HCRX_EL2.EnFPM == ↪ → '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.EnFPM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif CPACR_EL1.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL1, 0x07); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else X[t, 64] = FPMR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnFPM == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.EnFPM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else X[t, 64] = FPMR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TFP == '1' then AArch64.SystemAccessTrap(EL3, 0x07); else X[t, 64] = FPMR;
```

MSR FPMR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_FPMR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnFPM == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED;
```

```
elsif !ELIsInHost(EL0) && SCTLR_EL1.EnFPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && SCTLR_EL2.EnFPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && ((HaveEL(EL3) && SCR_EL3.HXEn == '0') || HCRX_EL2.EnFPM == ↪ → '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.EnFPM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !ELIsInHost(EL0) && CPACR_EL1.FPEN != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x00); else AArch64.SystemAccessTrap(EL1, 0x07); elsif ELIsInHost(EL0) && CPTR_EL2.FPEN != '11' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else FPMR = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnFPM == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED; elsif EL2Enabled() && !ELIsInHost(EL0) && ((HaveEL(EL3) && SCR_EL3.HXEn == '0') || HCRX_EL2.EnFPM == ↪ → '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.EnFPM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif CPACR_EL1.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL1, 0x07); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else FPMR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnFPM == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.EnFPM == '0' then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else FPMR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TFP == '1' then AArch64.SystemAccessTrap(EL3, 0x07); else FPMR = X[t, 64];
```

## C5.2.10 FPSR, Floating-point Status Register

The FPSR characteristics are:

## Purpose

Provides floating-point system status information.

## Configuration

On entry to or exit from Streaming SVE mode, FPSR.{IOC, DZC, OFC, UFC, IXC, IDC, QC} are set to 1 and the remaining bits are set to 0.

AArch64 System register FPSR bits [31:27] are architecturally mapped to AArch32 System register FPSCR[31:27].

AArch64 System register FPSR bit [7] is architecturally mapped to AArch32 System register FPSCR[7].

AArch64 System register FPSR bits [4:0] are architecturally mapped to AArch32 System register FPSCR[4:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to FPSR are UNDEFINED.

## Attributes

FPSR is a 64-bit register.

## Field descriptions

<!-- image -->

| 63    |    |    |       |      |          |     |    |    |         |     | 32   |
|-------|----|----|-------|------|----------|-----|----|----|---------|-----|------|
| RES0  |    |    |       |      |          |     |    |    |         |     |      |
| 31 26 | 30 | 29 | 28 27 |      | 7 6 5    | 4   | 3  | 2  |         | 1   | 0    |
| N     | Z  | C  | V QC  | RES0 | IDC RES0 | IXC |    |    | UFC OFC | DZC | IOC  |

## Bits [63:32]

Reserved, RES0.

## N, bit [31]

## When FEAT\_AA32 is implemented and FEAT\_FP is implemented:

Negative condition flag for AArch32 floating-point comparison operations.

Note

AArch64 floating-point comparisons set the PSTATE.N flag instead.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Z, bit [30]

## When FEAT\_AA32 is implemented and FEAT\_FP is implemented:

Zero condition flag for AArch32 floating-point comparison operations.

## C, bit [29]

## V, bit [28]

## Bits [26:8]

Note

AArch64 floating-point comparisons set the PSTATE.Z flag instead.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## When FEAT\_AA32 is implemented and FEAT\_FP is implemented:

Carry condition flag for AArch32 floating-point comparison operations.

Note

AArch64 floating-point comparisons set the PSTATE.C flag instead.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## When FEAT\_AA32 is implemented and FEAT\_FP is implemented:

Overflow condition flag for AArch32 floating-point comparison operations.

Note

AArch64 floating-point comparisons set the PSTATE.V flag instead.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## QC, bit [27]

Cumulative saturation bit, Advanced SIMD only. This bit is set to 1 to indicate that an Advanced SIMD integer operation has saturated since 0 was last written to this bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Reserved, RES0.

## IDC, bit [7]

Input Denormal cumulative floating-point exception bit. This bit is set to 1 to indicate that the Input Denormal floating-point exception has occurred since 0 was last written to this bit.

How scalar and Advanced SIMD floating-point instructions update this bit depends on the value of the FPCR.IDE bit. This bit is set to 1 to indicate a floating-point exception only if FPCR.IDE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [6:5]

Reserved, RES0.

## IXC, bit [4]

Inexact cumulative floating-point exception bit. This bit is set to 1 to indicate that the Inexact floating-point exception has occurred since 0 was last written to this bit.

How scalar and Advanced SIMD floating-point instructions update this bit depends on the value of the FPCR.IXE bit. This bit is set to 1 to indicate a floating-point exception only if FPCR.IXE is 0.

The criteria for the Inexact floating-point exception to occur are affected by whether denormalized numbers are flushed to zero and by the value of the FPCR.AH bit. For more information, see 'Floating-point exceptions and exception traps'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## UFC, bit [3]

Underflow cumulative floating-point exception bit. This bit is set to 1 to indicate that the Underflow floating-point exception has occurred since 0 was last written to this bit.

How scalar and Advanced SIMD floating-point instructions update this bit depends on the value of the FPCR.UFE bit. This bit is set to 1 to indicate a floating-point exception only if FPCR.UFE is 0 or if flushing denormalized numbers to zero is enabled.

The criteria for the Underflow floating-point exception to occur are affected by whether denormalized numbers are flushed to zero and by the value of the FPCR.AH bit. For more information, see 'Floating-point exceptions and exception traps'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## OFC, bit [2]

Overflow cumulative floating-point exception bit. This bit is set to 1 to indicate that the Overflow floating-point exception has occurred since 0 was last written to this bit.

How scalar and Advanced SIMD floating-point instructions update this bit depends on the value of the FPCR.OFE bit. This bit is set to 1 to indicate a floating-point exception only if FPCR.OFE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## DZC, bit [1]

Divide by Zero cumulative floating-point exception bit. This bit is set to 1 to indicate that the Divide by Zero floating-point exception has occurred since 0 was last written to this bit.

How scalar and Advanced SIMD floating-point instructions update this bit depends on the value of the FPCR.DZE bit. This bit is set to 1 to indicate a floating-point exception only if FPCR.DZE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IOC, bit [0]

Invalid Operation cumulative floating-point exception bit. This bit is set to 1 to indicate that the Invalid Operation floating-point exception has occurred since 0 was last written to this bit.

How scalar and Advanced SIMD floating-point instructions update this bit depends on the value of the FPCR.IOE bit. This bit is set to 1 to indicate a floating-point exception only if FPCR.IOE is 0.

The criteria for the Invalid Operation floating-point exception to occur are affected by the value of the FPCR.AH bit. For more information, see 'Floating-point exceptions and exception traps'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing FPSR

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, FPSR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0100 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED; elsif !ELIsInHost(EL0) && CPACR_EL1.FPEN != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x00); else AArch64.SystemAccessTrap(EL1, 0x07); elsif ELIsInHost(EL0) && CPTR_EL2.FPEN != '11' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else X[t, 64] = FPSR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED; elsif CPACR_EL1.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL1, 0x07); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else X[t, 64] = FPSR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED; elsif !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then
```

```
AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else X[t, 64] = FPSR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TFP == '1' then AArch64.SystemAccessTrap(EL3, 0x07); else X[t, 64] = FPSR;
```

MSR FPSR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0100 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED; elsif !ELIsInHost(EL0) && CPACR_EL1.FPEN != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x00); else AArch64.SystemAccessTrap(EL1, 0x07); elsif ELIsInHost(EL0) && CPTR_EL2.FPEN != '11' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else FPSR = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then UNDEFINED; elsif CPACR_EL1.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL1, 0x07); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else FPSR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TFP == '1' then
```

```
UNDEFINED; elsif !ELIsInHost(EL2) && CPTR_EL2.TFP == '1' then AArch64.SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && CPTR_EL2.FPEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x07); elsif HaveEL(EL3) && CPTR_EL3.TFP == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x07); else FPSR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TFP == '1' then AArch64.SystemAccessTrap(EL3, 0x07); else FPSR = X[t, 64];
```

## C5.2.11 NZCV, Condition Flags

The NZCV characteristics are:

## Purpose

Allows access to the condition flags.

## Configuration

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to NZCV are UNDEFINED.

## Attributes

NZCVis a 64-bit register.

## Field descriptions

<!-- image -->

| 63    |    |       |      | 32   |
|-------|----|-------|------|------|
|       |    |       | RES0 |      |
| 31 30 | 29 | 28 27 |      | 0    |
| N Z   | C  | V     | RES0 |      |

## Bits [63:32]

Reserved, RES0.

## N, bit [31]

Negative condition flag. Set to 1 if the result of the last flag-setting instruction was negative.

## Z, bit [30]

Zero condition flag. Set to 1 if the result of the last flag-setting instruction was zero, and to 0 otherwise. A result of zero often indicates an equal result from a comparison.

## C, bit [29]

Carry condition flag. Set to 1 if the last flag-setting instruction resulted in a carry condition, for example an unsigned overflow on an addition.

## V, bit [28]

Overflow condition flag. Set to 1 if the last flag-setting instruction resulted in an overflow condition, for example a signed overflow on an addition.

## Bits [27:0]

Reserved, RES0.

## Accessing NZCV

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, NZCV

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0010 | 0b000 |

if !IsFeatureImplemented(FEAT\_AA64) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

X[t, 64] = Zeros(32):PSTATE.&lt;N,Z,C,V&gt;:Zeros(28);

elsif PSTATE.EL == EL1 then

X[t, 64] = Zeros(32):PSTATE.&lt;N,Z,C,V&gt;:Zeros(28);

elsif PSTATE.EL == EL2 then

X[t, 64] = Zeros(32):PSTATE.&lt;N,Z,C,V&gt;:Zeros(28);

elsif PSTATE.EL == EL3 then

X[t, 64] = Zeros(32):PSTATE.&lt;N,Z,C,V&gt;:Zeros(28);

MSR NZCV, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0010 | 0b000 |

if !IsFeatureImplemented(FEAT\_AA64) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

PSTATE.&lt;N,Z,C,V&gt; = X[t, 64]&lt;31:28&gt;;

elsif PSTATE.EL == EL1 then

PSTATE.&lt;N,Z,C,V&gt; = X[t, 64]&lt;31:28&gt;;

elsif PSTATE.EL == EL2 then

PSTATE.&lt;N,Z,C,V&gt; = X[t, 64]&lt;31:28&gt;;

elsif PSTATE.EL == EL3 then

PSTATE.&lt;N,Z,C,V&gt; = X[t, 64]&lt;31:28&gt;;

## C5.2.12 PAN, Privileged Access Never

The PAN characteristics are:

## Purpose

Allows access to the Privileged Access Never bit.

## Configuration

This register is present only when FEAT\_PAN is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PAN are UNDEFINED.

## Attributes

PAN is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:23]

Reserved, RES0.

## PAN, bit [22]

Privileged Access Never.

| PAN   | Meaning                                                                                                                                                |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Privileged reads and write are not disabled by this mechanism.                                                                                         |
| 0b1   | Disables privileged read and write accesses to addresses accessible at EL0 for an enabled stage 1 translation regime that defines the EL0 permissions. |

The value of this bit is usually preserved on taking an exception, except in the following situations:

- When the target of the exception is EL1, and the value of the SCTLR\_EL1.SPAN bit is 0, this bit is set to 1.
- When the target of the exception is EL2, the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, and the value of the SCTLR\_EL2.SPAN bit is 0, this bit is set to 1.

## Bits [21:0]

Reserved, RES0.

## Accessing PAN

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PAN

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0010 | 0b011 |

if !(IsFeatureImplemented(FEAT\_PAN) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

X[t, 64] = Zeros(41):PSTATE.PAN:Zeros(22);

elsif PSTATE.EL == EL2 then

X[t, 64] = Zeros(41):PSTATE.PAN:Zeros(22);

elsif PSTATE.EL == EL3 then

X[t, 64] = Zeros(41):PSTATE.PAN:Zeros(22);

MSR PAN, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0010 | 0b011 |

if !(IsFeatureImplemented(FEAT\_PAN) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

PSTATE.PAN = X[t, 64]&lt;22&gt;;

elsif PSTATE.EL == EL2 then

PSTATE.PAN = X[t, 64]&lt;22&gt;;

elsif PSTATE.EL == EL3 then

PSTATE.PAN = X[t, 64]&lt;22&gt;;

MSR PAN, #&lt;imm&gt;

| op0   | op1   | CRn    | op2   |
|-------|-------|--------|-------|
| 0b00  | 0b000 | 0b0100 | 0b100 |

## C5.2.13 PM, Profiling Exception Mask

The PM characteristics are:

## Purpose

Allows access to the Profiling exception Mask bit.

## Configuration

This register is present only when FEAT\_EBEP is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PM are UNDEFINED.

## Attributes

PMis a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 33 32   |
|------|---------|
| RES0 | PM      |
| 31   | 0       |
| RES0 |         |

## Bits [63:33]

Reserved, RES0.

## PM, bit [32]

PMUException Mask.

| PM   | Meaning                                              |
|------|------------------------------------------------------|
| 0b0  | Does not cause the Profiling exception to be masked. |
| 0b1  | Causes the Profiling exception to be masked.         |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [31:0]

Reserved, RES0.

## Accessing PM

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PM

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0011 | 0b001 |

if !(IsFeatureImplemented(FEAT\_EBEP) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then X[t, 64] = Zeros(31):PSTATE.PM:Zeros(32); elsif PSTATE.EL == EL2 then X[t, 64] = Zeros(31):PSTATE.PM:Zeros(32); elsif PSTATE.EL == EL3 then X[t, 64] = Zeros(31):PSTATE.PM:Zeros(32);

MSR PM, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0011 | 0b001 |

if !(IsFeatureImplemented(FEAT\_EBEP) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then PSTATE.PM = X[t, 64]&lt;32&gt;; elsif PSTATE.EL == EL2 then PSTATE.PM = X[t, 64]&lt;32&gt;; elsif PSTATE.EL == EL3 then PSTATE.PM = X[t, 64]&lt;32&gt;;

MSR PM, #&lt;imm&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b00  | 0b001 | 0b0100 | 0b001x | 0b000 |

## C5.2.14 SP\_EL0, Stack Pointer (EL0)

The SP\_EL0 characteristics are:

## Purpose

Holds the stack pointer associated with EL0. At higher Exception levels, this is used as the current stack pointer when the value of SPSel.SP is 0.

## Configuration

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to SP\_EL0 are UNDEFINED.

## Attributes

SP\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63            | 32            |               |
|---------------|---------------|---------------|
| Stack pointer | Stack pointer | Stack pointer |
| 31            | 0             |               |
| Stack pointer | Stack pointer | Stack pointer |

## StackPointer, bits [63:0]

Stack pointer.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SP\_EL0

When the value of PSTATE.SP is 0, this register is accessible at all Exception levels as the current stack pointer.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, SP_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if PSTATE.SP == '0' then UNDEFINED; else X[t, 64] = SP_EL0; elsif PSTATE.EL == EL2 then if PSTATE.SP == '0' then
```

```
UNDEFINED; else X[t, 64] = SP_EL0; elsif PSTATE.EL == EL3 then if PSTATE.SP == '0' then UNDEFINED; else X[t, 64] = SP_EL0;
```

MSR SP\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if PSTATE.SP == '0' then UNDEFINED; else SP_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if PSTATE.SP == '0' then UNDEFINED; else SP_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then if PSTATE.SP == '0' then UNDEFINED; else SP_EL0 = X[t, 64];
```

## C5.2.15 SP\_EL1, Stack Pointer (EL1)

The SP\_EL1 characteristics are:

## Purpose

Holds the stack pointer associated with EL1. The value of SPSel.SP determines the current stack pointer.

## Configuration

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to SP\_EL1 are UNDEFINED.

## Attributes

SP\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63            | 32            |
|---------------|---------------|
| Stack pointer |               |
| 31            | 0             |
| Stack pointer | Stack pointer |

## StackPointer, bits [63:0]

Stack pointer.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SP\_EL1

This accessibility information only applies to accesses using the MRS or MSR instructions.

When the value of SPSel.SP is 1, this register is also accessible at EL1 as the current stack pointer.

Note

When the value of SPSel.SP is 0, SP\_EL0 is used as the current stack pointer at all Exception levels.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SP\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then
```

{'xx1'} then

```
X[t, 64] = NVMem[0x240]; elsif EffectiveHCR_EL2_NVx() IN AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = SP_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = SP_EL1;
```

MSR SP\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x240] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then SP_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then SP_EL1 = X[t, 64];
```

## C5.2.16 SP\_EL2, Stack Pointer (EL2)

The SP\_EL2 characteristics are:

## Purpose

Holds the stack pointer associated with EL2. The value of SPSel.SP determines the current stack pointer.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to SP\_EL2 are UNDEFINED.

## Attributes

SP\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |               | 32   |
|------|---------------|------|
|      | Stack pointer |      |
| 31   |               | 0    |
|      | Stack pointer |      |

## StackPointer, bits [63:0]

Stack pointer.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SP\_EL2

This accessibility information only applies to accesses using the MRS or MSR instructions.

When the value of SPSel.SP is 1, this register is also accessible at EL2 as the current stack pointer.

Note

When the value of SPSel.SP is 0, SP\_EL0 is used as the current stack pointer at all Exception levels.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SP\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0100 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = SP_EL2;
```

MSR SP\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0100 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then SP_EL2 = X[t, 64];
```

## C5.2.17 SP\_EL3, Stack Pointer (EL3)

The SP\_EL3 characteristics are:

## Purpose

Holds the stack pointer associated with EL3. The value of SPSel.SP determines the current stack pointer.

## Configuration

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SP\_EL3 are UNDEFINED.

## Attributes

SP\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63            | 32            |               |
|---------------|---------------|---------------|
| Stack pointer | Stack pointer | Stack pointer |
| 31            | 0             |               |
| Stack pointer | Stack pointer | Stack pointer |

## StackPointer, bits [63:0]

Stack pointer.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SP\_EL3

This register is not accessible using MRS and MSR instructions.

When the value of SPSel.SP is 1, this register is accessible at EL3 as the current stack pointer.

Note

When the value of SPSel.SP is 0, SP\_EL0 is used as the current stack pointer at all Exception levels.

## C5.2.18 SPSel, Stack Pointer Select

The SPSel characteristics are:

## Purpose

Allows the Stack Pointer to be selected between SP\_EL0 and SP\_ELx.

## Configuration

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to SPSel are UNDEFINED.

## Attributes

SPSel is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32   |
|------|------|
| RES0 |      |
| 31   | 1 0  |
| RES0 | SP   |

## Bits [63:1]

Reserved, RES0.

## SP, bit [0]

Stack pointer to use. Possible values of this bit are:

| SP   | Meaning                                                                                                                                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Use SP_EL0 at all Exception levels.                                                                                                                                                                                             |
| 0b1  | Use SP_ELx for Exception level ELx. When FEAT_NMI is implemented and SCTLR_ELx.SPINTMASK is 1, if execution is at ELx, an IRQ or FIQ interrupt that is targeted to ELx is masked regardless of any indication of Superpriority. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '1' .

## Accessing SPSel

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPSel

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0010 | 0b000 |

if !IsFeatureImplemented(FEAT\_AA64) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then X[t, 64] = Zeros(63):PSTATE.SP; elsif PSTATE.EL == EL2 then X[t, 64] = Zeros(63):PSTATE.SP; elsif PSTATE.EL == EL3 then X[t, 64] = Zeros(63):PSTATE.SP;

MSR SPSel, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0010 | 0b000 |

if !IsFeatureImplemented(FEAT\_AA64) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then PSTATE.SP = X[t, 64]&lt;0&gt;; elsif PSTATE.EL == EL2 then PSTATE.SP = X[t, 64]&lt;0&gt;; elsif PSTATE.EL == EL3 then PSTATE.SP = X[t, 64]&lt;0&gt;;

MSR SPSel, #&lt;imm&gt;

| op0   | op1   | CRn    | op2   |
|-------|-------|--------|-------|
| 0b00  | 0b000 | 0b0100 | 0b101 |

## C5.2.19 SPSR\_abt, Saved Program Status Register (Abort mode)

The SPSR\_abt characteristics are:

## Purpose

Holds the saved process state when an exception is taken to Abort mode.

## Configuration

If EL1 only supports execution in AArch64 state, this register is RES0 from EL2 and EL3.

AArch64 System register SPSR\_abt bits [31:0] are architecturally mapped to AArch32 System register SPSR\_abt[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to SPSR\_abt are UNDEFINED.

## Attributes

SPSR\_abt is a 64-bit register.

## Field descriptions

When FEAT\_AA32EL1 is not implemented:

<!-- image -->

## Bits [63:0]

Reserved, RES0.

## Otherwise:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## N, bit [31]

Negative Condition flag. Set to the value of PSTATE.N on taking an exception to Abort mode, and copied to PSTATE.N on executing an exception return operation in Abort mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Z, bit [30]

Zero Condition flag. Set to the value of PSTATE.Z on taking an exception to Abort mode, and copied to PSTATE.Z on executing an exception return operation in Abort mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## C, bit [29]

Carry Condition flag. Set to the value of PSTATE.C on taking an exception to Abort mode, and copied to PSTATE.C on executing an exception return operation in Abort mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## V, bit [28]

Overflow Condition flag. Set to the value of PSTATE.V on taking an exception to Abort mode, and copied to PSTATE.V on executing an exception return operation in Abort mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Q, bit [27]

Overflow or saturation flag. Set to the value of PSTATE.Q on taking an exception to Abort mode, and copied to PSTATE.Q on executing an exception return operation in Abort mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IT, bits [15:10, 26:25]

If-Then. Set to the value of PSTATE.IT on taking an exception to Abort mode, and copied to PSTATE.IT on executing an exception return operation in Abort mode.

On executing an exception return operation in Abort mode, SPSR\_abt.IT must contain a value that is valid for the instruction being returned to.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## J, bit [24]

RES0.

In previous versions of the architecture, the {J, T} bits determined the AArch32 Instruction set state.

Armv8 does not support either Jazelle state or T32EE state, and the T bit determines the Instruction set state.

## SSBS, bit [23]

## When FEAT\_SSBS is implemented:

Speculative Store Bypass. Set to the value of PSTATE.SSBS on taking an exception to Abort mode, and copied to PSTATE.SSBS on executing an exception return operation in Abort mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PAN, bit [22]

## When FEAT\_PAN is implemented:

Privileged Access Never. Set to the value of PSTATE.PAN on taking an exception to Abort mode, and copied to PSTATE.PAN on executing an exception return operation in Abort mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DIT, bit [21]

## When FEAT\_DIT is implemented:

Data Independent Timing. Set to the value of PSTATE.DIT on taking an exception to Abort mode, and copied to PSTATE.DIT on executing an exception return operation in Abort mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## IL, bit [20]

Illegal Execution state. Set to the value of PSTATE.IL on taking an exception to Abort mode, and copied to PSTATE.IL on executing an exception return operation in Abort mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## GE, bits [19:16]

Greater than or Equal flags. Set to the value of PSTATE.GE on taking an exception to Abort mode, and copied to PSTATE.GE on executing an exception return operation in Abort mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## E, bit [9]

Endianness. Set to the value of PSTATE.E on taking an exception to Abort mode, and copied to PSTATE.E on executing an exception return operation in Abort mode.

If the implementation does not support big-endian operation, SPSR\_abt.E is RES0. If the implementation does not support little-endian operation, SPSR\_abt.E is RES1. On executing an exception return operation in Abort mode, if the implementation does not support big-endian operation at the Exception level being returned to, SPSR\_abt.E is RES0, and if the implementation does not support little-endian operation at the Exception level being returned to, SPSR\_abt.E is RES1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## A, bit [8]

SError exception mask. Set to the value of PSTATE.A on taking an exception to Abort mode, and copied to PSTATE.A on executing an exception return operation in Abort mode.

The reset behavior of this field is:

## I, bit [7]

IRQ interrupt mask. Set to the value of PSTATE.I on taking an exception to Abort mode, and copied to PSTATE.I on executing an exception return operation in Abort mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [6]

FIQ interrupt mask. Set to the value of PSTATE.F on taking an exception to Abort mode, and copied to PSTATE.F on executing an exception return operation in Abort mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## T, bit [5]

T32 Instruction set state. Set to the value of PSTATE.T on taking an exception to Abort mode, and copied to PSTATE.T on executing an exception return operation in Abort mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[4:0], bits [4:0]

Mode. Set to the value of PSTATE.M[4:0] on taking an exception to Abort mode, and copied to PSTATE.M[4:0] on executing an exception return operation in Abort mode.

| M[4:0]   | Meaning     |
|----------|-------------|
| 0b10000  | User.       |
| 0b10001  | FIQ.        |
| 0b10010  | IRQ.        |
| 0b10011  | Supervisor. |
| 0b10111  | Abort.      |
| 0b11011  | Undefined.  |
| 0b11111  | System.     |

Other values are reserved. If SPSR\_abt.M[4:0] has a Reserved value, or a value for an unimplemented Exception level, executing an exception return operation in Abort mode is an illegal return event, as described in 'Illegal return events from AArch32 state'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SPSR\_abt

Accesses to this register use the following encodings in the System register encoding space:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

MRS &lt;Xt&gt;, SPSR\_abt

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0011 | 0b001 |

if !IsFeatureImplemented(FEAT\_AA64) then

```
UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = SPSR_abt; elsif PSTATE.EL == EL3 then X[t, 64] = SPSR_abt;
```

MSR SPSR\_abt, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0011 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then SPSR_abt = X[t, 64]; elsif PSTATE.EL == EL3 then SPSR_abt = X[t, 64];
```

## C5.2.20 SPSR\_EL1, Saved Program Status Register (EL1)

The SPSR\_EL1 characteristics are:

## Purpose

Holds the saved process state when an exception is taken to EL1.

## Configuration

AArch64 System register SPSR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register SPSR\_svc[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to SPSR\_EL1 are UNDEFINED.

## Attributes

SPSR\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented and exception taken from AArch32 state:

<!-- image -->

An exception return from EL1 using AArch64 makes SPSR\_EL1 become UNKNOWN.

## Bits [63:37]

Reserved, RES0.

## UINJ, bit [36]

## When FEAT\_UINJ is implemented:

Inject Undefined Instruction exception. Set to 0 on taking an exception to EL1, and copied to PSTATE.UINJ on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [35:34]

Reserved, RES0.

## PPEND, bit [33]

## When FEAT\_SEBEP is implemented:

PMUProfiling exception pending bit. Set to the value of PSTATE.PPEND on taking an exception to EL1, and conditionally copied to PSTATE.PPEND on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [32]

Reserved, RES0.

## N, bit [31]

Negative Condition flag. Set to the value of PSTATE.N on taking an exception to EL1, and copied to PSTATE.N on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Z, bit [30]

Zero Condition flag. Set to the value of PSTATE.Z on taking an exception to EL1, and copied to PSTATE.Z on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## C, bit [29]

Carry Condition flag. Set to the value of PSTATE.C on taking an exception to EL1, and copied to PSTATE.C on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## V, bit [28]

Overflow Condition flag. Set to the value of PSTATE.V on taking an exception to EL1, and copied to PSTATE.V on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Q, bit [27]

Overflow or saturation flag. Set to the value of PSTATE.Q on taking an exception to EL1, and copied to PSTATE.Q on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IT, bits [15:10, 26:25]

If-Then. Set to the value of PSTATE.IT on taking an exception to EL1, and copied to PSTATE.IT on executing an exception return operation in EL1.

On executing an exception return operation in EL1, SPSR\_EL1.IT must contain a value that is valid for the instruction being returned to.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## DIT, bit [24]

## When FEAT\_DIT is implemented:

Data Independent Timing. Set to the value of PSTATE.DIT on taking an exception to EL1, and copied to PSTATE.DIT on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SSBS, bit [23]

## When FEAT\_SSBS is implemented:

Speculative Store Bypass. Set to the value of PSTATE.SSBS on taking an exception to EL1, and copied to PSTATE.SSBS on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PAN, bit [22]

## When FEAT\_PAN is implemented:

Privileged Access Never. Set to the value of PSTATE.PAN on taking an exception to EL1, and copied to PSTATE.PAN on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SS, bit [21]

Software Step. Set to the value of PSTATE.SS on taking an exception to EL1, and conditionally copied to PSTATE.SS on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IL, bit [20]

Illegal Execution state. Set to the value of PSTATE.IL on taking an exception to EL1, and copied to PSTATE.IL on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## GE, bits [19:16]

Greater than or Equal flags. Set to the value of PSTATE.GE on taking an exception to EL1, and copied to PSTATE.GE on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## E, bit [9]

Endianness. Set to the value of PSTATE.E on taking an exception to EL1, and copied to PSTATE.E on executing an exception return operation in EL1.

If the implementation does not support big-endian operation, SPSR\_EL1.E is RES0. If the implementation does not support little-endian operation, SPSR\_EL1.E is RES1. On executing an exception return operation in EL1, if the implementation does not support big-endian operation at the Exception level being returned to, SPSR\_EL1.E is RES0, and if the implementation does not support little-endian operation at the Exception level being returned to, SPSR\_EL1.E is RES1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## A, bit [8]

SError exception mask. Set to the value of PSTATE.A on taking an exception to EL1, and copied to PSTATE.A on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## I, bit [7]

IRQ interrupt mask. Set to the value of PSTATE.I on taking an exception to EL1, and copied to PSTATE.I on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [6]

FIQ interrupt mask. Set to the value of PSTATE.F on taking an exception to EL1, and copied to PSTATE.F on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## T, bit [5]

T32 Instruction set state. Set to the value of PSTATE.T on taking an exception to EL1, and copied to PSTATE.T on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[4], bit [4]

Execution state. Set to 0b1 , the value of PSTATE.nRW, on taking an exception to EL1 from AArch32 state, and copied to PSTATE.nRW on executing an exception return operation in EL1.

| M[4]   | Meaning                  |
|--------|--------------------------|
| 0b1    | AArch32 execution state. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[3:0], bits [3:0]

AArch32 Mode. Set to the value of PSTATE.M[3:0] on taking an exception to EL1, and copied to PSTATE.M[3:0] on executing an exception return operation in EL1.

| M[3:0]   | Meaning     |
|----------|-------------|
| 0b0000   | User.       |
| 0b0001   | FIQ.        |
| 0b0010   | IRQ.        |
| 0b0011   | Supervisor. |
| 0b0111   | Abort.      |
| 0b1011   | Undefined.  |
| 0b1111   | System.     |

Other values are reserved. If SPSR\_EL1.M[3:0] has a Reserved value, or a value for an unimplemented Exception level, executing an exception return operation in EL1 is an illegal return event, as described in 'Illegal return events from AArch64 state'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When exception taken from AArch64 state:

<!-- image -->

An exception return from EL1 using AArch64 makes SPSR\_EL1 become UNKNOWN.

## Bits [63:37]

Reserved, RES0.

## UINJ, bit [36]

## When FEAT\_UINJ is implemented:

Inject Undefined Instruction exception. Set to 0 on taking an exception to EL1, and copied to PSTATE.UINJ on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PACM, bit [35]

## When FEAT\_PAuth\_LR is implemented:

PACM. Set to the value of PSTATE.PACM on taking an exception to EL1, and copied to PSTATE.PACM on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLOCK, bit [34]

## When FEAT\_GCS is implemented:

Exception return state lock. Set to the value of PSTATE.EXLOCK on taking an exception to EL1, and copied to PSTATE.EXLOCK on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PPEND, bit [33]

## When FEAT\_SEBEP is implemented:

PMUProfiling exception pending bit. Set to the value of PSTATE.PPEND on taking an exception to EL1, and conditionally copied to PSTATE.PPEND on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PM, bit [32]

## When FEAT\_EBEP is implemented:

Profiling exception mask bit. Set to the value of PSTATE.PM on taking an exception to EL1, and copied to PSTATE.PM on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## N, bit [31]

Negative Condition flag. Set to the value of PSTATE.N on taking an exception to EL1, and copied to PSTATE.N on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Z, bit [30]

Zero Condition flag. Set to the value of PSTATE.Z on taking an exception to EL1, and copied to PSTATE.Z on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## C, bit [29]

Carry Condition flag. Set to the value of PSTATE.C on taking an exception to EL1, and copied to PSTATE.C on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## V, bit [28]

Overflow Condition flag. Set to the value of PSTATE.V on taking an exception to EL1, and copied to PSTATE.V on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [27:26]

Reserved, RES0.

## TCO, bit [25]

## When FEAT\_MTE is implemented:

Tag Check Override. Set to the value of PSTATE.TCO on taking an exception to EL1, and copied to PSTATE.TCO on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DIT, bit [24]

## When FEAT\_DIT is implemented:

Data Independent Timing. Set to the value of PSTATE.DIT on taking an exception to EL1, and copied to PSTATE.DIT on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## UAO, bit [23]

## When FEAT\_UAO is implemented:

User Access Override. Set to the value of PSTATE.UAO on taking an exception to EL1, and copied to PSTATE.UAO on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PAN, bit [22]

## When FEAT\_PAN is implemented:

Privileged Access Never. Set to the value of PSTATE.PAN on taking an exception to EL1, and copied to PSTATE.PAN on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SS, bit [21]

Software Step. Set to the value of PSTATE.SS on taking an exception to EL1, and conditionally copied to PSTATE.SS on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IL, bit [20]

Illegal Execution state. Set to the value of PSTATE.IL on taking an exception to EL1, and copied to PSTATE.IL on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [19:14]

Reserved, RES0.

## ALLINT, bit [13]

## When FEAT\_NMI is implemented:

All IRQ or FIQ interrupts mask. Set to the value of PSTATE.ALLINT on taking an exception to EL1, and copied to PSTATE.ALLINT on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SSBS, bit [12]

## When FEAT\_SSBS is implemented:

Speculative Store Bypass. Set to the value of PSTATE.SSBS on taking an exception to EL1, and copied to PSTATE.SSBS on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## BTYPE, bits [11:10]

## When FEAT\_BTI is implemented:

Branch Type Indicator. Set to the value of PSTATE.BTYPE on taking an exception to EL1, and copied to PSTATE.BTYPE on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## D, bit [9]

Debug exception mask. Set to the value of PSTATE.D on taking an exception to EL1, and copied to PSTATE.D on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## A, bit [8]

SError exception mask. Set to the value of PSTATE.A on taking an exception to EL1, and copied to PSTATE.A on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## I, bit [7]

IRQ interrupt mask. Set to the value of PSTATE.I on taking an exception to EL1, and copied to PSTATE.I on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [6]

FIQ interrupt mask. Set to the value of PSTATE.F on taking an exception to EL1, and copied to PSTATE.F on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [5]

Reserved, RES0.

## M[4], bit [4]

Execution state. Set to 0b0 , the value of PSTATE.nRW, on taking an exception to EL1 from AArch64 state, and copied to PSTATE.nRW on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[3:0], bits [3:0]

AArch64 Exception level and selected Stack Pointer.

| M[3:0]   | Meaning                                                                                     |
|----------|---------------------------------------------------------------------------------------------|
| 0b0000   | EL0.                                                                                        |
| 0b0100   | EL1 with SP_EL0 (EL1t).                                                                     |
| 0b0101   | EL1 with SP_EL1 (EL1h).                                                                     |
| 0b1000   | EL1 with SP_EL0 (EL1t) and either HCR_EL2.{NV, NV1} is {1,0} or HCR_EL2.{NV, NV2} is {1,1}. |
| 0b1001   | EL1 with SP_EL1 (EL1h) and either HCR_EL2.{NV, NV1} is {1,0} or HCR_EL2.{NV, NV2} is {1,1}. |

Other values are reserved. If SPSR\_EL1.M[3:0] has a Reserved value, or a value for an unimplemented Exception level, executing an exception return operation in EL1 is an illegal return event, as described in 'Illegal return events from AArch64 state'.

The bits in this field are interpreted as follows:

- M[3:2]: On an exception to EL1:
- If the exception is taken from EL0:
- M[3:2] is set to the value of PSTATE.EL on taking an exception to EL1.
- If the exception is taken from EL1:
- If the Effective value of HCR\_EL2.{NV, NV1} is not {1,0} and the Effective value of HCR\_EL2.{NV, NV2} is not {1,1}, then M[3:2] is set to the value of PSTATE.EL on taking an exception to EL1.
- If the Effective value of HCR\_EL2.{NV, NV1} is {1,0} or if the Effective value of HCR\_EL2.{NV, NV2} is {1,1}, then M[3:2] is set to 0b10 .
- M[3:2] is copied to PSTATE.EL on executing a legal exception return operation in EL1.
- M[1] is unused and is 0 for all non-reserved values.
- M[0] is set to the value of PSTATE.SP on taking an exception to EL1 and copied to PSTATE.SP on executing an exception return operation in EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SPSR\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name SPSR\_EL1 or SPSR\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

| M[4]   | Meaning                  |
|--------|--------------------------|
| 0b0    | AArch64 execution state. |

MRS &lt;Xt&gt;, SPSR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '011' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x160]; else X[t, 64] = SPSR_EL1; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = SPSR_EL2; else X[t, 64] = SPSR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = SPSR_EL1;
```

MSR SPSR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' && ↪ → !(EffectiveHCR_EL2_NVx() IN {'x11'}) then EXLOCKException(); elsif EffectiveHCR_EL2_NVx() == '011' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x160] = X[t, 64]; else SPSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' && ↪ → ELIsInHost(EL2) then EXLOCKException(); elsif ELIsInHost(EL2) then SPSR_EL2 = X[t, 64]; else SPSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then SPSR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, SPSR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x160]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = SPSR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = SPSR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR SPSR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x160] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then SPSR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then SPSR_EL1 = X[t, 64]; else UNDEFINED;
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, SPSR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = SPSR_EL1; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = SPSR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = SPSR_EL2;
```

When FEAT\_VHE is implemented MSR SPSR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' ↪ → && EffectiveHCR_EL2_NVx() IN {'xx1'} then EXLOCKException(); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then SPSR_EL1 = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' ↪ → then EXLOCKException(); else SPSR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then SPSR_EL2 = X[t, 64];
```

## C5.2.21 SPSR\_EL2, Saved Program Status Register (EL2)

The SPSR\_EL2 characteristics are:

## Purpose

Holds the saved process state when an exception is taken to EL2.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register SPSR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register SPSR\_hyp[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to SPSR\_EL2 are UNDEFINED.

## Attributes

SPSR\_EL2 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented and exception taken from AArch32 state:

<!-- image -->

An exception return from EL2 using AArch64 makes SPSR\_EL2 become UNKNOWN.

## Bits [63:37]

Reserved, RES0.

## UINJ, bit [36]

## When FEAT\_UINJ is implemented:

Inject Undefined Instruction exception. Set to 0 on taking an exception to EL2, and copied to PSTATE.UINJ on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [35:34]

Reserved, RES0.

PPEND, bit [33]

## When FEAT\_SEBEP is implemented:

PMUProfiling exception pending bit. Set to the value of PSTATE.PPEND on taking an exception to EL2, and conditionally copied to PSTATE.PPEND on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [32]

Reserved, RES0.

## N, bit [31]

Negative Condition flag. Set to the value of PSTATE.N on taking an exception to EL2, and copied to PSTATE.N on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Z, bit [30]

Zero Condition flag. Set to the value of PSTATE.Z on taking an exception to EL2, and copied to PSTATE.Z on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## C, bit [29]

Carry Condition flag. Set to the value of PSTATE.C on taking an exception to EL2, and copied to PSTATE.C on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## V, bit [28]

Overflow Condition flag. Set to the value of PSTATE.V on taking an exception to EL2, and copied to PSTATE.V on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Q, bit [27]

Overflow or saturation flag. Set to the value of PSTATE.Q on taking an exception to EL2, and copied to PSTATE.Q on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IT, bits [15:10, 26:25]

If-Then. Set to the value of PSTATE.IT on taking an exception to EL2, and copied to PSTATE.IT on executing an exception return operation in EL2.

On executing an exception return operation in EL2, SPSR\_EL2.IT must contain a value that is valid for the instruction being returned to.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## DIT, bit [24]

## When FEAT\_DIT is implemented:

Data Independent Timing. Set to the value of PSTATE.DIT on taking an exception to EL2, and copied to PSTATE.DIT on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SSBS, bit [23]

## When FEAT\_SSBS is implemented:

Speculative Store Bypass. Set to the value of PSTATE.SSBS on taking an exception to EL2, and copied to PSTATE.SSBS on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PAN, bit [22]

## When FEAT\_PAN is implemented:

Privileged Access Never. Set to the value of PSTATE.PAN on taking an exception to EL2, and copied to PSTATE.PAN on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SS, bit [21]

Software Step. Set to the value of PSTATE.SS on taking an exception to EL2, and conditionally copied to PSTATE.SS on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IL, bit [20]

Illegal Execution state. Set to the value of PSTATE.IL on taking an exception to EL2, and copied to PSTATE.IL on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## GE, bits [19:16]

Greater than or Equal flags. Set to the value of PSTATE.GE on taking an exception to EL2, and copied to PSTATE.GE on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## E, bit [9]

Endianness. Set to the value of PSTATE.E on taking an exception to EL2, and copied to PSTATE.E on executing an exception return operation in EL2.

If the implementation does not support big-endian operation, SPSR\_EL2.E is RES0. If the implementation does not support little-endian operation, SPSR\_EL2.E is RES1. On executing an exception return operation in EL2, if the implementation does not support big-endian operation at the Exception level being returned to, SPSR\_EL2.E is RES0, and if the implementation does not support little-endian operation at the Exception level being returned to, SPSR\_EL2.E is RES1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## A, bit [8]

SError exception mask. Set to the value of PSTATE.A on taking an exception to EL2, and copied to PSTATE.A on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## I, bit [7]

IRQ interrupt mask. Set to the value of PSTATE.I on taking an exception to EL2, and copied to PSTATE.I on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [6]

FIQ interrupt mask. Set to the value of PSTATE.F on taking an exception to EL2, and copied to PSTATE.F on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## T, bit [5]

T32 Instruction set state. Set to the value of PSTATE.T on taking an exception to EL2, and copied to PSTATE.T on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[4], bit [4]

Execution state. Set to 0b1 , the value of PSTATE.nRW, on taking an exception to EL2 from AArch32 state, and copied to PSTATE.nRW on executing an exception return operation in EL2.

| M[4]   | Meaning                  |
|--------|--------------------------|
| 0b1    | AArch32 execution state. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[3:0], bits [3:0]

AArch32 Mode. Set to the value of PSTATE.M[3:0] on taking an exception to EL2, and copied to PSTATE.M[3:0] on executing an exception return operation in EL2.

| M[3:0]   | Meaning     |
|----------|-------------|
| 0b0000   | User.       |
| 0b0001   | FIQ.        |
| 0b0010   | IRQ.        |
| 0b0011   | Supervisor. |
| 0b0111   | Abort.      |
| 0b1010   | Hyp.        |
| 0b1011   | Undefined.  |
| 0b1111   | System.     |

Other values are reserved. If SPSR\_EL2.M[3:0] has a Reserved value, or a value for an unimplemented Exception level, executing an exception return operation in EL2 is an illegal return event, as described in 'Illegal return events from AArch64 state'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When exception taken from AArch64 state:

<!-- image -->

An exception return from EL2 using AArch64 makes SPSR\_EL2 become UNKNOWN.

## Bits [63:37]

Reserved, RES0.

## UINJ, bit [36]

## When FEAT\_UINJ is implemented:

Inject Undefined Instruction exception. Set to 0 on taking an exception to EL2, and copied to PSTATE.UINJ on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PACM, bit [35]

## When FEAT\_PAuth\_LR is implemented:

PACM. Set to the value of PSTATE.PACM on taking an exception to EL2, and copied to PSTATE.PACM on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLOCK, bit [34]

## When FEAT\_GCS is implemented:

Exception return state lock. Set to the value of PSTATE.EXLOCK on taking an exception to EL2, and copied to PSTATE.EXLOCK on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PPEND, bit [33]

## When FEAT\_SEBEP is implemented:

PMUProfiling exception pending bit. Set to the value of PSTATE.PPEND on taking an exception to EL2, and conditionally copied to PSTATE.PPEND on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PM, bit [32]

## When FEAT\_EBEP is implemented:

Profiling exception mask bit. Set to the value of PSTATE.PM on taking an exception to EL2, and copied to PSTATE.PM on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## N, bit [31]

Negative Condition flag. Set to the value of PSTATE.N on taking an exception to EL2, and copied to PSTATE.N on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Z, bit [30]

Zero Condition flag. Set to the value of PSTATE.Z on taking an exception to EL2, and copied to PSTATE.Z on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## C, bit [29]

Carry Condition flag. Set to the value of PSTATE.C on taking an exception to EL2, and copied to PSTATE.C on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## V, bit [28]

Overflow Condition flag. Set to the value of PSTATE.V on taking an exception to EL2, and copied to PSTATE.V on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [27:26]

Reserved, RES0.

## TCO, bit [25]

## When FEAT\_MTE is implemented:

Tag Check Override. Set to the value of PSTATE.TCO on taking an exception to EL2, and copied to PSTATE.TCO on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DIT, bit [24]

## When FEAT\_DIT is implemented:

Data Independent Timing. Set to the value of PSTATE.DIT on taking an exception to EL2, and copied to PSTATE.DIT on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## UAO, bit [23]

## When FEAT\_UAO is implemented:

User Access Override. Set to the value of PSTATE.UAO on taking an exception to EL2, and copied to PSTATE.UAO on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PAN, bit [22]

## When FEAT\_PAN is implemented:

Privileged Access Never. Set to the value of PSTATE.PAN on taking an exception to EL2, and copied to PSTATE.PAN on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SS, bit [21]

Software Step. Set to the value of PSTATE.SS on taking an exception to EL2, and conditionally copied to PSTATE.SS on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IL, bit [20]

Illegal Execution state. Set to the value of PSTATE.IL on taking an exception to EL2, and copied to PSTATE.IL on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [19:14]

Reserved, RES0.

## ALLINT, bit [13]

## When FEAT\_NMI is implemented:

All IRQ or FIQ interrupts mask. Set to the value of PSTATE.ALLINT on taking an exception to EL2, and copied to PSTATE.ALLINT on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SSBS, bit [12]

## When FEAT\_SSBS is implemented:

Speculative Store Bypass. Set to the value of PSTATE.SSBS on taking an exception to EL2, and copied to PSTATE.SSBS on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## BTYPE, bits [11:10]

## When FEAT\_BTI is implemented:

Branch Type Indicator. Set to the value of PSTATE.BTYPE on taking an exception to EL2, and copied to PSTATE.BTYPE on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## D, bit [9]

Debug exception mask. Set to the value of PSTATE.D on taking an exception to EL2, and copied to PSTATE.D on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## A, bit [8]

SError exception mask. Set to the value of PSTATE.A on taking an exception to EL2, and copied to PSTATE.A on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## I, bit [7]

IRQ interrupt mask. Set to the value of PSTATE.I on taking an exception to EL2, and copied to PSTATE.I on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [6]

FIQ interrupt mask. Set to the value of PSTATE.F on taking an exception to EL2, and copied to PSTATE.F on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [5]

Reserved, RES0.

## M[4], bit [4]

Execution state. Set to 0b0 , the value of PSTATE.nRW, on taking an exception to EL2 from AArch64 state, and copied to PSTATE.nRW on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[3:0], bits [3:0]

AArch64 Exception level and selected Stack Pointer.

| M[4]   | Meaning                  |
|--------|--------------------------|
| 0b0    | AArch64 execution state. |

| M[3:0]   | Meaning                 |
|----------|-------------------------|
| 0b0000   | EL0.                    |
| 0b0100   | EL1 with SP_EL0 (EL1t). |
| 0b0101   | EL1 with SP_EL1 (EL1h). |
| 0b1000   | EL2 with SP_EL0 (EL2t). |
| 0b1001   | EL2 with SP_EL2 (EL2h). |

Other values are reserved. If SPSR\_EL2.M[3:0] has a Reserved value, or a value for an unimplemented Exception level, executing an exception return operation in EL2 is an illegal return event, as described in 'Illegal return events from AArch64 state'.

The bits in this field are interpreted as follows:

- M[3:2] is set to the value of PSTATE.EL on taking an exception to EL2 and copied to PSTATE.EL on executing an exception return operation in EL2.
- M[1] is unused and is 0 for all non-reserved values.
- M[0] is set to the value of PSTATE.SP on taking an exception to EL2 and copied to PSTATE.SP on executing an exception return operation in EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SPSR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name SPSR\_EL2 or SPSR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED;
```

```
elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = SPSR_EL1; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = SPSR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = SPSR_EL2;
```

MSR SPSR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' && ↪ → EffectiveHCR_EL2_NVx() IN {'xx1'} then EXLOCKException(); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then SPSR_EL1 = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' then EXLOCKException(); else SPSR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then SPSR_EL2 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, SPSR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '011' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x160]; else
```

```
X[t, 64] = SPSR_EL1; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = SPSR_EL2; else X[t, 64] = SPSR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = SPSR_EL1;
```

When FEAT\_VHE is implemented MSR SPSR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' ↪ → && !(EffectiveHCR_EL2_NVx() IN {'x11'}) then EXLOCKException(); elsif EffectiveHCR_EL2_NVx() == '011' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x160] = X[t, 64]; else SPSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' ↪ → && ELIsInHost(EL2) then EXLOCKException(); elsif ELIsInHost(EL2) then SPSR_EL2 = X[t, 64]; else SPSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then SPSR_EL1 = X[t, 64];
```

## C5.2.22 SPSR\_EL3, Saved Program Status Register (EL3)

The SPSR\_EL3 characteristics are:

## Purpose

Holds the saved process state when an exception is taken to EL3.

## Configuration

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPSR\_EL3 are UNDEFINED.

## Attributes

SPSR\_EL3 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented and exception taken from AArch32 state:

<!-- image -->

An exception return from EL3 using AArch64 makes SPSR\_EL3 become UNKNOWN.

## Bits [63:37]

Reserved, RES0.

## UINJ, bit [36]

## When FEAT\_UINJ is implemented:

Inject Undefined Instruction exception. Set to 0 on taking an exception to EL3, and copied to PSTATE.UINJ on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [35:34]

Reserved, RES0.

## PPEND, bit [33]

## When FEAT\_SEBEP is implemented:

PMUProfiling exception pending bit. Set to the value of PSTATE.PPEND on taking an exception to EL3, and conditionally copied to PSTATE.PPEND on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [32]

Reserved, RES0.

## N, bit [31]

Negative Condition flag. Set to the value of PSTATE.N on taking an exception to EL3, and copied to PSTATE.N on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Z, bit [30]

Zero Condition flag. Set to the value of PSTATE.Z on taking an exception to EL3, and copied to PSTATE.Z on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## C, bit [29]

Carry Condition flag. Set to the value of PSTATE.C on taking an exception to EL3, and copied to PSTATE.C on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## V, bit [28]

Overflow Condition flag. Set to the value of PSTATE.V on taking an exception to EL3, and copied to PSTATE.V on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Q, bit [27]

Overflow or saturation flag. Set to the value of PSTATE.Q on taking an exception to EL3, and copied to PSTATE.Q on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IT, bits [15:10, 26:25]

If-Then. Set to the value of PSTATE.IT on taking an exception to EL3, and copied to PSTATE.IT on executing an exception return operation in EL3.

On executing an exception return operation in EL3, SPSR\_EL3.IT must contain a value that is valid for the instruction being returned to.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

DIT, bit [24]

## When FEAT\_DIT is implemented:

Data Independent Timing. Set to the value of PSTATE.DIT on taking an exception to EL3, and copied to PSTATE.DIT on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SSBS, bit [23]

## When FEAT\_SSBS is implemented:

Speculative Store Bypass. Set to the value of PSTATE.SSBS on taking an exception to EL3, and copied to PSTATE.SSBS on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PAN, bit [22]

## When FEAT\_PAN is implemented:

Privileged Access Never. Set to the value of PSTATE.PAN on taking an exception to EL3, and copied to PSTATE.PAN on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SS, bit [21]

Software Step. Set to the value of PSTATE.SS on taking an exception to EL3, and conditionally copied to PSTATE.SS on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IL, bit [20]

Illegal Execution state. Set to the value of PSTATE.IL on taking an exception to EL3, and copied to PSTATE.IL on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## GE, bits [19:16]

Greater than or Equal flags. Set to the value of PSTATE.GE on taking an exception to EL3, and copied to PSTATE.GE on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## E, bit [9]

Endianness. Set to the value of PSTATE.E on taking an exception to EL3, and copied to PSTATE.E on executing an exception return operation in EL3.

If the implementation does not support big-endian operation, SPSR\_EL3.E is RES0. If the implementation does not support little-endian operation, SPSR\_EL3.E is RES1. On executing an exception return operation in EL3, if the implementation does not support big-endian operation at the Exception level being returned to, SPSR\_EL3.E is RES0, and if the implementation does not support little-endian operation at the Exception level being returned to, SPSR\_EL3.E is RES1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## A, bit [8]

SError exception mask. Set to the value of PSTATE.A on taking an exception to EL3, and copied to PSTATE.A on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## I, bit [7]

IRQ interrupt mask. Set to the value of PSTATE.I on taking an exception to EL3, and copied to PSTATE.I on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [6]

FIQ interrupt mask. Set to the value of PSTATE.F on taking an exception to EL3, and copied to PSTATE.F on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## T, bit [5]

T32 Instruction set state. Set to the value of PSTATE.T on taking an exception to EL3, and copied to PSTATE.T on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[4], bit [4]

Execution state. Set to 0b1 , the value of PSTATE.nRW, on taking an exception to EL3 from AArch32 state, and copied to PSTATE.nRW on executing an exception return operation in EL3.

| M[4]   | Meaning                  |
|--------|--------------------------|
| 0b1    | AArch32 execution state. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[3:0], bits [3:0]

AArch32 Mode. Set to the value of PSTATE.M[3:0] on taking an exception to EL3, and copied to PSTATE.M[3:0] on executing an exception return operation in EL3.

| M[3:0]   | Meaning     | Applies when            |
|----------|-------------|-------------------------|
| 0b0000   | User.       |                         |
| 0b0001   | FIQ.        |                         |
| 0b0010   | IRQ.        |                         |
| 0b0011   | Supervisor. |                         |
| 0b0110   | Monitor.    | FEAT_EL3 is implemented |
| 0b0111   | Abort.      |                         |
| 0b1010   | Hyp.        |                         |
| 0b1011   | Undefined.  |                         |
| 0b1111   | System.     |                         |

Other values are reserved. If SPSR\_EL3.M[3:0] has a Reserved value, or a value for an unimplemented Exception level, executing an exception return operation in EL3 is an illegal return event, as described in 'Illegal return events from AArch64 state'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When exception taken from AArch64 state:

<!-- image -->

An exception return from EL3 using AArch64 makes SPSR\_EL3 become UNKNOWN.

## Bits [63:37]

Reserved, RES0.

## UINJ, bit [36]

## When FEAT\_UINJ is implemented:

Inject Undefined Instruction exception. Set to 0 on taking an exception to EL3, and copied to PSTATE.UINJ on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PACM, bit [35]

## When FEAT\_PAuth\_LR is implemented:

PACM. Set to the value of PSTATE.PACM on taking an exception to EL3, and copied to PSTATE.PACM on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLOCK, bit [34]

## When FEAT\_GCS is implemented:

Exception return state lock. Set to the value of PSTATE.EXLOCK on taking an exception to EL3, and copied to PSTATE.EXLOCK on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PPEND, bit [33]

## When FEAT\_SEBEP is implemented:

PMUProfiling exception pending bit. Set to the value of PSTATE.PPEND on taking an exception to EL3, and conditionally copied to PSTATE.PPEND on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PM, bit [32]

## When FEAT\_EBEP is implemented:

Profiling exception mask bit. Set to the value of PSTATE.PM on taking an exception to EL3, and copied to PSTATE.PM on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## N, bit [31]

Negative Condition flag. Set to the value of PSTATE.N on taking an exception to EL3, and copied to PSTATE.N on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Z, bit [30]

Zero Condition flag. Set to the value of PSTATE.Z on taking an exception to EL3, and copied to PSTATE.Z on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## C, bit [29]

Carry Condition flag. Set to the value of PSTATE.C on taking an exception to EL3, and copied to PSTATE.C on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## V, bit [28]

Overflow Condition flag. Set to the value of PSTATE.V on taking an exception to EL3, and copied to PSTATE.V on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [27:26]

Reserved, RES0.

## TCO, bit [25]

## When FEAT\_MTE is implemented:

Tag Check Override. Set to the value of PSTATE.TCO on taking an exception to EL3, and copied to PSTATE.TCO on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DIT, bit [24]

## When FEAT\_DIT is implemented:

Data Independent Timing. Set to the value of PSTATE.DIT on taking an exception to EL3, and copied to PSTATE.DIT on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## UAO, bit [23]

## When FEAT\_UAO is implemented:

User Access Override. Set to the value of PSTATE.UAO on taking an exception to EL3, and copied to PSTATE.UAO on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PAN, bit [22]

## When FEAT\_PAN is implemented:

Privileged Access Never. Set to the value of PSTATE.PAN on taking an exception to EL3, and copied to PSTATE.PAN on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SS, bit [21]

Software Step. Set to the value of PSTATE.SS on taking an exception to EL3, and conditionally copied to PSTATE.SS on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IL, bit [20]

Illegal Execution state. Set to the value of PSTATE.IL on taking an exception to EL3, and copied to PSTATE.IL on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [19:14]

Reserved, RES0.

## ALLINT, bit [13]

## When FEAT\_NMI is implemented:

All IRQ or FIQ interrupts mask. Set to the value of PSTATE.ALLINT on taking an exception to EL3, and copied to PSTATE.ALLINT on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SSBS, bit [12]

## When FEAT\_SSBS is implemented:

Speculative Store Bypass. Set to the value of PSTATE.SSBS on taking an exception to EL3, and copied to PSTATE.SSBS on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## BTYPE, bits [11:10]

## When FEAT\_BTI is implemented:

Branch Type Indicator. Set to the value of PSTATE.BTYPE on taking an exception to EL3, and copied to PSTATE.BTYPE on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## D, bit [9]

Debug exception mask. Set to the value of PSTATE.D on taking an exception to EL3, and copied to PSTATE.D on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## A, bit [8]

SError exception mask. Set to the value of PSTATE.A on taking an exception to EL3, and copied to PSTATE.A on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## I, bit [7]

IRQ interrupt mask. Set to the value of PSTATE.I on taking an exception to EL3, and copied to PSTATE.I on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [6]

FIQ interrupt mask. Set to the value of PSTATE.F on taking an exception to EL3, and copied to PSTATE.F on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [5]

Reserved, RES0.

## M[4], bit [4]

Execution state. Set to 0b0 , the value of PSTATE.nRW, on taking an exception to EL3 from AArch64 state, and copied to PSTATE.nRW on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[3:0], bits [3:0]

AArch64 Exception level and selected Stack Pointer.

| M[3:0]   | Meaning                 | Applies when            |
|----------|-------------------------|-------------------------|
| 0b0000   | EL0.                    |                         |
| 0b0100   | EL1 with SP_EL0 (EL1t). |                         |
| 0b0101   | EL1 with SP_EL1 (EL1h). |                         |
| 0b1000   | EL2 with SP_EL0 (EL2t). |                         |
| 0b1001   | EL2 with SP_EL2 (EL2h). |                         |
| 0b1100   | EL3 with SP_EL0 (EL3t). | FEAT_EL3 is implemented |
| 0b1101   | EL3 with SP_EL3 (EL3h). | FEAT_EL3 is implemented |

Other values are reserved. If SPSR\_EL3.M[3:0] has a Reserved value, or a value for an unimplemented Exception level, executing an exception return operation in EL3 is an illegal return event, as described in 'Illegal return events from AArch64 state'.

The bits in this field are interpreted as follows:

- M[3:2] is set to the value of PSTATE.EL on taking an exception to EL3 and copied to PSTATE.EL on executing an exception return operation in EL3.
- M[1] is unused and is 0 for all non-reserved values.
- M[0] is set to the value of PSTATE.SP on taking an exception to EL3 and copied to PSTATE.SP on executing an exception return operation in EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SPSR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0100 | 0b0000 | 0b000 |

| M[4]   | Meaning                  |
|--------|--------------------------|
| 0b0    | AArch64 execution state. |

```
IsFeatureImplemented(FEAT_AA64)) then
```

```
if !(HaveEL(EL3) && UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = SPSR_EL3;
```

MSR SPSR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0100 | 0b0000 | 0b000 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_GCS) && GetCurrentEXLOCKEN() && !Halted() && PSTATE.EXLOCK == '1' then EXLOCKException(); else SPSR_EL3 = X[t, 64];
```

## C5.2.23 SPSR\_fiq, Saved Program Status Register (FIQ mode)

The SPSR\_fiq characteristics are:

## Purpose

Holds the saved process state when an exception is taken to FIQ mode.

## Configuration

If EL1 only supports execution in AArch64 state, this register is RES0 from EL2 and EL3.

AArch64 System register SPSR\_fiq bits [31:0] are architecturally mapped to AArch32 System register SPSR\_fiq[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to SPSR\_fiq are UNDEFINED.

## Attributes

SPSR\_fiq is a 64-bit register.

## Field descriptions

When FEAT\_AA32EL1 is not implemented:

<!-- image -->

## Bits [63:0]

Reserved, RES0.

## Otherwise:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## N, bit [31]

Negative Condition flag. Set to the value of PSTATE.N on taking an exception to FIQ mode, and copied to PSTATE.N on executing an exception return operation in FIQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Z, bit [30]

Zero Condition flag. Set to the value of PSTATE.Z on taking an exception to FIQ mode, and copied to PSTATE.Z on executing an exception return operation in FIQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## C, bit [29]

Carry Condition flag. Set to the value of PSTATE.C on taking an exception to FIQ mode, and copied to PSTATE.C on executing an exception return operation in FIQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## V, bit [28]

Overflow Condition flag. Set to the value of PSTATE.V on taking an exception to FIQ mode, and copied to PSTATE.V on executing an exception return operation in FIQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Q, bit [27]

Overflow or saturation flag. Set to the value of PSTATE.Q on taking an exception to FIQ mode, and copied to PSTATE.Q on executing an exception return operation in FIQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IT, bits [15:10, 26:25]

If-Then. Set to the value of PSTATE.IT on taking an exception to FIQ mode, and copied to PSTATE.IT on executing an exception return operation in FIQ mode.

On executing an exception return operation in FIQ mode, SPSR\_fiq.IT must contain a value that is valid for the instruction being returned to.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## J, bit [24]

RES0.

In previous versions of the architecture, the {J, T} bits determined the AArch32 Instruction set state.

Armv8 does not support either Jazelle state or T32EE state, and the T bit determines the Instruction set state.

## SSBS, bit [23]

## When FEAT\_SSBS is implemented:

Speculative Store Bypass. Set to the value of PSTATE.SSBS on taking an exception to FIQ mode, and copied to PSTATE.SSBS on executing an exception return operation in FIQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PAN, bit [22]

## When FEAT\_PAN is implemented:

Privileged Access Never. Set to the value of PSTATE.PAN on taking an exception to FIQ mode, and copied to PSTATE.PAN on executing an exception return operation in FIQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DIT, bit [21]

## When FEAT\_DIT is implemented:

Data Independent Timing. Set to the value of PSTATE.DIT on taking an exception to FIQ mode, and copied to PSTATE.DIT on executing an exception return operation in FIQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## IL, bit [20]

Illegal Execution state. Set to the value of PSTATE.IL on taking an exception to FIQ mode, and copied to PSTATE.IL on executing an exception return operation in FIQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## GE, bits [19:16]

Greater than or Equal flags. Set to the value of PSTATE.GE on taking an exception to FIQ mode, and copied to PSTATE.GE on executing an exception return operation in FIQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## E, bit [9]

Endianness. Set to the value of PSTATE.E on taking an exception to FIQ mode, and copied to PSTATE.E on executing an exception return operation in FIQ mode.

If the implementation does not support big-endian operation, SPSR\_fiq.E is RES0. If the implementation does not support little-endian operation, SPSR\_fiq.E is RES1. On executing an exception return operation in FIQ mode, if the implementation does not support big-endian operation at the Exception level being returned to, SPSR\_fiq.E is RES0, and if the implementation does not support little-endian operation at the Exception level being returned to, SPSR\_fiq.E is RES1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## A, bit [8]

SError exception mask. Set to the value of PSTATE.A on taking an exception to FIQ mode, and copied to PSTATE.A on executing an exception return operation in FIQ mode.

The reset behavior of this field is:

## I, bit [7]

IRQ interrupt mask. Set to the value of PSTATE.I on taking an exception to FIQ mode, and copied to PSTATE.I on executing an exception return operation in FIQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [6]

FIQ interrupt mask. Set to the value of PSTATE.F on taking an exception to FIQ mode, and copied to PSTATE.F on executing an exception return operation in FIQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## T, bit [5]

T32 Instruction set state. Set to the value of PSTATE.T on taking an exception to FIQ mode, and copied to PSTATE.T on executing an exception return operation in FIQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[4:0], bits [4:0]

Mode. Set to the value of PSTATE.M[4:0] on taking an exception to FIQ mode, and copied to PSTATE.M[4:0] on executing an exception return operation in FIQ mode.

| M[4:0]   | Meaning     |
|----------|-------------|
| 0b10000  | User.       |
| 0b10001  | FIQ.        |
| 0b10010  | IRQ.        |
| 0b10011  | Supervisor. |
| 0b10111  | Abort.      |
| 0b11011  | Undefined.  |
| 0b11111  | System.     |

Other values are reserved. If SPSR\_fiq.M[4:0] has a Reserved value, or a value for an unimplemented Exception level, executing an exception return operation in FIQ mode is an illegal return event, as described in 'Illegal return events from AArch32 state'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SPSR\_fiq

Accesses to this register use the following encodings in the System register encoding space:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

MRS &lt;Xt&gt;, SPSR\_fiq

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0011 | 0b011 |

if !IsFeatureImplemented(FEAT\_AA64) then

```
UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = SPSR_fiq; elsif PSTATE.EL == EL3 then X[t, 64] = SPSR_fiq;
```

MSR SPSR\_fiq, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0011 | 0b011 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then SPSR_fiq = X[t, 64]; elsif PSTATE.EL == EL3 then SPSR_fiq = X[t, 64];
```

## C5.2.24 SPSR\_irq, Saved Program Status Register (IRQ mode)

The SPSR\_irq characteristics are:

## Purpose

Holds the saved process state when an exception is taken to IRQ mode.

## Configuration

If EL1 only supports execution in AArch64 state, this register is RES0 from EL2 and EL3.

AArch64 System register SPSR\_irq bits [31:0] are architecturally mapped to AArch32 System register SPSR\_irq[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to SPSR\_irq are UNDEFINED.

## Attributes

SPSR\_irq is a 64-bit register.

## Field descriptions

When FEAT\_AA32EL1 is not implemented:

<!-- image -->

## Bits [63:0]

Reserved, RES0.

## Otherwise:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## N, bit [31]

Negative Condition flag. Set to the value of PSTATE.N on taking an exception to IRQ mode, and copied to PSTATE.N on executing an exception return operation in IRQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Z, bit [30]

Zero Condition flag. Set to the value of PSTATE.Z on taking an exception to IRQ mode, and copied to PSTATE.Z on executing an exception return operation in IRQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## C, bit [29]

Carry Condition flag. Set to the value of PSTATE.C on taking an exception to IRQ mode, and copied to PSTATE.C on executing an exception return operation in IRQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## V, bit [28]

Overflow Condition flag. Set to the value of PSTATE.V on taking an exception to IRQ mode, and copied to PSTATE.V on executing an exception return operation in IRQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Q, bit [27]

Overflow or saturation flag. Set to the value of PSTATE.Q on taking an exception to IRQ mode, and copied to PSTATE.Q on executing an exception return operation in IRQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IT, bits [15:10, 26:25]

If-Then. Set to the value of PSTATE.IT on taking an exception to IRQ mode, and copied to PSTATE.IT on executing an exception return operation in IRQ mode.

On executing an exception return operation in IRQ mode, SPSR\_irq.IT must contain a value that is valid for the instruction being returned to.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## J, bit [24]

RES0.

In previous versions of the architecture, the {J, T} bits determined the AArch32 Instruction set state.

Armv8 does not support either Jazelle state or T32EE state, and the T bit determines the Instruction set state.

## SSBS, bit [23]

## When FEAT\_SSBS is implemented:

Speculative Store Bypass. Set to the value of PSTATE.SSBS on taking an exception to IRQ mode, and copied to PSTATE.SSBS on executing an exception return operation in IRQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PAN, bit [22]

## When FEAT\_PAN is implemented:

Privileged Access Never. Set to the value of PSTATE.PAN on taking an exception to IRQ mode, and copied to PSTATE.PAN on executing an exception return operation in IRQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DIT, bit [21]

## When FEAT\_DIT is implemented:

Data Independent Timing. Set to the value of PSTATE.DIT on taking an exception to IRQ mode, and copied to PSTATE.DIT on executing an exception return operation in IRQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## IL, bit [20]

Illegal Execution state. Set to the value of PSTATE.IL on taking an exception to IRQ mode, and copied to PSTATE.IL on executing an exception return operation in IRQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## GE, bits [19:16]

Greater than or Equal flags. Set to the value of PSTATE.GE on taking an exception to IRQ mode, and copied to PSTATE.GE on executing an exception return operation in IRQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## E, bit [9]

Endianness. Set to the value of PSTATE.E on taking an exception to IRQ mode, and copied to PSTATE.E on executing an exception return operation in IRQ mode.

If the implementation does not support big-endian operation, SPSR\_irq.E is RES0. If the implementation does not support little-endian operation, SPSR\_irq.E is RES1. On executing an exception return operation in IRQ mode, if the implementation does not support big-endian operation at the Exception level being returned to, SPSR\_irq.E is RES0, and if the implementation does not support little-endian operation at the Exception level being returned to, SPSR\_irq.E is RES1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## A, bit [8]

SError exception mask. Set to the value of PSTATE.A on taking an exception to IRQ mode, and copied to PSTATE.A on executing an exception return operation in IRQ mode.

The reset behavior of this field is:

## I, bit [7]

IRQ interrupt mask. Set to the value of PSTATE.I on taking an exception to IRQ mode, and copied to PSTATE.I on executing an exception return operation in IRQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [6]

FIQ interrupt mask. Set to the value of PSTATE.F on taking an exception to IRQ mode, and copied to PSTATE.F on executing an exception return operation in IRQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## T, bit [5]

T32 Instruction set state. Set to the value of PSTATE.T on taking an exception to IRQ mode, and copied to PSTATE.T on executing an exception return operation in IRQ mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[4:0], bits [4:0]

Mode. Set to the value of PSTATE.M[4:0] on taking an exception to IRQ mode, and copied to PSTATE.M[4:0] on executing an exception return operation in IRQ mode.

| M[4:0]   | Meaning     |
|----------|-------------|
| 0b10000  | User.       |
| 0b10001  | FIQ.        |
| 0b10010  | IRQ.        |
| 0b10011  | Supervisor. |
| 0b10111  | Abort.      |
| 0b11011  | Undefined.  |
| 0b11111  | System.     |

Other values are reserved. If SPSR\_irq.M[4:0] has a Reserved value, or a value for an unimplemented Exception level, executing an exception return operation in IRQ mode is an illegal return event, as described in 'Illegal return events from AArch32 state'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SPSR\_irq

Accesses to this register use the following encodings in the System register encoding space:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

MRS &lt;Xt&gt;, SPSR\_irq

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0011 | 0b000 |

if !IsFeatureImplemented(FEAT\_AA64) then

```
UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = SPSR_irq; elsif PSTATE.EL == EL3 then X[t, 64] = SPSR_irq;
```

MSR SPSR\_irq, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then SPSR_irq = X[t, 64]; elsif PSTATE.EL == EL3 then SPSR_irq = X[t, 64];
```

## C5.2.25 SPSR\_und, Saved Program Status Register (Undefined mode)

The SPSR\_und characteristics are:

## Purpose

Holds the saved process state when an exception is taken to Undefined mode.

## Configuration

If EL1 only supports execution in AArch64 state, this register is RES0 from EL2 and EL3.

AArch64 System register SPSR\_und bits [31:0] are architecturally mapped to AArch32 System register SPSR\_und[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to SPSR\_und are UNDEFINED.

## Attributes

SPSR\_und is a 64-bit register.

## Field descriptions

When FEAT\_AA32EL1 is not implemented:

<!-- image -->

## Bits [63:0]

Reserved, RES0.

## Otherwise:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## N, bit [31]

Negative Condition flag. Set to the value of PSTATE.N on taking an exception to Undefined mode, and copied to PSTATE.N on executing an exception return operation in Undefined mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Z, bit [30]

Zero Condition flag. Set to the value of PSTATE.Z on taking an exception to Undefined mode, and copied to PSTATE.Z on executing an exception return operation in Undefined mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## C, bit [29]

Carry Condition flag. Set to the value of PSTATE.C on taking an exception to Undefined mode, and copied to PSTATE.C on executing an exception return operation in Undefined mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## V, bit [28]

Overflow Condition flag. Set to the value of PSTATE.V on taking an exception to Undefined mode, and copied to PSTATE.V on executing an exception return operation in Undefined mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Q, bit [27]

Overflow or saturation flag. Set to the value of PSTATE.Q on taking an exception to Undefined mode, and copied to PSTATE.Q on executing an exception return operation in Undefined mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IT, bits [15:10, 26:25]

If-Then. Set to the value of PSTATE.IT on taking an exception to Undefined mode, and copied to PSTATE.IT on executing an exception return operation in Undefined mode.

On executing an exception return operation in Undefined mode, SPSR\_und.IT must contain a value that is valid for the instruction being returned to.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## J, bit [24]

RES0.

In previous versions of the architecture, the {J, T} bits determined the AArch32 Instruction set state.

Armv8 does not support either Jazelle state or T32EE state, and the T bit determines the Instruction set state.

## SSBS, bit [23]

## When FEAT\_SSBS is implemented:

Speculative Store Bypass. Set to the value of PSTATE.SSBS on taking an exception to Undefined mode, and copied to PSTATE.SSBS on executing an exception return operation in Undefined mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PAN, bit [22]

## When FEAT\_PAN is implemented:

Privileged Access Never. Set to the value of PSTATE.PAN on taking an exception to Undefined mode, and copied to PSTATE.PAN on executing an exception return operation in Undefined mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DIT, bit [21]

## When FEAT\_DIT is implemented:

Data Independent Timing. Set to the value of PSTATE.DIT on taking an exception to Undefined mode, and copied to PSTATE.DIT on executing an exception return operation in Undefined mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## IL, bit [20]

Illegal Execution state. Set to the value of PSTATE.IL on taking an exception to Undefined mode, and copied to PSTATE.IL on executing an exception return operation in Undefined mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## GE, bits [19:16]

Greater than or Equal flags. Set to the value of PSTATE.GE on taking an exception to Undefined mode, and copied to PSTATE.GE on executing an exception return operation in Undefined mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## E, bit [9]

Endianness. Set to the value of PSTATE.E on taking an exception to Undefined mode, and copied to PSTATE.E on executing an exception return operation in Undefined mode.

If the implementation does not support big-endian operation, SPSR\_und.E is RES0. If the implementation does not support little-endian operation, SPSR\_und.E is RES1. On executing an exception return operation in Undefined mode, if the implementation does not support big-endian operation at the Exception level being returned to, SPSR\_und.E is RES0, and if the implementation does not support little-endian operation at the Exception level being returned to, SPSR\_und.E is RES1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## A, bit [8]

SError exception mask. Set to the value of PSTATE.A on taking an exception to Undefined mode, and copied to PSTATE.A on executing an exception return operation in Undefined mode.

The reset behavior of this field is:

## I, bit [7]

IRQ interrupt mask. Set to the value of PSTATE.I on taking an exception to Undefined mode, and copied to PSTATE.I on executing an exception return operation in Undefined mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [6]

FIQ interrupt mask. Set to the value of PSTATE.F on taking an exception to Undefined mode, and copied to PSTATE.F on executing an exception return operation in Undefined mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## T, bit [5]

T32 Instruction set state. Set to the value of PSTATE.T on taking an exception to Undefined mode, and copied to PSTATE.T on executing an exception return operation in Undefined mode.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[4:0], bits [4:0]

Mode. Set to the value of PSTATE.M[4:0] on taking an exception to Undefined mode, and copied to PSTATE.M[4:0] on executing an exception return operation in Undefined mode.

| M[4:0]   | Meaning     |
|----------|-------------|
| 0b10000  | User.       |
| 0b10001  | FIQ.        |
| 0b10010  | IRQ.        |
| 0b10011  | Supervisor. |
| 0b10111  | Abort.      |
| 0b11011  | Undefined.  |
| 0b11111  | System.     |

Other values are reserved. If SPSR\_und.M[4:0] has a Reserved value, or a value for an unimplemented Exception level, executing an exception return operation in Undefined mode is an illegal return event, as described in 'Illegal return events from AArch32 state'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SPSR\_und

Accesses to this register use the following encodings in the System register encoding space:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

MRS &lt;Xt&gt;, SPSR\_und

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = SPSR_und; elsif PSTATE.EL == EL3 then X[t, 64] = SPSR_und;
```

MSR SPSR\_und, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0100 | 0b0011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then SPSR_und = X[t, 64]; elsif PSTATE.EL == EL3 then SPSR_und = X[t, 64];
```

## C5.2.26 SSBS, Speculative Store Bypass Safe

The SSBS characteristics are:

## Purpose

Allows access to the Speculative Store Bypass Safe bit.

## Configuration

This register is present only when FEAT\_SSBS2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SSBS are UNDEFINED.

## Attributes

SSBS is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:13]

Reserved, RES0.

## SSBS, bit [12]

Speculative Store Bypass Safe.

Prohibits speculative loads or stores which might practically allow a cache timing side channel.

Aspeculative value in a register is used in a potentially speculatively exploitable manner if it is used to form an address, generate condition codes, or generate SVE predicate values to be used by other instructions in the speculative sequence or if the execution timing of any other instructions in the speculative sequence is a function of the data loaded under speculation.

| SSBS   | Meaning                                                                                                                                                                                                                                                                                                                                                     |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Hardware is not permitted to use speculative register values in a potentially speculatively exploitable manner if the speculative read that loads the register is from earlier in the coherence order than the entry generated by the latest store to that location using the same virtual address as the load instruction.                                 |
| 0b1    | When the value of PSTATE.SSBS is 1, hardware is permitted to use speculative register values in a potentially speculatively exploitable manner if the speculative read that loads the register is from earlier in the coherence order than the entry generated by the latest store to that location using the same virtual address as the load instruction. |

The value of this bit is set to the value in the SCTLR\_ELx.DSSBS field on taking an exception to ELx.

The reset behavior of this field is:

· On a Warm reset, this field resets to an IMPLEMENTATION DEFINED value.

## Bits [11:0]

Reserved, RES0.

## Accessing SSBS

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SSBS

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0010 | 0b110 |

elsif PSTATE.EL == EL0 then

X[t, 64] = Zeros(51):PSTATE.SSBS:Zeros(12);

elsif PSTATE.EL == EL1 then

X[t, 64] = Zeros(51):PSTATE.SSBS:Zeros(12);

elsif PSTATE.EL == EL2 then

X[t, 64] = Zeros(51):PSTATE.SSBS:Zeros(12);

elsif

PSTATE.EL == EL3

then

X[t, 64] = Zeros(51):PSTATE.SSBS:Zeros(12);

MSR SSBS, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0010 | 0b110 |

UNDEFINED; elsif PSTATE.EL == EL0 then PSTATE.SSBS = X[t, 64]&lt;12&gt;; elsif PSTATE.EL == EL1 then PSTATE.SSBS = X[t, 64]&lt;12&gt;; elsif PSTATE.EL == EL2 then PSTATE.SSBS = X[t, 64]&lt;12&gt;; elsif PSTATE.EL == EL3 then PSTATE.SSBS = X[t, 64]&lt;12&gt;;

MSR SSBS, #&lt;imm&gt;

| op0   | op1   | CRn    | op2   |
|-------|-------|--------|-------|
| 0b00  | 0b011 | 0b0100 | 0b001 |

## C5.2.27 SVCR, Streaming Vector Control Register

The SVCR characteristics are:

## Purpose

Allows access to the Streaming SVE mode in PSTATE.SM, and the SME storage enable in PSTATE.ZA.

## Configuration

This register is present only when FEAT\_SME is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SVCR are UNDEFINED.

## Attributes

SVCR is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32    |
|------|-------|
| RES0 |       |
| RES0 | ZA SM |

## Bits [63:2]

Reserved, RES0.

## ZA, bit [1]

Access to PSTATE.ZA, SME storage enable.

When this storage is disabled, execution of an instruction which can access it is trapped. The exception is reported using an ESR\_ELx.{EC, SMTC} value of { 0x1D , 0x3 }.

The possible values of this bit are:

| ZA   | Meaning                                                                                                                                                                                        |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | SMEZAstorage and, if implemented, ZT0 storage are invalid and not accessible. This control causes execution at any Exception level of instructions that can access this storage to be trapped. |
| 0b1  | SMEZAstorage and, if implemented, ZT0 storage are valid and accessible. This control does not cause execution of any instructions to be trapped.                                               |

When a write to SVCR.ZA changes the value of PSTATE.ZA from 0 to 1, all implemented bits of the storage are set to zero.

Changes to this field do not have an effect on the SVE vector and predicate registers and FPSR.

Adirect or indirect read of ZA appears to occur in program order relative to a direct write of SVCR, and to MSR SVCRZA and MSR SVCRSMZA instructions, without the need for explicit synchronization.

The reset behavior of this field is:

· On a Warm reset, PSTATE.ZA resets to '0'.

## SM, bit [0]

Access to PSTATE.SM, Streaming SVE mode.

When the PE is in Streaming SVE mode, the Streaming SVE vector length (SVL) applies to SVE instructions, and execution at any Exception level of an instruction which is illegal in that mode is trapped. The exception is reported using an ESR\_ELx.{EC, SMTC} value of { 0x1D , 0x1 }.

When the PE is not in Streaming SVE mode, the SVE vector length (VL) applies to SVE instructions, and execution at any Exception level of an instruction which is only legal in that mode is trapped. The exception is reported using an ESR\_ELx.{EC, SMTC} value of { 0x1D , 0x2 }.

The possible values of this bit are:

| SM   | Meaning                              |
|------|--------------------------------------|
| 0b0  | The PE is not in Streaming SVE mode. |
| 0b1  | The PE is in Streaming SVE mode.     |

When a write to SVCR.SM changes the value of PSTATE.SM, the following applies:

- When changed from 0 to 1, an entry to Streaming SVE mode is performed.
- When changed from 1 to 0, an exit from Streaming SVE mode is performed.
- All implemented bits of the SVE registers Z0-Z31, P0-P15, and FFR in the new mode are set to zero.
- All bits in FPMR are set to zero.
- FPSR in the new mode is set to 0x0000 \_0000\_0800\_009f, in which all cumulative status bits are set to 1.

Changes to this field do not have an effect on SME ZA storage or, if implemented, ZT0 storage.

Adirect or indirect read of SM appears to occur in program order relative to a direct write of SVCR, and to MSR SVCRSM and MSR SVCRSMZA instructions, without the need for explicit synchronization.

The reset behavior of this field is:

- On a Warm reset, PSTATE.SM resets to '0'.

## Accessing SVCR

SVCR is read/write and can be accessed from any Exception level.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SVCR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0010 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SME) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED; elsif !ELIsInHost(EL0) && CPACR_EL1.SMEN != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x1D); else AArch64.SystemAccessTrap(EL1, 0x1D); elsif ELIsInHost(EL0) && CPTR_EL2.SMEN != '11' then
```

```
AArch64.SystemAccessTrap(EL2, 0x1D); elsif ELIsInHost(EL2) && CPTR_EL2.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x1D); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TSM == '1' then AArch64.SystemAccessTrap(EL2, 0x1D); elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x1D); else X[t, 64] = SVCR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED; elsif CPACR_EL1.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL1, 0x1D); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TSM == '1' then AArch64.SystemAccessTrap(EL2, 0x1D); elsif ELIsInHost(EL2) && CPTR_EL2.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x1D); elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x1D); else X[t, 64] = SVCR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED; elsif !ELIsInHost(EL2) && CPTR_EL2.TSM == '1' then AArch64.SystemAccessTrap(EL2, 0x1D); elsif ELIsInHost(EL2) && CPTR_EL2.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x1D); elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x1D); else X[t, 64] = SVCR; elsif PSTATE.EL == EL3 then if CPTR_EL3.ESM == '0' then AArch64.SystemAccessTrap(EL3, 0x1D); else X[t, 64] = SVCR;
```

MSR SVCR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0010 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SME) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED; elsif !ELIsInHost(EL0) && CPACR_EL1.SMEN != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x1D); else AArch64.SystemAccessTrap(EL1, 0x1D); elsif ELIsInHost(EL0) && CPTR_EL2.SMEN != '11' then AArch64.SystemAccessTrap(EL2, 0x1D); elsif ELIsInHost(EL2) && CPTR_EL2.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x1D); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TSM == '1' then AArch64.SystemAccessTrap(EL2, 0x1D); elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x1D); else SVCR = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED; elsif CPACR_EL1.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL1, 0x1D); elsif EL2Enabled() && !ELIsInHost(EL2) && CPTR_EL2.TSM == '1' then AArch64.SystemAccessTrap(EL2, 0x1D); elsif ELIsInHost(EL2) && CPTR_EL2.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x1D); elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x1D); else SVCR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED; elsif !ELIsInHost(EL2) && CPTR_EL2.TSM == '1' then AArch64.SystemAccessTrap(EL2, 0x1D); elsif ELIsInHost(EL2) && CPTR_EL2.SMEN IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x1D); elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x1D); else SVCR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.ESM == '0' then AArch64.SystemAccessTrap(EL3, 0x1D); else SVCR = X[t, 64];
```

MSR SVCRSM, #&lt;imm&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b00  | 0b011 | 0b0100 | 0b001x | 0b011 |

MSR SVCRZA, #&lt;imm&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b00  | 0b011 | 0b0100 | 0b010x | 0b011 |

MSR SVCRSMZA, #&lt;imm&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b00  | 0b011 | 0b0100 | 0b011x | 0b011 |

## C5.2.28 TCO, Tag Check Override

The TCO characteristics are:

## Purpose

When FEAT\_MTE is implemented, this register allows tag checks to be disabled globally.

When FEAT\_MTE2 is not implemented, it is IMPLEMENTATION DEFINED if accesses to this register access PSTATE.TCO or are RAZ/WI.

## Configuration

This register is present only when FEAT\_MTE is implemented. Otherwise, direct accesses to TCO are UNDEFINED.

## Attributes

TCOis a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |          |      | 32   |
|------|----------|------|------|
| 31   | 26 25 24 |      | 0    |
| RES0 | TCO      | RES0 |      |

## Bits [63:26]

Reserved, RES0.

## TCO, bit [25]

Allows memory tag checks to be globally disabled.

| TCO   | Meaning                                            |
|-------|----------------------------------------------------|
| 0b0   | Loads and Stores are not affected by this control. |
| 0b1   | Loads and Stores are unchecked.                    |

## Bits [24:0]

Reserved, RES0.

## Accessing TCO

For information about the operation of the MSR (immediate) accessor, see MSR (immediate).

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TCO

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0010 | 0b111 |

if !IsFeatureImplemented(FEAT\_MTE) then UNDEFINED; elsif PSTATE.EL == EL0 then X[t, 64] = Zeros(38):PSTATE.TCO:Zeros(25); elsif PSTATE.EL == EL1 then X[t, 64] = Zeros(38):PSTATE.TCO:Zeros(25); elsif PSTATE.EL == EL2 then X[t, 64] = Zeros(38):PSTATE.TCO:Zeros(25); elsif PSTATE.EL == EL3 then X[t, 64] = Zeros(38):PSTATE.TCO:Zeros(25);

MSR TCO, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0010 | 0b111 |

if !IsFeatureImplemented(FEAT\_MTE) then UNDEFINED; elsif PSTATE.EL == EL0 then PSTATE.TCO = X[t, 64]&lt;25&gt;; elsif PSTATE.EL == EL1 then PSTATE.TCO = X[t, 64]&lt;25&gt;; elsif PSTATE.EL == EL2 then PSTATE.TCO = X[t, 64]&lt;25&gt;; elsif PSTATE.EL == EL3 then PSTATE.TCO = X[t, 64]&lt;25&gt;;

MSR TCO, #&lt;imm&gt;

| op0   | op1   | CRn    | op2   |
|-------|-------|--------|-------|
| 0b00  | 0b011 | 0b0100 | 0b100 |

## C5.2.29 UAO, User Access Override

The UAO characteristics are:

## Purpose

Allows access to the User Access Override bit.

## Configuration

This register is present only when FEAT\_UAO is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to UAO are UNDEFINED.

## Attributes

UAOis a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:24]

Reserved, RES0.

## UAO, bit [23]

User Access Override.

| UAO   | Meaning                                                                                                                      |
|-------|------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Explicit Memory Effects generated by unprivileged memory access instructions and described as unprivileged are unprivileged. |
| 0b1   | Explicit Memory Effects generated by unprivileged memory access instructions and described as unprivileged are privileged.   |

The Effective value of PSTATE.UAO is 0 when execution is at EL0.

The Effective value of PSTATE.UAO is 1 when any of the following is true:

- Execution is at EL1, and HCR\_EL2.{NV, NV1} is {1, 1}.
- Execution is at EL2, and the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.
- Execution is at EL3.

## Bits [22:0]

Reserved, RES0.

## Accessing UAO

For more information about the operation of the MSR (immediate) accessor, see 'MSR (immediate)'.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, UAO

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0010 | 0b100 |

if !(IsFeatureImplemented(FEAT\_UAO) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

X[t, 64] = Zeros(40):PSTATE.UAO:Zeros(23);

elsif PSTATE.EL == EL2 then

X[t, 64] = Zeros(40):PSTATE.UAO:Zeros(23);

elsif PSTATE.EL == EL3 then

X[t, 64] =

Zeros(40):PSTATE.UAO:Zeros(23);

MSR UAO, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0100 | 0b0010 | 0b100 |

if !(IsFeatureImplemented(FEAT\_UAO) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

PSTATE.UAO = X[t, 64]&lt;23&gt;;

elsif PSTATE.EL == EL2 then

PSTATE.UAO = X[t, 64]&lt;23&gt;;

elsif PSTATE.EL == EL3 then

PSTATE.UAO = X[t, 64]&lt;23&gt;;

MSR UAO, #&lt;imm&gt;

| op0   | op1   | CRn    | op2   |
|-------|-------|--------|-------|
| 0b00  | 0b000 | 0b0100 | 0b011 |