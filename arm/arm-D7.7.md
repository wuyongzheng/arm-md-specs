## D7.7 Memory barrier instructions

Memory barriers describes the memory barrier instructions. This section describes the system level controls of those instructions.

## D7.7.1 EL2 control of the shareability of data barrier instructions executed at EL0 or EL1

In an implementation that includes EL2 enabled in the current Security state and supports shareability limitations on the data barrier instructions, the HCR\_EL2.BSU field can modify the required shareability of an instruction that is executed at EL0 or EL1. Table D7-9 shows the encoding of this field.

Table D7-9 EL2 control of shareability of barrier instructions executed at EL0 or EL1

|   HCR_EL2.BSU | Minimum shareability of barrier instructions               |
|---------------|------------------------------------------------------------|
|            00 | No effect, shareability is as specified by the instruction |
|            01 | Inner Shareable                                            |
|            10 | Outer Shareable                                            |
|            11 | Full system                                                |

For an instruction executed at EL0 or EL1, Table D7-10 shows how the HCR\_EL2.BSU is combined with the shareability specified by the argument of the DMB or DSB instruction to give the scope of the instruction.

Table D7-10 Effect of HCR\_EL2.BSU on barrier instructions executed at EL1 or EL0

| Shareability specified by the DMB or DSB argument   | HCR_EL2.BSU          | Resultant shareability   |
|-----------------------------------------------------|----------------------|--------------------------|
| Full system                                         | Any                  | Full system              |
| Outer Shareable                                     | 00 , 01 , or 10      | Outer Shareable          |
|                                                     | 11 , Full system     | Full system              |
| Inner Shareable                                     | 00 or 01             | Inner Shareable          |
|                                                     | 10 , Outer Shareable | Outer Shareable          |
|                                                     | 11 , Full system     | Full system              |
| Non-shareable                                       | 00 , No effect       | Non-shareable            |
|                                                     | 01 , Inner Shareable | Inner Shareable          |
|                                                     | 10 , Outer Shareable | Outer Shareable          |
|                                                     | 11 , Full system     | Full system              |