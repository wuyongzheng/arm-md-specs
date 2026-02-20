## G4.7 Memory barrier instructions

Memory barriers describes the memory barrier instructions. This section describes the system level controls of those instructions.

## G4.7.1 EL2 control of the Shareability of data barrier instructions executed at EL0 or EL1

In an implementation that includes EL2 and supports Shareability limitations on the data barrier instructions, the HCR.BSU field can modify the required Shareability of an instruction that is executed at EL0 or EL1 in Non-secure state. Table G4-8 shows the encoding of this field:

## Table G4-8 EL2 control of Shareability of barrier instructions executed at EL0 or EL1

|   HCR.BSU | Minimum Shareability of barrier instructions               |
|-----------|------------------------------------------------------------|
|        00 | No effect, Shareability is as specified by the instruction |
|        01 | Inner Shareable                                            |
|        10 | Outer Shareable                                            |
|        11 | Full system                                                |

For an instruction executed at EL0 or EL1 in Non-secure state, Table G4-9 shows how the HCR.BSU is combined with the Shareability specified by the argument of the DMB or DSB instruction to give the scope of the instruction:

Table G4-9 Effect of the HCR\_EL2.BSU on barrier instructions executed at Non-secure EL1 or EL1

| Shareability specified by the DMB or DSB argument   | HCR.BSU              | Resultant Shareability   |
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