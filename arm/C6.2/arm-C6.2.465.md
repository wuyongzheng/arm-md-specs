## C6.2.465 SVC

Supervisor call

This instruction causes an exception to be taken to EL1.

On executing an SVC instruction, the PE records the exception as a Supervisor Call exception in ESR\_ELx, using the EC syndrome value 0x15 , and the value of the immediate argument.

<!-- image -->

<!-- image -->

## Assembler Symbols

&lt;imm&gt;

Is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm16' field.

## Operation

```
AArch64.CheckForSVCTrap(imm); AArch64.CallSupervisor(imm);
```
