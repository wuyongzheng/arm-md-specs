## F2.8 Miscellaneous instructions

Table F2-14 summarizes the miscellaneous instructions in the T32 and A32 instruction sets.

Table F2-14 Miscellaneous instructions

| Instruction                         | See                                                    |
|-------------------------------------|--------------------------------------------------------|
| Clear Branch History                | CLRBHB                                                 |
| Clear-Exclusive                     | CLREX                                                  |
| Data Memory Barrier                 | DMB                                                    |
| Data Synchronization Barrier        | DSB                                                    |
| Error Synchronization Barrier       | ESB                                                    |
| Instruction Synchronization Barrier | ISB                                                    |
| If-Then                             | IT                                                     |
| No Operation                        | NOP                                                    |
| Preload Data                        | PLD, PLDW(immediate) PLD (literal) PLD, PLDW(register) |
| Preload Instruction                 | PLI (immediate, literal) PLI (register)                |
| Speculation Barrier                 | SB                                                     |
| Set Endianness                      | SETEND a                                               |
| Set Privileged Access Never         | SETPAN                                                 |
| Send Event                          | SEV                                                    |
| Send Event Local                    | SEVL                                                   |
| Wait For Event                      | WFE                                                    |
| Wait For Interrupt                  | WFI                                                    |
| Yield                               | YIELD b                                                |

b. See also The Yield instruction.

Note

Previous versions of the architecture defined the DBG instruction, that could provide a hint to the debug system, in this group. From the introduction of Armv8, this instruction executes as a NOP. Armdeprecates any use of the DBG instruction.

## F2.8.1 The Yield instruction

In a Symmetric Multithreading (SMT) design, a thread can use the YIELD instruction to give a hint to the PE that it is running on. The YIELD hint indicates that whatever the thread is currently doing is of low importance, and so could yield. For example, the thread might be sitting in a spin-lock. A similar use might be in modifying the arbitration priority of the snoop bus in a multiprocessor (MP) system. Defining such an instruction permits binary compatibility between SMTand SMP systems.

AArch32 state defines a YIELD instruction as a specific NOP (No Operation) hint instruction.

The YIELD instruction has no effect in a single-threaded system, but developers of such systems can use the instruction to flag its intended use on migration to a multiprocessor or multithreading system. Operating systems can use YIELD in places where a yield hint is wanted, knowing that it will be treated as a NOP if there is no implementation benefit.