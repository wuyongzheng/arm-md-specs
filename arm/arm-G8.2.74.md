## G8.2.74 HSR, Hyp Syndrome Register

The HSR characteristics are:

## Purpose

Holds syndrome information for an exception taken to Hyp mode.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register HSR bits [31:0] are architecturally mapped to AArch64 System register ESR\_EL2[31:0].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to HSR are UNDEFINED.

## Attributes

HSR is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 26 25 24   | 0   |
|------|------------|-----|
| EC   | IL         | ISS |

Execution in any Non-secure PE mode other than Hyp mode makes this register UNKNOWN.

When an UNPREDICTABLE instruction is treated as UNDEFINED, and the exception is taken to EL2, the value of HSR is UNKNOWN. The value written to HSR must be consistent with a value that could be created as a result of an exception from the same Exception level that generated the exception as a result of a situation that is not UNPREDICTABLE at that Exception level, in order to avoid the possibility of a privilege violation.

## EC, bits [31:26]

Exception Class. Indicates the reason for the exception that this register holds information about. Possible values of this field are:

| EC       | Meaning                                                                                                                                      | ISS                                                     |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| 0b000000 | Unknown reason.                                                                                                                              | ISS encoding for exceptions with an unknown reason      |
| 0b000001 | Trapped WFI or WFEinstruction execution. Conditional WFEand WFI instructions that fail their condition code check do not cause an exception. | ISS encoding for Exception from a WFI or WFEinstruction |
| 0b000011 | Trapped MCRorMRCaccess with (coproc== 0b1111 ) that is not reported using EC value 0b000000 .                                                | ISS encoding for Exception from an MCRor MRCaccess      |
| 0b000100 | Trapped MCRRor MRRCaccess with (coproc== 0b1111 ) that is not reported using EC value 0b000000 .                                             | ISS encoding for Exception from an MCRRor MRRCaccess    |
| 0b000101 | Trapped MCRor MRCaccess with (coproc== 0b1110 ).                                                                                             | ISS encoding for Exception from an MCRor MRCaccess      |

| EC       | Meaning                                                                                                                                                                                                                                   | ISS                                                                                                     |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| 0b000110 | Trapped LDCor STC access. The only architected uses of these instructions are: • An STC to write data to memory from DBGDTRRXint. • An LDCto read data from memory to DBGDTRTXint.                                                        | ISS encoding for Exception from anLDC or STC instruction                                                |
| 0b000111 | Access to Advanced SIMD or floating-point functionality trapped by a HCPTR.{TASE, TCP10} control. Excludes exceptions generated because Advanced SIMD and floating-point are not implemented. These are reported with EC value 0b000000 . | ISS encoding for Exception from an access to SIMD or floating-point functionality, resulting from HCPTR |
| 0b001000 | Trapped VMRSaccess, from ID group trap, that is not reported using EC value 0b000111 .                                                                                                                                                    | ISS encoding for Exception from an MCRor MRCaccess                                                      |
| 0b001100 | Trapped MRRCaccess with (coproc== 0b1110 ).                                                                                                                                                                                               | ISS encoding for Exception from an MCRRor MRRCaccess                                                    |
| 0b001110 | Illegal exception return to AArch32 state.                                                                                                                                                                                                | ISS encoding for Exception from an Illegal state or PC alignment fault                                  |
| 0b010001 | Exception on SVC instruction execution in AArch32 state routed to EL2.                                                                                                                                                                    | ISS encoding for Exception from HVCor SVC instruction execution                                         |
| 0b010010 | HVCinstruction execution in AArch32 state, when HVCis not disabled.                                                                                                                                                                       | ISS encoding for Exception from HVCor SVC instruction execution                                         |
| 0b010011 | Trapped execution of SMCinstruction in AArch32 state.                                                                                                                                                                                     | ISS encoding for Exception fromSMC instruction execution                                                |
| 0b100000 | Prefetch Abort from a lower Exception level.                                                                                                                                                                                              | ISS encoding for Exception from a Prefetch Abort                                                        |
| 0b100001 | Prefetch Abort taken without a change in Exception level.                                                                                                                                                                                 | ISS encoding for Exception from a Prefetch Abort                                                        |
| 0b100010 | PC alignment fault exception.                                                                                                                                                                                                             | ISS encoding for Exception from an Illegal state or PC alignment fault                                  |
| 0b100100 | Data Abort exception from a lower Exception level.                                                                                                                                                                                        | ISS encoding for Exception from a Data Abort                                                            |
| 0b100101 | Data Abort exception taken without a change in Exception level.                                                                                                                                                                           | ISS encoding for Exception from a Data Abort                                                            |

All other EC values are reserved by Arm, and:

- Unused values in the range 0b000000 -0b101100 ( 0x00 -0x2C ) are reserved for future use for synchronous exceptions.
- Unused values in the range 0b101101 -0b111111 ( 0x2D -0x3F ) are reserved for future use, and might be used for synchronous or asynchronous exceptions.

The effect of programming this field to a reserved value is that behavior is CONSTRAINED UNPREDICTABLE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IL, bit [25]

Instruction length bit. Indicates the size of the instruction that has been trapped to Hyp mode. When this bit is valid, possible values of this bit are:

| IL   | Meaning                     |
|------|-----------------------------|
| 0b0  | 16-bit instruction trapped. |
| 0b1  | 32-bit instruction trapped. |

This field is RES1 and not valid for the following cases:

- When the EC value is 0b000000 , indicating an exception with an unknown reason.
- Prefetch Aborts.
- Data Abort exceptions for which the HSR.ISS.ISV field is 0.
- When the EC value is 0b001110 , indicating an Illegal state exception.

The IL field is not valid and is UNKNOWN on an exception from a PC alignment fault.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ISS, bits [24:0]

Instruction Specific Syndrome. Architecturally, this field can be defined independently for each defined Exception class. However, in practice, some ISS encodings are used for more than one Exception class.

## ISS encoding for exceptions with an unknown reason

<!-- image -->

## Bits [24:0]

Reserved, RES0.

## Additional Information for ISS encoding for exceptions with an unknown reason

This EC value is used for all exceptions that are not covered by any other EC value. This includes exceptions that are generated in the following situations:

- The attempted execution of an instruction bit pattern that has no allocated instruction or is not accessible in the current PE mode in the current Security state, including:
- Aread access using a System register encoding pattern that is not allocated for reads or that does not permit reads in the current PE mode and Security state.
- Awrite access using a System register encoding pattern that is not allocated for writes or that does not permit writes in the current PE mode and Security state.
- Instruction encodings that are unallocated.
- Instruction encodings for instructions not implemented in the implementation.
- In Debug state, the attempted execution of an instruction bit pattern that is not accessible in Debug state.
- In Non-debug state, the attempted execution of an instruction bit pattern that is not accessible in Non-debug state.
- The attempted execution of a short vector floating-point instruction.
- In an implementation that does not include Advanced SIMD and floating-point functionality, an attempted access to Advanced SIMD or floating-point functionality under conditions where that access would be permitted if that functionality was present. This includes the attempted execution of an Advanced SIMD or floating-point instruction, and attempted accesses to Advanced SIMD and floating-point System registers.
- An exception generated because of the value of one of the SCTLR.{ITD, SED, CP15BEN} control bits.
- Attempted execution of:
- An HVC instruction when disabled by HCR.HCD, SCR.HCE, or SCR\_EL3.HCE.

- An SMC instruction when disabled by SCR.SCD or SCR\_EL3.SMD.
- An HLT instruction when disabled by EDSCR.HDE.
- An HVC instruction when disabled by HCR.HCD, SCR.HCE, or SCR\_EL3.HCE.An SMC instruction when disabled by SCR.SCD or SCR\_EL3.SMD.An HLT instruction when disabled by EDSCR.HDE.
- An exception generated because of the attempted execution of an MSR (Banked register) or MRS (Banked register) instruction that would access a Banked register that is not accessible from the Security state and PE mode at which the instruction was executed.

Note

An exception is generated only if the CONSTRAINED UNPREDICTABLE behavior of the instruction is that it is UNDEFINED, see 'MSR (banked register) and MRS (banked register)'.

- Attempted execution, in Debug state, of:
- ADCPS1 instruction in Non-secure state from EL0 when EL2 is using AArch32 and the value of HCR.TGE is 1.
- ADCPS2instruction at EL1 or EL0 when EL2 is not implemented, or when EL3 is using AArch32 and the value of SCR.NS is 0, or when EL3 is using AArch64 and the value of SCR\_EL3.NS is 0.
- ADCPS3 instruction when EL3 is not implemented, or when the value of EDSCR.SDD is 1.
- In Debug state when the value of EDSCR.SDD is 1, the attempted execution at EL2, EL1, and EL0 of an instruction that is configured to trap to EL3.
- 'Undefined Instruction exception, when the value of HCR.TGE is 1' describes the configuration settings for a trap that returns an EC value of 0b000000 .

## ISS encoding for Exception from a WFI or WFE instruction

<!-- image -->

## CV, bit [24]

Condition code valid. Possible values of this bit are:

| CV   | Meaning                     |
|------|-----------------------------|
| 0b0  | The CONDfield is not valid. |
| 0b1  | The CONDfield is valid.     |

When an A32 instruction is trapped, CV is set to 1.

When a T32 instruction is trapped, it is IMPLEMENTATION DEFINED whether CV is set to 1 or set to 0. For more information, see the description of the COND field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## COND, bits [23:20]

The condition code for the trapped instruction.

When an A32 instruction is trapped, CV is set to 1 and:

- If the instruction is conditional, COND is set to the condition code field value from the instruction.
- If the instruction is unconditional, COND is set to 0b1110 .

Aconditional A32 instruction that is known to pass its condition code check can be presented either:

- With COND set to 0b1110 , the value for unconditional.
- With the COND value held in the instruction.

When a T32 instruction is trapped, it is IMPLEMENTATION DEFINED whether:

- CVis set to 0 and COND is set to an UNKNOWN value. Software must examine the SPSR.IT field to determine the condition, if any, of the T32 instruction.
- CVis set to 1 and COND is set to the condition code for the condition that applied to the instruction.

For an implementation that, for both T32 and A32 instructions, takes an exception on a trapped conditional instruction only if the instruction passes its condition code check, these definitions mean that when CV is set to 1 it is IMPLEMENTATION DEFINED whether the COND field is set to 0b1110 , or to the value of any condition that applied to the instruction.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [19:1]

Reserved, RES0.

## TI, bit [0]

Trapped instruction. Possible values of this bit are:

| TI   | Meaning      |
|------|--------------|
| 0b0  | WFI trapped. |
| 0b1  | WFEtrapped.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Additional Information for ISS encoding for Exception from a WFI or WFE instruction

HCR.{TWE, TWI} describe the configuration settings for this trap.

## ISS encoding for Exception from an MCR or MRC access

<!-- image -->

## CV, bit [24]

Condition code valid. Possible values of this bit are:

| CV   | Meaning                     |
|------|-----------------------------|
| 0b0  | The CONDfield is not valid. |
| 0b1  | The CONDfield is valid.     |

When an A32 instruction is trapped, CV is set to 1.

When a T32 instruction is trapped, it is IMPLEMENTATION DEFINED whether CV is set to 1 or set to 0. For more information, see the description of the COND field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## COND, bits [23:20]

The condition code for the trapped instruction.

When an A32 instruction is trapped, CV is set to 1 and:

- If the instruction is conditional, COND is set to the condition code field value from the instruction.
- If the instruction is unconditional, COND is set to 0b1110 .

Aconditional A32 instruction that is known to pass its condition code check can be presented either:

- With COND set to 0b1110 , the value for unconditional.
- With the COND value held in the instruction.

When a T32 instruction is trapped, it is IMPLEMENTATION DEFINED whether:

- CVis set to 0 and COND is set to an UNKNOWN value. Software must examine the SPSR.IT field to determine the condition, if any, of the T32 instruction.
- CVis set to 1 and COND is set to the condition code for the condition that applied to the instruction.

For an implementation that, for both T32 and A32 instructions, takes an exception on a trapped conditional instruction only if the instruction passes its condition code check, these definitions mean that when CV is set to 1 it is IMPLEMENTATION DEFINED whether the COND field is set to 0b1110 , or to the value of any condition that applied to the instruction.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Opc2, bits [19:17]

The Opc2 value from the issued instruction.

For a trapped VMRS access, holds the value 0b000 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Opc1, bits [16:14]

The Opc1 value from the issued instruction.

For a trapped VMRS access, holds the value 0b111 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CRn, bits [13:10]

The CRn value from the issued instruction.

For a trapped VMRS access, holds the reg field from the VMRS instruction encoding.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [9]

Reserved, RES0.

## Rt, bits [8:5]

The Rt value from the issued instruction, the general-purpose register used for the transfer.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CRm, bits [4:1]

The CRm value from the issued instruction.

For a trapped VMRS access, holds the value 0b0000 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Direction, bit [0]

Indicates the direction of the trapped instruction.

| Direction   | Meaning                                                 |
|-------------|---------------------------------------------------------|
| 0b0         | Write to System register space. MCRinstruction.         |
| 0b1         | Read from System register space. MRCorVMRS instruction. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Additional Information for ISS encoding for Exception from an MCR or MRC access

The following fields describe configuration settings for traps from an MCR or MCR access using coproc 0b1111 that are reported using EC value 0b000011 :

- HCR.{TID1, TID2, TID3}, for Non-secure accesses to the ID registers at EL0 and EL1, trapped to EL2.
- HCR.TIDCP, for Non-secure accesses to lockdown, DMA, and TCM operations at EL0 and EL1, trapped to EL2.
- HCR.{TSW, TPC, TPU}, for Non-secure execution of cache maintenance instructions at EL1, trapped to EL2.
- HCR.TTLB, for Non-secure execution of TLB maintenance instructions at EL1, trapped to EL2.
- HCR.TAC, for Non-secure accesses to the Auxiliary Control Register at EL1, trapped to EL2.
- HDCR.{TPM, TPMCR}, for Non-secure accesses to Performance Monitors registers at EL0 and EL1, trapped to EL2.
- HCPTR.TAM, for Non-secure accesses to Activity Monitor registers at EL0 and EL1, trapped to EL2.
- HCPTR.TCPAC, for Non-secure accesses to the CPACR at EL1, trapped to EL2.
- HCR.{TRVM, TVM}, for Non-secure accesses to virtual memory control registers at EL1, trapped to EL2.
- HSTR.T&lt;n&gt;, for Non-secure accesses to System registers in the (coproc == 1111) encoding space at EL0 and EL1, trapped to EL2.
- HDCR.TTRF, for Non-secure accesses to trace filter control registers from System register, trapped to EL2.
- CNTHCTL.PL1PCEN, for Non-secure accesses to the Generic Timer registers at EL0 and EL1, trapped to EL2.
- HCR2.TERR, for Non-secure accesses to the RAS error record registers at EL1, trapped to EL2.

The following fields describe configuration settings for traps from an MCR or MRC access using coproc 0b1110 that are reported using EC value 0b000101 :

- HCR.TID0, for Non-secure accesses to the Primary device identification registers at EL0 and EL1, trapped to EL2.
- HCPTR.TTA, for Non-secure accesses to trace registers from System register, trapped to EL2.
- HDCR.TDRA, for Non-secure accesses to Debug ROM registers from System register, trapped to EL2.
- HDCR.TDOSA, for Non-secure accesses to powerdown debug registers from System register, trapped to EL2.
- HDCR.TDA, for Non-secure accesses to debug registers from System register, trapped to EL2.

The following fields describes configuration settings for traps from a VMSR or VMRS access that are reported using EC value 0b001000 :

- HCR.TID0, for Non-secure accesses to the Primary device identification registers at EL1, for ID group traps trapped to EL2.
- HCR.TID3, for Non-secure accesses to the Detailed feature identification registers at EL0 and EL1, for ID group traps trapped to EL2.
- HCPTR.{TCP10, TCP11}, for Non-secure accesses to FPSCR, FPSID, FPEXC, MVFR0, MVFR1, and MVFR2, trapped to EL2.

## ISS encoding for Exception from an MCRR or MRRC access

<!-- image -->

## CV, bit [24]

Condition code valid. Possible values of this bit are:

| CV   | Meaning                     |
|------|-----------------------------|
| 0b0  | The CONDfield is not valid. |
| 0b1  | The CONDfield is valid.     |

When an A32 instruction is trapped, CV is set to 1.

When a T32 instruction is trapped, it is IMPLEMENTATION DEFINED whether CV is set to 1 or set to 0. For more information, see the description of the COND field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## COND, bits [23:20]

The condition code for the trapped instruction.

When an A32 instruction is trapped, CV is set to 1 and:

- If the instruction is conditional, COND is set to the condition code field value from the instruction.
- If the instruction is unconditional, COND is set to 0b1110 .

Aconditional A32 instruction that is known to pass its condition code check can be presented either:

- With COND set to 0b1110 , the value for unconditional.

- With the COND value held in the instruction.

When a T32 instruction is trapped, it is IMPLEMENTATION DEFINED whether:

- CVis set to 0 and COND is set to an UNKNOWN value. Software must examine the SPSR.IT field to determine the condition, if any, of the T32 instruction.
- CVis set to 1 and COND is set to the condition code for the condition that applied to the instruction.

For an implementation that, for both T32 and A32 instructions, takes an exception on a trapped conditional instruction only if the instruction passes its condition code check, these definitions mean that when CV is set to 1 it is IMPLEMENTATION DEFINED whether the COND field is set to 0b1110 , or to the value of any condition that applied to the instruction.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Opc1, bits [19:16]

The Opc1 value from the issued instruction.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [15:14]

Reserved, RES0.

## Rt2, bits [13:10]

The Rt2 value from the issued instruction, the second general-purpose register used for the transfer.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [9]

Reserved, RES0.

## Rt, bits [8:5]

The Rt value from the issued instruction, the first general-purpose register used for the transfer.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CRm, bits [4:1]

The CRm value from the issued instruction.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Direction, bit [0]

Indicates the direction of the trapped instruction.

| Direction   | Meaning                                           |
|-------------|---------------------------------------------------|
| 0b0         | Write to System register space. MCRRinstruction.  |
| 0b1         | Read from System register space. MRRCinstruction. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Additional Information for ISS encoding for Exception from an MCRR or MRRC access

The following fields describe configuration settings for traps from an MCRR or MRRC access using coproc 0b1111 that are reported using EC value 0b000100 :

- HCR.{TRVM, TVM}, for Non-secure accesses to virtual memory control registers at EL1, trapped to EL2.
- HDCR.TPM, for Non-secure accesses to Performance Monitors registers at EL0 and EL1, trapped to EL2.
- HCPTR.TAM, for Non-secure accesses to Activity Monitor registers at EL0 and EL1, trapped to EL2.
- CNTHCTL.{PL1PCEN, PL1PCTEN}, for Non-secure accesses to the Generic Timer registers at EL0 and EL1, trapped to EL2.
- HSTR.T&lt;n&gt;, for Non-secure accesses to System registers in the (coproc == 1111) encoding space at EL0 and EL1, trapped to EL2.
- HCR2.TERR, for Non-secure accesses to the RAS error record registers at EL1, trapped to EL2.

The following fields describe configuration settings for traps from an MCRR or MRRC access using coproc 0b1110 that are reported using EC value 0b001100 :

- HCPTR.TTA, for Non-secure accesses to trace registers from System register, trapped to EL2.
- HDCR.TDRA, for Non-secure accesses to Debug ROM registers from System register, trapped to EL2.

## ISS encoding for Exception from an LDC or STC instruction

<!-- image -->

## CV, bit [24]

Condition code valid. Possible values of this bit are:

| CV   | Meaning                     |
|------|-----------------------------|
| 0b0  | The CONDfield is not valid. |
| 0b1  | The CONDfield is valid.     |

When an A32 instruction is trapped, CV is set to 1.

When a T32 instruction is trapped, it is IMPLEMENTATION DEFINED whether CV is set to 1 or set to 0. For more information, see the description of the COND field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## COND, bits [23:20]

The condition code for the trapped instruction.

When an A32 instruction is trapped, CV is set to 1 and:

- If the instruction is conditional, COND is set to the condition code field value from the instruction.
- If the instruction is unconditional, COND is set to 0b1110 .

Aconditional A32 instruction that is known to pass its condition code check can be presented either:

- With COND set to 0b1110 , the value for unconditional.
- With the COND value held in the instruction.

When a T32 instruction is trapped, it is IMPLEMENTATION DEFINED whether:

- CVis set to 0 and COND is set to an UNKNOWN value. Software must examine the SPSR.IT field to determine the condition, if any, of the T32 instruction.
- CVis set to 1 and COND is set to the condition code for the condition that applied to the instruction.

For an implementation that, for both T32 and A32 instructions, takes an exception on a trapped conditional instruction only if the instruction passes its condition code check, these definitions mean that when CV is set to 1 it is IMPLEMENTATION DEFINED whether the COND field is set to 0b1110 , or to the value of any condition that applied to the instruction.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## imm8, bits [19:12]

The immediate value from the issued instruction.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:9]

Reserved, RES0.

## Rn, bits [8:5]

The Rn value from the issued instruction. Valid only when AM[2] is 0, indicating an immediate form of the LDCor STC instruction.

When AM[2] is 1, indicating a literal form of the LDC or STC instruction, this field is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Offset, bit [4]

Indicates whether the offset is added or subtracted:

| Offset   | Meaning          |
|----------|------------------|
| 0b0      | Subtract offset. |
| 0b1      | Add offset.      |

This bit corresponds to the U bit in the instruction encoding.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## AM, bits [3:1]

Addressing mode. The permitted values of this field are:

| AM    | Meaning                                                                                                                                                 |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b000 | Immediate unindexed.                                                                                                                                    |
| 0b001 | Immediate post-indexed.                                                                                                                                 |
| 0b010 | Immediate offset.                                                                                                                                       |
| 0b011 | Immediate pre-indexed.                                                                                                                                  |
| 0b100 | Literal unindexed. LDCinstruction in A32 instruction set only. For a trapped STC instruction or a trapped T32 LDCinstruction this encoding is reserved. |
| 0b110 | Literal offset. LDCinstruction only. For a trapped STC instruction, this encoding is reserved.                                                          |

The values 0b101 and 0b111 are reserved. The effect of programming this field to a reserved value is that behavior is CONSTRAINED UNPREDICTABLE.

Bit [2] in this subfield indicates the instruction form, immediate or literal.

Bits [1:0] in this subfield correspond to the bits {P, W} in the instruction encoding.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Direction, bit [0]

Indicates the direction of the trapped instruction.

| Direction   | Meaning                           |
|-------------|-----------------------------------|
| 0b0         | Write to memory. STC instruction. |
| 0b1         | Read from memory. LDCinstruction. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Additional Information for ISS encoding for Exception from an LDC or STC instruction

HDCR.TDA describes the configuration settings for the trap that is reported using EC value 0b000110 .

## ISS encoding for Exception from an access to SIMD or floating-point functionality, resulting from HCPTR

<!-- image -->

Excludes exceptions that occur because Advanced SIMD and floating-point functionality is not implemented, or because the value of HCR.TGE or HCR\_EL2.TGE is 1. These are reported with EC value 0b000000 .

## CV, bit [24]

Condition code valid. Possible values of this bit are:

| CV   | Meaning                     |
|------|-----------------------------|
| 0b0  | The CONDfield is not valid. |
| 0b1  | The CONDfield is valid.     |

When an A32 instruction is trapped, CV is set to 1.

When a T32 instruction is trapped, it is IMPLEMENTATION DEFINED whether CV is set to 1 or set to 0. For more information, see the description of the COND field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## COND, bits [23:20]

The condition code for the trapped instruction.

When an A32 instruction is trapped, CV is set to 1 and:

- If the instruction is conditional, COND is set to the condition code field value from the instruction.
- If the instruction is unconditional, COND is set to 0b1110 .

Aconditional A32 instruction that is known to pass its condition code check can be presented either:

- With COND set to 0b1110 , the value for unconditional.
- With the COND value held in the instruction.

When a T32 instruction is trapped, it is IMPLEMENTATION DEFINED whether:

- CVis set to 0 and COND is set to an UNKNOWN value. Software must examine the SPSR.IT field to determine the condition, if any, of the T32 instruction.
- CVis set to 1 and COND is set to the condition code for the condition that applied to the instruction.

For an implementation that, for both T32 and A32 instructions, takes an exception on a trapped conditional instruction only if the instruction passes its condition code check, these definitions mean that when CV is set to 1 it is IMPLEMENTATION DEFINED whether the COND field is set to 0b1110 , or to the value of any condition that applied to the instruction.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [19:6]

Reserved, RES0.

## TA, bit [5]

Indicates trapped use of Advanced SIMD functionality.

| TA   | Meaning                                                                 |
|------|-------------------------------------------------------------------------|
| 0b0  | Exception was not caused by trapped use of Advanced SIMD functionality. |
| 0b1  | Exception was caused by trapped use of Advanced SIMD functionality.     |

Any use of an Advanced SIMD instruction that is not also a floating-point instruction that is trapped to Hyp mode because of a trap configured in the HCPTR sets this bit to 1.

For a list of these instructions, see 'Controls of Advanced SIMD operation that do not apply to floating-point operation'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [4]

Reserved, RES0.

## coproc, bits [3:0]

When the HSR.TA field returns the value 1, this field returns the value 0b1010 . Otherwise, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Additional Information for ISS encoding for Exception from an access to SIMD or floating-point functionality, resulting from HCPTR

The following fields describe the configuration settings for the traps that are reported using EC value 0b000111 :

- HCPTR.{TCP11, TCP10}, for Non-secure accesses to the SIMD and floating-point registers, trapped to EL2.
- HCPTR.TASE, for Non-secure accesses to Advanced SIMD functionality, trapped to EL2.

## ISS encoding for Exception from HVC or SVC instruction execution

<!-- image -->

## Bits [24:16]

Reserved, RES0.

## imm16, bits [15:0]

The value of the immediate field from the HVC or SVC instruction.

For an HVC instruction, this is the value of the imm16 field of the issued instruction.

For an SVC instruction:

- If the instruction is unconditional, then:
- For the T32 instruction, this field is zero-extended from the imm8 field of the instruction.
- For the A32 instruction, this field is the bottom 16 bits of the imm24 field of the instruction.
- For the T32 instruction, this field is zero-extended from the imm8 field of the instruction.For the A32 instruction, this field is the bottom 16 bits of the imm24 field of the instruction.
- If the instruction is conditional, this field is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Additional Information for ISS encoding for Exception from HVC or SVC instruction execution

The HVC instruction is unconditional, and a conditional SVC instruction generates an exception only if it passes its condition code check. Therefore, the syndrome information for these exceptions does not require conditionality information.

'Supervisor Call exception, when the value of HCR.TGE is 1' describes the configuration settings for the trap reported with EC value 0b010001 .

## ISS encoding for Exception from SMC instruction execution

<!-- image -->

## CV, bit [24]

Condition code valid. Possible values of this bit are:

| CV   | Meaning                     |
|------|-----------------------------|
| 0b0  | The CONDfield is not valid. |
| 0b1  | The CONDfield is valid.     |

When an A32 instruction is trapped, CV is set to 1.

When a T32 instruction is trapped, it is IMPLEMENTATION DEFINED whether CV is set to 1 or set to 0. For more information, see the description of the COND field.

This field is valid only if CCKNOWNPASS is 1, otherwise it is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## COND, bits [23:20]

The condition code for the trapped instruction.

When an A32 instruction is trapped, CV is set to 1 and:

- If the instruction is conditional, COND is set to the condition code field value from the instruction.
- If the instruction is unconditional, COND is set to 0b1110 .

Aconditional A32 instruction that is known to pass its condition code check can be presented either:

- With COND set to 0b1110 , the value for unconditional.
- With the COND value held in the instruction.

When a T32 instruction is trapped, it is IMPLEMENTATION DEFINED whether:

- CVis set to 0 and COND is set to an UNKNOWN value. Software must examine the SPSR.IT field to determine the condition, if any, of the T32 instruction.
- CVis set to 1 and COND is set to the condition code for the condition that applied to the instruction.

For an implementation that, for both T32 and A32 instructions, takes an exception on a trapped conditional instruction only if the instruction passes its condition code check, these definitions mean that when CV is set to 1 it is IMPLEMENTATION DEFINED whether the COND field is set to 0b1110 , or to the value of any condition that applied to the instruction.

This field is valid only if CCKNOWNPASS is 1, otherwise it is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CCKNOWNPASS,bit [19]

Indicates whether the instruction might have failed its condition code check.

| CCKNOWNPASS   | Meaning                                                                                    |
|---------------|--------------------------------------------------------------------------------------------|
| 0b0           | The instruction was unconditional, or was conditional and passed its condition code check. |
| 0b1           | The instruction was conditional, and might have failed its condition code check.           |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [18:0]

Reserved, RES0.

Additional Information for ISS encoding for Exception from SMC instruction execution

HCR.TSC describes the configuration settings for this trap for instructions executed in Non-secure EL1.

## ISS encoding for Exception from a Prefetch Abort

<!-- image -->

## Bits [24:11]

Reserved, RES0.

## FnV, bit [10]

FAR not Valid, for a synchronous External abort other than a synchronous External abort on a translation table walk.

| FnV   | Meaning                                         |
|-------|-------------------------------------------------|
| 0b0   | HIFAR is valid.                                 |
| 0b1   | HIFAR is not valid, and holds an UNKNOWN value. |

This field is valid only if the IFSC code is 0b010000 . It is RES0 for all other aborts.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EA, bit [9]

External abort type. This bit can provide an IMPLEMENTATION DEFINED classification of External aborts.

For any abort other than an External abort this bit returns a value of 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [8]

Reserved, RES0.

## S1PTW, bit [7]

For a stage 2 fault, indicates whether the fault was a stage 2 fault on an access made for a stage 1 translation table walk:

| S1PTW   | Meaning                                                                             |
|---------|-------------------------------------------------------------------------------------|
| 0b0     | Fault not on a stage 2 translation for a stage 1 translation table walk.            |
| 0b1     | Fault on the stage 2 translation of an access for a stage 1 translation table walk. |

For any abort other than a stage 2 fault this bit is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [6]

Reserved, RES0.

## IFSC, bits [5:0]

Instruction Fault Status Code. Possible values of this field are:

| IFSC     | Meaning                                                        | Applies when   |
|----------|----------------------------------------------------------------|----------------|
| 0b000000 | Address size fault in translation table base register.         |                |
| 0b000001 | Address size fault, level 1.                                   |                |
| 0b000010 | Address size fault, level 2.                                   |                |
| 0b000011 | Address size fault, level 3.                                   |                |
| 0b000101 | Translation fault, level 1.                                    |                |
| 0b000110 | Translation fault, level 2.                                    |                |
| 0b000111 | Translation fault, level 3.                                    |                |
| 0b001001 | Access flag fault, level 1.                                    |                |
| 0b001010 | Access flag fault, level 2.                                    |                |
| 0b001011 | Access flag fault, level 3.                                    |                |
| 0b001101 | Permission fault, level 1.                                     |                |
| 0b001110 | Permission fault, level 2.                                     |                |
| 0b001111 | Permission fault, level 3.                                     |                |
| 0b010000 | Synchronous External abort, not on translation table walk.     |                |
| 0b010101 | Synchronous External abort on translation table walk, level 1. |                |
| 0b010110 | Synchronous External abort on translation table walk, level 2. |                |

| IFSC     | Meaning                                                                              | Applies when                |
|----------|--------------------------------------------------------------------------------------|-----------------------------|
| 0b010111 | Synchronous External abort on translation table walk, level 3.                       |                             |
| 0b011000 | Synchronous parity or ECC error on memory access, not on translation table walk.     | FEAT_RAS is not implemented |
| 0b011101 | Synchronous parity or ECC error on memory access on translation table walk, level 1. | FEAT_RAS is not implemented |
| 0b011110 | Synchronous parity or ECC error on memory access on translation table walk, level 2. | FEAT_RAS is not implemented |
| 0b011111 | Synchronous parity or ECC error on memory access on translation table walk, level 3. | FEAT_RAS is not implemented |
| 0b100010 | Debug exception.                                                                     |                             |
| 0b110000 | TLB conflict abort.                                                                  |                             |

All other values are reserved.

For more information about the lookup level associated with a fault, see 'The level associated with MMU faults on a Long-descriptor translation table lookup'.

If the S1PTW bit is set, then the level refers the level of the stage2 translation that is translating a stage 1 translation walk.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Additional Information for ISS encoding for Exception from a Prefetch Abort

The following sections describe cases where Prefetch Abort exceptions can be routed to Hyp mode, generating exceptions that are reported in the HSR with EC value 0b100000 :

- 'Abort exceptions, when the value of HCR.TGE is 1'.
- 'Routing debug exceptions to EL2 using AArch32'.

## ISS encoding for Exception from an Illegal state or PC alignment fault

<!-- image -->

| 24   | 0   |
|------|-----|

## Bits [24:0]

Reserved, RES0.

## Additional Information for ISS encoding for Exception from an Illegal state or PC alignment fault

For more information about the Illegal state exception, see:

- 'Illegal changes to PSTATE.M'.
- 'Illegal return events from AArch32 state'.
- 'Legal returns that set PSTATE.IL to 1'.
- 'The Illegal Execution state exception'.

For more information about the PC alignment fault exception, see 'Branching to an unaligned PC'.

## ISS encoding for Exception from a Data Abort

<!-- image -->

## ISV, bit [24]

Instruction Syndrome Valid. Indicates whether the syndrome information in ISS[23:14] is valid.

| ISV   | Meaning                                             |
|-------|-----------------------------------------------------|
| 0b0   | No valid instruction syndrome. ISS[23:14] are RES0. |
| 0b1   | ISS[23:14] hold a valid instruction syndrome.       |

This bit is 0 for all faults except Data Abort exceptions generated by stage 2 address translations for which all the following apply to the instruction that generated the Data Abort exception:

- The instruction is an LDR, LDA, LDRT, LDRSH, LDRSHT, LDRH, LDAH, LDRHT, LDRSB, LDRSBT, LDRB, LDAB, LDRBT, STR, STL, STRT, STRH, STLH, STRHT, STRB, STLB, or STRBT instruction.
- The instruction is not performing register writeback.
- The instruction is not using the PC as a source or destination register.

For these cases, ISV is UNKNOWN if the exception was generated in Debug state in Memory access mode, as described in 'Data Abort exceptions in Memory access mode', and otherwise indicates whether ISS[23:14] hold a valid syndrome.

Note

In the A32 instruction set, LDR*T and STR*T instructions always perform register writeback and therefore never return a valid instruction syndrome.

When FEAT\_RAS is implemented, ISV is 0 for any synchronous External abort.

ISV is set to 0 on a stage 2 abort on a stage 1 translation table walk.

When FEAT\_RAS is not implemented, it is IMPLEMENTATION DEFINED whether ISV is set to 1 or 0 on a synchronous External abort on a stage 2 translation table walk.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SAS, bits [23:22]

Syndrome Access Size. When ISV is 1, indicates the size of the access attempted by the faulting operation.

| SAS   | Meaning    |
|-------|------------|
| 0b00  | Byte       |
| 0b01  | Halfword   |
| 0b10  | Word       |
| 0b11  | Doubleword |

This field is UNKNOWN when the value of ISV is UNKNOWN.

This field is RES0 when the value of ISV is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SSE, bit [21]

Syndrome Sign Extend. When ISV is 1, for a byte, halfword, or word load operation, indicates whether the data item must be sign extended. For these cases, the possible values of this bit are:

| SSE   | Meaning                          |
|-------|----------------------------------|
| 0b0   | Sign-extension not required.     |
| 0b1   | Data item must be sign-extended. |

For all other operations this bit is 0.

This field is UNKNOWN when the value of ISV is UNKNOWN.

This field is RES0 when the value of ISV is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [20]

Reserved, RES0.

## SRT, bits [19:16]

Syndrome Register Transfer. When ISV is 1, the register number of the Rt operand of the faulting instruction.

This field is UNKNOWN when the value of ISV is UNKNOWN.

This field is RES0 when the value of ISV is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [15]

Reserved, RES0.

## AR, bit [14]

Acquire/Release. When ISV is 1, the possible values of this bit are:

| AR   | Meaning                                             |
|------|-----------------------------------------------------|
| 0b0  | Instruction did not have acquire/release semantics. |
| 0b1  | Instruction did have acquire/release semantics.     |

This field is UNKNOWN when the value of ISV is UNKNOWN.

This field is RES0 when the value of ISV is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [13:12]

Reserved, RES0.

## Bits [11:10]

## When FEAT\_RAS is implemented:

## AET, bits [11:10]

Asynchronous Error Type. When DFSC is 0b010001 , describes the PE error state after taking the SError exception.

| AET   | Meaning                    |
|-------|----------------------------|
| 0b00  | Uncontainable (UC).        |
| 0b01  | Unrecoverable state (UEU). |
| 0b10  | Restartable state (UEO).   |
| 0b11  | Recoverable state (UER).   |

On a synchronous Data Abort exception, this field is RES0.

In the event of multiple errors taken as a single SError exception, the overall PE error state is reported.

<!-- image -->

Software can use this information to determine what recovery might be possible. The recovery software must also examine any implemented fault records to determine the location and extent of the error.

When FEAT\_RAS is not implemented, or when DFSC is not 0b010001 :

- Bit[11] is RES0.
- Bit[10] forms the FnV field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

## FnV, bit [0] of bits [11:10]

FAR not Valid, for a synchronous External abort other than a synchronous External abort on a translation table walk.

| FnV   | Meaning                                         |
|-------|-------------------------------------------------|
| 0b0   | HDFAR is valid.                                 |
| 0b1   | HDFAR is not valid, and holds an UNKNOWN value. |

When FEAT\_RAS is not implemented, this field is valid only if DFSC is 0b010000 . It is RES0 for all other aborts.

When FEAT\_RAS is implemented:

- If DFSC is 0b010000 , this field is valid.

- If DFSC is 0b010001 , this bit forms part of the AET field, becoming AET[0].
- This field is RES0 for all other aborts.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EA, bit [9]

External Abort type. This bit can provide an IMPLEMENTATION DEFINED classification of External aborts.

For any abort other than an External abort this bit returns a value of 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CM, bit [8]

Cache Maintenance. For a synchronous fault, identifies fault that comes from a cache maintenance or address translation instruction. For synchronous faults, the possible values of this bit are:

| CM   | Meaning                                                                        |
|------|--------------------------------------------------------------------------------|
| 0b0  | Fault not generated by a cache maintenance or address translation instruction. |
| 0b1  | Fault generated by a cache maintenance or address translation instruction.     |

For an asynchronous Data Abort exception, this bit is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## S1PTW, bit [7]

For a stage 2 fault, indicates whether the fault was a stage 2 fault on an access made for a stage 1 translation table walk:

| S1PTW   | Meaning                                                                             |
|---------|-------------------------------------------------------------------------------------|
| 0b0     | Fault not on a stage 2 translation for a stage 1 translation table walk.            |
| 0b1     | Fault on the stage 2 translation of an access for a stage 1 translation table walk. |

For any abort other than a stage 2 fault this bit is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## WnR, bit [6]

Write not Read. Indicates whether a synchronous abort was caused by a write instruction or a read instruction.

| WnR   | Meaning                              |
|-------|--------------------------------------|
| 0b0   | Abort caused by a read instruction.  |
| 0b1   | Abort caused by a write instruction. |

For faults on cache maintenance and address translation instructions, this bit always returns a value of 1.

On an asynchronous Data Abort exception:

- When FEAT\_RAS is not implemented, this bit is UNKNOWN.
- When FEAT\_RAS is implemented, this bit is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## DFSC, bits [5:0]

Data Fault Status Code. Possible values of this field are:

| DFSC     | Meaning                                                                          | Applies when                |
|----------|----------------------------------------------------------------------------------|-----------------------------|
| 0b000000 | Address size fault in translation table base register.                           |                             |
| 0b000001 | Address size fault, level 1.                                                     |                             |
| 0b000010 | Address size fault, level 2.                                                     |                             |
| 0b000011 | Address size fault, level 3.                                                     |                             |
| 0b000101 | Translation fault, level 1.                                                      |                             |
| 0b000110 | Translation fault, level 2.                                                      |                             |
| 0b000111 | Translation fault, level 3.                                                      |                             |
| 0b001001 | Access flag fault, level 1.                                                      |                             |
| 0b001010 | Access flag fault, level 2.                                                      |                             |
| 0b001011 | Access flag fault, level 3.                                                      |                             |
| 0b001101 | Permission fault, level 1.                                                       |                             |
| 0b001110 | Permission fault, level 2.                                                       |                             |
| 0b001111 | Permission fault, level 3.                                                       |                             |
| 0b010000 | Synchronous External abort, not on translation table walk.                       |                             |
| 0b010001 | Asynchronous SError exception.                                                   |                             |
| 0b010101 | Synchronous External abort on translation table walk, level 1.                   |                             |
| 0b010110 | Synchronous External abort on translation table walk, level 2.                   |                             |
| 0b010111 | Synchronous External abort on translation table walk, level 3.                   |                             |
| 0b011000 | Synchronous parity or ECC error on memory access, not on translation table walk. | FEAT_RAS is not implemented |
| 0b011001 | Asynchronous SError exception, from a parity or ECC error on memory access.      | FEAT_RAS is not implemented |

| DFSC     | Meaning                                                                              | Applies when                |
|----------|--------------------------------------------------------------------------------------|-----------------------------|
| 0b011101 | Synchronous parity or ECC error on memory access on translation table walk, level 1. | FEAT_RAS is not implemented |
| 0b011110 | Synchronous parity or ECC error on memory access on translation table walk, level 2. | FEAT_RAS is not implemented |
| 0b011111 | Synchronous parity or ECC error on memory access on translation table walk, level 3. | FEAT_RAS is not implemented |
| 0b100001 | Alignment fault.                                                                     |                             |
| 0b100010 | Debug exception.                                                                     |                             |
| 0b110000 | TLB conflict abort.                                                                  |                             |
| 0b110100 | IMPLEMENTATION DEFINED fault (Lockdown).                                             |                             |
| 0b110101 | IMPLEMENTATION DEFINED fault (Unsupported Exclusive access).                         |                             |

All other values are reserved.

For more information about the lookup level associated with a fault, see 'The level associated with MMU faults on a Long-descriptor translation table lookup'.

If the S1PTW bit is set, then the level refers the level of the stage2 translation that is translating a stage 1 translation walk.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Additional Information for ISS encoding for Exception from a Data Abort

The following describe cases where Data Abort exceptions can be routed to Hyp mode, generating exceptions that are reported in the HSR with EC value 0b100100 :

- 'Abort exceptions, when the value of HCR.TGE is 1'.
- 'Routing debug exceptions to EL2 using AArch32'.

The following describe cases that can cause a Data Abort exception that is taken to Hyp mode, and reported in the HSR with EC value of 0b100000 or 0b100100 :

- 'Hyp mode control of Non-secure access permissions'.
- 'Memory fault reporting in Hyp mode'.

## Accessing HSR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0101 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == '1' ↪ → then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = HSR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = HSR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0101 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T5 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T5 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then HSR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else HSR = R[t];
```