## F5.1.193 SMC

Secure Monitor Call causes a Secure Monitor Call exception. For more information, see Secure Monitor Call (SMC) exception.

SMC is available only for software executing at EL1 or higher. It is UNDEFINED in User mode.

If the values of HCR.TSC and SCR.SCD are both 0, execution of an SMC instruction at EL1 or higher generates a Secure Monitor Call exception that is taken to EL3. When EL3 is using AArch32 this exception is taken to Monitor mode. When EL3 is using AArch64, it is the SCR\_EL3.SMD bit, rather than the SCR.SCD bit, that can change the effect of executing an SMC instruction.

If the value of HCR.TSC is 1, execution of an SMC instruction in a Non-secure EL1 mode generates an exception that is taken to EL2, regardless of the value of SCR.SCD. When EL2 is using AArch32, this is a Hyp Trap exception that is taken to Hyp mode. For more information, see HCR.TSC.

If the value of HCR.TSC is 0 and the value of SCR.SCD is 1, the SMC instruction is:

- UNDEFINED in Non-secure state.
- CONSTRAINED UNPREDICTABLE if executed in Secure state at EL1 or higher.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

SMC{&lt;c&gt;}{&lt;q&gt;}

{#}&lt;imm4&gt;

## Decode for this encoding

// imm4 is for assembly/disassembly only and is ignored by hardware

T1

<!-- image -->

<!-- image -->

Listing F5-77

## Decode for this encoding

```
// imm4 is for assembly/disassembly only and is ignored by hardware if InITBlock() && !LastInITBlock() then UNPREDICTABLE; end
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## &lt;imm4&gt;

Is a 4-bit unsigned immediate value, in the range 0 to 15, encoded in the 'imm4' field. This is ignored by the PE. The Secure Monitor Call exception handler (Secure Monitor code) can use this value to determine what service is being requested, but Arm does not recommend this.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); AArch32.CheckForSMCUndefOrTrap(); if !ELUsingAArch32(EL3) then if SCR_EL3.SMD == '1' then // SMC disabled. UNDEFINED; end else if SCR.SCD == '1' then // SMC disabled if CurrentSecurityState() == SS_Secure then // Executes either as a NOP or UNALLOCATED. constant Constraint c = ConstrainUnpredictable(Unpredictable_SMD); assert c IN {Constraint_NOP, Constraint_UNDEF}; if c == Constraint_NOP then ExecuteAsNOP(); end end UNDEFINED; end end if !ELUsingAArch32(EL3) then AArch64.CallSecureMonitor(Zeros(16)); else AArch32.TakeSMCException(); end end
```

## CONSTRAINED UNPREDICTABLE behavior

If SCR.SCD == '1' &amp;&amp; CurrentSecurityState() == SS\_Secure , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

Listing F5-79