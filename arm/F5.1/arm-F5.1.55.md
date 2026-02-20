## F5.1.55 HVC

Hypervisor Call causes a Hypervisor Call exception. For more information, see Hypervisor Call (HVC) exception. Software executing at EL1 can use this instruction to call the hypervisor to request a service.

The HVC instruction is UNDEFINED:

- When EL3 is implemented and using AArch64, and SCR\_EL3.HCE is set to 0.
- In Non-secure EL1 modes when EL3 is implemented and using AArch32, and SCR.HCE is set to 0.
- When EL3 is not implemented and either HCR\_EL2.HCD is set to 1 or HCR.HCD is set to 1.
- When EL2 is not implemented.
- In Secure state, if EL2 is not enabled in the current Security state.
- In User mode.

The HVC instruction is CONSTRAINED UNPREDICTABLE in Hyp mode when EL3 is implemented and using AArch32, and SCR.HCE is set to 0.

On executing an HVC instruction, the HSR, Hyp Syndrome Register reports the exception as a Hypervisor Call exception, using the EC value 0x12 , and captures the value of the immediate argument, see Use of the HSR.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

<!-- image -->

## Decode for this encoding

```
if cond != '1110' then UNPREDICTABLE; end constant bits(16) imm16 = imm12:imm4;
```

## CONSTRAINED UNPREDICTABLE behavior

If cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes unconditionally.
- The instruction executes conditionally.

T1

<!-- image -->

## Encoding

Listing F5-46

```
HVC{<q>} {#}<imm16>
```

## Decode for this encoding

```
constant bits(16) imm16 = imm4:imm12; if InITBlock() then UNPREDICTABLE;
```

```
end
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;q&gt;

See Standard assembler syntax fields. An HVC instruction must be unconditional.

## &lt;imm16&gt;

For the 'A1' variant: is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm12:imm4' field. This value is for assembly and disassembly only. It is reported in the HSR but otherwise is ignored by hardware. An HVC handler might interpret imm16, for example to determine the required service.

For the 'T1' variant: is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm4:imm12' field. This value is for assembly and disassembly only. It is reported in the HSR but otherwise is ignored by hardware. An HVC handler might interpret imm16, for example to determine the required service.

## Operation

```
EncodingSpecificOperations(); if PSTATE.EL IN {EL0, EL3} || !EL2Enabled() then UNDEFINED; end bit hvc_enable; if HaveEL(EL3) then if ELUsingAArch32(EL3) then if SCR.HCE == '0' && PSTATE.EL == EL2 then UNPREDICTABLE; end hvc_enable = SCR.HCE; else hvc_enable = SCR_EL3.HCE; end else hvc_enable = if ELUsingAArch32(EL2) then NOT(HCR.HCD) else end if hvc_enable == '0' then UNDEFINED; else AArch32.CallHypervisor(imm16); end
```

## CONSTRAINED UNPREDICTABLE behavior

If ELUsingAArch32(EL3) &amp;&amp; SCR.HCE == '0' &amp;&amp; PSTATE.EL == EL2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .

```
NOT(HCR_EL2.HCD);
```

Listing F5-47

Listing F5-48