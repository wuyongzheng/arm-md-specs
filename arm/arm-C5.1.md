## C5.1 The System instruction class encoding space

Part of the A64 instruction encoding space is assigned to instructions that access the System register encoding space. These instructions provide:

- Access to System registers , including the debug registers, that provide system control, and system status information.
- Access to Special-purpose registers such as SPSR\_ELx, ELR\_ELx, and the equivalent fields of the Process State.
- The cache and TLB maintenance instructions and address translation instructions.
- Barriers and the CLREX instruction.
- Architectural hint instructions.

This section describes the general model for accessing this functionality.

Note

- See Fixed values in AArch64 instruction and System register descriptions for information about abbreviations used in the System instruction descriptions.
- In AArch32 state much of this functionality is provided through the System register interface described in The AArch32 System register interface. In AArch64 state, the parameters used to characterize the System register encoding space are { op0 , op1 , CRn , CRm , op2 }. These are based on the parameters that characterize the AArch32 System register encoding space, which reflect the original implementation of these registers, as described in Background to the System register interface. There is no particular significance to the naming of these parameters, and no functional distinction between the opn parameters and the CRx parameters.

Principles of the System instruction class encoding describes some general properties of these encodings. System instruction class encoding overview then describes the top-level encoding of these instructions, and the following sections then describe the next level of the encoding hierarchy of System instructions and Special-purpose registers:

- op0 == 0b00 , architectural hints, barriers and CLREX, and PSTATE access.
- op0 == 0b01 , cache maintenance, TLB maintenance, address translation, prediction restriction, BRBE, Trace Extension, and Guarded Control Stack instructions.
- op0 == 0b11 , Moves to and from Special-purpose registers.

For the description of the next level of encoding hierarchy of System registers, see:

- Moves to and from debug and trace System registers.
- Moves to and from non-debug System registers, Special-purpose registers.
- Reserved encodings for IMPLEMENTATION DEFINED registers.

## C5.1.1 Principles of the System instruction class encoding

An encoding in the System instruction space is identified by a set of arguments,{ op0 , op1 , CRn , CRm , op2 }. These form an encoding hierarchy, where:

| op0   | Defines the top-level division of the encoding space, see System instruction class encoding overview.                                                                                                                                                                                                                                                                                        |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| op1   | Identifies the lowest Exception level at which the encoding is accessible, as follows: Accessible at EL0 op1 has the value 0b011 . at EL1 op1 has the value 0b000 , 0b001 , or 0b010 . The value is the same as used to access the equivalent AArch32 register. at Secure EL1 op1 has the value 0b111 . Accessible at EL2 op1 has the value 0b100 or 0b101 . The value 0b101 is used for the |
|       | Accessible the op1 value                                                                                                                                                                                                                                                                                                                                                                     |
|       | Accessible                                                                                                                                                                                                                                                                                                                                                                                   |
|       | EL12 encodings that access EL1 System registers used when FEAT_VHE is implemented and the Effective value of HCR_EL2.E2H is 1.                                                                                                                                                                                                                                                               |

0b10

Accessible at EL3 op1 has the value 0b110 .

Arm strongly recommends that implementers adopt this use of op1 when using the IMPLEMENTATION DEFINED regions of the encoding space described in Reserved encodings for IMPLEMENTATION DEFINED registers.

## C5.1.2 System instruction class encoding overview

The encoding of the System instruction class describes each instruction as being either:

- Atransfer to a System register. This is a System instruction with the semantics of a write.
- Atransfer from a System register. This is a System instruction with the semantics of a read.

ASystem instruction that initiates an operation operates as if it was making a transfer to a register.

In the AArch64 instruction set, the decode structure for the System instruction class is:

| 31 30 29 28 27 26 25 24 23 22 21 20 19 18   | 16 15     | 12 11   | 8 7   | 5 4     | 0   |
|---------------------------------------------|-----------|---------|-------|---------|-----|
| 1 1 0 1 0 1 0 1                             | 0 0 L op0 | op1     | CRn   | CRm op2 | Rt  |

The value of L indicates the transfer direction:

- 0 Transfer to System register.
- 1 Transfer from System register.

The op0 field is the top-level encoding of the System instruction type. Its possible values are:

0b00 These encodings provide:

- Instructions with an immediate field for accessing PSTATE, the current PE state.
- The architectural hint instructions.
- Barriers and the CLREX instruction.

For more information about these encodings, see op0 == 0b00 , architectural hints, barriers and CLREX, and PSTATE access.

0b01 These encodings provide:

- Cache maintenance instructions.
- TLB maintenance instructions.
- Address translation instructions.
- Prediction restriction instructions.
- BRBE instructions.

Note

These are equivalent to operations in the AArch32 ( coproc == 0b1111 ) encoding space.

For more information, see op0 == 0b01 , cache maintenance, TLB maintenance, address translation, prediction restriction, BRBE, Trace Extension, and Guarded Control Stack instructions.

These encodings provide moves to and from:

- Legacy AArch32 System registers for execution environments, to provide access to these registers from higher Exception levels that are using AArch64.
- Debug, PMU, System PMU, and trace registers.

Note

These are equivalent to the registers in the AArch32 ( coproc == 0b1110 ) encoding space.

For more information, see Moves to and from debug and trace System registers.

## 0b11 These encodings provide:

- Moves to and from Non-debug System registers. The accessed registers provide system control, and system status information.

Note

The accessed registers are equivalent to the registers in the AArch32 ( coproc == 0b1111 ) encoding space.

- Access to Special-purpose registers.

For more information, see Instructions for accessing Special-purpose registers and Instructions for accessing non-debug System registers.

## C5.1.2.1 UNDEFINED behaviors

In the System register instruction encoding space, the following principles apply:

- All unallocated encodings are treated as UNDEFINED.
- All encodings with L == 1 and op0 == 0b0x are UNDEFINED, except for encodings in the area reserved for IMPLEMENTATION DEFINED use, see Reserved encoding space for IMPLEMENTATION DEFINED instructions.

For registers and operations that are accessible from a particular Exception level, any attempt to access those registers from a lower Exception level is UNDEFINED.

If a particular Exception level:

- Defines a register to be RO, then any attempt to write to that register, at that Exception level, is UNDEFINED. This means that any access to that register with L == 0 is UNDEFINED.
- Defines a register to be WO, then any attempt to read from that register, at that Exception level, is UNDEFINED. This means that any access to that register with L == 1 is UNDEFINED.

For IMPLEMENTATION DEFINED encoding spaces, the treatment of the encodings is IMPLEMENTATION DEFINED, but see the recommendation in Principles of the System instruction class encoding.

## C5.1.3 op0 == 0b00 , architectural hints, barriers and CLREX , and PSTATE access

The different groups of System register instructions with op0 == 0b00 :

- Are identified by the value of CRn .
- Are always encoded with a value of 0b11111 in the Rt field.

The encoding of these instructions is:

<!-- image -->

The encoding of the CRn field is as follows:

0b0010

See Architectural hint instructions.

0b0011

See Barriers and CLREX.

0b0100

See Instructions for accessing the PSTATE fields.

## C5.1.3.1 Architectural hint instructions

Within the op0==0b00 encodings, the architectural hint instructions are identified by CRn having the value 0b0010 . The encoding of these instructions is:

<!-- image -->

The value of op&lt;6:0&gt; , formed by concatenating the CRm and op2 fields, determines the hint instruction as follows:

```
0b0000000 NOP instruction. 0b0000001 YIELD instruction. 0b0000010 WFE instruction. 0b0000011 WFI instruction. 0b0000100 SEV instruction. 0b0000101 SEVL instruction. 0b0000110 DGH instruction. 0b0000111 XPACD, XPACI, XPACLRI instruction. 0b0001000 PACIA, PACIA1716, PACIASP, PACIAZ, PACIZA instruction, PACIA1716 variant. 0b0001010 PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZB instruction, PACIB1716 variant. 0b0001100 AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIZA instruction, AUTIA1716 variant. 0b0001110 AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZB instruction, AUTIB1716 variant. 0b0010000 ESB instruction. 0b0010001 : PSB instruction. 0b0010010 : TSB instruction. 0b0010100 CSDB instruction. 0b0010110 CLRBHB instruction. 0b0011000 PACIA, PACIA1716, PACIASP, PACIAZ, PACIZA instruction, PACIAZ variant. 0b0011001 PACIA, PACIA1716, PACIASP, PACIAZ, PACIZA instruction, PACIASP variant. 0b0011010 PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZB instruction, PACIBZ variant. 0b0011011 PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZB instruction, PACIBSP variant. 0b0011100 AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIZA instruction, AUTIAZ variant.
```

0b0011101 AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIZA instruction, AUTIASP variant.

0b0011110 AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZB instruction, AUTIBZ variant. 0b0011111 AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZB instruction, AUTIBSP variant. 0b0101000 CHKFEAT instruction. 0b0100xx0 BTI instruction. 0b011000x STSHH instruction.

## These instructions are described in A64 Base Instruction Descriptions.

Note

- Instruction encodings with bits[4:0] not set to 0b11111 are UNDEFINED.
- The operation of the A64 instructions for architectural hints are identical to the corresponding T32 and A32 instructions.

## For more information about:

- The WFE , WFI , SEV , and SEVL instructions, see Mechanisms for entering a low-power state.
- The YIELD instruction, see Software control features and EL0.
- The STSHH instruction, see Use of the FEAT\_PCDPHINT STSHH and PRFM IR (immediate) instructions.

## C5.1.3.2 Barriers and CLREX

Within the op0==0b00 encodings, the barriers and CLREX instructions are identified by CRn having the value 0b0011 . The encoding of these instructions is:

<!-- image -->

## The value of op2 determines the instruction, as follows.

0b001 DSB instruction, Memory nXS barrier variant. 0b010 CLREX instruction. 0b100 DSB instruction, Memory barrier variant. 0b101 DMB instruction. 0b110 ISB instruction. 0b111 SB instruction. 0b000 ; 0b011 UNDEFINED.

These instructions are described in A64 Base Instruction Descriptions.

Note

- Instruction encodings with bits[4:0] not set to 0b11111 are UNDEFINED.
- The operation of the A64 instructions for barriers and CLREX are identical to the corresponding T32 and A32 instructions.

For more information about:

- The barrier instructions, see Memory barriers.
- The CLREX instruction, see Synchronization and semaphores.

## C5.1.3.3 Instructions for accessing the PSTATE fields

Within the op0==0b00 encodings, the instructions that can be used to modify PSTATE fields directly are identified by CRn having the value 0b0100 . The encoding of these instructions is shown in Figure C5-1 and Figure C5-2:

Figure C5-1 Instructions using #Imm4

<!-- image -->

Figure C5-2 Instructions using #Imm1

<!-- image -->

## These instructions are:

```
CFINV ; Inverts the value of PSTATE.C MSR DAIFSet, #Imm4 ; Used to set any or all of DAIF to 1 MSR DAIFClr, #Imm4 ; Used to clear any or all of DAIF to 0 MSR SPSel, #Imm4 ; Used to select the Stack Pointer, between SP_EL0 and SP_ELx MSR UAO, #Imm4 ; Used to set the value of PSTATE.UAO MSR PAN, #Imm4 ; Used to set the value of PSTATE.PAN MSR DIT, #Imm4 ; Used to set the value of PSTATE.DIT MSR SSBS, #Imm4 ; Used to set the value of PSTATE.SSBS MSR TCO, #Imm4 ; Used to set the value of PSTATE.TCO MSR ALLINT, #Imm1 ; Used to set the value of PSTATE.ALLINT
```

The value of op2 selects the instruction form, which defines the constraints on the values of the op1 and Imm4 or Imm1 arguments, as follows:

```
op2 == 0b000 Selects the CFINV instruction. op2 == 0b011 Selects the MSR UAO instruction. op2 == 0b100 Selects the MSR PAN instruction. op2 == 0b101 Selects the MSR SPSel instruction. op2 == 0b001 Selects the MSR SSBS instruction. op2 == 0b010 Selects the MSR DIT instruction. op2 == 0b100 Selects the MSR TCO instruction. op2 == 0b110 Selects the MSR DAIFSet instruction, that sets the specified PSTATE.{D, A, I, F} bits to 1. op2 == 0b111 Selects the MSR DAIFClr instruction, that clears the specified PSTATE.{D, A, I, F} bits to 0. op2 == 0b000 Selects the MSR ALLINT instruction.
```

All other combinations of op1 and op2 are reserved, and the corresponding instructions are UNDEFINED.

Note

For PSTATE updates, instruction encodings with bits[4:0] not set to 0b11111 are UNDEFINED.

Writes to PSTATE occur in program order without the need for additional synchronization. Changing PSTATE.SP to use SP\_EL0 synchronizes any updates to SP\_EL0 that have been written by an MSR to SP\_EL0, without the need for additional synchronization.

## C5.1.4 op0 == 0b01 , cache maintenance, TLB maintenance, address translation, prediction restriction, BRBE, Trace Extension, and Guarded Control Stack instructions

The System instructions are encoded with op0 == 0b01 . The different groups of System instructions are identified by the values of CRn and CRm , except that some of this encoding space is reserved for IMPLEMENTATION DEFINED functionality. The encoding of these instructions is:

<!-- formula-not-decoded -->

op0

The grouping of these instructions depending on the CRn and CRm fields is as follows:

CRn == 0b0111 The instruction group is determined by the value of CRm , as follows:

CRm == { 0b0001 , 0b0101 } Instruction cache maintenance instructions.

See Cache maintenance instructions, and data cache zero operations.

CRm == 0b0010 Branch Record Buffer and Trace Extension instructions.

See Branch Record Buffer instructions and Trace Extension instructions.

CRm == 0b0011 Prediction restriction instructions.

See Prediction restriction instructions.

CRm == 0b0100 Data cache zero operations.

See Cache maintenance instructions, and data cache zero operations.

CRm == { 0b0110 , 0b1010 , 0b1011 , 0b1100 , 0b1101 , 0b1110 , 0b1111 } Data cache maintenance instructions.

See Cache maintenance instructions, and data cache zero operations.

CRm == 0b0111 Guarded Control Stack instructions.

See Guarded Control Stack instructions.

CRm == { 0b1000 , 0b1001 } See Address translation instructions.

CRn == { 0b1000 , 0b1001 } See TLB maintenance instructions.

CRn == { 0b1011 , 0b1111 } See Reserved encoding space for IMPLEMENTATION DEFINED instructions.

## C5.1.4.1 Cache maintenance instructions, and data cache zero operations

Table C5-1 lists the Cache maintenance instructions and their encodings. Instructions that take an argument include Xt in the instruction syntax. For instructions that do not take an argument, the Xt field is encoded as 0b11111 . For these instructions, if the Xt field is not set to 0b11111 , it is CONSTRAINED UNPREDICTABLE whether:

- The instruction is UNDEFINED.

- The instruction behaves as if the Xt field is set to 0b11111 .

Table C5-1 Cache maintenance instructions and data cache zero operations

| op0   | op1   | CRn    | CRm    | op2   | Mnemonic   |
|-------|-------|--------|--------|-------|------------|
| 0b01  | 0b000 | 0b0111 | 0b0001 | 0b000 | ICIALLUIS  |
| 0b01  | 0b000 | 0b0111 | 0b0101 | 0b000 | IC IALLU   |
| 0b01  | 0b000 | 0b0111 | 0b0110 | 0b001 | DCIVAC     |
| 0b01  | 0b000 | 0b0111 | 0b0110 | 0b010 | DCISW      |
| 0b01  | 0b000 | 0b0111 | 0b0110 | 0b011 | DCIGVAC    |
| 0b01  | 0b000 | 0b0111 | 0b0110 | 0b100 | DCIGSW     |
| 0b01  | 0b000 | 0b0111 | 0b0110 | 0b101 | DCIGDVAC   |
| 0b01  | 0b000 | 0b0111 | 0b0110 | 0b110 | DCIGDSW    |
| 0b01  | 0b000 | 0b0111 | 0b1010 | 0b010 | DCCSW      |
| 0b01  | 0b000 | 0b0111 | 0b1010 | 0b100 | DCCGSW     |
| 0b01  | 0b000 | 0b0111 | 0b1010 | 0b110 | DCCGDSW    |
| 0b01  | 0b000 | 0b0111 | 0b1110 | 0b010 | DCCISW     |
| 0b01  | 0b000 | 0b0111 | 0b1110 | 0b100 | DCCIGSW    |
| 0b01  | 0b000 | 0b0111 | 0b1110 | 0b110 | DCCIGDSW   |
| 0b01  | 0b000 | 0b0111 | 0b1111 | 0b001 | DCCIVAPS   |
| 0b01  | 0b000 | 0b0111 | 0b1111 | 0b101 | DCCIGDVAPS |
| 0b01  | 0b011 | 0b0111 | 0b0100 | 0b001 | DCZVA      |
| 0b01  | 0b011 | 0b0111 | 0b0100 | 0b011 | DCGVA      |
| 0b01  | 0b011 | 0b0111 | 0b0100 | 0b100 | DCGZVA     |
| 0b01  | 0b011 | 0b0111 | 0b0101 | 0b001 | IC IVAU    |
| 0b01  | 0b011 | 0b0111 | 0b1010 | 0b001 | DCCVAC     |
| 0b01  | 0b011 | 0b0111 | 0b1010 | 0b011 | DCCGVAC    |
| 0b01  | 0b011 | 0b0111 | 0b1010 | 0b101 | DCCGDVAC   |
| 0b01  | 0b011 | 0b0111 | 0b1011 | 0b000 | DCCVAOC    |
| 0b01  | 0b011 | 0b0111 | 0b1011 | 0b001 | DCCVAU     |
| 0b01  | 0b011 | 0b0111 | 0b1011 | 0b111 | DCCGDVAOC  |
| 0b01  | 0b011 | 0b0111 | 0b1100 | 0b001 | DCCVAP     |
| 0b01  | 0b011 | 0b0111 | 0b1100 | 0b011 | DCCGVAP    |
| 0b01  | 0b011 | 0b0111 | 0b1100 | 0b101 | DCCGDVAP   |
| 0b01  | 0b011 | 0b0111 | 0b1101 | 0b001 | DCCVADP    |
| 0b01  | 0b011 | 0b0111 | 0b1101 | 0b011 | DCCGVADP   |
| 0b01  | 0b011 | 0b0111 | 0b1101 | 0b101 | DCCGDVADP  |
| 0b01  | 0b011 | 0b0111 | 0b1110 | 0b001 | DCCIVAC    |
| 0b01  | 0b011 | 0b0111 | 0b1110 | 0b011 | DCCIGVAC   |
| 0b01  | 0b011 | 0b0111 | 0b1110 | 0b101 | DCCIGDVAC  |

| op0   | op1   | CRn    | CRm    | op2   | Mnemonic   |
|-------|-------|--------|--------|-------|------------|
| 0b01  | 0b011 | 0b0111 | 0b1111 | 0b000 | DCCIVAOC   |
| 0b01  | 0b011 | 0b0111 | 0b1111 | 0b111 | DCCIGDVAOC |
| 0b01  | 0b100 | 0b0111 | 0b1110 | 0b000 | DCCIPAE    |
| 0b01  | 0b100 | 0b0111 | 0b1110 | 0b111 | DCCIGDPAE  |
| 0b01  | 0b110 | 0b0111 | 0b1110 | 0b001 | DCCIPAPA   |
| 0b01  | 0b110 | 0b0111 | 0b1110 | 0b101 | DCCIGDPAPA |

For more information about these instructions, see About cache maintenance in AArch64 state and A64 Cache maintenance instructions.

## C5.1.4.2 Prediction restriction instructions

Table C5-2 lists the Prediction restriction instructions and their encodings. Instructions that take an argument include Xt in the instruction syntax.

Table C5-2 Prediction restriction instructions

| op0   | op1   | CRn    | CRm    | op2   | Mnemonic   |
|-------|-------|--------|--------|-------|------------|
| 0b01  | 0b011 | 0b0111 | 0b0011 | 0b100 | CFPRCTX    |
| 0b01  | 0b011 | 0b0111 | 0b0011 | 0b101 | DVPRCTX    |
| 0b01  | 0b011 | 0b0111 | 0b0011 | 0b110 | COSPRCTX   |
| 0b01  | 0b011 | 0b0111 | 0b0011 | 0b111 | CPPRCTX    |

For more information about these instructions, see Execution, data prediction and prefetching restriction System instructions.

## C5.1.4.3 Address translation instructions

Table C5-3 lists the Address translation instructions and their encodings. The syntax of the instructions includes Xt , that provides the address to be translated.

Table C5-3 Address translation instructions

| op0   | op1   | CRn    | CRm    | op2   | Mnemonic   |
|-------|-------|--------|--------|-------|------------|
| 0b01  | 0b000 | 0b0111 | 0b1000 | 0b000 | AT S1E1R   |
| 0b01  | 0b000 | 0b0111 | 0b1000 | 0b001 | AT S1E1W   |
| 0b01  | 0b000 | 0b0111 | 0b1000 | 0b010 | AT S1E0R   |
| 0b01  | 0b000 | 0b0111 | 0b1000 | 0b011 | AT S1E0W   |
| 0b01  | 0b000 | 0b0111 | 0b1001 | 0b000 | ATS1E1RP   |
| 0b01  | 0b000 | 0b0111 | 0b1001 | 0b001 | ATS1E1WP   |
| 0b01  | 0b000 | 0b0111 | 0b1001 | 0b010 | AT S1E1A   |
| 0b01  | 0b100 | 0b0111 | 0b1000 | 0b000 | AT S1E2R   |

| op0   | op1   | CRn    | CRm    | op2   | Mnemonic   |
|-------|-------|--------|--------|-------|------------|
| 0b01  | 0b100 | 0b0111 | 0b1000 | 0b001 | AT S1E2W   |
| 0b01  | 0b100 | 0b0111 | 0b1000 | 0b100 | ATS12E1R   |
| 0b01  | 0b100 | 0b0111 | 0b1000 | 0b101 | ATS12E1W   |
| 0b01  | 0b100 | 0b0111 | 0b1000 | 0b110 | ATS12E0R   |
| 0b01  | 0b100 | 0b0111 | 0b1000 | 0b111 | ATS12E0W   |
| 0b01  | 0b100 | 0b0111 | 0b1001 | 0b010 | AT S1E2A   |
| 0b01  | 0b110 | 0b0111 | 0b1000 | 0b000 | AT S1E3R   |
| 0b01  | 0b110 | 0b0111 | 0b1000 | 0b001 | AT S1E3W   |
| 0b01  | 0b110 | 0b0111 | 0b1001 | 0b010 | AT S1E3A   |

For more information about these instructions, see Address translation instructions.

## C5.1.4.4 TLB maintenance instructions

Table C5-4 lists the TLB maintenance instructions and their encodings. Instructions that take an argument include Xt in the instruction syntax. For instructions that do not take an argument, the Xt field is encoded as 0b11111 . For these instructions, if the Xt field is not set to 0b11111 , it is CONSTRAINED UNPREDICTABLE whether:

- The instruction is UNDEFINED.
- The instruction behaves as if the Xt field is set to 0b11111 .

Table C5-4 TLB maintenance instructions

| op0   | op1   | CRn    | CRm    | op2   | Mnemonic       |
|-------|-------|--------|--------|-------|----------------|
| 0b01  | 0b000 | 0b1000 | 0b0001 | 0b000 | TLBIVMALLE1OS  |
| 0b01  | 0b000 | 0b1000 | 0b0001 | 0b001 | TLBI VAE1OS    |
| 0b01  | 0b000 | 0b1000 | 0b0001 | 0b001 | TLBIP VAE1OS   |
| 0b01  | 0b000 | 0b1000 | 0b0001 | 0b010 | TLBI ASIDE1OS  |
| 0b01  | 0b000 | 0b1000 | 0b0001 | 0b011 | TLBI VAAE1OS   |
| 0b01  | 0b000 | 0b1000 | 0b0001 | 0b011 | TLBIP VAAE1OS  |
| 0b01  | 0b000 | 0b1000 | 0b0001 | 0b101 | TLBI VALE1OS   |
| 0b01  | 0b000 | 0b1000 | 0b0001 | 0b101 | TLBIP VALE1OS  |
| 0b01  | 0b000 | 0b1000 | 0b0001 | 0b111 | TLBI VAALE1OS  |
| 0b01  | 0b000 | 0b1000 | 0b0001 | 0b111 | TLBIP VAALE1OS |
| 0b01  | 0b000 | 0b1000 | 0b0010 | 0b001 | TLBI RVAE1IS   |
| 0b01  | 0b000 | 0b1000 | 0b0010 | 0b001 | TLBIP RVAE1IS  |
| 0b01  | 0b000 | 0b1000 | 0b0010 | 0b011 | TLBI RVAAE1IS  |
| 0b01  | 0b000 | 0b1000 | 0b0010 | 0b011 | TLBIP RVAAE1IS |
| 0b01  | 0b000 | 0b1000 | 0b0010 | 0b101 | TLBI RVALE1IS  |
| 0b01  | 0b000 | 0b1000 | 0b0010 | 0b101 | TLBIP RVALE1IS |
| 0b01  | 0b000 | 0b1000 | 0b0010 | 0b111 | TLBI RVAALE1IS |

| op0   | op1   | CRn    | CRm    | op2   | Mnemonic         |
|-------|-------|--------|--------|-------|------------------|
| 0b01  | 0b000 | 0b1000 | 0b0010 | 0b111 | TLBIP RVAALE1IS  |
| 0b01  | 0b000 | 0b1000 | 0b0011 | 0b000 | TLBI VMALLE1IS   |
| 0b01  | 0b000 | 0b1000 | 0b0011 | 0b001 | TLBI VAE1IS      |
| 0b01  | 0b000 | 0b1000 | 0b0011 | 0b001 | TLBIP VAE1IS     |
| 0b01  | 0b000 | 0b1000 | 0b0011 | 0b010 | TLBI ASIDE1IS    |
| 0b01  | 0b000 | 0b1000 | 0b0011 | 0b011 | TLBI VAAE1IS     |
| 0b01  | 0b000 | 0b1000 | 0b0011 | 0b011 | TLBIP VAAE1IS    |
| 0b01  | 0b000 | 0b1000 | 0b0011 | 0b101 | TLBI VALE1IS     |
| 0b01  | 0b000 | 0b1000 | 0b0011 | 0b101 | TLBIP VALE1IS    |
| 0b01  | 0b000 | 0b1000 | 0b0011 | 0b111 | TLBI VAALE1IS    |
| 0b01  | 0b000 | 0b1000 | 0b0011 | 0b111 | TLBIP VAALE1IS   |
| 0b01  | 0b000 | 0b1000 | 0b0101 | 0b001 | TLBI RVAE1OS     |
| 0b01  | 0b000 | 0b1000 | 0b0101 | 0b001 | TLBIP RVAE1OS    |
| 0b01  | 0b000 | 0b1000 | 0b0101 | 0b011 | TLBI RVAAE1OS    |
| 0b01  | 0b000 | 0b1000 | 0b0101 | 0b011 | TLBIP RVAAE1OS   |
| 0b01  | 0b000 | 0b1000 | 0b0101 | 0b101 | TLBI RVALE1OS    |
| 0b01  | 0b000 | 0b1000 | 0b0101 | 0b101 | TLBIP RVALE1OS   |
| 0b01  | 0b000 | 0b1000 | 0b0101 | 0b111 | TLBI RVAALE1OS   |
| 0b01  | 0b000 | 0b1000 | 0b0101 | 0b111 | TLBIP RVAALE1OS  |
| 0b01  | 0b000 | 0b1000 | 0b0110 | 0b001 | TLBI RVAE1       |
| 0b01  | 0b000 | 0b1000 | 0b0110 | 0b001 | TLBIP RVAE1      |
| 0b01  | 0b000 | 0b1000 | 0b0110 | 0b011 | TLBI RVAAE1      |
| 0b01  | 0b000 | 0b1000 | 0b0110 | 0b011 | TLBIP RVAAE1     |
| 0b01  | 0b000 | 0b1000 | 0b0110 | 0b101 | TLBI RVALE1      |
| 0b01  | 0b000 | 0b1000 | 0b0110 | 0b101 | TLBIP RVALE1     |
| 0b01  | 0b000 | 0b1000 | 0b0110 | 0b111 | TLBI RVAALE1     |
| 0b01  | 0b000 | 0b1000 | 0b0110 | 0b111 | TLBIP RVAALE1    |
| 0b01  | 0b000 | 0b1000 | 0b0111 | 0b000 | TLBIVMALLE1      |
| 0b01  | 0b000 | 0b1000 | 0b0111 | 0b001 | TLBI VAE1        |
| 0b01  | 0b000 | 0b1000 | 0b0111 | 0b001 | TLBIP VAE1       |
| 0b01  | 0b000 | 0b1000 | 0b0111 | 0b010 | TLBI ASIDE1      |
| 0b01  | 0b000 | 0b1000 | 0b0111 | 0b011 | TLBI VAAE1       |
| 0b01  | 0b000 | 0b1000 | 0b0111 | 0b011 | TLBIP VAAE1      |
| 0b01  | 0b000 | 0b1000 | 0b0111 | 0b101 | TLBIP VALE1      |
| 0b01  | 0b000 | 0b1000 | 0b0111 | 0b111 | TLBI VAALE1      |
| 0b01  | 0b000 | 0b1000 | 0b0111 | 0b111 | TLBIP VAALE1     |
| 0b01  | 0b000 | 0b1001 | 0b0001 | 0b000 | TLBIVMALLE1OSNXS |
| 0b01  | 0b000 | 0b1001 | 0b0001 | 0b001 | TLBI VAE1OSNXS   |
| 0b01  | 0b000 | 0b1001 | 0b0001 | 0b001 | TLBIP VAE1OSNXS  |

| op0   | op1   | CRn    | CRm    | op2   | Mnemonic          |
|-------|-------|--------|--------|-------|-------------------|
| 0b01  | 0b000 | 0b1001 | 0b0001 | 0b010 | TLBI ASIDE1OSNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0001 | 0b011 | TLBI VAAE1OSNXS   |
| 0b01  | 0b000 | 0b1001 | 0b0001 | 0b011 | TLBIP VAAE1OSNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0001 | 0b101 | TLBI VALE1OSNXS   |
| 0b01  | 0b000 | 0b1001 | 0b0001 | 0b101 | TLBIP VALE1OSNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0001 | 0b111 | TLBI VAALE1OSNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0001 | 0b111 | TLBIPVAALE1OSNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0010 | 0b001 | TLBI RVAE1ISNXS   |
| 0b01  | 0b000 | 0b1001 | 0b0010 | 0b001 | TLBIP RVAE1ISNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0010 | 0b011 | TLBI RVAAE1ISNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0010 | 0b011 | TLBIP RVAAE1ISNXS |
| 0b01  | 0b000 | 0b1001 | 0b0010 | 0b101 | TLBI RVALE1ISNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0010 | 0b101 | TLBIP RVALE1ISNXS |
| 0b01  | 0b000 | 0b1001 | 0b0010 | 0b111 | TLBI RVAALE1ISNXS |
| 0b01  | 0b000 | 0b1001 | 0b0010 | 0b111 | TLBIPRVAALE1ISNXS |
| 0b01  | 0b000 | 0b1001 | 0b0011 | 0b000 | TLBIVMALLE1ISNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0011 | 0b001 | TLBI VAE1ISNXS    |
| 0b01  | 0b000 | 0b1001 | 0b0011 | 0b001 | TLBIP VAE1ISNXS   |
| 0b01  | 0b000 | 0b1001 | 0b0011 | 0b010 | TLBI ASIDE1ISNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0011 | 0b011 | TLBI VAAE1ISNXS   |
| 0b01  | 0b000 | 0b1001 | 0b0011 | 0b011 | TLBIP VAAE1ISNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0011 | 0b101 | TLBI VALE1ISNXS   |
| 0b01  | 0b000 | 0b1001 | 0b0011 | 0b101 | TLBIP VALE1ISNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0011 | 0b111 | TLBI VAALE1ISNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0011 | 0b111 | TLBIP VAALE1ISNXS |
| 0b01  | 0b000 | 0b1001 | 0b0101 | 0b001 | TLBI RVAE1OSNXS   |
| 0b01  | 0b000 | 0b1001 | 0b0101 | 0b001 | TLBIP RVAE1OSNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0101 | 0b011 | TLBI RVAAE1OSNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0101 | 0b011 | TLBIPRVAAE1OSNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0101 | 0b101 | TLBI RVALE1OSNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0101 | 0b101 | TLBIPRVALE1OSNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0101 | 0b111 | TLBIRVAALE1OSNXS  |
| 0b01  | 0b000 | 0b1001 | 0b0101 | 0b111 | TLBIPRVAALE1OSNXS |
| 0b01  | 0b000 | 0b1001 | 0b0110 | 0b001 | TLBI RVAE1NXS     |
| 0b01  | 0b000 | 0b1001 | 0b0110 | 0b001 | TLBIP RVAE1NXS    |
| 0b01  | 0b000 | 0b1001 | 0b0110 | 0b011 | TLBI RVAAE1NXS    |
| 0b01  | 0b000 | 0b1001 | 0b0110 | 0b011 | TLBIP RVAAE1NXS   |
| 0b01  | 0b000 | 0b1001 | 0b0110 | 0b101 | TLBI RVALE1NXS    |
| 0b01  | 0b000 | 0b1001 | 0b0110 | 0b101 | TLBIP RVALE1NXS   |
| 0b01  | 0b000 | 0b1001 | 0b0110 | 0b111 | TLBI RVAALE1NXS   |

| op0   | op1   | CRn    | CRm    | op2   | Mnemonic          |
|-------|-------|--------|--------|-------|-------------------|
| 0b01  | 0b000 | 0b1001 | 0b0110 | 0b111 | TLBIP RVAALE1NXS  |
| 0b01  | 0b000 | 0b1001 | 0b0111 | 0b000 | TLBIVMALLE1NXS    |
| 0b01  | 0b000 | 0b1001 | 0b0111 | 0b001 | TLBI VAE1NXS      |
| 0b01  | 0b000 | 0b1001 | 0b0111 | 0b001 | TLBIP VAE1NXS     |
| 0b01  | 0b000 | 0b1001 | 0b0111 | 0b010 | TLBI ASIDE1NXS    |
| 0b01  | 0b000 | 0b1001 | 0b0111 | 0b011 | TLBI VAAE1NXS     |
| 0b01  | 0b000 | 0b1001 | 0b0111 | 0b011 | TLBIP VAAE1NXS    |
| 0b01  | 0b000 | 0b1001 | 0b0111 | 0b101 | TLBI VALE1NXS     |
| 0b01  | 0b000 | 0b1001 | 0b0111 | 0b101 | TLBIP VALE1NXS    |
| 0b01  | 0b000 | 0b1001 | 0b0111 | 0b111 | TLBI VAALE1NXS    |
| 0b01  | 0b000 | 0b1001 | 0b0111 | 0b111 | TLBIP VAALE1NXS   |
| 0b01  | 0b100 | 0b1000 | 0b0000 | 0b001 | TLBI IPAS2E1IS    |
| 0b01  | 0b100 | 0b1000 | 0b0000 | 0b001 | TLBIP IPAS2E1IS   |
| 0b01  | 0b100 | 0b1000 | 0b0000 | 0b010 | TLBI RIPAS2E1IS   |
| 0b01  | 0b100 | 0b1000 | 0b0000 | 0b010 | TLBIP RIPAS2E1IS  |
| 0b01  | 0b100 | 0b1000 | 0b0000 | 0b101 | TLBI IPAS2LE1IS   |
| 0b01  | 0b100 | 0b1000 | 0b0000 | 0b101 | TLBIP IPAS2LE1IS  |
| 0b01  | 0b100 | 0b1000 | 0b0000 | 0b110 | TLBI RIPAS2LE1IS  |
| 0b01  | 0b100 | 0b1000 | 0b0000 | 0b110 | TLBIP RIPAS2LE1IS |
| 0b01  | 0b100 | 0b1000 | 0b0001 | 0b000 | TLBI ALLE2OS      |
| 0b01  | 0b100 | 0b1000 | 0b0001 | 0b001 | TLBI VAE2OS       |
| 0b01  | 0b100 | 0b1000 | 0b0001 | 0b001 | TLBIP VAE2OS      |
| 0b01  | 0b100 | 0b1000 | 0b0001 | 0b100 | TLBI ALLE1OS      |
| 0b01  | 0b100 | 0b1000 | 0b0001 | 0b101 | TLBI VALE2OS      |
| 0b01  | 0b100 | 0b1000 | 0b0001 | 0b101 | TLBIP VALE2OS     |
| 0b01  | 0b100 | 0b1000 | 0b0001 | 0b110 | TLBIVMALLS12E1OS  |
| 0b01  | 0b100 | 0b1000 | 0b0010 | 0b001 | TLBI RVAE2IS      |
| 0b01  | 0b100 | 0b1000 | 0b0010 | 0b001 | TLBIP RVAE2IS     |
| 0b01  | 0b100 | 0b1000 | 0b0010 | 0b010 | TLBIVMALLWS2E1IS  |
| 0b01  | 0b100 | 0b1000 | 0b0010 | 0b101 | TLBI RVALE2IS     |
| 0b01  | 0b100 | 0b1000 | 0b0010 | 0b101 | TLBIP RVALE2IS    |
| 0b01  | 0b100 | 0b1000 | 0b0011 | 0b000 | TLBI ALLE2IS      |
| 0b01  | 0b100 | 0b1000 | 0b0011 | 0b001 | TLBI VAE2IS       |
| 0b01  | 0b100 | 0b1000 | 0b0011 | 0b001 | TLBIP VAE2IS      |
| 0b01  | 0b100 | 0b1000 | 0b0011 | 0b100 | TLBI ALLE1IS      |
| 0b01  | 0b100 | 0b1000 | 0b0011 | 0b101 | TLBI VALE2IS      |
| 0b01  | 0b100 | 0b1000 | 0b0011 | 0b101 | TLBIP VALE2IS     |
| 0b01  | 0b100 | 0b1000 | 0b0011 | 0b110 | TLBI VMALLS12E1IS |
| 0b01  | 0b100 | 0b1000 | 0b0100 | 0b000 | TLBI IPAS2E1OS    |
| 0b01  | 0b100 | 0b1000 | 0b0100 | 0b000 | TLBIP IPAS2E1OS   |

| op0       | op1         | CRn           | CRm           | op2         | Mnemonic                          |
|-----------|-------------|---------------|---------------|-------------|-----------------------------------|
| 0b01      | 0b100       | 0b1000        | 0b0100        | 0b001       | TLBI IPAS2E1                      |
| 0b01      | 0b100       | 0b1000        | 0b0100        | 0b001       | TLBIP IPAS2E1                     |
| 0b01      | 0b100       | 0b1000        | 0b0100        | 0b010       | TLBI RIPAS2E1                     |
| 0b01      | 0b100       | 0b1000        | 0b0100        | 0b010       | TLBIP RIPAS2E1                    |
| 0b01      | 0b100       | 0b1000        | 0b0100        | 0b011       | TLBI RIPAS2E1OS                   |
| 0b01      | 0b100       | 0b1000        | 0b0100        | 0b011       | TLBIP RIPAS2E1OS                  |
| 0b01      | 0b100       | 0b1000        | 0b0100        | 0b100       | TLBI IPAS2LE1OS                   |
| 0b01      | 0b100       | 0b1000        | 0b0100        | 0b100       | TLBIP IPAS2LE1OS                  |
| 0b01      | 0b100       | 0b1000        | 0b0100        | 0b101       | TLBI IPAS2LE1                     |
| 0b01      | 0b100       | 0b1000        | 0b0100        | 0b101       | TLBIP IPAS2LE1                    |
| 0b01      | 0b100       | 0b1000        | 0b0100        | 0b110       | TLBI RIPAS2LE1                    |
| 0b01      | 0b100       | 0b1000        | 0b0100        | 0b110       | TLBIP RIPAS2LE1                   |
| 0b01      | 0b100       | 0b1000        | 0b0100        | 0b111       | TLBI RIPAS2LE1OS                  |
| 0b01      | 0b100       | 0b1000        | 0b0100        | 0b111       | TLBIP RIPAS2LE1OS                 |
| 0b01      | 0b100       | 0b1000        | 0b0101        | 0b001       | TLBI RVAE2OS                      |
| 0b01      | 0b100       | 0b1000        | 0b0101        | 0b001       | TLBIP RVAE2OS                     |
| 0b01      | 0b100       | 0b1000        | 0b0101        | 0b010       | TLBIVMALLWS2E1OS                  |
| 0b01      | 0b100       | 0b1000        | 0b0101        | 0b101       | TLBI RVALE2OS                     |
| 0b01      | 0b100       | 0b1000        | 0b0101        | 0b101       | TLBIP RVALE2OS                    |
| 0b01      | 0b100       | 0b1000        | 0b0110        | 0b001       | TLBI RVAE2                        |
| 0b01      | 0b100       | 0b1000        | 0b0110        | 0b001       | TLBIP RVAE2                       |
| 0b01      | 0b100       | 0b1000        | 0b0110        | 0b010       | TLBI VMALLWS2E1                   |
| 0b01      | 0b100       | 0b1000        | 0b0110        | 0b101       | TLBI RVALE2                       |
| 0b01      | 0b100       | 0b1000        | 0b0110        | 0b101       | TLBIP RVALE2                      |
| 0b01      | 0b100       | 0b1000        | 0b0111        | 0b000       | TLBI ALLE2                        |
| 0b01      | 0b100       | 0b1000        | 0b0111        | 0b001       | TLBI VAE2                         |
| 0b01      | 0b100       | 0b1000        | 0b0111        | 0b001       | TLBIP VAE2                        |
| 0b01 0b01 | 0b100 0b100 | 0b1000 0b1000 | 0b0111 0b0111 | 0b100 0b101 | TLBI ALLE1 TLBI VALE2             |
| 0b01      | 0b100       | 0b1000        | 0b0111        | 0b101       | TLBIP VALE2                       |
| 0b01 0b01 | 0b100 0b100 | 0b1000 0b1001 | 0b0111 0b0000 | 0b110 0b001 | TLBI VMALLS12E1 TLBI IPAS2E1ISNXS |
|           |             | 0b1001        | 0b0000        |             | TLBIP IPAS2E1ISNXS                |
| 0b01      | 0b100       |               |               | 0b001       |                                   |
| 0b01      | 0b100       | 0b1001        | 0b0000        | 0b010       | TLBI RIPAS2E1ISNXS                |
| 0b01      | 0b100       | 0b1001        | 0b0000        | 0b010       | TLBIPRIPAS2E1ISNXS                |
| 0b01      | 0b100       | 0b1001        | 0b0000        | 0b101       | TLBI IPAS2LE1ISNXS                |
| 0b01      | 0b100       | 0b1001        | 0b0000        | 0b101       | TLBIPIPAS2LE1ISNXS                |
| 0b01      | 0b100       | 0b1001        | 0b0000        | 0b110       | TLBIRIPAS2LE1ISNXS                |
| 0b01      | 0b100       | 0b1001        | 0b0000        | 0b110       | TLBIPRIPAS2LE1ISNXS               |
| 0b01      | 0b100       | 0b1001        | 0b0001        | 0b000       | TLBI ALLE2OSNXS                   |

| op0   | op1   | CRn    | CRm    | op2   | Mnemonic            |
|-------|-------|--------|--------|-------|---------------------|
| 0b01  | 0b100 | 0b1001 | 0b0001 | 0b001 | TLBI VAE2OSNXS      |
| 0b01  | 0b100 | 0b1001 | 0b0001 | 0b001 | TLBIP VAE2OSNXS     |
| 0b01  | 0b100 | 0b1001 | 0b0001 | 0b100 | TLBI ALLE1OSNXS     |
| 0b01  | 0b100 | 0b1001 | 0b0001 | 0b101 | TLBI VALE2OSNXS     |
| 0b01  | 0b100 | 0b1001 | 0b0001 | 0b101 | TLBIP VALE2OSNXS    |
| 0b01  | 0b100 | 0b1001 | 0b0001 | 0b110 | TLBIVMALLS12E1OSNXS |
| 0b01  | 0b100 | 0b1001 | 0b0010 | 0b001 | TLBI RVAE2ISNXS     |
| 0b01  | 0b100 | 0b1001 | 0b0010 | 0b001 | TLBIP RVAE2ISNXS    |
| 0b01  | 0b100 | 0b1001 | 0b0010 | 0b010 | TLBIVMALLWS2E1ISNXS |
| 0b01  | 0b100 | 0b1001 | 0b0010 | 0b101 | TLBI RVALE2ISNXS    |
| 0b01  | 0b100 | 0b1001 | 0b0010 | 0b101 | TLBIP RVALE2ISNXS   |
| 0b01  | 0b100 | 0b1001 | 0b0011 | 0b000 | TLBI ALLE2ISNXS     |
| 0b01  | 0b100 | 0b1001 | 0b0011 | 0b001 | TLBI VAE2ISNXS      |
| 0b01  | 0b100 | 0b1001 | 0b0011 | 0b001 | TLBIP VAE2ISNXS     |
| 0b01  | 0b100 | 0b1001 | 0b0011 | 0b100 | TLBI ALLE1ISNXS     |
| 0b01  | 0b100 | 0b1001 | 0b0011 | 0b101 | TLBI VALE2ISNXS     |
| 0b01  | 0b100 | 0b1001 | 0b0011 | 0b101 | TLBIP VALE2ISNXS    |
| 0b01  | 0b100 | 0b1001 | 0b0011 | 0b110 | TLBIVMALLS12E1ISNXS |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b000 | TLBI IPAS2E1OSNXS   |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b000 | TLBIPIPAS2E1OSNXS   |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b001 | TLBI IPAS2E1NXS     |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b001 | TLBIP IPAS2E1NXS    |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b010 | TLBI RIPAS2E1NXS    |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b010 | TLBIP RIPAS2E1NXS   |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b011 | TLBIRIPAS2E1OSNXS   |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b011 | TLBIPRIPAS2E1OSNXS  |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b100 | TLBIIPAS2LE1OSNXS   |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b100 | TLBIPIPAS2LE1OSNXS  |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b101 | TLBI IPAS2LE1NXS    |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b101 | TLBIP IPAS2LE1NXS   |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b110 | TLBI RIPAS2LE1NXS   |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b110 | TLBIPRIPAS2LE1NXS   |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b111 | TLBIRIPAS2LE1OSNXS  |
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b111 | TLBIPRIPAS2LE1OSNXS |
| 0b01  | 0b100 | 0b1001 | 0b0101 | 0b001 | TLBI RVAE2OSNXS     |
| 0b01  | 0b100 | 0b1001 | 0b0101 | 0b001 | TLBIP RVAE2OSNXS    |
| 0b01  | 0b100 | 0b1001 | 0b0101 | 0b010 | TLBIVMALLWS2E1OSNXS |
| 0b01  | 0b100 | 0b1001 | 0b0101 | 0b101 | TLBI RVALE2OSNXS    |
| 0b01  | 0b100 | 0b1001 | 0b0101 | 0b101 | TLBIPRVALE2OSNXS    |
| 0b01  | 0b100 | 0b1001 | 0b0110 | 0b001 | TLBI RVAE2NXS       |

| op0       | op1         | CRn           | CRm           | op2         | Mnemonic                |
|-----------|-------------|---------------|---------------|-------------|-------------------------|
| 0b01      | 0b100       | 0b1001        | 0b0110        | 0b001       | TLBIP RVAE2NXS          |
| 0b01      | 0b100       | 0b1001        | 0b0110        | 0b010       | TLBIVMALLWS2E1NXS       |
| 0b01      | 0b100       | 0b1001        | 0b0110        | 0b101       | TLBI RVALE2NXS          |
| 0b01      | 0b100       | 0b1001        | 0b0110        | 0b101       | TLBIP RVALE2NXS         |
| 0b01      | 0b100       | 0b1001        | 0b0111        | 0b000       | TLBI ALLE2NXS           |
| 0b01      | 0b100       | 0b1001        | 0b0111        | 0b001       | TLBI VAE2NXS            |
| 0b01      | 0b100       | 0b1001        | 0b0111        | 0b001       | TLBIP VAE2NXS           |
| 0b01      | 0b100       | 0b1001        | 0b0111        | 0b100       | TLBI ALLE1NXS           |
| 0b01      | 0b100       | 0b1001        | 0b0111        | 0b101       | TLBI VALE2NXS           |
| 0b01      | 0b100       | 0b1001        | 0b0111        | 0b101       | TLBIP VALE2NXS          |
| 0b01      | 0b100       | 0b1001        | 0b0111        | 0b110       | TLBIVMALLS12E1NXS       |
| 0b01      | 0b110       | 0b1000        | 0b0001        | 0b000       | TLBI ALLE3OS            |
| 0b01      | 0b110       | 0b1000        | 0b0001        | 0b001       | TLBI VAE3OS             |
| 0b01      | 0b110       | 0b1000        | 0b0001        | 0b001       | TLBIP VAE3OS            |
| 0b01      | 0b110       | 0b1000        | 0b0001        | 0b100       | TLBI PAALLOS            |
| 0b01      | 0b110       | 0b1000        | 0b0001        | 0b101       | TLBI VALE3OS            |
| 0b01      | 0b110       | 0b1000        | 0b0001        | 0b101       | TLBIP VALE3OS           |
| 0b01      | 0b110       | 0b1000        | 0b0010        | 0b001       | TLBI RVAE3IS            |
| 0b01      | 0b110       | 0b1000        | 0b0010        | 0b001       | TLBIP RVAE3IS           |
| 0b01      | 0b110       | 0b1000        | 0b0010        | 0b101       | TLBI RVALE3IS           |
| 0b01      | 0b110       | 0b1000        | 0b0010        | 0b101       | TLBIP RVALE3IS          |
| 0b01      | 0b110       | 0b1000        | 0b0011        | 0b000       | TLBI ALLE3IS            |
| 0b01      | 0b110       | 0b1000        | 0b0011        | 0b001       | TLBI VAE3IS             |
| 0b01      | 0b110       | 0b1000        | 0b0011        | 0b001       | TLBIP VAE3IS            |
| 0b01      | 0b110       | 0b1000        | 0b0011        | 0b101       | TLBI VALE3IS            |
| 0b01      | 0b110       | 0b1000        | 0b0011        | 0b101       | TLBIP VALE3IS           |
| 0b01      | 0b110       | 0b1000        | 0b0100        | 0b011       | TLBI RPAOS              |
| 0b01      | 0b110       | 0b1000        | 0b0100        | 0b111       | TLBI RPALOS             |
| 0b01      | 0b110       | 0b1000        | 0b0101        | 0b001       | TLBI RVAE3OS            |
| 0b01      | 0b110       | 0b1000        | 0b0101        | 0b001       | TLBIP RVAE3OS           |
| 0b01      | 0b110       | 0b1000        | 0b0101        | 0b101       | TLBIP RVALE3OS          |
| 0b01      | 0b110       |               | 0b0110        | 0b001       | TLBI RVAE3              |
|           |             | 0b1000        |               |             |                         |
| 0b01      | 0b110       | 0b1000        | 0b0110        | 0b101       | TLBI RVALE3             |
| 0b01 0b01 | 0b110 0b110 | 0b1000 0b1000 | 0b0110 0b0111 | 0b101 0b000 | TLBIP RVALE3 TLBI ALLE3 |
| 0b01      | 0b110       | 0b1000        | 0b0111        | 0b001       | TLBI VAE3               |
| 0b01      | 0b110       | 0b1000        | 0b0111        | 0b001       | TLBIP VAE3              |
| 0b01      | 0b110       | 0b1000        | 0b0111        | 0b100       | TLBI PAALL              |

| op0   | op1   | CRn    | CRm    | op2   | Mnemonic          |
|-------|-------|--------|--------|-------|-------------------|
| 0b01  | 0b110 | 0b1000 | 0b0111 | 0b101 | TLBI VALE3        |
| 0b01  | 0b110 | 0b1000 | 0b0111 | 0b101 | TLBIP VALE3       |
| 0b01  | 0b110 | 0b1001 | 0b0001 | 0b000 | TLBI ALLE3OSNXS   |
| 0b01  | 0b110 | 0b1001 | 0b0001 | 0b001 | TLBI VAE3OSNXS    |
| 0b01  | 0b110 | 0b1001 | 0b0001 | 0b001 | TLBIP VAE3OSNXS   |
| 0b01  | 0b110 | 0b1001 | 0b0001 | 0b101 | TLBI VALE3OSNXS   |
| 0b01  | 0b110 | 0b1001 | 0b0001 | 0b101 | TLBIP VALE3OSNXS  |
| 0b01  | 0b110 | 0b1001 | 0b0010 | 0b001 | TLBI RVAE3ISNXS   |
| 0b01  | 0b110 | 0b1001 | 0b0010 | 0b001 | TLBIP RVAE3ISNXS  |
| 0b01  | 0b110 | 0b1001 | 0b0010 | 0b101 | TLBI RVALE3ISNXS  |
| 0b01  | 0b110 | 0b1001 | 0b0010 | 0b101 | TLBIP RVALE3ISNXS |
| 0b01  | 0b110 | 0b1001 | 0b0011 | 0b000 | TLBI ALLE3ISNXS   |
| 0b01  | 0b110 | 0b1001 | 0b0011 | 0b001 | TLBI VAE3ISNXS    |
| 0b01  | 0b110 | 0b1001 | 0b0011 | 0b001 | TLBIP VAE3ISNXS   |
| 0b01  | 0b110 | 0b1001 | 0b0011 | 0b101 | TLBI VALE3ISNXS   |
| 0b01  | 0b110 | 0b1001 | 0b0011 | 0b101 | TLBIP VALE3ISNXS  |
| 0b01  | 0b110 | 0b1001 | 0b0101 | 0b001 | TLBI RVAE3OSNXS   |
| 0b01  | 0b110 | 0b1001 | 0b0101 | 0b001 | TLBIP RVAE3OSNXS  |
| 0b01  | 0b110 | 0b1001 | 0b0101 | 0b101 | TLBI RVALE3OSNXS  |
| 0b01  | 0b110 | 0b1001 | 0b0101 | 0b101 | TLBIPRVALE3OSNXS  |
| 0b01  | 0b110 | 0b1001 | 0b0110 | 0b001 | TLBI RVAE3NXS     |
| 0b01  | 0b110 | 0b1001 | 0b0110 | 0b001 | TLBIP RVAE3NXS    |
| 0b01  | 0b110 | 0b1001 | 0b0110 | 0b101 | TLBI RVALE3NXS    |
| 0b01  | 0b110 | 0b1001 | 0b0110 | 0b101 | TLBIP RVALE3NXS   |
| 0b01  | 0b110 | 0b1001 | 0b0111 | 0b000 | TLBI ALLE3NXS     |
| 0b01  | 0b110 | 0b1001 | 0b0111 | 0b001 | TLBI VAE3NXS      |
| 0b01  | 0b110 | 0b1001 | 0b0111 | 0b001 | TLBIP VAE3NXS     |
| 0b01  | 0b110 | 0b1001 | 0b0111 | 0b101 | TLBI VALE3NXS     |
| 0b01  | 0b110 | 0b1001 | 0b0111 | 0b101 | TLBIP VALE3NXS    |

For more information about these instructions, see TLB maintenance instructions.

## C5.1.4.5 Branch Record Buffer instructions

Table C5-5 lists the Branch Record Buffer instructions and their encodings.

## Table C5-5 Branch Record Buffer instructions

| op0   | op1   | CRn    | CRm    | op2   | Mnemonic   |
|-------|-------|--------|--------|-------|------------|
| 0b01  | 0b001 | 0b0111 | 0b0010 | 0b100 | BRBIALL    |

0b01

0b001

0b0111

0b0010

0b101

BRBINJ

For more information, see The Branch Record Buffer Extension.

## C5.1.4.6 Instrumentation Trace Extension instructions

Table C5-6 lists the Instrumentation Trace Extension instructions and their encodings.

## Table C5-6 Trace Extension instructions

| op0   | op1   | CRn    | CRm    | op2   | Mnemonic   |
|-------|-------|--------|--------|-------|------------|
| 0b01  | 0b011 | 0b0111 | 0b0010 | 0b111 | TRCIT      |

For more information, see Instrumentation extension.

## C5.1.4.7 Guarded Control Stack instructions

Table C5-7 lists the Guarded Control Stack instructions and their encodings.

Table C5-7 Guarded Control Stack instructions

| op0   | op1   | CRn    | CRm    | op2   | Mnemonic   |
|-------|-------|--------|--------|-------|------------|
| 0b01  | 0b000 | 0b0111 | 0b0111 | 0b100 | GCSPUSHX   |
| 0b01  | 0b000 | 0b0111 | 0b0111 | 0b101 | GCSPOPCX   |
| 0b01  | 0b000 | 0b0111 | 0b0111 | 0b110 | GCSPOPX    |
| 0b01  | 0b011 | 0b0111 | 0b0111 | 0b000 | GCSPUSHM   |
| 0b01  | 0b011 | 0b0111 | 0b0111 | 0b001 | GCSPOPM    |
| 0b01  | 0b011 | 0b0111 | 0b0111 | 0b010 | GCSSS1     |
| 0b01  | 0b011 | 0b0111 | 0b0111 | 0b011 | GCSSS2     |

For more information, see The Guarded Control Stack.

## C5.1.4.8 Reserved encoding space for IMPLEMENTATION DEFINED instructions

The A64 instruction set reserves the following encoding space for IMPLEMENTATION DEFINED instructions:

<!-- image -->

The value of L defines the use of Rt as follows:

- 0

Rt is an argument supplied to the instruction.

- 1

Rt is a result returned by the instruction.

IMPLEMENTATION DEFINED instructions in this encoding space are accessed using the SYS , SYSL , and SYSP instructions, see SYS, SYSL and SYSP.

See also Reserved encodings for IMPLEMENTATION DEFINED registers.

## C5.1.5 op0 == 0b11 , Moves to and from Special-purpose registers

The instructions that move data to and from non-debug System registers are encoded with op0 == 0b11 , except that some of this encoding space is reserved for IMPLEMENTATION DEFINED functionality. The encoding of these instructions is:

| 31 30 29 28 27 26 25 24 23 22 21 20 19 18   | 16 15   | 12 11   | 8 7   | 5 4   | 0   |
|---------------------------------------------|---------|---------|-------|-------|-----|
| 1 1 0 1 0 1 0 1 0 0 L 1 1                   | op1     | CRn     | CRm   | op2   | Rt  |

op0

## C5.1.5.1 Instructions for accessing Special-purpose registers

The value of CRn provides the next level of decode of these instructions. For Special-purpose registers, the value of CRn is 4.

## The A64 instructions for accessing Special-purpose registers are:

MSR &lt;Special-purpose\_register&gt;, Xt

; Write to Special-purpose register

MRS Xt, &lt;Special-purpose\_register&gt;

;

Read

from

Special-purpose register

Where &lt;Special-purpose\_register&gt; is the register name, for example SP\_EL0.

For these accesses, CRn has the value 0b0100 . The encoding for Special-purpose register accesses is:

<!-- image -->

The full list of Special-purpose registers is in Table C5-8. The characteristic of a Special-purpose register is that all direct and indirect reads and writes to the register appear to occur in program order relative to other instructions, without the need for any explicit synchronization.

Table C5-8 lists the encodings for op1 , CRm , and op2 fields for accesses to the Special-purpose registers in AArch64.

## Table C5-8 Instruction encodings for Special-purpose register accesses

| op1   | CRn    | CRm    | op2   | Access   | Mnemonic   | Accesses          |
|-------|--------|--------|-------|----------|------------|-------------------|
| 0b000 | 0b0100 | 0b0000 | 0b000 | RW       | SPSR_EL1   | SPSR_EL1 SPSR_EL2 |
| 0b000 | 0b0100 | 0b0000 | 0b001 | RW       | ELR_EL1    | ELR_EL1 ELR_EL2   |
| 0b000 | 0b0100 | 0b0001 | 0b000 | RW       | SP_EL0     | SP_EL0            |
| 0b000 | 0b0100 | 0b0010 | 0b000 | RW       | SPSel      | SPSel             |

| op1   | CRn    | CRm    | op2   | Access   | Mnemonic    | Accesses                |
|-------|--------|--------|-------|----------|-------------|-------------------------|
| 0b000 | 0b0100 | 0b0010 | 0b010 | RO       | CurrentEL   | CurrentEL               |
| 0b000 | 0b0100 | 0b0010 | 0b011 | RW       | PAN         | PAN                     |
| 0b000 | 0b0100 | 0b0010 | 0b100 | RW       | UAO         | UAO                     |
| 0b000 | 0b0100 | 0b0011 | 0b000 | RW       | ALLINT      | ALLINT                  |
| 0b000 | 0b0100 | 0b0011 | 0b001 | RW       | PM          | PM                      |
| 0b000 | 0b0100 | 0b0110 | 0b000 | RW       | ICC_PMR_EL1 | ICC_PMR_EL1 ICV_PMR_EL1 |
| 0b011 | 0b0100 | 0b0010 | 0b000 | RW       | NZCV        | NZCV                    |
| 0b011 | 0b0100 | 0b0010 | 0b001 | RW       | DAIF        | DAIF                    |
| 0b011 | 0b0100 | 0b0010 | 0b010 | RW       | SVCR        | SVCR                    |
| 0b011 | 0b0100 | 0b0010 | 0b101 | RW       | DIT         | DIT                     |
| 0b011 | 0b0100 | 0b0010 | 0b110 | RW       | SSBS        | SSBS                    |
| 0b011 | 0b0100 | 0b0010 | 0b111 | RW       | TCO         | TCO                     |
| 0b011 | 0b0100 | 0b0100 | 0b000 | RW       | FPCR        | FPCR                    |
| 0b011 | 0b0100 | 0b0100 | 0b001 | RW       | FPSR        | FPSR                    |
| 0b011 | 0b0100 | 0b0100 | 0b010 | RW       | FPMR        | FPMR                    |
| 0b011 | 0b0100 | 0b0101 | 0b000 | RW       | DSPSR_EL0   | DSPSR_EL0               |
| 0b011 | 0b0100 | 0b0101 | 0b001 | RW       | DLR_EL0     | DLR_EL0                 |
| 0b100 | 0b0100 | 0b0000 | 0b000 | RW       | SPSR_EL2    | SPSR_EL1 SPSR_EL2       |
| 0b100 | 0b0100 | 0b0000 | 0b001 | RW       | ELR_EL2     | ELR_EL1 ELR_EL2         |
| 0b100 | 0b0100 | 0b0001 | 0b000 | RW       | SP_EL1      | SP_EL1                  |
| 0b100 | 0b0100 | 0b0011 | 0b000 | RW       | SPSR_irq    | SPSR_irq                |
| 0b100 | 0b0100 | 0b0011 | 0b001 | RW       | SPSR_abt    | SPSR_abt                |
| 0b100 | 0b0100 | 0b0011 | 0b010 | RW       | SPSR_und    | SPSR_und                |
| 0b100 | 0b0100 | 0b0011 | 0b011 | RW       | SPSR_fiq    | SPSR_fiq                |
| 0b101 | 0b0100 | 0b0000 | 0b000 | RW       | SPSR_EL12   | SPSR_EL1                |
| 0b101 | 0b0100 | 0b0000 | 0b001 | RW       | ELR_EL12    | ELR_EL1                 |
| 0b110 | 0b0100 | 0b0000 | 0b000 | RW       | SPSR_EL3    | SPSR_EL3                |
| 0b110 | 0b0100 | 0b0000 | 0b001 | RW       | ELR_EL3     | ELR_EL3                 |
| 0b110 | 0b0100 | 0b0001 | 0b000 | RW       | SP_EL2      | SP_EL2                  |

All direct and indirect reads and writes to Special-purpose registers appear to occur in program order relative to other instructions.