## K7.1 Legacy Instruction Syntax

Early versions of the Arm Architecture defined an assembly language for A32 (ARM) instructions, and a separate assembly language for T32 (Thumb) instructions. UAL is based on the A32 assembly language, with some changes to the instruction syntax. The appendix describes those changes. The pre-UAL mnemonics are compatible with UAL, and might be supported by an assembler.

The original T32 assembly language is not compatible with UAL, and is not described in the manual.

## K7.1.1 Pre-UAL instruction syntax for the A32 base instructions

Table K7-1 lists the syntax for the A32 base instructions that have changed after UAL was introduced.

Table K7-1 Pre-UAL instruction syntax for the A32 base instructions

| Pre-UAL syntax      | UAL equivalent   | See                                                                                                                                        |
|---------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ADC<c>S             | ADCS<c>          | ADC, ADCS(immediate), ADC, ADCS(register), ADC, ADCS(register-shifted register)                                                            |
| ADD<c>S             | ADDS<c>          | ADD, ADDS(immediate), ADD, ADDS(register), ADD, ADDS(register-shifted register), ADD, ADDS(SP plus immediate), ADD, ADDS(SP plus register) |
| AND<c>S             | ANDS<c>          | AND, ANDS(immediate), AND, ANDS(register), AND, ANDS(register-shifted register)                                                            |
| BIC<c>S             | BICS<c>          | BIC, BICS (immediate), BIC, BICS (register), BIC, BICS (register-shifted register)                                                         |
| EOR<c>S             | EORS<c>          | EOR, EORS (immediate), EOR, EORS (register), EOR, EORS (register-shifted register)                                                         |
| LDC<c>L             | LDCL<c>          | LDC(immediate), LDC(literal)                                                                                                               |
| LDM<c>IA , LDM<c>FD | LDM<c>           | LDM, LDMIA,LDMFD                                                                                                                           |
| LDM<c>DA , LDM<c>FA | LDMDA<c>         | LDMDA,LDMFA                                                                                                                                |
| LDM<c>DB , LDM<c>EA | LDMDB<c>         | LDMDB,LDMEA                                                                                                                                |
| LDM<c>IB , LDM<c>ED | LDMIB<c>         | LDMIB,LDMED                                                                                                                                |
| LDR<c>B             | LDRB<c>          | LDRB(immediate), LDRB(literal), LDRB(register)                                                                                             |
| LDR<c>BT            | LDRBT<c>         | LDRBT                                                                                                                                      |
| LDR<c>D             | LDRD<c>          | LDRD(immediate), LDRD(literal), LDRD(register)                                                                                             |
| LDR<c>H             | LDRH<c>          | LDRH(immediate), LDRH(literal), LDRH(register)                                                                                             |

| Pre-UAL syntax        | UAL equivalent   | See                                                                                |
|-----------------------|------------------|------------------------------------------------------------------------------------|
| LDR<c>SB              | LDRSB<c>         | LDRSB (immediate). LDRSB (literal), LDRSB (register)                               |
| LDR<c>SH              | LDRSH<c>         | LDRSH (immediate), LDRSH (literal), LDRSH (register)                               |
| LDR<c>T               | LDRT<c>          | LDRT                                                                               |
| MLA<c>S               | MLAS<c>          | MLA,MLAS                                                                           |
| LSLS <Rd> , <Rn> , #0 | MOVS <Rd> , <Rm> | MOV, MOVS(immediate),                                                              |
| MOV<c>S               | MOVS<c>          | MOV, MOVS(register)                                                                |
| MUL<c>S               | MULS<c>          | MUL,MULS                                                                           |
| MVN<c>S               | MVNS<c>          | MVN, MVNS(immediate), MVN, MVNS(register), MVN, MVNS(register-shifted register)    |
| ORR<c>S               | ORRS<C>          | ORR, ORRS (immediate), ORR, ORRS (register), ORR, ORRS (register-shifted register) |
| QADDSUBX              | QASX             | QASX                                                                               |
| QSUBADDX              | QSAX             | QSAX                                                                               |
| RSB<c>S               | RSBS<c>          | RSB, RSBS (immediate), RSB, RSBS (register), RSB, RSBS (register-shifted register) |
| RSC<c>S               | RSCS<c>          | RSC, RSCS (immediate), RSC, RSCS (register), RSC, RSCS (register-shifted register) |
| SADDSUBX              | SASX             | SASX                                                                               |
| SBC<c>S               | SBCS<c>          | SBC, SBCS (immediate), SBC, SBCS (register), SBC, SBCS (register-shifted register) |
| SHADDSUBX             | SHASX            | SHASX                                                                              |
| SHSUBADDX             | SHSAX            | SHSAX                                                                              |
| SMI<c>                | SMC<c>           | SMC                                                                                |
| SMLAL<c>S             | SMLALS<c>        | SMLAL, SMLALS                                                                      |
| SMULL<c>S             | SMULLS<c>        | SMULL, SMULLS                                                                      |
| SSUBADDX<c>           | SSAX<c>          | SSAX                                                                               |
| STC<c>L               | STCL<c>          | STC                                                                                |
| STM<c>EA , STM<c>IA   | STM<c>           | STM, STMIA,STMEA                                                                   |
| STM<c>DA , STM<c>ED   | STMDA<c>         | STMDA,STMED                                                                        |
| STM<c>DB , STM<c>FD   | STMDB<c>         | STMDB,STMFD                                                                        |
| STM<c>IB , STM<c>FA   | STMIB<c>         | STMIB, STMFA                                                                       |
| STR<c>B               | STRB<c>          | STRB (immediate), STRB (register)                                                  |
| STR<c>BT              | STRBT<c>         | STRBT                                                                              |
| STR<c>D               | STRD<c>          | STRD (immediate), STRD (register)                                                  |

| Pre-UAL syntax   | UAL equivalent   | See                                                                                                                                               |
|------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| STR<c>H          | STRH<c>          | STRH (immediate), STRH (register)                                                                                                                 |
| STR<c>T          | STRT<c>          | STRT                                                                                                                                              |
| SUB<c>S          | SUBS<c>          | SUB, SUBS (immediate), SUB, SUBS (register), SUB, SUBS (register-shifted register), SUB, SUBS (SP minus immediate), SUB, SUBS (SP minus register) |
| SWI              | SVC              | SVC                                                                                                                                               |
| UADDSUBX         | UASX             | UASX                                                                                                                                              |
| UHADDSUBX        | UHASX            | UHASX                                                                                                                                             |
| UHSUBADDX        | UHSAX            | UHSAX                                                                                                                                             |
| UMLAL<c>S        | UMLALS<c>        | UMLAL,UMLALS                                                                                                                                      |
| UMULL<c>S        | UMULLS<c>        | UMULL,UMULLS                                                                                                                                      |
| UQADDSUBX        | UQASX            | UQASX                                                                                                                                             |
| UQSUBADDX        | UQSAX            | UQSAX                                                                                                                                             |
| USUBADDX         | USAX             | USAX                                                                                                                                              |
| UEXT8            | UXTB             | UXTB                                                                                                                                              |
| UEXT16           | UXTH             | UXTH                                                                                                                                              |

## K7.1.2 Pre-UAL instruction syntax for the A32 floating-point instructions

Table K7-2 lists the syntax for A32 floating-point instructions that have changed after UAL was introduced.

Table K7-2 Pre-UAL instruction syntax for A32 floating-point instructions

| Pre-UAL syntax        | UAL equivalent          | See                                                 |
|-----------------------|-------------------------|-----------------------------------------------------|
| FABSD                 | VABS.F64                | VABS                                                |
| FABSS                 | VABS.F32                |                                                     |
| FADDD                 | VADD.F64                | VADD(floating-point)                                |
| FADDS                 | VADD.F32                |                                                     |
| FCMPEZD               | VCMPE.F64               | VCMPE                                               |
| FCMPEZS               | VCMPE.F32               |                                                     |
| FCMPZD                | VCMP.F64                | VCMP,                                               |
| FCMPZS                | VCMP.F32                |                                                     |
| FCONSTD <Dd>, #<imm8> | VMOV.F64 <Dd>, #<fpimm> | VMOV(immediate) For more information, see FCONST.   |
| FCONSTS <Sd>, #<imm8> | VMOV.F32 <Sd>, #<fpimm> |                                                     |
| FCPYD                 | VMOV.F64                | VMOV(register)                                      |
| FCPYS                 | VMOV.F32                |                                                     |
| FCVTDS                | VCVT.F64.F32            | VCVT(between double-precision and single-precision) |

| Pre-UAL syntax   | UAL equivalent        | See                                                                                  |
|------------------|-----------------------|--------------------------------------------------------------------------------------|
| FCVTSD           | VCVT.F32.F64          |                                                                                      |
| FDIVD            | VDIV.F64              | VDIV                                                                                 |
| FDIVS            | VDIV.F32              |                                                                                      |
| FLDD             | VLDR.F64              | VLDR(immediate) VLDR(literal)                                                        |
| FLDMD , FLDMIAD  | VLDM.F64              | VLDM,VLDMDB,VLDMIA                                                                   |
| FLDMS            | VLDM.F32              |                                                                                      |
| FLDS             | VLDR.F32              | VLDR(immediate) VLDR(literal)                                                        |
| FMACD            | VMLA.F64              | VMLA(floating-point)                                                                 |
| FMACS            | VMLA.F32              |                                                                                      |
| FMDHR <Dd>, <Rt> | VMOV <Dd[1]>, <Rt>    | VMOV(general-purpose register to scalar)                                             |
| FMDLR <Dd>, <Rt> | VMOV <Dd[0]>, <Rt>    |                                                                                      |
| FMDRR            | VMOV                  | VMOV(between two general-purpose registers and a doubleword floating-point register) |
| FMRDH <Rt>, <Dd> | VMOV <Rt>, <Dd[1]>    | VMOV(scalar to general-purpose register)                                             |
| FMRDL <Rt>, <Dd> | VMOV <Rt>, <Dd[0]>    |                                                                                      |
| FMRRD            | VMOV                  | VMOV(between two general-purpose registers and a doubleword floating-point register) |
| FMRRS            | VMOV                  | VMOV(between two general-purpose registers and two single-precision registers)       |
| FMRS             | VMOV                  | VMOV(between general-purpose register and single-precision)                          |
| FMRX             | VMRS                  | VMRS                                                                                 |
| FMSCD            | VNMLS.F64             | VNMLS                                                                                |
| FMSCS            | VNMLS.F32             |                                                                                      |
| FMSR             | VMOV                  | VMOV(between general-purpose register and single-precision)                          |
| FMSRR            | VMOV                  | VMOV(between two general-purpose registers and two single-precision registers)       |
| FMSTAT           | VMRS APSR_nzcv, FPSCR | VMRS                                                                                 |
| FMULD            | VMUL.F64              | VMUL(floating-point)                                                                 |
| FMULS            | VMUL.F32              |                                                                                      |
| FMXR             | VMSR                  | VMSR                                                                                 |
| FNEGD            | VNEG.F64              | VNEG                                                                                 |
| FNEGS            | VNEG.F32              |                                                                                      |
| FNMACD           | VMLS.F64              | VNMLS                                                                                |
| FNMACS           | VMLS.F32              |                                                                                      |
| FNMSCD           | VNMLA.F64             | VNMLA                                                                                |
| FNMSCS           | VNMLA.F32             |                                                                                      |
| FNMULD           | VNMUL.F64             | VNMUL                                                                                |
| FNMULS           | VNMUL.F32             |                                                                                      |
| FSHTOD           | VCVT.F64.S16          | VCVT(between floating-point and fixed-point, floating-point)                         |
| FSHTOS           | VCVT.F32.S16          |                                                                                      |
| FSITOD           | VCVT.F64.S32          | VCVT(between floating-point and integer, Advanced SIMD),VCVTR                        |

| Pre-UAL syntax   | UAL equivalent   | See                                                          |
|------------------|------------------|--------------------------------------------------------------|
| FSITOS           | VCVT.F32.S32     |                                                              |
| FSLTOD           | VCVT.F64.S32     | VCVT(between floating-point and fixed-point, floating-point) |
| FSLTOS           | VCVT.F32.S32     |                                                              |
| FSQRTD           | VSQRT.F64        | VSQRT                                                        |
| FSQRTS           | VSQRT.F32        |                                                              |
| FSTD             | VSTR             | VSTR                                                         |
| FSTMD , FSTMIAS  | VSTM.F64         | VSTM, VSTMDB, VSTMIA                                         |
| FSTMS            | VSTM.F32         |                                                              |
| FSTS             | VSTR             | VSTR                                                         |
| FSUBD            | VSUB.F64         | VSUB(floating-point)                                         |
| FSUBS            | VSUB.F32         |                                                              |
| FTOSHD           | VCVT.S16.F64     | VCVT(between floating-point and fixed-point, floating-point) |
| FTOSHS           | VCVT.S16.F23     |                                                              |
| FTOSID           | VCVT.S32.F64     | VCVT(between floating-point and integer, Advanced SIMD)      |
| FTOSIS           | VCVT.S32.F32     |                                                              |
| FTOSIZD          | VCVTR.S32.F64    | VCVTR                                                        |
| FTOSIZS          | VCVTR.S32.F32    |                                                              |
| FTOSLD           | VCVT.S32.F64     | VCVT(between floating-point and fixed-point, floating-point) |
| FTOSLS           | VCVT.S32.F32     |                                                              |
| FTOUHD           | VCVT.U16.F64     |                                                              |
| FTOUHS           | VCVT.U16.F32     |                                                              |
| FTOUID           | VCVT.U32.F64     | VCVT(between floating-point and integer, Advanced SIMD)      |
| FTOUIS           | VCVT.U32.F32     |                                                              |
| FTOUIZD          | VCVTR.U32.F64    | VCVTR                                                        |
| FTOUIZS          | VCVTR.U32.F32    |                                                              |
| FTOULD           | VCVT.U32.F64     | VCVT(between floating-point and fixed-point, floating-point) |
| FTOULS           | VCVT.U32.F32     |                                                              |
| FUHTOD ,         | VCVT.F64.U16     |                                                              |
| FUHTOS           | VCVT.F64.U16     |                                                              |
| FUITOD           | VCVT.F64.U32     | VCVT(between floating-point and integer, Advanced SIMD)      |
| FUITOS           | VCVT.F32.U32     |                                                              |
| FULTOD           | VCVT.F64.U32     | VCVT(between floating-point and fixed-point, floating-point) |
| FULTOS           | VCVT.F32.U32     |                                                              |

## K7.1.3 FCONST

The syntax of FCONST is

FCONST&lt;dest&gt;{&lt;c&gt;} &lt;Fd&gt;, #&lt;imm8&gt;

where:

&lt;dest&gt;

Specifies the destination data type. It must be one of:

S Single-precision floating-point.

D Double-precision floating-point.

&lt;c&gt;

This is an optional field. It specifies the condition under which the instruction is executed. See Conditional execution for the range of available conditions and their encoding. If &lt;c&gt; is omitted, it defaults to always ( AL ).

&lt;Fd&gt; Specifies the destination register. It must be one of:

&lt;Dd&gt; 64-bit name of the SIMD&amp;FP destination register.

&lt;Sd&gt; 32-bit name of the SMID&amp;FP destination register.

&lt;imm8&gt; Specifies the immediate value used to generate the floating-point constant.

FCONSTD{&lt;c&gt;} &lt;Dd&gt;, #&lt;imm8&gt; maps to VMOV.F64 &lt;Dd&gt;, #&lt;fpimm&gt;

FCONSTS{&lt;c&gt;} &lt;Sd&gt;, #&lt;imm8&gt; maps to VMOV.F32 &lt;Sd&gt;, #&lt;fpimm&gt;

## Appendix K8 Address Translation Examples

This appendix gives examples of address translations using the translation regimes described in The AArch64 Virtual Memory System Architecture and The AArch32 Virtual Memory System Architecture. It contains the following sections:

- AArch64 Address translation examples.
- AArch32 Address translation examples.

Note

This chapter gives examples of translation table lookups for the Armv8 address translation stages. It does not define any part of the address translation mechanism. If any information in this appendix appears to contradict the information in The AArch64 Virtual Memory System Architecture or The AArch32 Virtual Memory System Architecture then the information in The AArch64 Virtual Memory System Architecture or The AArch32 Virtual Memory System Architecture must be taken as the definition of the required behavior.