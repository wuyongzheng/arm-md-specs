## C6.2.371 SMC

Secure monitor call

This instruction causes an exception to EL3.

SMC is available only for software executing at EL1 or higher. It is UNDEFINED at EL0.

If the values of HCR\_EL2.TSC and SCR\_EL3.SMD are both 0, execution of an SMC instruction at EL1 or higher generates a Secure Monitor Call exception, recording it in ESR\_ELx, using the EC syndrome value 0x17 , that is taken to EL3.

If the value of HCR\_EL2.TSC is 1 and EL2 is enabled in the current Security state, execution of an SMC instruction at EL1 generates an exception that is taken to EL2, regardless of the value of SCR\_EL3.SMD.

If the value of HCR\_EL2.TSC is 0 and the value of SCR\_EL3.SMD is 1, the SMC instruction is UNDEFINED.

<!-- image -->

## Encoding

SMC

#&lt;imm&gt;

## Decode for this encoding

```
constant bits(16) imm = imm16;
```

## Assembler Symbols

&lt;imm&gt;

Is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm16' field.

## Operation

```
if PSTATE.EL == EL0 then UNDEFINED; AArch64.CheckForSMCUndefOrTrap(imm);
```

AArch64.CallSecureMonitor(imm);
