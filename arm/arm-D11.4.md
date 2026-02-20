## D11.4 Exception returns

| I TRBJS   | When an exception is taken, information regarding where the exception was taken from is captured in various System registers, and is subsequently used to return from the exception. Such information is usually saved to memory and is therefore potentially vulnerable to a variety of attacks which could modify the return state. Given that exceptions can be taken from almost any location, exception returns are usually able to return to any location and therefore are quite powerful. Ensuring the exception return state is protected against unwanted modification provides additional protection against using exception returns to branch to any location.   |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G MDCFD   | FEAT_GCS provides means to protect exception return state from unwanted modification, for exceptions within the same Exception level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| G HVKNT   | FEAT_GCS uses the protection mechanisms provided by the Guarded Control Stack to protect exception return state, in addition to procedure return state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| G VQNZK   | FEAT_GCS provides protection against mis-use of exception return code sequences.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## D11.4.1 Pushing and popping exception return state

IKLWLQ

SSLHZY

Aset of instructions is provided to operate on the Guarded Control Stack specifically for exceptions and exception returns, to allow software to add entries and check entries.

- GCSPUSHX

This instruction creates a new Guarded Control Stack exception return record on the Guarded Control Stack containing the values of the ELR\_ELx and SPSR\_ELx for the current Exception level and the LR value. The intent is that such data is the contents of the ELR\_ELx and SPSR\_ELx, pushed soon after taking an exception. This instruction is more limited in its usage than GCSPUSHM , only allowing the ELR\_ELx, SPSR\_ELx and LR to be pushed. This instruction also avoids the exception return state being moved to general purpose registers before adding to the Guarded Control Stack, further reducing the attack surface.

- GCSPOPCX

This instruction pops a Guarded Control Stack exception return record from the top of the Guarded Control Stack and compares the values popped with the ELR\_ELx and SPSR\_ELx for the current Exception level and the LR value. If the values mismatch, a GCS Data Check exception is taken. The intent is that this instruction is used just before an exception return, to validate that the intended exception return state is the same as that which was pushed to the Guarded Control Stack on exception entry.

- GCSPOPX

This instruction pops a Guarded Control Stack exception return record from the top of the Guarded Control Stack. If the record is not a Guarded Control Stack exception return record, a GCS Data Check exception is taken. This instruction is intended to be used to remove a Guarded Control Stack exception return record, when modification of such a record is needed.

Exception handling software can use the GCSPUSHX instruction to save the exception return state to a memory location that is protected by the GCS permissions in stage 1 translations.

- Atypical preemptible operating system might employ a kernel stack for kernel execution on behalf of a thread. Software can create a Guarded Control Stack for each kernel stack and these instructions can be used to save the exception return state in the Guarded Control Stack that corresponds to the kernel stack of a thread.
- An interrupt handler might have its own stack that is different from the kernel stack of any thread. Software can create a Guarded Control Stack that corresponds to the interrupt stack and these instructions can be used to store the exception return state in that Guarded Control Stack.

ICCMMC PSTATE.EXLOCK is provided to allow software to ensure that the exception return state that is pushed to the Guarded Control Stack is the state of the PE when the exception was taken, and to ensure that once the exception return state is checked before an exception return that the values in ELR\_ELx and SPSR\_ELx are unable to be changed. When enabled, PSTATE.EXLOCK prevents MSR instructions from modifying the state of the ELR\_ELx and SPSR\_ELx, by causing such instructions to generate an EXLOCK Exception. When enabled, execution of an exception return instruction which targets the current Exception level will check PSTATE.EXLOCK and will set PSTATE.IL to cause an Illegal exception return.

- IRZZFL

The Guarded Control Stack exception return record pushed by the GCSPUSHX instruction contains a doubleword with the value 0x0000\_0000\_0000\_0009 . This value allows a Guarded Control Stack exception return record to be distinguishable from a Guarded Control Stack procedure return record, and allows the PE to ensure that an exception return does not use a procedure return address or a procedure return does not use an exception return address.

RTMRMG

- When a GCSPOPCX or GCSPOPX instruction is attempted where the top record on the Guarded Control Stack is a Guarded Control Stack procedure return record, the GCSPOPCX or GCSPOPX instruction detects the value in the lowest-addressed doubleword is not 0x0000\_0000\_0000\_0009 , and takes a GCS Data Check exception.
- When a procedure return instruction is attempted where the top record on the Guarded Control Stack is not a Guarded Control Stack procedure return record and therefore the bits [1:0] of the doubleword are not 0b00 , the procedure return will return to this location then take a PC Alignment exception.
- When a GCSPOPM instruction is attempted where the top record on the Guarded Control Stack is not a Guarded Control Stack procedure return record and therefore bits [1:0] of the value popped are not 0b00 , the GCSPOPM instruction takes a GCS Data Check exception.

RTNHNB A GCSPUSHX instruction executed at ELx, where x is 1 or greater:

- Performs a GCS exception push operation when all of the following are true:
- -The Guarded Control Stack at ELx is GCS Enabled.
- -The Effective value of GCSCR\_ELx.EXLOCKEN is 0 or PSTATE.EXLOCK is 1.
- Generates an EXLOCK Exception when all of the following are true:
- -The Guarded Control Stack at ELx is GCS Enabled.
- -The Effective value of GCSCR\_ELx.EXLOCKEN is 1 and PSTATE.EXLOCK is 0.
- Performs no operation if neither a GCS exception push operation nor an EXLOCK Exception is triggered.

Execution of GCSPUSHX at EL0 is UNDEFINED.

## RGWJCX AGCSexception push operation:

- Stores a Guarded Control Stack exception return record at the virtual address defined by the current Guarded Control Stack pointer register minus 32 bytes, consisting of:
- -The value of the LR, stored to the highest addressed doubleword of the Guarded Control Stack exception return record.
- -The value of the SPSR\_ELx for the current Exception level, stored to the second-highest addressed doubleword of the Guarded Control Stack exception return record.
- -The value of the ELR\_ELx for the current Exception level, stored to the third-highest addressed doubleword of the Guarded Control Stack exception return record.
- -Adoubleword with the value 0x0000\_0000\_0000\_0009 , stored to the lowest addressed doubleword of the Guarded Control Stack exception return record.
- Decrements the current Guarded Control Stack pointer registerby the size of a Guarded Control Stack exception return record.
- Sets PSTATE.EXLOCK to 0.

RJTRFY A GCSPOPCX instruction executed at ELx, where x is 1 or greater:

- Performs a GCS exception pop and compare operation when all of the following are true
- -Guarded Control Stacks are GCS Enabled at ELx.
- -The Effective value of GCSCR\_ELx.EXLOCKEN is 0 or PSTATE.EXLOCK is 0.
- Generates an EXLOCK Exception when all of the following are true:
- -Guarded Control Stacks are GCS Enabled at ELx.
- -The Effective value of GCSCR\_ELx.EXLOCKEN is 1 and PSTATE.EXLOCK is 1.
- Performs no operation if neither a GCS exception pop and compare operation nor an EXLOCK Exception is triggered.

RJYSCF Execution of GCSPOPCX at EL0 is UNDEFINED.

RPCQXX

AGCSexception pop and compare operation:

- Loads four doublewords of a Guarded Control Stack exception return record from the virtual address defined by the current Guarded Control Stack pointer register. Each access is single-copy atomic at doubleword granularity.
- If the value loaded from the lowest addressed doubleword of the Guarded Control Stack exception return record is not 0x0000\_0000\_0000\_0009 then a GCS Data Check exception is taken.
- Compares the value of LR with the value loaded from the highest addressed doubleword of the Guarded Control Stack exception return record, and takes a GCS Data Check exception if the values are not equal.
- Compares the value of the SPSR\_ELx for the current Exception level with the value loaded from the second-highest addressed doubleword of the Guarded Control Stack exception return record, and takes a GCS Data Check exception if the values are not equal.

IPTYBX

- Compares the value of the ELR\_ELx for the current Exception level with the value loaded from the third-highest addressed doubleword of the Guarded Control Stack exception return record, and takes a GCS Data Check exception if the values are not equal.
- If no exception is taken, increments the current Guarded Control Stack pointer register by the size of a Guarded Control Stack exception return record.
- Sets PSTATE.EXLOCK to the value of the Effective value of GCSCR\_ELx.EXLOCKEN.

Irrespective of whether address tagging for instruction addresses is enabled or not, all 64 bits of following registers are compared in the compare operation of the GCSPOPCX instruction:

- ELR\_ELx.
- LR.

RYMVVH Explicit synchronization is not required for direct writes to ELR\_ELx and SPSR\_ELx be observable to indirect reads made by the GCSPUSHX instruction.

RSSMHC

Explicit synchronization is not required for direct writes to ELR\_ELx and SPSR\_ELx be observable to indirect reads made by the GCSPOPCX instruction.

RHXXCL If Guarded Control Stacks are GCS Enabled at ELx, where x is 1 or greater, a GCSPOPX instruction executed at ELx performs the following operations:

- Load a Guarded Control Stack exception return record from the virtual address defined by the current Guarded Control Stack pointer register.
- If the value loaded from the lowest addressed doubleword of the Guarded Control Stack exception return record is not 0x0000\_0000\_0000\_0009 then a GCS Data Check exception is taken.
- Otherwise, the current Guarded Control Stack pointer register is incremented by the size of a Guarded Control Stack exception return record.

Execution of at EL0 is UNDEFINED.

RXHXGJ GCSPOPX

ICFFNS When an MSR instruction would write to the relevant ELR\_ELx or SPSR\_ELx for the current Exception level ELy, the Effective value of GCSCR\_ELy.EXLOCKEN and PSTATE.EXLOCK may prevent the write.

IDXBZZ For more information on exception entry and return, see Legal exception returns from AArch64 state, Illegal exception returns from AArch64 state, and Exception entry.

IBGLWD For more information on FEAT\_GCS in Debug state, see About Debug state.

- RYZBWD

RWRDNF

The Effective value of GCSCR\_ELx.EXLOCKEN is 1 for all purposes other than returning the value of a direct read of GCSCR\_ELx, if all of the following are true:

- GCSCR\_ELx.EXLOCKEN is 1.
- The PE is executing in Non-debug state.

The Effective value of GCSCR\_ELx.EXLOCKEN is 0 for all purposes other than returning the value of a direct read of GCSCR\_ELx, if any of the following are true:

- GCSCR\_ELx.EXLOCKEN is 0.
- The PE is executing in Debug state.

Note

While executing in Debug state, ELR\_ELx and SPSR\_ELx registers are accessible at ELx irrespective of the value of PSTATE.EXLOCK.

Execution of the GCSPUSHX instruction in Debug state is unaffected by the value of PSTATE.EXLOCK.

## D11.4.2 Using the exception return protection features

SMQBXD

Arm notes that the use of ERETAA, ERETAB for an exception return is unlikely when GCSPOPCX is used to validate the exception return state. This is because a prior GCSPUSHX instruction will have pushed an exception return address without a pointer authentication code to the Guarded Control Stack, and a GCSPOPCX will need to validate this exception

return address without a pointer authentication code. Therefore, the authentication would need to be performed before the GCSPOPCX instruction.

Exception handling software needs to be aware of the Guarded Control Stack for scenarios where an exception return does not return to the point where an exception was taken from, since this might require modification of the exception return state held on the Guarded Control Stack.