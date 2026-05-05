## C6.2.174 HVC

Hypervisor call

This instruction causes an exception to EL2. Software executing at EL1 can use this instruction to call the hypervisor to request a service.

The HVC instruction is UNDEFINED:

- When EL3 is implemented and SCR\_EL3.HCE is set to 0.
- When EL3 is not implemented and HCR\_EL2.HCD is set to 1.
- When EL2 is not implemented.
- At EL1 if EL2 is not enabled in the current Security state.
- At EL0.

On executing an HVC instruction, the PE records the exception as a Hypervisor Call exception in ESR\_ELx, using the EC syndrome value 0x16 , and the value of the immediate argument.

<!-- image -->

## Encoding

```
HVC #<imm>
```

## Decode for this encoding

```
if !HaveEL(EL2) then EndOfDecode(Decode_UNDEF);
```

```
constant bits(16) imm = imm16;
```

## Assembler Symbols

## &lt;imm&gt;

Is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm16' field.

## Operation

```
if PSTATE.EL == EL0 then UNDEFINED; if PSTATE.EL == EL1 && !EL2Enabled() then UNDEFINED; if !HaveEL(EL3) && HCR_EL2.HCD == '1' then UNDEFINED; if HaveEL(EL3) && SCR_EL3.HCE == '0' then UNDEFINED; AArch64.CallHypervisor(imm);
```
