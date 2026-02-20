## D11.7 Guarded Control Stack switching

GXMPQT FEAT\_GCS provides means to switch between multiple Guarded Control Stacks of an Exception level at the same Exception level, without providing direct write access to the current Guarded Control Stack pointer register.

GGTMLR Arm expects that an individual Guarded Control Stack is used by only one PE at a time, to ensure the stack is not being updated by one PE while being used by another.

IFZSVZ

When a Guarded Control Stack is not currently in use, the top entry contains a special value which indicates it is capped. The only way that the Guarded Control Stack can become uncapped is by execution of the GCSSS1 Xn and GCSSS2 Xn instructions, to switch between two Guarded Control Stacks. These instructions check the cap on the incoming Guarded Control Stack and then add a cap to the outgoing Guarded Control Stack. Since there is no direct write access to the current Guarded Control Stack pointer register, the only way the current Guarded Control Stack pointer register can be made to point to the new Guarded Control Stack is using these instructions, and the checks performed by these instructions ensure that the value loaded is always pointing to a capped Guarded Control Stack. This ensures that any arbitrary location in a Guarded Control Stack cannot be switched to.

Figure D11-1 shows the process of how these instructions perform the switching between 2 Guarded Control Stacks.

<!-- image -->

Figure D11-1 Guarded Control Stack switching

| I GPHKD   | The instruction pair GCSSS1 Xn and GCSSS2 Xn provide means to switch between Guarded Control Stacks of the current Exception level without directly accessing GCSPR_ELx at the same Exception level.                                               |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D PCHQS   | Avalue of 0b000000000001 in bits [11:0] of a Guarded Control Stack entry is called a Valid cap token.                                                                                                                                              |
| D QJDCV   | An entry in the Guarded Control Stack is defined as a Valid cap entry, if bits [63:12] of the entry value are the same as bits [63:12] of the address where the entry is stored and bits [11:0] contain a Valid cap token.                         |
| D ZNSQG   | Avalue of 0b101 in bits [2:0] of a Guarded Control Stack entry is called an In-progress cap token.                                                                                                                                                 |
| D XGMLV   | An entry in the Guarded Control Stack is defined as an In-progress cap entry, if bits [63:3] of the value are the same as bits [63:3] of the current Guarded Control Stack pointer register value and bits [2:0] contain an In-progress cap token. |

RQHSGP

RPBWVT

RPTCXM

RXTZVS

The GCSSS1 Xn instruction performs the following functionalities in order:

1. Adoubleword is loaded from the Guarded Control Stack that is pointed to by Xn .
2. If the loaded value is a Valid cap entry:
- The top entry of the Guarded Control Stack pointed to by Xn is overwritten with an In-progress cap entry:
4. -Bits [63:3] of the In-progress cap entry contain bits [63:3] of the current Guarded Control Stack pointer register.
5. -Bits [2:0] of the In-progress cap entry contain 0b101 .
- The current Guarded Control Stack pointer register is updated to the following value:
7. -Bits [63:3] are set to bits [63:3] of Xn .
8. -Bits [2:0] are set to 0b000 .
3. If the loaded value is not a Valid cap entry, a GCS Data Check exception is generated and no write is required to be performed.
4. All observers in the shareability domain observe the load and store atomically.

The GCSSS2 Xn instruction performs the following functionalities in order:

1. Adoubleword is loaded from the memory pointed by the current Guarded Control Stack pointer register.
2. If the loaded value contains an In-progress cap token:
- AValid cap entry is written to the outgoing GCS, with the following parameters:
4. -The target address of the write has:
5. -Bits [63:3] set to bits [63:3] of the loaded value, minus 1.
6. -Bits [2:0] set to 0b000 .
7. -The data value written has:
8. -Bits [63:12] set to bits [63:12] of the target address.
9. -Bits [11:0] set to 0b000000000001 .
- The current Guarded Control Stack pointer register is incremented by the size of a Guarded Control Stack procedure return record.
- Xn is updated to contain:
12. -Bits [63:3] set to bits [63:3] of the loaded value, minus 1.
13. -Bits [2:0] are set to 0b000 .
3. If the loaded value does not contain an In-progress cap token, a GCS Data Check exception is generated.

RKFMRX For the purpose of permission checking, and for watchpoints, the GCSSS1 Xn instruction is treated as performing both a load and a store, even if the store does not happen.

GHMJGM FEAT\_GCS allows software to use address tagging in a Guarded Control Stack Pointer.

IMGLTC

While address tagging for data addresses is enabled, if the tag value in the target address register of the GCSSS1 Xn instruction is not same as the tag value in the Valid cap entry, the comparison as part of the GCSSS1 Xn instruction will cause a GCS Data Check exception.

IMBHFS While address tagging for data addresses is enabled, the In-progress cap entry stored by the GCSSS1 Xn instruction will contain any tag value that is present in the current Guarded Control Stack pointer register.

RXWQDB

All restrictions that are applicable to usage of the atomic instructions are also applicable to the usage of the GCSSS1 Xn instruction.

IDDFMX For example, the memory types for which it is architecturally guaranteed that the GCSSS1 Xn instruction will be atomic are:

- Inner Shareable, Inner Write-Back, Outer Write-Back Normal memory.
- Outer Shareable, Inner Write-Back, Outer Write-Back Normal memory.

For the purpose of exception prioritization, a GCS Data Check exception from a GCSSS2 Xn instruction is considered to be caused by the load that is part of the same GCSSS2 Xn instruction.

For the purpose of prioritizing exceptions and debug events, all exceptions and debug events due to load part of a GCSSS2 Xn instruction are higher priority than exceptions and debug events due to store part of the same GCSSS2 Xn instruction.

Note

This is a stricter requirement when compared to most of other instructions that cause multiple single copy atomic accesses where the priority is not architecturally defined. See Prioritization of Synchronous exceptions taken to AArch64 state for more information.