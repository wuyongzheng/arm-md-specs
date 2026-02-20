## F2.9 Exception-generating and exception-handling instructions

The following instructions are intended specifically to cause a synchronous exception to occur:

- The SVC instruction generates a Supervisor Call exception. For more information, see Supervisor Call (SVC) exception.
- The Breakpoint instruction BKPT provides software breakpoints. For more information, see Breakpoint Instruction exceptions.
- In an implementation that includes EL3 the SMC instruction generates a Secure Monitor Call exception. For more information, see Secure Monitor Call (SMC) exception.
- In an implementation that includes EL2 the HVC instruction generates a Hypervisor Call exception. For more information, see Hypervisor Call (HVC) exception.

Debug state summarizes the Debug state instructions.

For an exception taken to an EL1 mode:

- The system level variants of the SUBS and LDM instructions can perform a return from an exception.

Note

The variants of SUBS include MOVS . See the references to Subtract (exception return), Move (exception return), and Load Multiple (exception return) in Table F2-15 for more information.

- The SRS instruction can be used near the start of the handler, to store return information. The RFE instruction can then perform a return from the exception using the stored return information.

In an implementation that includes EL2, the ERET instruction performs a return from an exception taken to Hyp mode.

For more information, see Exception return to an Exception level using AArch32.

Table F2-15 summarizes the instructions, in the T32 and A32 instruction sets, for generating or handling an exception. Except for BKPT and SVC , these are system level instructions.

Table F2-15 Exception-generating and exception-handling instructions

| Instruction                      | See                             |
|----------------------------------|---------------------------------|
| Supervisor Call                  | SVC                             |
| Breakpoint                       | BKPT                            |
| Secure Monitor Call              | SMC                             |
| Return From Exception            | RFE, RFEDA, RFEDB, RFEIA, RFEIB |
| Subtract (exception return) a    | SUB, SUBS (immediate) a         |
| Move (exception return) a        | MOV, MOVS(register) a           |
| Hypervisor Call                  | HVC                             |
| Exception Return                 | ERET                            |
| Load Multiple (exception return) | LDM(exception return)           |
| Store Return State               | SRS, SRSDA, SRSDB, SRSIA, SRSIB |

## F2.9.1 Debug state

Table F2-16 shows the Debug state instructions that are implemented in the T32 instruction set:

## Table F2-16 T32 Debug state instructions

| Mnemonic   | Instruction                   | See               | Note                                                                              |
|------------|-------------------------------|-------------------|-----------------------------------------------------------------------------------|
| DCPSn      | Debug switch to EL n          | DCPS1 DCPS2 DCPS3 | -                                                                                 |
| ERET       | Debug restore PE state (DRPS) | ERET              | When executed in Debug state, the T1 encoding of ERET performs the DRPS operation |